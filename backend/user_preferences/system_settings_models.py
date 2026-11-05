
from django.db import models


class SystemSettings(models.Model):
    platform_name = models.CharField(
        max_length=100,
        default="SkillSphere",
    )
    platform_tagline = models.CharField(
        max_length=255,
        default="Know Your Skills, Shape Your Future",
    )
    support_email = models.EmailField(
        blank=True,
        default="",
    )

    allow_registration = models.BooleanField(default=True)
    require_email_verification = models.BooleanField(default=True)
    maintenance_mode = models.BooleanField(default=False)

    email_notifications = models.BooleanField(default=True)
    learning_reminders = models.BooleanField(default=True)
    weekly_summary = models.BooleanField(default=True)

    minimum_password_length = models.PositiveSmallIntegerField(
        default=8,
    )
    session_timeout_minutes = models.PositiveIntegerField(
        default=60,
    )

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.platform_name

    @classmethod
    def get_settings(cls):
        instance, _ = cls.objects.get_or_create(pk=1)
        return instance
