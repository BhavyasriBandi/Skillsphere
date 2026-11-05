
import secrets

from django.conf import settings
from django.db import models
from django.utils import timezone


class EmailVerificationCode(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="email_verification_codes",
    )
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)

    @classmethod
    def generate_code(cls):
        return f"{secrets.randbelow(1_000_000):06d}"

    @property
    def is_expired(self):
        return timezone.now() >= self.expires_at

    def __str__(self):
        return f"Email verification for {self.user.email}"


class StudentProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student_profile",
    )
    phone = models.CharField(max_length=30, blank=True)
    college = models.CharField(max_length=255, blank=True)
    qualification = models.CharField(max_length=120, blank=True)
    branch = models.CharField(max_length=120, blank=True)
    graduation_year = models.CharField(max_length=4, blank=True)
    location = models.CharField(max_length=255, blank=True)
    career_interest = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile - {self.user.email}"
