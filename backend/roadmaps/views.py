
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, BasePermission

from .models import Roadmap
from .serializers import RoadmapSerializer


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True

        return request.user.is_staff


class RoadmapListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = RoadmapSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = Roadmap.objects.all()

        if self.request.user.is_staff:
            return queryset

        return queryset.filter(is_active=True)


class RoadmapDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoadmapSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    queryset = Roadmap.objects.all()

    def get_queryset(self):
        queryset = Roadmap.objects.all()

        if self.request.user.is_staff:
            return queryset

        return queryset.filter(is_active=True)
