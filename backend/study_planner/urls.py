
from django.urls import path

from .views import (
    StudySessionListCreateAPIView,
    StudySessionDetailAPIView,
)


urlpatterns = [
    path(
        "",
        StudySessionListCreateAPIView.as_view(),
        name="study-session-list-create",
    ),
    path(
        "<int:session_id>/",
        StudySessionDetailAPIView.as_view(),
        name="study-session-detail",
    ),
]
