from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CareerComparisonSerializer


# Sample career information for comparison.
CAREER_DATA = {
    "python developer": {
        "title": "Python Developer",
        "required_skills": [
            "Python",
            "Django",
            "SQL",
            "REST APIs",
            "Git",
        ],
        "learning_months": 6,
        "level": "Beginner to Intermediate",
        "roadmap": [
            "Learn Python fundamentals",
            "Practice data structures",
            "Learn Django and REST APIs",
            "Build projects",
            "Practice interviews",
        ],
    },
    "data analyst": {
        "title": "Data Analyst",
        "required_skills": [
            "SQL",
            "Python",
            "Excel",
            "Statistics",
            "Data Visualization",
        ],
        "learning_months": 5,
        "level": "Beginner to Intermediate",
        "roadmap": [
            "Learn Excel and statistics",
            "Learn SQL",
            "Practice Python for data analysis",
            "Learn data visualization",
            "Build analytics projects",
        ],
    },
    "frontend developer": {
        "title": "Frontend Developer",
        "required_skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Git",
        ],
        "learning_months": 5,
        "level": "Beginner to Intermediate",
        "roadmap": [
            "Learn HTML and CSS",
            "Practice JavaScript",
            "Learn React",
            "Build responsive interfaces",
            "Create portfolio projects",
        ],
    },
}


class CareerComparisonView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CareerComparisonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        first_name = serializer.validated_data["career_1"]
        second_name = serializer.validated_data["career_2"]

        first = CAREER_DATA.get(first_name.lower())
        second = CAREER_DATA.get(second_name.lower())

        if first is None or second is None:
            available = [
                career["title"]
                for career in CAREER_DATA.values()
            ]

            return Response({
                "error": "One or both careers are not available.",
                "available_careers": available,
            }, status=400)

        first_skills = set(first["required_skills"])
        second_skills = set(second["required_skills"])

        common_skills = sorted(first_skills & second_skills)

        result = {
            "career_1": first,
            "career_2": second,
            "comparison": {
                "common_skills": common_skills,
                "career_1_unique_skills": sorted(
                    first_skills - second_skills
                ),
                "career_2_unique_skills": sorted(
                    second_skills - first_skills
                ),
                "estimated_learning_months": {
                    first["title"]: first["learning_months"],
                    second["title"]: second["learning_months"],
                },
                "note": (
                    "Learning durations are illustrative estimates, "
                    "not guaranteed completion times."
                ),
            },
        }

        return Response(result)