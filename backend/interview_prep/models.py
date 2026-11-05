
from django.conf import settings
from django.db import models


class InterviewQuestion(models.Model):
    CATEGORY_CHOICES = [
        ("Python", "Python"),
        ("Java", "Java"),
        ("C", "C"),
        ("SQL", "SQL"),
        ("React", "React"),
        ("Django", "Django"),
        ("Data Structures", "Data Structures"),
        ("Web Development", "Web Development"),
        ("HR", "HR"),
        ("Aptitude", "Aptitude"),
        ("Other", "Other"),
    ]

    DIFFICULTY_CHOICES = [
        ("Beginner", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Advanced", "Advanced"),
    ]

    question = models.TextField()
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="Other",
    )
    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
        default="Beginner",
    )
    suggested_answer = models.TextField(blank=True, default="")
    explanation = models.TextField(blank=True, default="")
    keywords = models.JSONField(default=list, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["category", "difficulty", "id"]

    def __str__(self):
        return f"{self.category}: {self.question[:60]}"


class InterviewPractice(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="interview_practices",
    )
    question = models.ForeignKey(
        InterviewQuestion,
        on_delete=models.CASCADE,
        related_name="student_practices",
    )
    student_answer = models.TextField(blank=True, default="")
    is_practiced = models.BooleanField(default=False)
    is_bookmarked = models.BooleanField(default=False)
    last_practiced_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["student", "question"],
                name="unique_student_interview_question",
            )
        ]

    def __str__(self):
        return f"{self.student} - {self.question.question[:50]}"
