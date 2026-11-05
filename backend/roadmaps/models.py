
from django.db import models


class Roadmap(models.Model):
    LEVEL_CHOICES = [
        ("Beginner", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Advanced", "Advanced"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100)
    target_role = models.CharField(max_length=150)
    level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default="Beginner",
    )
    duration = models.CharField(max_length=100)
    skills = models.JSONField(default=list, blank=True)
    learning_steps = models.JSONField(default=list, blank=True)
    image_url = models.URLField(max_length=500, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
