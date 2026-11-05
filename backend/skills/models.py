
from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError


class SkillCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Skill categories"

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(
        SkillCategory,
        on_delete=models.PROTECT,
        related_name="skills",
    )
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class StudentSkill(models.Model):
    PROFICIENCY_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student_skills",
    )
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name="student_skills",
    )
    proficiency = models.CharField(
        max_length=20,
        choices=PROFICIENCY_CHOICES,
        default="beginner",
    )
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["skill__name"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "skill"],
                name="unique_user_skill",
            )
        ]

    def __str__(self):
        return f"{self.user} - {self.skill}"


class AssessmentQuestion(models.Model):
    DIFFICULTY_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
    ]

    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name="assessment_questions",
    )
    question_text = models.TextField()
    options = models.JSONField(
        help_text="Store exactly four answer options as a JSON list."
    )
    correct_answer = models.PositiveSmallIntegerField(
        help_text="Correct option index: 0, 1, 2 or 3."
    )
    explanation = models.TextField(blank=True)
    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
        default="beginner",
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["skill__name", "-created_at"]

    def clean(self):
        if not isinstance(self.options, list) or len(self.options) != 4:
            raise ValidationError({
                "options": "Exactly four options must be provided."
            })

        if not all(
            isinstance(option, str) and option.strip()
            for option in self.options
        ):
            raise ValidationError({
                "options": "All four options must be non-empty strings."
            })

        if self.correct_answer not in range(4):
            raise ValidationError({
                "correct_answer": "Correct answer must be between 0 and 3."
            })

    def __str__(self):
        return f"{self.skill.name} - {self.question_text[:60]}"


class AssessmentAttempt(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="assessment_attempts",
    )
    skill = models.ForeignKey(
        Skill,
        on_delete=models.PROTECT,
        related_name="assessment_attempts",
    )
    questions = models.ManyToManyField(
        AssessmentQuestion,
        related_name="attempts",
    )

    # Preserves the exact question order displayed to React.
    question_order = models.JSONField(default=list, blank=True)

    score = models.PositiveSmallIntegerField(default=0)
    total_questions = models.PositiveSmallIntegerField(default=10)
    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
    )
    submitted_answers = models.JSONField(default=list)
    is_completed = models.BooleanField(default=False)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-started_at"]

    def __str__(self):
        return f"{self.user} - {self.skill.name} - Attempt {self.pk}"


class SkillAssessmentResult(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="skill_assessment_results",
    )
    skill = models.ForeignKey(
        Skill,
        on_delete=models.PROTECT,
        related_name="assessment_results",
    )
    score = models.PositiveSmallIntegerField()
    total_questions = models.PositiveSmallIntegerField()
    percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
    answers = models.JSONField(default=list)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-completed_at"]

    def __str__(self):
        return f"{self.user} - {self.skill.name}: {self.percentage}%"
