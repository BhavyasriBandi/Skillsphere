
from django.urls import path

from .views import (
    CareerListAPIView,
    CareerDetailAPIView,
    CareerRecommendationsAPIView,
    MyCareerRecommendationsAPIView,
    CareerRoadmapAPIView,
    RoadmapTaskProgressAPIView,
)

urlpatterns = [
    path("", CareerListAPIView.as_view(), name="career-list"),

    path(
        "<int:career_id>/",
        CareerDetailAPIView.as_view(),
        name="career-detail",
    ),

    path(
        "recommendations/",
        CareerRecommendationsAPIView.as_view(),
        name="career-recommendations",
    ),

    path(
        "my-recommendations/",
        MyCareerRecommendationsAPIView.as_view(),
        name="my-career-recommendations",
    ),

    path(
        "roadmap/",
        CareerRoadmapAPIView.as_view(),
        name="career-roadmap",
    ),

    path(
        "roadmap-progress/",
        RoadmapTaskProgressAPIView.as_view(),
        name="roadmap-task-progress",
    ),
]
