
from django.urls import path

from .views import (
    TaskListCreateAPIView,
    TaskDetailAPIView,
    AssignmentSubmissionAPIView,
    TaskReviewAPIView,
)


urlpatterns = [
    path(
        "",
        TaskListCreateAPIView.as_view(),
        name="task-list-create",
    ),
    path(
        "<int:task_id>/",
        TaskDetailAPIView.as_view(),
        name="task-detail",
    ),
    path(
        "<int:task_id>/submit/",
        AssignmentSubmissionAPIView.as_view(),
        name="assignment-submit",
    ),
    path(
        "<int:task_id>/review/",
        TaskReviewAPIView.as_view(),
        name="task-review",
    ),
]
