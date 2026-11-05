
from django.urls import path

from .views import (
    FeedbackListCreateAPIView,
    FeedbackDetailAPIView,
)


urlpatterns = [
    path(
        "",
        FeedbackListCreateAPIView.as_view(),
        name="feedback-list-create",
    ),
    path(
        "<int:feedback_id>/",
        FeedbackDetailAPIView.as_view(),
        name="feedback-detail",
    ),
]
