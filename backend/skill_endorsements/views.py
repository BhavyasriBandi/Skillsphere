from django.shortcuts import render

# Create your views here.

from datetime import datetime, timezone

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema

from .serializers import SkillEndorsementSerializer


# Temporary storage only; data is not persisted.
ENDORSEMENTS = []
NEXT_ENDORSEMENT_ID = 1


def public_endorsement(item):
    return {
        key: value
        for key, value in item.items()
        if key != "mentor_id"
    }


class SkillEndorsementListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="List Skill Endorsements",
        responses=SkillEndorsementSerializer(many=True),
    )
    def get(self, request):
        endorsements = [
            public_endorsement(item)
            for item in ENDORSEMENTS
            if (
                item["student_id"] == request.user.pk
                or item["mentor_id"] == request.user.pk
            )
        ]

        return Response({
            "count": len(endorsements),
            "endorsements": endorsements,
        })

    @extend_schema(
        summary="Create a Skill Endorsement",
        request=SkillEndorsementSerializer,
    )
    def post(self, request):
        global NEXT_ENDORSEMENT_ID

        if not request.user.groups.filter(name="Mentor").exists():
            return Response(
                {"detail": "Only mentors can endorse skills."},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = SkillEndorsementSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        student_id = serializer.validated_data["student_id"]

        if student_id == request.user.pk:
            return Response(
                {"detail": "You cannot endorse your own skills."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        from django.contrib.auth import get_user_model

        User = get_user_model()

        student = User.objects.filter(
            pk=student_id,
            groups__name="Student",
        ).first()

        if student is None:
            return Response(
                {"detail": "Student not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        endorsement = {
            "id": NEXT_ENDORSEMENT_ID,
            "mentor_id": request.user.pk,
            "student_id": student_id,
            "skill_name": serializer.validated_data["skill_name"],
            "message": serializer.validated_data.get("message", ""),
            "endorsed_at": datetime.now(timezone.utc),
        }

        ENDORSEMENTS.append(endorsement)
        NEXT_ENDORSEMENT_ID += 1

        return Response(
            public_endorsement(endorsement),
            status=status.HTTP_201_CREATED,
        )


class SkillEndorsementDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_endorsement(self, request, endorsement_id):
        return next(
            (
                item for item in ENDORSEMENTS
                if item["id"] == endorsement_id
                and (
                    item["mentor_id"] == request.user.pk
                    or item["student_id"] == request.user.pk
                )
            ),
            None,
        )

    @extend_schema(summary="Delete a Skill Endorsement")
    def delete(self, request, endorsement_id):
        endorsement = self.get_endorsement(request, endorsement_id)

        if endorsement is None:
            return Response(
                {"detail": "Endorsement not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        if endorsement["mentor_id"] != request.user.pk:
            return Response(
                {"detail": "Only the endorsing mentor can delete it."},
                status=status.HTTP_403_FORBIDDEN,
            )

        ENDORSEMENTS.remove(endorsement)

        return Response(
            {"message": "Skill endorsement deleted successfully."},
            status=status.HTTP_200_OK,
        )
