
from django.conf import settings
from django.db import models


class Achievement(models.Model):
    TIER_CHOICES = [
        ("bronze", "Bronze"),
        ("silver", "Silver"),
        ("gold", "Gold"),
    ]

    CATEGORY_CHOICES = [
        ("Career", "Career"),
        ("Assessment", "Assessment"),
        ("Projects", "Projects"),
        ("Challenges", "Challenges"),
        ("Learning", "Learning"),
        ("Interview", "Interview"),
        ("Skills", "Skills"),
        ("Roadmap", "Roadmap"),
        ("Special", "Special"),
    ]

    badge_key = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.CharField(max_length=20, default="🏆")
    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default="Special",
    )
    tier = models.CharField(
        max_length=10,
        choices=TIER_CHOICES,
        default="bronze",
    )
    requirement = models.CharField(max_length=50)
    target = models.PositiveIntegerField(default=1)
    points = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["category", "id"]

    def __str__(self):
        return self.title


class StudentAchievement(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student_achievements",
    )
    achievement = models.ForeignKey(
        Achievement,
        on_delete=models.CASCADE,
        related_name="student_records",
    )
    is_earned = models.BooleanField(default=False)
    is_saved = models.BooleanField(default=False)
    earned_at = models.DateTimeField(null=True, blank=True)
    saved_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-earned_at", "achievement__title"]
        constraints = [
            models.UniqueConstraint(
                fields=["student", "achievement"],
                name="unique_student_achievement",
            )
        ]

    def __str__(self):
        return f"{self.student} - {self.achievement.title}"
