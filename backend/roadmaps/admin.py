
from django.contrib import admin
from .models import Roadmap


@admin.register(Roadmap)
class RoadmapAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "target_role",
        "level",
        "duration",
        "is_active",
        "created_at",
    )
    list_filter = ("level", "category", "is_active")
    search_fields = ("title", "target_role", "category")
    list_editable = ("is_active",)
