from django.urls import path

from .views import (
    BookmarkListCreateView,
    BookmarkDetailView,
)

urlpatterns = [
    path(
        "",
        BookmarkListCreateView.as_view(),
        name="bookmark-list-create",
    ),
    path(
        "<int:bookmark_id>/",
        BookmarkDetailView.as_view(),
        name="bookmark-detail",
    ),
]