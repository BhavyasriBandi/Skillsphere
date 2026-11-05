
from django.contrib import admin

from .models import UserPreferences
from .system_settings_models import SystemSettings


@admin.register(UserPreferences)
class UserPreferencesAdmin(admin.ModelAdmin):
    list_display = ("user", "language", "theme", "updated_at")


@admin.register(SystemSettings)
class SystemSettingsAdmin(admin.ModelAdmin):
    list_display = (
        "platform_name",
        "maintenance_mode",
        "allow_registration",
        "updated_at",
    )

    def has_add_permission(self, request):
        return not SystemSettings.objects.exists()
