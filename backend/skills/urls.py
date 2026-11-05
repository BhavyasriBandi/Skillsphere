
from django.urls import path

from .views import (
    SkillCategoriesAPIView,
    SkillCategoryDetailAPIView,
    SkillsListAPIView,
    SkillDetailAPIView,
    MySkillsAPIView,
    SkillAssessmentAPIView,
    SkillAssessmentStartAPIView,
    SkillAssessmentSubmitAPIView,
    SkillProgressAPIView,
)

from .admin_assessment_views import (
    AdminAssessmentResultsAPIView,
)


urlpatterns = [
    # Skill Categories
    path(
        "categories/",
        SkillCategoriesAPIView.as_view(),
        name="skill-categories",
    ),
    path(
        "categories/<int:pk>/",
        SkillCategoryDetailAPIView.as_view(),
        name="skill-category-detail",
    ),

    # Skills
    path(
        "",
        SkillsListAPIView.as_view(),
        name="skills-list",
    ),
    path(
        "<int:pk>/",
        SkillDetailAPIView.as_view(),
        name="skill-detail",
    ),
    path(
        "my-skills/",
        MySkillsAPIView.as_view(),
        name="my-skills",
    ),

    # Admin Assessment Results
    path(
        "assessments/admin/results/",
        AdminAssessmentResultsAPIView.as_view(),
        name="admin-assessment-results",
    ),

    # Student AI Skill Assessment
    path(
        "assessments/start/",
        SkillAssessmentStartAPIView.as_view(),
        name="skill-assessment-start",
    ),
    path(
        "assessments/submit/",
        SkillAssessmentSubmitAPIView.as_view(),
        name="skill-assessment-submit",
    ),
    path(
        "assessments/",
        SkillAssessmentAPIView.as_view(),
        name="skill-assessment",
    ),

    # Skill Progress
    path(
        "progress/",
        SkillProgressAPIView.as_view(),
        name="skill-progress",
    ),
]
