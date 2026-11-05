
from django.conf import settings
from django.db import models


class LearningResource(models.Model):
    CATEGORY_CHOICES = [
        ("Programming", "Programming"),
        ("Web Development", "Web Development"),
        ("Database", "Database"),
        ("Tools", "Tools"),
        ("Computer Science", "Computer Science"),
    ]

    LEVEL_CHOICES = [
        ("Beginner", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Advanced", "Advanced"),
    ]

    TYPE_CHOICES = [
        ("Course", "Course"),
        ("Tutorial", "Tutorial"),
        ("Documentation", "Documentation"),
        ("Practice", "Practice"),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
    )
    skill = models.CharField(max_length=100)
    level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default="Beginner",
    )
    resource_type = models.CharField(
        max_length=30,
        choices=TYPE_CHOICES,
        default="Tutorial",
    )
    description = models.TextField()
    url = models.URLField(max_length=500)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
