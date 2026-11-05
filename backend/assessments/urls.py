
from django.urls import path

from .views import (
    AssessmentQuestionsAPIView,
    AssessmentSubmitAPIView,
    AssessmentHistoryAPIView,
    SkillGapAnalysisAPIView,
)

from .admin_question_views import (
    AdminQuestionListCreateAPIView,
    AdminQuestionDetailAPIView,
)


urlpatterns = [
    # Student assessment APIs
    path(
        "questions/",
        AssessmentQuestionsAPIView.as_view(),
        name="assessment-questions",
    ),
    path(
        "submit/",
        AssessmentSubmitAPIView.as_view(),
        name="assessment-submit",
    ),
    path(
        "history/",
        AssessmentHistoryAPIView.as_view(),
        name="assessment-history",
    ),
    path(
        "skill-gap/",
        SkillGapAnalysisAPIView.as_view(),
        name="skill-gap-analysis",
    ),

    # Admin question management APIs
    path(
        "admin/questions/",
        AdminQuestionListCreateAPIView.as_view(),
        name="admin-assessment-question-list-create",
    ),
    path(
        "admin/questions/<int:pk>/",
        AdminQuestionDetailAPIView.as_view(),
        name="admin-assessment-question-detail",
    ),
]
