from django.urls import path
from .views import ReportsAnalyticsAPIView

urlpatterns = [
    path(
        "analytics/",
        ReportsAnalyticsAPIView.as_view(),
        name="reports-analytics",
    ),
]
