
from django.contrib import admin

from .models import Achievement, StudentAchievement


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "badge_key",
        "category",
        "tier",
        "points",
        "is_active",
    )
    list_filter = ("category", "tier", "is_active")
    search_fields = ("title", "badge_key", "description")
    ordering = ("category", "id")


@admin.register(StudentAchievement)
class StudentAchievementAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "achievement",
        "is_earned",
        "is_saved",
        "earned_at",
        "saved_at",
    )
    list_filter = ("is_earned", "is_saved", "achievement__category")
    search_fields = (
        "student__username",
        "student__email",
        "achievement__title",
        "achievement__badge_key",
    )
    readonly_fields = ("created_at", "updated_at")
    list_select_related = ("student", "achievement")
