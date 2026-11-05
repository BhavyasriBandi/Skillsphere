
from django.urls import path

from .views import (
    StudentProjectListCreateAPIView,
    StudentProjectDetailAPIView,
    AdminProjectListCreateAPIView,
    AdminProjectDetailAPIView,
)

urlpatterns = [
    # Existing student routes.
    path(
        "",
        StudentProjectListCreateAPIView.as_view(),
        name="student-project-list-create",
    ),
    path(
        "<int:id>/",
        StudentProjectDetailAPIView.as_view(),
        name="student-project-detail",
    ),

    # New admin routes.
    path(
        "admin/",
        AdminProjectListCreateAPIView.as_view(),
        name="admin-project-list-create",
    ),
    path(
        "admin/<int:id>/",
        AdminProjectDetailAPIView.as_view(),
        name="admin-project-detail",
    ),
]
