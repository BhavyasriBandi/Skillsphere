
from django.urls import path

from .views import (
    RoadmapListCreateAPIView,
    RoadmapDetailAPIView,
)

urlpatterns = [
    path("", RoadmapListCreateAPIView.as_view(), name="roadmap-list-create"),
    path("<int:pk>/", RoadmapDetailAPIView.as_view(), name="roadmap-detail"),
]
