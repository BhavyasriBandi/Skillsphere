from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LeaderboardSerializer


# Sample data only. These are not live student rankings.
SAMPLE_LEADERBOARD = [
    {
        "student_id": 101,
        "student_name": "Student One",
        "completed_assessments": 8,
        "completed_goals": 6,
        "points": 140,
    },
    {
        "student_id": 102,
        "student_name": "Student Two",
        "completed_assessments": 6,
        "completed_goals": 7,
        "points": 125,
    },
    {
        "student_id": 103,
        "student_name": "Student Three",
        "completed_assessments": 5,
        "completed_goals": 5,
        "points": 95,
    },
]


class LeaderboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Sort by points, then completed assessments.
        sorted_students = sorted(
            SAMPLE_LEADERBOARD,
            key=lambda student: (
                student["points"],
                student["completed_assessments"],
            ),
            reverse=True,
        )

        ranked_students = []

        for rank, student in enumerate(sorted_students, start=1):
            ranked_students.append({
                "rank": rank,
                **student,
            })

        serializer = LeaderboardSerializer(
            ranked_students,
            many=True,
        )

        return Response({
            "count": len(ranked_students),
            "results": serializer.data,
            "notice": (
                "These are sample rankings, not actual student results."
            ),
        })


class MyLeaderboardPositionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # The sample records do not contain real authenticated user IDs.
        return Response({
            "message": (
                "Your personal rank is not available until the "
                "leaderboard is connected to actual student progress."
            )
        })
