
from django.urls import path

from .views import (
    AchievementListView,
    AwardAchievementView,
    AchievementDetailView,
    SaveAchievementView,
    AdminAchievementListCreateView,
    AdminAchievementDetailView,
    AdminAchievementActivationView,
)

urlpatterns = [
    # Existing student APIs
    path("", AchievementListView.as_view(), name="achievement-list"),
    path("award/", AwardAchievementView.as_view(), name="award-achievement"),
    path(
        "<int:achievement_id>/",
        AchievementDetailView.as_view(),
        name="achievement-detail",
    ),
    path(
        "<int:achievement_id>/save/",
        SaveAchievementView.as_view(),
        name="save-achievement",
    ),

    # New admin APIs
    path(
        "admin/",
        AdminAchievementListCreateView.as_view(),
        name="admin-achievement-list-create",
    ),
    path(
        "admin/<int:achievement_id>/",
        AdminAchievementDetailView.as_view(),
        name="admin-achievement-detail",
    ),
    path(
        "admin/<int:achievement_id>/activation/",
        AdminAchievementActivationView.as_view(),
        name="admin-achievement-activation",
    ),
]
