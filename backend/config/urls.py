from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)


urlpatterns = [
    # Django Admin
    path("admin/", admin.site.urls),

    # API Documentation
    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="schema",
    ),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),

    # Authentication
    path("api/auth/", include("accounts.urls")),

    # Skills and Careers
    path("api/skills/", include("skills.urls")),
    path("api/careers/", include("careers.urls")),

    # Learning and Study
    path("api/learning-goals/", include("learning_goals.urls")),
    path("api/study-planner/", include("study_planner.urls")),
    path("api/learning-resources/", include("learning_resources.urls")),
    path("api/resources/", include("resources.urls")),
    path("api/roadmaps/", include("roadmaps.urls")),
    path("api/challenges/", include("challenges.urls")),
    path("api/study-streaks/", include("study_streaks.urls")),

    # Assessments and Progress
    path("api/assessments/", include("assessments.urls")),
    path("api/progress/", include("progress.urls")),

    # Portfolio and Achievements
    path("api/portfolio/", include("portfolios.urls")),
    path("api/certificates/", include("certificates.urls")),
    path("api/achievements/", include("achievements.urls")),
    path("api/skill-endorsements/", include("skill_endorsements.urls")),

    # Projects and Tasks
    path("api/projects/", include("projects.urls")),
    path("api/tasks/", include("tasks.urls")),

    # Interview Preparation and Mentors
    path("api/interview-prep/", include("interview_prep.urls")),
    path("api/mentors/", include("mentors.urls")),

    # Notifications
    path("api/notifications/", include("notifications.urls")),

    # User Settings
    path("api/user-preferences/", include("user_preferences.urls")),

    # Activity and Engagement
    path("api/activity-feed/", include("activity_feed.urls")),
    path("api/bookmarks/", include("bookmarks.urls")),
    path("api/leaderboard/", include("leaderboard.urls")),
    path("api/feedback/", include("feedback.urls")),

    # Career and Job Opportunities
    path("api/career-comparison/", include("career_comparison.urls")),
    path("api/job-opportunities/", include("job_opportunities.urls")),

    # Support and Reports
    path("api/support/", include("support.urls")),
    path("api/reports/", include("reports.urls")),
    path("api/files/", include("files.urls")),
]
