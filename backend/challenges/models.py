
from django.db import models


class Challenge(models.Model):
    DIFFICULTY_CHOICES = [
        ("Beginner", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Advanced", "Advanced"),
    ]

    CHALLENGE_TYPE_CHOICES = [
        ("Coding", "Coding"),
        ("Quiz", "Quiz"),
        ("Project", "Project"),
        ("Problem Solving", "Problem Solving"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100, default="Programming")
    challenge_type = models.CharField(
        max_length=30,
        choices=CHALLENGE_TYPE_CHOICES,
        default="Coding",
    )
    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
        default="Beginner",
    )
    points = models.PositiveIntegerField(default=100)
    duration_minutes = models.PositiveIntegerField(default=30)
    instructions = models.TextField(blank=True)
    starter_code = models.TextField(blank=True)
    test_cases = models.JSONField(default=list, blank=True)
    skills = models.JSONField(default=list, blank=True)
    is_active = models.BooleanField(default=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
