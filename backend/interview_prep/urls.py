
from django.urls import path

from .views import (
    InterviewQuestionListView,
    InterviewPracticeListCreateView,
    InterviewPracticeDetailView,
    InterviewPracticeMarkView,
    AdminInterviewQuestionListCreateView,
    AdminInterviewQuestionDetailView,
)

urlpatterns = [
    # Student: interview questions
    path(
        "questions/",
        InterviewQuestionListView.as_view(),
        name="interview-question-list",
    ),

    # Student: practice records
    path(
        "practice/",
        InterviewPracticeListCreateView.as_view(),
        name="interview-practice-list-create",
    ),
    path(
        "practice/<int:pk>/",
        InterviewPracticeDetailView.as_view(),
        name="interview-practice-detail",
    ),
    path(
        "practice/<int:pk>/mark/",
        InterviewPracticeMarkView.as_view(),
        name="interview-practice-mark",
    ),

    # Admin: manage interview questions
    path(
        "admin/questions/",
        AdminInterviewQuestionListCreateView.as_view(),
        name="admin-interview-question-list-create",
    ),
    path(
        "admin/questions/<int:pk>/",
        AdminInterviewQuestionDetailView.as_view(),
        name="admin-interview-question-detail",
    ),
]
