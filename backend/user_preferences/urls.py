
from django.urls import path

from .views import UserPreferencesView
from .system_settings_views import AdminSystemSettingsAPIView

urlpatterns = [
    path("", UserPreferencesView.as_view(), name="user-preferences"),
    path(
        "system/",
        AdminSystemSettingsAPIView.as_view(),
        name="admin-system-settings",
    ),
]
