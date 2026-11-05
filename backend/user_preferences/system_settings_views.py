
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from accounts.views import get_user_role

from .system_settings_models import SystemSettings
from .system_settings_serializers import SystemSettingsSerializer


class AdminSystemSettingsAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = SystemSettingsSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "put", "patch", "head", "options"]

    def get_object(self):
        if get_user_role(self.request.user) != "Admin":
            raise PermissionDenied(
                "Only administrators can manage system settings."
            )

        return SystemSettings.get_settings()
