
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserPreferences
from .serializers import UserPreferencesSerializer


class UserPreferencesView(APIView):
    permission_classes = [IsAuthenticated]

    def get_user_preferences(self, user):
        preferences, _ = UserPreferences.objects.get_or_create(
            user=user
        )
        return preferences

    def get(self, request):
        preferences = self.get_user_preferences(request.user)
        serializer = UserPreferencesSerializer(preferences)

        return Response(serializer.data)

    def put(self, request):
        preferences = self.get_user_preferences(request.user)

        serializer = UserPreferencesSerializer(
            preferences,
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "message": "Preferences saved successfully.",
            "preferences": serializer.data,
        })

    def patch(self, request):
        preferences = self.get_user_preferences(request.user)

        serializer = UserPreferencesSerializer(
            preferences,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "message": "Preferences updated successfully.",
            "preferences": serializer.data,
        })
