
from django.conf import settings
from django.db import models


class Portfolio(models.Model):
    student = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="portfolio",
    )

    # Personal information
    full_name = models.CharField(max_length=150)
    professional_title = models.CharField(
        max_length=150,
        default="Aspiring Software Developer",
    )
    email = models.EmailField(blank=True, default="")
    location = models.CharField(max_length=200, blank=True, default="")
    phone = models.CharField(max_length=30, blank=True, default="")
    summary = models.TextField(max_length=2000, blank=True, default="")

    # Portfolio content
    skills = models.TextField(
        blank=True,
        default="Python, Java, JavaScript, React, Django, SQL",
    )
    education = models.JSONField(default=list, blank=True)
    projects = models.JSONField(default=list, blank=True)
    certifications = models.TextField(blank=True, default="")

    # Optional professional links
    resume_url = models.URLField(blank=True, default="")
    portfolio_url = models.URLField(blank=True, default="")
    github_url = models.URLField(blank=True, default="")
    linkedin_url = models.URLField(blank=True, default="")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return f"{self.full_name} - Portfolio"
