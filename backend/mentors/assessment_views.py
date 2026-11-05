
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from accounts.permissions import IsMentor
from mentors.models import MentorStudentAssignment
from assessments.models import AssessmentResult
from skills.models import SkillAssessmentResult


class MentorAssessmentsAPIView(APIView):
    permission_classes = [IsAuthenticated, IsMentor]

    def get(self, request):
        assignments = (
            MentorStudentAssignment.objects
            .filter(
                mentor=request.user,
                status="Active",
            )
            .select_related("student")
        )

        student_ids = assignments.values_list(
            "student_id", flat=True
        ).distinct()

        assessments = []

        # Overall assessment results
        overall_results = (
            AssessmentResult.objects
            .filter(user_id__in=student_ids)
            .select_related("user")
            .order_by("-created_at")
        )

        for result in overall_results:
            assessments.append({
                "id": result.id,
                "assessment_type": "Overall Assessment",
                "student_id": result.user_id,
                "student_name": (
                    result.user.get_full_name()
                    or result.user.username
                ),
                "student_email": result.user.email,
                "skill": result.skill,
                "score": result.correct_answers,
                "total_questions": result.total_questions,
                "percentage": str(result.score_percentage),
                "estimated_level": result.estimated_level,
                "completed_at": result.created_at,
            })

        # Skill-specific assessment results
        skill_results = (
            SkillAssessmentResult.objects
            .filter(user_id__in=student_ids)
            .select_related("user", "skill")
            .order_by("-completed_at")
        )

        for result in skill_results:
            assessments.append({
                "id": result.id,
                "assessment_type": "Skill Assessment",
                "student_id": result.user_id,
                "student_name": (
                    result.user.get_full_name()
                    or result.user.username
                ),
                "student_email": result.user.email,
                "skill": result.skill.name,
                "score": result.score,
                "total_questions": result.total_questions,
                "percentage": str(result.percentage),
                "estimated_level": None,
                "completed_at": result.completed_at,
            })

        # Sort both assessment types newest first
        assessments.sort(
            key=lambda item: item["completed_at"],
            reverse=True,
        )

        total = len(assessments)

        return Response(
            {
                "count": total,
                "student_count": len(student_ids),
                "summary": {
                    "total_assessments": total,
                    "overall_assessments": len(overall_results),
                    "skill_assessments": len(skill_results),
                },
                "assessments": assessments,
            },
            status=status.HTTP_200_OK,
        )
