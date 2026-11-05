from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema

from .serializers import (
    ProgressSummarySerializer,
    SkillProgressSerializer,
    CareerReadinessSerializer,
    AchievementSerializer,
)


AVAILABLE_SKILLS = [
    "Python",
    "Java",
    "C Programming",
    "SQL",
    "PostgreSQL",
    "HTML",
    "CSS",
    "React",
    "Data Structures",
    "Machine Learning",
]

CAREERS = {
    1: {
        "title": "Python Developer",
        "required_skills": [
            "Python", "Django", "REST API", "SQL", "Git"
        ],
    },
    2: {
        "title": "Full-Stack Developer",
        "required_skills": [
            "HTML", "CSS", "JavaScript", "React",
            "Python", "Django", "SQL"
        ],
    },
    3: {
        "title": "Data Analyst",
        "required_skills": [
            "Python", "SQL", "Excel",
            "Statistics", "Data Visualization"
        ],
    },
    4: {
        "title": "Java Developer",
        "required_skills": [
            "Java", "OOP", "Data Structures", "SQL", "Git"
        ],
    },
    5: {
        "title": "AI and Machine Learning Engineer",
        "required_skills": [
            "Python", "Statistics", "Linear Algebra",
            "Machine Learning", "Data Structures"
        ],
    },
}


class ProgressSummaryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="get_progress_summary",
        summary="Get Student Progress Summary",
        responses={200: ProgressSummarySerializer},
    )
    def get(self, request):
        data = {
            "user_id": request.user.pk,
            "skills_available": len(AVAILABLE_SKILLS),
            "career_paths_available": len(CAREERS),
            "assessment_attempts": 0,
            "completed_assessments": 0,
            "progress_percentage": 0.0,
            "message": (
                "This is an initial summary. Assessment history "
                "and personal progress are not persisted yet."
            ),
        }

        serializer = ProgressSummarySerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SkillProgressListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="list_student_skill_progress",
        summary="Get Student Skill Progress",
        responses={200: SkillProgressSerializer(many=True)},
    )
    def get(self, request):
        results = [
            {
                "skill_name": skill,
                "current_level": "Not assessed",
                "progress_percentage": 0.0,
                "status": "Not started",
            }
            for skill in AVAILABLE_SKILLS
        ]

        serializer = SkillProgressSerializer(results, many=True)
        return Response(
            {
                "count": len(results),
                "skills": serializer.data,
                "message": (
                    "Personal progress will be available when "
                    "assessment history is stored."
                ),
            },
            status=status.HTTP_200_OK,
        )


class CareerReadinessAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="get_career_readiness",
        summary="Estimate Career Readiness",
        description=(
            "Supply comma-separated skills, for example "
            "?career_id=1&skills=Python,SQL. This is a simple "
            "skill-coverage estimate, not an employment prediction."
        ),
    )
    def get(self, request):
        career_id_value = request.query_params.get("career_id", "1")
        skills_value = request.query_params.get("skills", "")

        try:
            career_id = int(career_id_value)
        except (ValueError, TypeError):
            return Response(
                {"detail": "career_id must be an integer."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        career = CAREERS.get(career_id)

        if career is None:
            return Response(
                {"detail": "Career path not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        current_skills = {
            skill.strip().casefold()
            for skill in skills_value.split(",")
            if skill.strip()
        }

        required = career["required_skills"]
        matched = [
            skill for skill in required
            if skill.casefold() in current_skills
        ]
        missing = [
            skill for skill in required
            if skill.casefold() not in current_skills
        ]

        readiness = round(len(matched) / len(required) * 100, 2)

        result = {
            "career_id": career_id,
            "career_title": career["title"],
            "required_skills_count": len(required),
            "matched_skills": matched,
            "missing_skills": missing,
            "readiness_percentage": readiness,
        }

        serializer = CareerReadinessSerializer(result)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AchievementsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="list_student_achievements",
        summary="Get Student Achievements",
        responses={200: AchievementSerializer(many=True)},
    )
    def get(self, request):
        achievements = [
            {
                "id": 1,
                "title": "First Steps",
                "description": "Complete your first skill assessment.",
                "status": "Not earned",
            },
            {
                "id": 2,
                "title": "Skill Explorer",
                "description": "Explore at least five available skills.",
                "status": "Not earned",
            },
            {
                "id": 3,
                "title": "Career Planner",
                "description": "Explore a career path and its requirements.",
                "status": "Not earned",
            },
        ]

        serializer = AchievementSerializer(achievements, many=True)

        return Response(
            {
                "user_id": request.user.pk,
                "count": len(achievements),
                "achievements": serializer.data,
                "message": (
                    "These are sample achievement definitions. "
                    "Achievement history is not stored."
                ),
            },
            status=status.HTTP_200_OK,
        )
