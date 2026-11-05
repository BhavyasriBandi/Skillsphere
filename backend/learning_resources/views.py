
from rest_framework import generics
from rest_framework.permissions import BasePermission, IsAuthenticated

from .models import LearningResource
from .serializers import LearningResourceSerializer


class IsAdminOrReadOnly(BasePermission):
    """
    Authenticated users can read resources.
    Only staff admins can create, update, or delete resources.
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True

        return request.user.is_staff


class LearningResourceListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = LearningResourceSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = LearningResource.objects.all().order_by("-created_at")

        if self.request.user.is_staff:
            return queryset

        return queryset.filter(is_active=True)


class LearningResourceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LearningResourceSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    queryset = LearningResource.objects.all()
    lookup_field = "pk"

    def get_queryset(self):
        queryset = LearningResource.objects.all()

        if self.request.user.is_staff:
            return queryset

        return queryset.filter(is_active=True)
