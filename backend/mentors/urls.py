
from django.urls import path

from .views import (
    MentorListAPIView,
    MentorDetailAPIView,
    MentorshipRequestAPIView,
    MyMentorshipRequestsAPIView,
    MentorFeedbackAPIView,
    MentorAssignmentManagementAPIView,
    MentorProfileAPIView,
    MentorStudentProgressAPIView,
)

from .assessment_views import MentorAssessmentsAPIView
from .skill_analysis_views import MentorSkillAnalysisAPIView
from .skill_gap_views import MentorSkillGapsAPIView
from .roadmap_views import MentorRoadmapsAPIView
from .learning_resources_views import MentorLearningResourcesAPIView
from .project_views import MentorProjectsAPIView
from .interview_prep_views import MentorInterviewPrepAPIView

# New Feedback and Messages APIs
from .feedback_messages_views import (
    MentorStudentFeedbackAPIView,
    MentorMessagesAPIView,
    MentorMessageReadAPIView,
)


urlpatterns = [

    # =================================================
    # MENTOR LIST
    # =================================================

    path(
        "",
        MentorListAPIView.as_view(),
        name="mentor-list",
    ),

    # =================================================
    # STUDENT MENTORSHIP REQUESTS
    # =================================================

    path(
        "requests/",
        MentorshipRequestAPIView.as_view(),
        name="mentorship-request",
    ),

    path(
        "my-requests/",
        MyMentorshipRequestsAPIView.as_view(),
        name="my-mentorship-requests",
    ),

    # =================================================
    # STUDENT TO MENTOR FEEDBACK
    # Existing API - preserved
    # =================================================

    path(
        "feedback/",
        MentorFeedbackAPIView.as_view(),
        name="mentor-feedback",
    ),

    # =================================================
    # MENTOR TO STUDENT FEEDBACK
    # =================================================

    path(
        "student-feedback/",
        MentorStudentFeedbackAPIView.as_view(),
        name="mentor-student-feedback",
    ),

    # =================================================
    # MENTOR AND STUDENT MESSAGES
    # =================================================

    path(
        "messages/",
        MentorMessagesAPIView.as_view(),
        name="mentor-messages",
    ),

    path(
        "messages/<int:message_id>/read/",
        MentorMessageReadAPIView.as_view(),
        name="mentor-message-read",
    ),

    # =================================================
    # MENTOR STUDENTS AND ASSIGNMENTS
    # =================================================

    path(
        "my-students/",
        MentorAssignmentManagementAPIView.as_view(),
        name="mentor-my-students",
    ),

    path(
        "my-students/<int:assignment_id>/",
        MentorAssignmentManagementAPIView.as_view(),
        name="mentor-assignment-decision",
    ),

    # =================================================
    # MENTOR PROFILE
    # =================================================

    path(
        "profile/",
        MentorProfileAPIView.as_view(),
        name="mentor-profile",
    ),

    # =================================================
    # STUDENT PROGRESS
    # =================================================

    path(
        "student-progress/",
        MentorStudentProgressAPIView.as_view(),
        name="mentor-student-progress",
    ),

    # =================================================
    # MENTOR ASSESSMENTS
    # =================================================

    path(
        "assessments/",
        MentorAssessmentsAPIView.as_view(),
        name="mentor-assessments",
    ),

    # =================================================
    # MENTOR SKILL ANALYSIS
    # =================================================

    path(
        "skill-analysis/",
        MentorSkillAnalysisAPIView.as_view(),
        name="mentor-skill-analysis",
    ),

    # =================================================
    # MENTOR SKILL GAPS
    # =================================================

    path(
        "skill-gaps/",
        MentorSkillGapsAPIView.as_view(),
        name="mentor-skill-gaps",
    ),

    # =================================================
    # MENTOR ROADMAPS
    # =================================================

    path(
        "roadmaps/",
        MentorRoadmapsAPIView.as_view(),
        name="mentor-roadmaps",
    ),

    # =================================================
    # MENTOR LEARNING RESOURCES
    # =================================================

    path(
        "learning-resources/",
        MentorLearningResourcesAPIView.as_view(),
        name="mentor-learning-resources",
    ),

    # =================================================
    # MENTOR PROJECTS
    # =================================================

    path(
        "projects/",
        MentorProjectsAPIView.as_view(),
        name="mentor-projects",
    ),

    # =================================================
    # MENTOR INTERVIEW PREPARATION
    # =================================================

    path(
        "interview-prep/",
        MentorInterviewPrepAPIView.as_view(),
        name="mentor-interview-prep",
    ),

    # =================================================
    # INDIVIDUAL MENTOR DETAILS
    # Keep this route last
    # =================================================

    path(
        "<int:mentor_id>/",
        MentorDetailAPIView.as_view(),
        name="mentor-detail",
    ),

]
