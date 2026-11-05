
from django.urls import path

from .views import (
    LearningResourceListCreateAPIView,
    LearningResourceDetailAPIView,
)

urlpatterns = [
    path(
        "",
        LearningResourceListCreateAPIView.as_view(),
        name="learning-resource-list-create",
    ),
    path(
        "<int:pk>/",
        LearningResourceDetailAPIView.as_view(),
        name="learning-resource-detail",
    ),
]
