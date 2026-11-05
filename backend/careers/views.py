
from django.shortcuts import render

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

from .models import RoadmapTaskProgress
from .serializers import (
    CareerSerializer,
    CareerRecommendationRequestSerializer,
    CareerProgressQuerySerializer,
    RoadmapTaskProgressSerializer,
)


CAREER_PATHS = [
    {
        "id": 1,
        "title": "Python Developer",
        "description": (
            "Build applications, automation tools, and backend services "
            "using Python."
        ),
        "required_skills": ["Python", "Django", "REST API", "SQL", "Git"],
        "opportunities": [
            "Python Developer",
            "Backend Developer",
            "Automation Engineer",
        ],
        "learning_duration": "4-6 months",
    },
    {
        "id": 2,
        "title": "Full-Stack Developer",
        "description": (
            "Develop complete web applications using frontend and "
            "backend technologies."
        ),
        "required_skills": [
            "HTML", "CSS", "JavaScript", "React", "Python", "Django", "SQL"
        ],
        "opportunities": [
            "Full-Stack Developer",
            "Web Application Developer",
            "Software Engineer",
        ],
        "learning_duration": "6-9 months",
    },
    {
        "id": 3,
        "title": "Data Analyst",
        "description": (
            "Analyze data and communicate insights to support "
            "business decisions."
        ),
        "required_skills": [
            "Python", "SQL", "Excel", "Statistics", "Data Visualization"
        ],
        "opportunities": [
            "Data Analyst",
            "Business Intelligence Analyst",
            "Reporting Analyst",
        ],
        "learning_duration": "4-6 months",
    },
    {
        "id": 4,
        "title": "Java Developer",
        "description": (
            "Create software applications and backend systems using Java."
        ),
        "required_skills": [
            "Java", "OOP", "Data Structures", "SQL", "Git"
        ],
        "opportunities": [
            "Java Developer",
            "Backend Developer",
            "Software Engineer",
        ],
        "learning_duration": "4-7 months",
    },
    {
        "id": 5,
        "title": "AI and Machine Learning Engineer",
        "description": (
            "Develop intelligent systems using data, algorithms, "
            "and machine learning techniques."
        ),
        "required_skills": [
            "Python",
            "Statistics",
            "Linear Algebra",
            "Machine Learning",
            "Data Structures",
        ],
        "opportunities": [
            "Machine Learning Engineer",
            "AI Developer",
            "Junior Data Scientist",
        ],
        "learning_duration": "8-12 months",
    },
]


def calculate_recommendations(skills, interests):
    """Rank sample career paths using skill and interest matches."""
    normalized_skills = {skill.strip().casefold() for skill in skills}
    normalized_interests = {
        interest.strip().casefold() for interest in interests
    }
    results = []

    for career in CAREER_PATHS:
        required = {
            skill.casefold() for skill in career["required_skills"]
        }
        matched_skills = sorted(
            skill for skill in career["required_skills"]
            if skill.casefold() in normalized_skills
        )
        matched_interests = [
            interest
            for interest in normalized_interests
            if interest in career["title"].casefold()
            or interest in career["description"].casefold()
            or any(
                interest in opportunity.casefold()
                for opportunity in career["opportunities"]
            )
        ]
        skill_score = (
            len(required.intersection(normalized_skills)) / len(required)
        ) * 80
        interest_score = min(len(matched_interests) * 10, 20)
        score = round(min(skill_score + interest_score, 100), 2)

        if score > 0:
            results.append({
                **career,
                "match_percentage": score,
                "matched_skills": matched_skills,
                "matched_interests": matched_interests,
                "missing_skills": sorted(
                    skill for skill in career["required_skills"]
                    if skill.casefold() not in normalized_skills
                ),
            })

    results.sort(
        key=lambda item: item["match_percentage"],
        reverse=True,
    )
    return results


class CareerListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="list_career_paths",
        summary="List Career Paths",
        responses={200: CareerSerializer(many=True)},
    )
    def get(self, request):
        serializer = CareerSerializer(CAREER_PATHS, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CareerDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="get_career_details",
        summary="Get Career Details",
        responses={200: CareerSerializer},
    )
    def get(self, request, career_id):
        career = next(
            (item for item in CAREER_PATHS if item["id"] == career_id),
            None,
        )
        if career is None:
            return Response(
                {"detail": "Career path not found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = CareerSerializer(career)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CareerRecommendationsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="generate_career_recommendations",
        summary="Generate Career Recommendations",
        request=CareerRecommendationRequestSerializer,
        responses={200: CareerSerializer(many=True)},
        description=(
            "Ranks sample career paths using supplied skills and interests. "
            "Results are calculated dynamically and are not saved to a database."
        ),
    )
    def post(self, request):
        serializer = CareerRecommendationRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        recommendations = calculate_recommendations(
            serializer.validated_data["skills"],
            serializer.validated_data.get("interests", []),
        )
        return Response(
            {
                "user_id": request.user.pk,
                "count": len(recommendations),
                "recommendations": recommendations,
                "message": (
                    "Recommendations generated successfully."
                    if recommendations
                    else (
                        "No matching career paths found. "
                        "Try adding more skills or interests."
                    )
                ),
            },
            status=status.HTTP_200_OK,
        )


class MyCareerRecommendationsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="get_my_career_recommendations",
        summary="Get My Career Recommendations",
        description=(
            "Saved recommendation history is not available because "
            "persistent storage is not configured."
        ),
    )
    def get(self, request):
        return Response(
            {
                "user_id": request.user.pk,
                "recommendations": [],
                "count": 0,
                "message": (
                    "Recommendation history is not saved yet. "
                    "Submit skills to the recommendations endpoint "
                    "to generate results."
                ),
            },
            status=status.HTTP_200_OK,
        )


class CareerRoadmapAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="get_career_roadmap",
        summary="Get Career Roadmap",
        parameters=[CareerProgressQuerySerializer],
    )
    def get(self, request):
        query_serializer = CareerProgressQuerySerializer(
            data=request.query_params
        )
        query_serializer.is_valid(raise_exception=True)
        career_id = query_serializer.validated_data.get("career_id")

        if career_id is None:
            return Response(
                {
                    "available_careers": [
                        {"id": career["id"], "title": career["title"]}
                        for career in CAREER_PATHS
                    ],
                    "message": (
                        "Provide a career_id query parameter to "
                        "retrieve its roadmap."
                    ),
                },
                status=status.HTTP_200_OK,
            )

        career = next(
            (item for item in CAREER_PATHS if item["id"] == career_id),
            None,
        )
        if career is None:
            return Response(
                {"detail": "Career path not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        roadmap = [
            {
                "stage": 1,
                "title": "Foundation",
                "skills": career["required_skills"][:2],
                "goal": "Understand the fundamentals.",
            },
            {
                "stage": 2,
                "title": "Core Skills",
                "skills": career["required_skills"][2:4],
                "goal": "Practice the essential technical skills.",
            },
            {
                "stage": 3,
                "title": "Projects and Practice",
                "skills": career["required_skills"][4:],
                "goal": "Build practical projects and use Git.",
            },
            {
                "stage": 4,
                "title": "Career Preparation",
                "skills": [
                    "Portfolio", "Resume", "Interview Preparation"
                ],
                "goal": (
                    "Prepare a portfolio and practice "
                    "career-related interviews."
                ),
            },
        ]
        return Response(
            {
                "career_id": career["id"],
                "career_title": career["title"],
                "learning_duration": career["learning_duration"],
                "roadmap": roadmap,
            },
            status=status.HTTP_200_OK,
        )


class RoadmapTaskProgressAPIView(APIView):
    """Read, save, and reset progress for the authenticated student."""

    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="list_roadmap_task_progress",
        summary="Get My Roadmap Task Progress",
        responses={200: RoadmapTaskProgressSerializer(many=True)},
    )
    def get(self, request):
        queryset = RoadmapTaskProgress.objects.filter(student=request.user)
        career = request.query_params.get("career")
        if career:
            queryset = queryset.filter(career=career)
        serializer = RoadmapTaskProgressSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        operation_id="save_roadmap_task_progress",
        summary="Save My Roadmap Task Progress",
        request=RoadmapTaskProgressSerializer,
        responses={200: RoadmapTaskProgressSerializer},
    )
    def post(self, request):
        career = request.data.get("career")
        task_id = request.data.get("task_id")
        task_name = request.data.get("task_name")
        is_completed = request.data.get("is_completed")

        errors = {}
        if not isinstance(career, str) or not career.strip():
            errors["career"] = "A career name is required."
        if not isinstance(task_id, str) or not task_id.strip():
            errors["task_id"] = "A task ID is required."
        if not isinstance(task_name, str) or not task_name.strip():
            errors["task_name"] = "A task name is required."
        if not isinstance(is_completed, bool):
            errors["is_completed"] = "Provide true or false."
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        progress, _created = RoadmapTaskProgress.objects.update_or_create(
            student=request.user,
            career=career.strip(),
            task_id=task_id.strip(),
            defaults={
                "task_name": task_name.strip(),
                "is_completed": is_completed,
            },
        )
        serializer = RoadmapTaskProgressSerializer(progress)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        operation_id="reset_roadmap_task_progress",
        summary="Reset My Roadmap Task Progress",
        responses={200: None},
    )
    def delete(self, request):
        career = request.query_params.get("career", "").strip()
        if not career:
            return Response(
                {"detail": "Provide a career query parameter."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        deleted_count, _details = RoadmapTaskProgress.objects.filter(
            student=request.user,
            career=career,
        ).delete()
        return Response(
            {"deleted_count": deleted_count, "career": career},
            status=status.HTTP_200_OK,
        )
