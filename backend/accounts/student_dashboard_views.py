
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsStudent


class StudentDashboardAPIView(APIView):
    """
    Return dashboard information for the currently authenticated student.
    The data is scoped to request.user; students cannot access another
    student's dashboard data through this endpoint.
    """
    permission_classes = [IsAuthenticated, IsStudent]

    def get(self, request):
        user = request.user
        full_name = (
            f"{user.first_name} {user.last_name}".strip()
            or user.get_username()
        )

        return Response({
            "student": {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "full_name": full_name,
                "email": user.email,
                "role": "Student",
            },
            "stats": {
                "skills_assessed": 0,
                "roadmap_progress": 0,
                "tasks_completed": 0,
                "total_tasks": 0,
                "achievements": 0,
            },
            "tasks": [],
            "roadmap": [],
        })
