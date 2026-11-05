
from django.contrib import admin

from .models import (
    SkillCategory,
    Skill,
    StudentSkill,
    SkillAssessmentResult,
    AssessmentQuestion,
    AssessmentAttempt,
)


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "is_active")
    list_filter = ("category", "is_active")
    search_fields = ("name",)


@admin.register(StudentSkill)
class StudentSkillAdmin(admin.ModelAdmin):
    list_display = ("user", "skill", "proficiency", "updated_at")
    list_filter = ("proficiency",)
    search_fields = ("user__username", "skill__name")


@admin.register(SkillAssessmentResult)
class SkillAssessmentResultAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "skill",
        "score",
        "total_questions",
        "percentage",
        "completed_at",
    )
    list_filter = ("skill",)
    search_fields = ("user__username", "skill__name")
    readonly_fields = ("completed_at",)


@admin.register(AssessmentQuestion)
class AssessmentQuestionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "skill",
        "question_text",
        "difficulty",
        "is_active",
        "created_at",
    )
    list_filter = ("skill", "difficulty", "is_active")
    search_fields = ("question_text", "skill__name")
    list_editable = ("difficulty", "is_active")
    readonly_fields = ("created_at",)


@admin.register(AssessmentAttempt)
class AssessmentAttemptAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "skill",
        "score",
        "total_questions",
        "percentage",
        "is_completed",
        "started_at",
    )
    list_filter = ("skill", "is_completed")
    search_fields = ("user__username", "skill__name")
    readonly_fields = (
        "user",
        "skill",
        "score",
        "total_questions",
        "percentage",
        "submitted_answers",
        "started_at",
        "completed_at",
    )
