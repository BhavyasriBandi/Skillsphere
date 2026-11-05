
from rest_framework import serializers

from .system_settings_models import SystemSettings


class SystemSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSettings
        fields = [
            "id",
            "platform_name",
            "platform_tagline",
            "support_email",
            "allow_registration",
            "require_email_verification",
            "maintenance_mode",
            "email_notifications",
            "learning_reminders",
            "weekly_summary",
            "minimum_password_length",
            "session_timeout_minutes",
            "updated_at",
        ]
        read_only_fields = ["id", "updated_at"]

    def validate_platform_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError(
                "Platform name cannot be empty."
            )
        return value

    def validate_minimum_password_length(self, value):
        if not 8 <= value <= 128:
            raise serializers.ValidationError(
                "Password length must be between 8 and 128."
            )
        return value

    def validate_session_timeout_minutes(self, value):
        if not 5 <= value <= 1440:
            raise serializers.ValidationError(
                "Session timeout must be between 5 and 1440 minutes."
            )
        return value
