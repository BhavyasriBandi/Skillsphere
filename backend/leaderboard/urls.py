from django.urls import path

from .views import (
    LeaderboardView,
    MyLeaderboardPositionView,
)

urlpatterns = [
    path("", LeaderboardView.as_view(), name="leaderboard"),
    path(
        "my-position/",
        MyLeaderboardPositionView.as_view(),
        name="my-leaderboard-position",
    ),
]
