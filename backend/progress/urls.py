
from django.urls import path

from .views import (
    ProgressSummaryAPIView,
    SkillProgressListAPIView,
    CareerReadinessAPIView,
    AchievementsAPIView,
)
from .learning_hub_views import LearningHubProgressAPIView
from .challenge_progress_views import ChallengeProgressAPIView


urlpatterns = [
    path(
        "summary/",
        ProgressSummaryAPIView.as_view(),
        name="progress-summary",
    ),
    path(
        "skills/",
        SkillProgressListAPIView.as_view(),
        name="student-skill-progress",
    ),
    path(
        "career-readiness/",
        CareerReadinessAPIView.as_view(),
        name="career-readiness",
    ),
    path(
        "achievements/",
        AchievementsAPIView.as_view(),
        name="student-achievements",
    ),
    path(
        "learning-hub/",
        LearningHubProgressAPIView.as_view(),
        name="learning-hub-progress",
    ),
    path(
        "challenges/",
        ChallengeProgressAPIView.as_view(),
        name="challenge-progress",
    ),
]
