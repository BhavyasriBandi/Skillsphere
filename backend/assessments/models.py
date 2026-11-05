
from django.conf import settings
from django.db import models


class AssessmentResult(models.Model):
    LEVEL_CHOICES = [
        ("Beginner", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Advanced", "Advanced"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="assessment_results",
    )
    skill = models.CharField(max_length=100)
    total_questions = models.PositiveIntegerField()
    correct_answers = models.PositiveIntegerField()
    score_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    estimated_level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Assessment Result"
        verbose_name_plural = "Assessment Results"

    def __str__(self):
        return f"{self.user} - {self.skill} - {self.score_percentage}%"


class AssessmentQuestion(models.Model):
    legacy_id = models.CharField(
        max_length=30,
        unique=True,
        null=True,
        blank=True,
    )
    skill = models.CharField(max_length=100, db_index=True)
    question = models.TextField()
    options = models.JSONField()
    correct_answer = models.PositiveSmallIntegerField()
    explanation = models.TextField(blank=True, default="")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.skill}: {self.question[:70]}"

    def clean(self):
        from django.core.exceptions import ValidationError

        if not isinstance(self.options, list) or len(self.options) < 2:
            raise ValidationError({
                "options": "Provide at least two answer options."
            })

        if not all(
            isinstance(option, str) and option.strip()
            for option in self.options
        ):
            raise ValidationError({
                "options": "Every option must contain text."
            })

        if (
            self.correct_answer < 0
            or self.correct_answer >= len(self.options)
        ):
            raise ValidationError({
                "correct_answer": "Correct answer index is outside the options."
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
