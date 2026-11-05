
from django.urls import path

from .views import (
    LearningGoalListCreateAPIView,
    LearningGoalDetailAPIView,
    CareerGoalAPIView,
)


urlpatterns = [
    path(
        "career-goal/",
        CareerGoalAPIView.as_view(),
        name="career-goal",
    ),
    path(
        "",
        LearningGoalListCreateAPIView.as_view(),
        name="learning-goal-list-create",
    ),
    path(
        "<int:goal_id>/",
        LearningGoalDetailAPIView.as_view(),
        name="learning-goal-detail",
    ),
]
