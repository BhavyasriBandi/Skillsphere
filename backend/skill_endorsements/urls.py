
from django.urls import path

from .views import (
    SkillEndorsementListCreateAPIView,
    SkillEndorsementDetailAPIView,
)


urlpatterns = [
    path(
        "",
        SkillEndorsementListCreateAPIView.as_view(),
        name="skill-endorsement-list-create",
    ),
    path(
        "<int:endorsement_id>/",
        SkillEndorsementDetailAPIView.as_view(),
        name="skill-endorsement-detail",
    ),
]
