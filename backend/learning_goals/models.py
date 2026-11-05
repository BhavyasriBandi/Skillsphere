
from django.conf import settings
from django.db import models


class LearningGoal(models.Model):
    STATUS_CHOICES = [
        ("Not Started", "Not Started"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="learning_goals",
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    target_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Not Started",
    )
    progress_percentage = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["target_date", "id"]

    def __str__(self):
        return f"{self.title} - {self.user}"


class CareerGoal(models.Model):
    EXPERIENCE_CHOICES = [
        ("Beginner", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Advanced", "Advanced"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="career_goal",
    )
    career_role = models.CharField(max_length=200, blank=True, default="")
    domain = models.CharField(max_length=120, blank=True, default="")
    experience_level = models.CharField(
        max_length=20,
        choices=EXPERIENCE_CHOICES,
        default="Beginner",
    )
    target_date = models.DateField(null=True, blank=True)
    objective = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Career Goal - {self.user}"
