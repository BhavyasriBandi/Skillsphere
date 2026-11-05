
from django.urls import path

from .views import (
    ManagedFileListCreateAPIView,
    ManagedFileDetailAPIView,
    ManagedFileDownloadAPIView,
)

urlpatterns = [
    path("", ManagedFileListCreateAPIView.as_view(), name="file-list-create"),
    path("<int:pk>/", ManagedFileDetailAPIView.as_view(), name="file-detail"),
    path(
        "<int:file_id>/download/",
        ManagedFileDownloadAPIView.as_view(),
        name="file-download",
    ),
]
