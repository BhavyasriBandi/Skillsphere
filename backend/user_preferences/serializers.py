
from rest_framework import serializers

from .models import UserPreferences


class UserPreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPreferences
        fields = [
            "learning_format",
            "career_interests",
            "email_notifications",
            "learning_reminders",
            "weekly_summary",
            "language",
            "theme",
        ]
        extra_kwargs = {
            "learning_format": {"required": False},
            "career_interests": {"required": False},
            "email_notifications": {"required": False},
            "learning_reminders": {"required": False},
            "weekly_summary": {"required": False},
            "language": {"required": False},
            "theme": {"required": False},
        }
