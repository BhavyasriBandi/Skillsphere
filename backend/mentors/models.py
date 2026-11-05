
from django.conf import settings
from django.db import models


# =====================================================
# MENTOR-STUDENT ASSIGNMENT
# =====================================================

class MentorStudentAssignment(models.Model):

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Active", "Active"),
        ("Rejected", "Rejected"),
    ]

    SOURCE_CHOICES = [
        ("Admin", "Admin"),
        ("Student Request", "Student Request"),
    ]

    mentor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="mentor_assignments",
    )

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student_mentor_assignments",
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending",
    )

    source = models.CharField(
        max_length=30,
        choices=SOURCE_CHOICES,
        default="Student Request",
    )

    assigned_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-assigned_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["mentor", "student"],
                name="unique_mentor_student_assignment",
            )
        ]

    def __str__(self):
        return f"{self.mentor} - {self.student} ({self.status})"


# =====================================================
# MENTOR PROFILE
# =====================================================

class MentorProfile(models.Model):

    mentor = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="mentor_profile",
    )

    phone = models.CharField(
        max_length=30,
        blank=True,
        default="",
    )

    location = models.CharField(
        max_length=255,
        blank=True,
        default="",
    )

    qualification = models.CharField(
        max_length=150,
        blank=True,
        default="",
    )

    college = models.CharField(
        max_length=255,
        blank=True,
        default="",
    )

    specialization = models.CharField(
        max_length=150,
        blank=True,
        default="",
    )

    expertise = models.TextField(
        blank=True,
        default="",
    )

    skills = models.TextField(
        blank=True,
        default="",
    )

    experience = models.PositiveSmallIntegerField(default=0)

    bio = models.TextField(
        max_length=1000,
        blank=True,
        default="",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return f"Mentor Profile - {self.mentor.email}"


# =====================================================
# MENTOR TO STUDENT FEEDBACK
# =====================================================

class MentorFeedback(models.Model):

    mentor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="given_mentor_feedback",
    )

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="received_mentor_feedback",
    )

    subject = models.CharField(max_length=200)

    feedback = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"{self.mentor} - {self.student} - {self.subject}"
        )


# =====================================================
# MENTOR AND STUDENT MESSAGES
# =====================================================

class MentorMessage(models.Model):

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_mentor_messages",
    )

    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="received_mentor_messages",
    )

    message = models.TextField()

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.sender} to {self.recipient}"
