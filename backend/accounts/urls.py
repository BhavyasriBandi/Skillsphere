
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    RegisterView,
    VerifyEmailView,
    ResendVerificationCodeView,
    LoginView,
    LogoutView,
    CurrentUserView,
    AdminUserListAPIView,
    AssignUserRoleAPIView,
    AdminUserStatusAPIView,
    StudentDashboardAPIView,
    MentorDashboardAPIView,
    AdminDashboardAPIView,
    AdminSendEmailAPIView,
)

from .profile_views import (
    ProfileAPIView,
    ChangePasswordAPIView,
)


urlpatterns = [
    # Authentication
    path("register/", RegisterView.as_view(), name="register"),
    path("verify-email/", VerifyEmailView.as_view(), name="verify-email"),
    path(
        "resend-verification/",
        ResendVerificationCodeView.as_view(),
        name="resend-verification",
    ),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    # JWT Token Refresh
    path(
        "token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),

    # Current User
    path("me/", CurrentUserView.as_view(), name="current-user"),

    # Profile and Password
    path("profile/", ProfileAPIView.as_view(), name="profile"),
    path(
        "change-password/",
        ChangePasswordAPIView.as_view(),
        name="change-password",
    ),

    # Admin User Management
    path("users/", AdminUserListAPIView.as_view(), name="admin-users"),
    path(
        "users/<int:user_id>/role/",
        AssignUserRoleAPIView.as_view(),
        name="assign-user-role",
    ),
    path(
        "users/<int:user_id>/status/",
        AdminUserStatusAPIView.as_view(),
        name="admin-user-status",
    ),

    # Admin Email Management
    path(
        "admin/email/",
        AdminSendEmailAPIView.as_view(),
        name="admin-send-email",
    ),

    # Student Dashboard
    path(
        "student/dashboard/",
        StudentDashboardAPIView.as_view(),
        name="student-dashboard",
    ),

    # Mentor Dashboard
    path(
        "mentor/dashboard/",
        MentorDashboardAPIView.as_view(),
        name="mentor-dashboard",
    ),

    # Admin Dashboard
    path(
        "admin/dashboard/",
        AdminDashboardAPIView.as_view(),
        name="admin-dashboard",
    ),

    # Backward Compatibility
    path(
        "dashboard/",
        AdminDashboardAPIView.as_view(),
        name="admin-dashboard-legacy",
    ),
]
