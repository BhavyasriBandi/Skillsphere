from django.urls import path

from .views import (
    JobOpportunityListView,
    JobOpportunityDetailView,
)

urlpatterns = [
    path(
        "",
        JobOpportunityListView.as_view(),
        name="job-opportunity-list",
    ),
    path(
        "<int:job_id>/",
        JobOpportunityDetailView.as_view(),
        name="job-opportunity-detail",
    ),
]