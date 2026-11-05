
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework import status
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Achievement, StudentAchievement
from .serializers import AchievementDefinitionSerializer


def serialize_achievement(record):
    achievement = record.achievement

    return {
        "id": achievement.id,
        "badge_key": achievement.badge_key,
        "title": achievement.title,
        "description": achievement.description,
        "icon": achievement.icon,
        "category": achievement.category,
        "badge_type": achievement.tier,
        "tier": achievement.tier,
        "points": achievement.points,
        "requirement": achievement.requirement,
        "target": achievement.target,
        "is_earned": record.is_earned,
        "is_saved": record.is_saved,
        "earned_at": record.earned_at,
        "saved_at": record.saved_at,
    }


class IsAchievementAdmin(BasePermission):
    message = "Only members of the Admin group can manage achievements."

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        return (
            user.is_superuser
            or user.groups.filter(name="Admin").exists()
        )


# --------------------------------------------------
# EXISTING STUDENT APIs
# --------------------------------------------------

class AchievementListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        definitions = Achievement.objects.filter(is_active=True)

        with transaction.atomic():
            for achievement in definitions:
                StudentAchievement.objects.get_or_create(
                    student=request.user,
                    achievement=achievement,
                )

        records = list(
            StudentAchievement.objects.filter(
                student=request.user,
                achievement__is_active=True,
            ).select_related("achievement")
        )

        earned_records = [
            record for record in records if record.is_earned
        ]

        return Response({
            "count": len(earned_records),
            "total_badges": definitions.count(),
            "results": [
                serialize_achievement(record)
                for record in records
            ],
            "total_points": sum(
                record.achievement.points
                for record in earned_records
            ),
        })


class AwardAchievementView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response(
            {
                "error": (
                    "Badges can only be unlocked after the backend "
                    "verifies the student's activity."
                )
            },
            status=status.HTTP_403_FORBIDDEN,
        )


class AchievementDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, achievement_id):
        record = get_object_or_404(
            StudentAchievement.objects.select_related("achievement"),
            student=request.user,
            achievement_id=achievement_id,
            is_earned=True,
        )

        return Response(serialize_achievement(record))


class SaveAchievementView(APIView):
    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request, achievement_id):
        achievement = get_object_or_404(
            Achievement,
            id=achievement_id,
            is_active=True,
        )

        record, _ = StudentAchievement.objects.get_or_create(
            student=request.user,
            achievement=achievement,
        )

        if not record.is_earned:
            return Response(
                {
                    "error": (
                        "You must earn this achievement before saving it."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not record.is_saved:
            record.is_saved = True
            record.saved_at = timezone.now()
            record.save(
                update_fields=["is_saved", "saved_at", "updated_at"]
            )

        return Response(serialize_achievement(record))


def evaluate_achievements(student, activity_counts):
    """
    Call only with activity counts calculated from trusted backend records.
    Never use counts supplied directly by the frontend.
    """
    unlocked = []

    with transaction.atomic():
        definitions = Achievement.objects.filter(is_active=True)

        for achievement in definitions:
            requirement = achievement.requirement

            if requirement == "badges":
                previously_earned = StudentAchievement.objects.filter(
                    student=student,
                    is_earned=True,
                    achievement__is_active=True,
                ).exclude(
                    achievement=achievement
                ).count()

                eligible = previously_earned >= achievement.target
            else:
                eligible = (
                    activity_counts.get(requirement, 0)
                    >= achievement.target
                )

            if not eligible:
                continue

            record, _ = StudentAchievement.objects.get_or_create(
                student=student,
                achievement=achievement,
            )

            if not record.is_earned:
                record.is_earned = True
                record.earned_at = timezone.now()
                record.save(
                    update_fields=[
                        "is_earned",
                        "earned_at",
                        "updated_at",
                    ]
                )
                unlocked.append(serialize_achievement(record))

    return unlocked


# --------------------------------------------------
# NEW ADMIN APIs
# --------------------------------------------------

class AdminAchievementListCreateView(APIView):
    permission_classes = [IsAuthenticated, IsAchievementAdmin]

    def get(self, request):
        achievements = Achievement.objects.all().order_by(
            "category", "id"
        )
        serializer = AchievementDefinitionSerializer(
            achievements, many=True
        )

        return Response({
            "count": achievements.count(),
            "results": serializer.data,
        })

    def post(self, request):
        serializer = AchievementDefinitionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        achievement = serializer.save()

        return Response(
            AchievementDefinitionSerializer(achievement).data,
            status=status.HTTP_201_CREATED,
        )


class AdminAchievementDetailView(APIView):
    permission_classes = [IsAuthenticated, IsAchievementAdmin]

    def get_object(self, achievement_id):
        return get_object_or_404(
            Achievement,
            pk=achievement_id,
        )

    def get(self, request, achievement_id):
        achievement = self.get_object(achievement_id)

        return Response(
            AchievementDefinitionSerializer(achievement).data
        )

    def put(self, request, achievement_id):
        achievement = self.get_object(achievement_id)

        serializer = AchievementDefinitionSerializer(
            achievement,
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        achievement = serializer.save()

        return Response(
            AchievementDefinitionSerializer(achievement).data
        )

    def patch(self, request, achievement_id):
        achievement = self.get_object(achievement_id)

        serializer = AchievementDefinitionSerializer(
            achievement,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        achievement = serializer.save()

        return Response(
            AchievementDefinitionSerializer(achievement).data
        )

    def delete(self, request, achievement_id):
        achievement = self.get_object(achievement_id)

        if achievement.is_active:
            achievement.is_active = False
            achievement.save(update_fields=["is_active"])

        return Response(
            {
                "message": "Achievement deactivated successfully.",
                "id": achievement.id,
                "is_active": achievement.is_active,
            },
            status=status.HTTP_200_OK,
        )


class AdminAchievementActivationView(APIView):
    permission_classes = [IsAuthenticated, IsAchievementAdmin]

    def patch(self, request, achievement_id):
        achievement = get_object_or_404(
            Achievement,
            pk=achievement_id,
        )

        is_active = request.data.get("is_active")

        if not isinstance(is_active, bool):
            return Response(
                {"is_active": "Provide true or false."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        achievement.is_active = is_active
        achievement.save(update_fields=["is_active"])

        return Response(
            AchievementDefinitionSerializer(achievement).data
        )
