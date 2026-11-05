
from django.db.models import Q

from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SkillAssessmentResult


class AdminAssessmentResultsAPIView(APIView):
    """
    Admin API to view completed student skill assessment results.
    """

    permission_classes = [IsAdminUser]

    def get(self, request):
        results = (
            SkillAssessmentResult.objects
            .select_related("user", "skill")
            .order_by("-completed_at")
        )

        # Filter by skill
        skill_name = request.query_params.get("skill", "").strip()

        if skill_name and skill_name.lower() not in ["all", "all skills"]:
            results = results.filter(
                skill__name__iexact=skill_name
            )

        # Search by student name, username or email
        search = request.query_params.get("search", "").strip()

        if search:
            results = results.filter(
                Q(user__username__icontains=search)
                | Q(user__email__icontains=search)
                | Q(user__first_name__icontains=search)
                | Q(user__last_name__icontains=search)
                | Q(skill__name__icontains=search)
            )

        result_data = []

        for result in results:
            total = result.total_questions
            correct = result.score

            result_data.append({
                "id": result.id,
                "student_id": result.user_id,
                "student_name": (
                    result.user.get_full_name()
                    or result.user.username
                ),
                "student_email": result.user.email,
                "skill": result.skill.name,
                "score": correct,
                "total_questions": total,
                "correct_answers": correct,
                "wrong_answers": max(total - correct, 0),
                "percentage": float(result.percentage),
                "completed_at": result.completed_at,
            })

        return Response(
            {
                "count": len(result_data),
                "results": result_data,
            },
            status=status.HTTP_200_OK,
        )
