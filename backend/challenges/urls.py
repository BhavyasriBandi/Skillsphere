
from django.urls import path

from .views import (
    ChallengeListCreateAPIView,
    ChallengeDetailAPIView,
)

urlpatterns = [
    path("", ChallengeListCreateAPIView.as_view(), name="challenge-list-create"),
    path("<int:pk>/", ChallengeDetailAPIView.as_view(), name="challenge-detail"),
]
