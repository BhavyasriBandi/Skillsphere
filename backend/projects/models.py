from django.conf import settings
from django.db import models


class StudentProject(models.Model):
    STATUS_CHOICES = [
        ("Planning", "Planning"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
        ("On Hold", "On Hold"),
    ]

    CATEGORY_CHOICES = [
        ("Web Development", "Web Development"),
        ("Full Stack", "Full Stack"),
        ("AI / Machine Learning", "AI / Machine Learning"),
        ("Data Science", "Data Science"),
        ("Mobile Development", "Mobile Development"),
        ("Database", "Database"),
        ("Other", "Other"),
    ]

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student_projects",
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="Web Development",
    )

    technologies = models.JSONField(
        default=list,
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Planning",
    )

    github = models.URLField(
        max_length=500,
        blank=True,
        default="",
    )

    live_demo = models.URLField(
        max_length=500,
        blank=True,
        default="",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-created_at", "-id"]

    def __str__(self):
        return f"{self.title} - {self.student}"