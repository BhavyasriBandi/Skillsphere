
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from accounts.permissions import IsMentor
from roadmaps.models import Roadmap


class MentorRoadmapsAPIView(APIView):
    permission_classes = [IsAuthenticated, IsMentor]

    def get(self, request):
        roadmaps = Roadmap.objects.filter(
            is_active=True
        ).order_by("-created_at")

        # Optional search
        search = request.query_params.get("search", "").strip()

        if search:
            roadmaps = roadmaps.filter(
                title__icontains=search
            ) | roadmaps.filter(
                target_role__icontains=search
            ) | roadmaps.filter(
                category__icontains=search
            )

        # Optional level filter
        level = request.query_params.get("level", "").strip()

        if level:
            roadmaps = roadmaps.filter(level__iexact=level)

        roadmap_data = []

        for roadmap in roadmaps:
            roadmap_data.append({
                "id": roadmap.id,
                "title": roadmap.title,
                "description": roadmap.description,
                "category": roadmap.category,
                "target_role": roadmap.target_role,
                "level": roadmap.level,
                "duration": roadmap.duration,
                "skills": roadmap.skills or [],
                "learning_steps": roadmap.learning_steps or [],
                "image_url": roadmap.image_url,
                "created_at": roadmap.created_at,
                "updated_at": roadmap.updated_at,
            })

        return Response(
            {
                "count": len(roadmap_data),
                "roadmaps": roadmap_data,
            },
            status=status.HTTP_200_OK,
        )
