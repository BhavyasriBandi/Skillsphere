
from django.urls import path

from .views import (
    ActivityFeedAPIView,
    ActivityFeedCreateAPIView,
)


urlpatterns = [
    path(
        "",
        ActivityFeedAPIView.as_view(),
        name="activity-feed",
    ),
    path(
        "create/",
        ActivityFeedCreateAPIView.as_view(),
        name="activity-feed-create",
    ),
]
