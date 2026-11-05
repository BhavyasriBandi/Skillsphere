
from django.urls import path

from .views import (
    LearningResourceListAPIView,
    LearningResourceDetailAPIView,
    RecommendedResourcesAPIView,
)


urlpatterns = [
    path(
        "recommended/",
        RecommendedResourcesAPIView.as_view(),
        name="recommended-resources",
    ),
    path(
        "",
        LearningResourceListAPIView.as_view(),
        name="resource-list",
    ),
    path(
        "<int:resource_id>/",
        LearningResourceDetailAPIView.as_view(),
        name="resource-detail",
    ),
]
