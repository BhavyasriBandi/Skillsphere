
from django.conf import settings
from django.db import models

from .system_settings_models import SystemSettings

class UserPreferences(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="skillsphere_preferences",
    )

    learning_format = models.CharField(
        max_length=20,
        default="Mixed",
    )

    career_interests = models.JSONField(default=list, blank=True)

    email_notifications = models.BooleanField(default=True)
    learning_reminders = models.BooleanField(default=True)
    weekly_summary = models.BooleanField(default=True)

    language = models.CharField(
        max_length=30,
        default="English",
    )

    theme = models.CharField(
        max_length=20,
        default="light",
    )

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Preferences for {self.user}"
