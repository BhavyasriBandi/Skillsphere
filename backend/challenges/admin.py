
from django.contrib import admin
from .models import Challenge


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "challenge_type",
        "difficulty",
        "points",
        "is_active",
        "created_at",
    )

    list_filter = (
        "category",
        "challenge_type",
        "difficulty",
        "is_active",
    )

    search_fields = (
        "title",
        "description",
        "category",
    )

    list_editable = ("is_active",)
    readonly_fields = ("created_at", "updated_at")
