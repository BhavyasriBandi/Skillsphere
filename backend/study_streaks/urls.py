from django.urls import path

from .views import StudyStreakView, RecordStudyDayView


urlpatterns = [
    path("", StudyStreakView.as_view(), name="study-streak"),
    path(
        "record/",
        RecordStudyDayView.as_view(),
        name="record-study-day",
    ),
]