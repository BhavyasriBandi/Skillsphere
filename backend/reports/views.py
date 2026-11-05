from django.contrib.auth import get_user_model
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.utils.dateparse import parse_date

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsPlatformAdmin
from achievements.models import Achievement, StudentAchievement


User = get_user_model()


class ReportsAnalyticsAPIView(APIView):
    permission_classes = [IsAuthenticated, IsPlatformAdmin]

    def get(self, request):
        # 1. Validate the optional date filters.
        start_date_text = request.query_params.get("start_date")
        end_date_text = request.query_params.get("end_date")

        start_date = None
        end_date = None

        if start_date_text:
            start_date = parse_date(start_date_text)
            if start_date is None:
                return Response(
                    {"error": "Invalid start_date. Use YYYY-MM-DD."},
                    status=400,
                )

        if end_date_text:
            end_date = parse_date(end_date_text)
            if end_date is None:
                return Response(
                    {"error": "Invalid end_date. Use YYYY-MM-DD."},
                    status=400,
                )

        if start_date and end_date and start_date > end_date:
            return Response(
                {"error": "start_date cannot be later than end_date."},
                status=400,
            )

        # 2. Filter users by registration date.
        users = User.objects.all()

        if start_date:
            users = users.filter(date_joined__date__gte=start_date)

        if end_date:
            users = users.filter(date_joined__date__lte=end_date)

        # 3. User metrics.
        total_users = users.count()
        active_users = users.filter(is_active=True).count()

        total_students = users.filter(
            groups__name__iexact="Student"
        ).distinct().count()

        total_mentors = users.filter(
            groups__name__iexact="Mentor"
        ).distinct().count()

        # 4. Achievement metrics.
        achievements = Achievement.objects.all()

        if start_date:
            achievements = achievements.filter(
                created_at__date__gte=start_date
            )

        if end_date:
            achievements = achievements.filter(
                created_at__date__lte=end_date
            )

        total_achievements = achievements.count()

        student_achievements = StudentAchievement.objects.filter(
            achievement__in=achievements,
            is_earned=True,
        )

        if start_date:
            student_achievements = student_achievements.filter(
                earned_at__date__gte=start_date
            )

        if end_date:
            student_achievements = student_achievements.filter(
                earned_at__date__lte=end_date
            )

        earned_achievements = student_achievements.count()

        # 5. Monthly user registrations.
        registration_rows = (
            users.annotate(month=TruncMonth("date_joined"))
            .values("month")
            .annotate(count=Count("id"))
            .order_by("month")
        )

        registrations = [
            {
                "month": row["month"].strftime("%B %Y"),
                "count": row["count"],
            }
            for row in registration_rows
            if row["month"] is not None
        ]

        # 6. User role distribution.
        role_rows = (
            users.values("groups__name")
            .annotate(count=Count("id", distinct=True))
            .order_by("groups__name")
        )

        roles = [
            {
                "role": row["groups__name"] or "Unassigned",
                "count": row["count"],
            }
            for row in role_rows
        ]

        # 7. Return the response expected by ReportsAnalytics.js.
        return Response(
            {
                "metrics": {
                    "total_users": total_users,
                    "total_students": total_students,
                    "total_mentors": total_mentors,
                    "total_achievements": total_achievements,
                    "earned_achievements": earned_achievements,
                    "active_users": active_users,
                },
                "registrations": registrations,
                "roles": roles,
            }
        )
