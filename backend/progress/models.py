
from django.conf import settings
from django.db import models


class LearningHubProgress(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="learning_hub_progress",
    )

    completed_lessons = models.JSONField(default=list, blank=True)
    saved_courses = models.JSONField(default=list, blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "learning_hub_progress"
        verbose_name = "Learning Hub Progress"
        verbose_name_plural = "Learning Hub Progress"

    def __str__(self):
        return f"Learning Hub Progress - {self.user}"


class ChallengeProgress(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="challenge_progress",
    )

    completed_ids = models.JSONField(default=list, blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "challenge_progress"
        verbose_name = "Challenge Progress"
        verbose_name_plural = "Challenge Progress"

    def __str__(self):
        return f"Challenge Progress - {self.user}"
