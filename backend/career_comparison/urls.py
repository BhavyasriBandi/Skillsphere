from django.urls import path

from .views import CareerComparisonView


urlpatterns = [
    path(
        "",
        CareerComparisonView.as_view(),
        name="career-comparison",
    ),
]