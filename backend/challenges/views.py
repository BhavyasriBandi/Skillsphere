
from rest_framework import generics
from rest_framework.permissions import BasePermission, IsAuthenticated

from .models import Challenge
from .serializers import ChallengeSerializer


class IsAdminOrReadOnly(BasePermission):
    """
    Authenticated users can view active challenges.
    Staff users can create, update, and delete challenges.
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True

        return request.user.is_staff


class ChallengeListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ChallengeSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = Challenge.objects.all()

        if self.request.user.is_staff:
            return queryset

        return queryset.filter(is_active=True)


class ChallengeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChallengeSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = Challenge.objects.all()

        if self.request.user.is_staff:
            return queryset

        return queryset.filter(is_active=True)
