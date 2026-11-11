import json
import os
import secrets
import urllib.error
import urllib.request
from datetime import timedelta

from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import Group
from django.db import transaction
from django.db.models import Q
from django.utils import timezone

from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.throttling import ScopedRateThrottle

from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema

from .models import EmailVerificationCode
from .serializers import (
    RegisterSerializer,
    ProfileUpdateSerializer,
    ChangePasswordSerializer,
)
from .permissions import IsStudent, IsMentor, IsPlatformAdmin

from .profile_views import *

from mentors.models import MentorStudentAssignment
from assessments.models import AssessmentResult


User = get_user_model()

SKILLSPHERE_ROLES = ["Student", "Mentor", "Admin"]
OTP_EXPIRY_MINUTES = 1


# =====================================================
# BREVO TRANSACTIONAL EMAIL HELPER
# =====================================================

def send_skillsphere_email(recipient, subject, message):
    """Send a transactional email through Brevo without SMTP."""
    api_key = os.environ.get("BREVO_API_KEY") or getattr(
        settings, "BREVO_API_KEY", ""
    )
    sender_email = getattr(settings, "DEFAULT_FROM_EMAIL", "")

    if not api_key:
        raise RuntimeError("Brevo API key is not configured.")
    if not sender_email:
        raise RuntimeError("SkillSphere sender email is not configured.")

    payload = {
        "sender": {
            "name": "SkillSphere",
            "email": sender_email,
        },
        "to": [{"email": recipient}],
        "subject": subject,
        "textContent": message,
    }

    request = urllib.request.Request(
        url="https://api.brevo.com/v3/smtp/email",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "accept": "application/json",
            "api-key": api_key,
            "content-type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return response.status in (200, 201, 202)
    except urllib.error.HTTPError as exc:
        # Do not expose the API key or provider response to the client.
        raise RuntimeError(
            f"Brevo rejected the email request (HTTP {exc.code})."
        ) from None
    except (urllib.error.URLError, TimeoutError) as exc:
        raise RuntimeError("Could not connect to Brevo email service.") from None


# =====================================================
# ROLE HELPER
# =====================================================

def get_user_role(user):
    if user.is_staff or user.is_superuser:
        return "Admin"

    for role in SKILLSPHERE_ROLES:
        if user.groups.filter(name=role).exists():
            return role

    return "Unassigned"


def is_admin_user(user):
    return (
        user.is_staff
        or user.is_superuser
        or user.groups.filter(name="Admin").exists()
    )


# =====================================================
# EMAIL VERIFICATION HELPER
# =====================================================

def issue_verification_code(user):
    EmailVerificationCode.objects.filter(
        user=user,
        is_used=False,
    ).update(is_used=True)

    code = f"{secrets.randbelow(1_000_000):06d}"

    EmailVerificationCode.objects.create(
        user=user,
        code=code,
        expires_at=timezone.now()
        + timedelta(minutes=OTP_EXPIRY_MINUTES),
    )

    email_message = (
        f"Hello {user.first_name},\n\n"
        f"Your SkillSphere verification code is: {code}\n\n"
        f"This code expires in {OTP_EXPIRY_MINUTES} minutes.\n"
        "If you did not request this code, please ignore this email."
    )
    if not send_skillsphere_email(
        recipient=user.email,
        subject="SkillSphere Email Verification",
        message=email_message,
    ):
        raise RuntimeError("Brevo did not accept the verification email.")


# =====================================================
# REGISTRATION
# =====================================================

class RegisterView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    @extend_schema(
        request=RegisterSerializer,
        description="Register and send an email verification code.",
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = None

        try:
            user = serializer.save()
            issue_verification_code(user)

        except Exception:
            if user is not None:
                user.delete()

            return Response(
                {
                    "detail": (
                        "Registration could not be completed. "
                        "Check the email configuration and try again."
                    )
                },
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        return Response(
            {
                "message": (
                    "Registration received. Check your email "
                    "for the verification code."
                ),
                "email": user.email,
            },
            status=status.HTTP_201_CREATED,
        )


# =====================================================
# EMAIL VERIFICATION
# =====================================================

class VerifyEmailView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    @extend_schema(
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "email": {"type": "string", "format": "email"},
                    "code": {"type": "string"},
                },
                "required": ["email", "code"],
            }
        },
        description="Verify a six-digit email code.",
    )
    def post(self, request):
        email = request.data.get("email", "")
        code = request.data.get("code", "")

        if not isinstance(email, str) or not isinstance(code, str):
            return Response(
                {"detail": "Email and code must be strings."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        email = email.strip().lower()
        code = code.strip()

        if not email or len(code) != 6 or not code.isdigit():
            return Response(
                {"detail": "Enter a valid email and six-digit code."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User.objects.filter(email__iexact=email).first()

        if not user:
            return Response(
                {"detail": "Invalid email or verification code."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        verification = (
            EmailVerificationCode.objects.filter(
                user=user,
                is_used=False,
            )
            .order_by("-created_at")
            .first()
        )

        if (
            not verification
            or verification.code != code
            or verification.is_expired
        ):
            return Response(
                {"detail": "Invalid or expired verification code."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        verification.is_used = True
        verification.save(update_fields=["is_used"])

        user.is_active = True
        user.save(update_fields=["is_active"])

        return Response(
            {
                "message": (
                    "Email verified successfully. You can now log in."
                )
            },
            status=status.HTTP_200_OK,
        )


# =====================================================
# RESEND VERIFICATION CODE
# =====================================================

class ResendVerificationCodeView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    @extend_schema(
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "email": {"type": "string", "format": "email"},
                },
                "required": ["email"],
            }
        },
        description="Send a new email verification code.",
    )
    def post(self, request):
        email = request.data.get("email", "")

        if not isinstance(email, str) or not email.strip():
            return Response(
                {"detail": "A valid email is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User.objects.filter(
            email__iexact=email.strip(),
            is_active=False,
        ).first()

        if not user:
            return Response(
                {
                    "message": (
                        "If an eligible unverified account exists, "
                        "a verification email will be sent."
                    )
                },
                status=status.HTTP_200_OK,
            )

        try:
            issue_verification_code(user)
        except Exception:
            return Response(
                {"detail": "Unable to send the verification email."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        return Response(
            {"message": "A new verification code has been sent."},
            status=status.HTTP_200_OK,
        )


# =====================================================
# LOGIN - ROLE VALIDATION + RATE LIMITING
# =====================================================

class LoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "login"

    @extend_schema(
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "email": {
                        "type": "string",
                        "format": "email",
                    },
                    "password": {
                        "type": "string",
                        "format": "password",
                    },
                    "role": {
                        "type": "string",
                        "enum": ["Student", "Mentor", "Admin"],
                    },
                },
                "required": ["email", "password", "role"],
            }
        },
        description="Login using email, password and selected role.",
    )
    def post(self, request):
        email = request.data.get("email", "")
        password = request.data.get("password", "")
        requested_role = request.data.get("role", "")

        if not all(
            isinstance(value, str)
            for value in [email, password, requested_role]
        ):
            return Response(
                {"detail": "Email, password and role must be strings."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        email = email.strip().lower()

        role_mapping = {
            "student": "Student",
            "mentor": "Mentor",
            "admin": "Admin",
        }

        requested_role = role_mapping.get(
            requested_role.strip().lower()
        )

        if not email or not password:
            return Response(
                {"detail": "Email and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if requested_role is None:
            return Response(
                {"detail": "Please select a valid role."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        matching_users = User.objects.filter(
            email__iexact=email
        ).order_by("pk")

        if not matching_users.exists():
            return Response(
                {"detail": "Invalid email or password."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        authenticated_user = None
        inactive_password_matches = False

        for candidate in matching_users:
            if not candidate.is_active:
                if candidate.check_password(password):
                    inactive_password_matches = True
                continue

            user = authenticate(
                request,
                username=candidate.get_username(),
                password=password,
            )

            if user is not None:
                authenticated_user = user
                break

        if authenticated_user is None:
            if inactive_password_matches:
                return Response(
                    {
                        "detail": (
                            "Please verify your email before logging in."
                        )
                    },
                    status=status.HTTP_403_FORBIDDEN,
                )

            return Response(
                {"detail": "Invalid email or password."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        actual_role = get_user_role(authenticated_user)

        if requested_role != actual_role:
            return Response(
                {
                    "detail": (
                        f"This account is registered as {actual_role}. "
                        f"You cannot log in as {requested_role}."
                    )
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        refresh = RefreshToken.for_user(authenticated_user)

        return Response(
            {
                "message": "Login successful.",
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "user": {
                    "id": authenticated_user.id,
                    "first_name": authenticated_user.first_name,
                    "last_name": authenticated_user.last_name,
                    "email": authenticated_user.email,
                    "role": actual_role,
                },
            },
            status=status.HTTP_200_OK,
        )


# =====================================================
# CURRENT USER
# =====================================================

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        return Response(
            {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "role": get_user_role(user),
            }
        )


# =====================================================
# LOGOUT - BLACKLIST REFRESH TOKEN
# =====================================================

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "refresh": {"type": "string"},
                },
                "required": ["refresh"],
            }
        },
        description="Blacklist the refresh token and log out the user.",
    )
    def post(self, request):
        refresh_token = request.data.get("refresh")

        if not isinstance(refresh_token, str) or not refresh_token.strip():
            return Response(
                {"detail": "Refresh token is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            token = RefreshToken(refresh_token.strip())
            token.blacklist()

        except Exception:
            return Response(
                {
                    "detail": (
                        "Invalid or already blacklisted refresh token."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {"message": "Logout successful."},
            status=status.HTTP_200_OK,
        )


# =====================================================
# PROFILE
# =====================================================

class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="get_profile",
        summary="Get My Profile",
    )
    def get(self, request):
        user = request.user

        return Response(
            {
                "id": user.pk,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "role": get_user_role(user),
            }
        )

    @extend_schema(
        operation_id="update_profile",
        summary="Update My Profile",
        request=ProfileUpdateSerializer,
    )
    def patch(self, request):
        serializer = ProfileUpdateSerializer(
            request.user,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user = request.user

        return Response(
            {
                "message": "Profile updated successfully.",
                "profile": {
                    "id": user.pk,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                    "role": get_user_role(user),
                },
            }
        )


# =====================================================
# CHANGE PASSWORD
# =====================================================

class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="change_password",
        summary="Change Password",
        request=ChangePasswordSerializer,
    )
    def post(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)

        user = request.user
        user.set_password(serializer.validated_data["new_password"])
        user.save(update_fields=["password"])

        return Response(
            {
                "message": (
                    "Password changed successfully. "
                    "Please log in again with your new password."
                )
            }
        )


# =====================================================
# ADMIN: LIST USERS
# =====================================================


# =====================================================
# ADMIN: LIST VERIFIED USERS
# =====================================================

class AdminUserListAPIView(APIView):
    permission_classes = [IsAuthenticated, IsPlatformAdmin]

    @extend_schema(
        operation_id="admin_list_users",
        summary="List Verified Users",
        description=(
            "Returns only users whose email verification is complete. "
            "Admin-deactivated verified accounts remain visible."
        ),
    )
    def get(self, request):
        # Users with an unused verification code have not completed OTP.
        # Users without verification records (such as admin-created
        # accounts) remain visible.
        users = (
            User.objects
            .exclude(email_verification_codes__is_used=False)
            .distinct()
            .order_by("-date_joined")
        )

        results = [
            {
                "id": user.id,
                "username": user.get_username(),
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "role": get_user_role(user),
                "is_active": user.is_active,
                "date_joined": user.date_joined,
            }
            for user in users
        ]

        return Response(
            {
                "count": len(results),
                "results": results,
            },
            status=status.HTTP_200_OK,
        )


# =====================================================
# ADMIN: ASSIGN USER ROLE
# =====================================================

class AssignUserRoleAPIView(APIView):
    permission_classes = [IsAuthenticated, IsPlatformAdmin]

    @extend_schema(
        description="Assign a SkillSphere role to a user.",
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "role": {
                        "type": "string",
                        "enum": SKILLSPHERE_ROLES,
                    }
                },
                "required": ["role"],
            }
        },
    )
    def post(self, request, user_id):
        role = request.data.get("role")

        if not isinstance(role, str):
            return Response(
                {"detail": "A valid role is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        role_mapping = {
            "student": "Student",
            "mentor": "Mentor",
            "admin": "Admin",
        }

        role = role_mapping.get(role.strip().lower())

        if role is None:
            return Response(
                {"detail": "Choose Student, Mentor, or Admin."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if str(request.user.pk) == str(user_id):
            return Response(
                {"detail": "You cannot change your own role."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        with transaction.atomic():
            try:
                target_user = User.objects.select_for_update().get(
                    pk=user_id
                )
            except User.DoesNotExist:
                return Response(
                    {"detail": "User not found."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            if target_user.is_superuser:
                return Response(
                    {
                        "detail": (
                            "A superuser's role cannot be changed here."
                        )
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if role == "Admin" and not target_user.is_active:
                return Response(
                    {
                        "detail": (
                            "Only active, email-verified accounts "
                            "can be promoted to Admin."
                        )
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            currently_admin = is_admin_user(target_user)

            if currently_admin and role != "Admin":
                other_active_admins = (
                    User.objects.filter(is_active=True)
                    .filter(
                        Q(is_staff=True)
                        | Q(is_superuser=True)
                        | Q(groups__name="Admin")
                    )
                    .exclude(pk=target_user.pk)
                    .distinct()
                    .count()
                )

                if other_active_admins == 0:
                    return Response(
                        {
                            "detail": (
                                "The last active Admin cannot be demoted. "
                                "Promote another user first."
                            )
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            groups = Group.objects.filter(
                name__in=SKILLSPHERE_ROLES
            )

            group, _ = Group.objects.get_or_create(name=role)

            target_user.groups.remove(*groups)
            target_user.groups.add(group)

            target_user.is_staff = role == "Admin"
            target_user.save(update_fields=["is_staff"])

        return Response(
            {
                "message": "Role assigned successfully.",
                "user_id": target_user.id,
                "email": target_user.email,
                "role": role,
            },
            status=status.HTTP_200_OK,
        )


# =====================================================
# ADMIN: ACTIVATE / DEACTIVATE USER
# =====================================================

class AdminUserStatusAPIView(APIView):
    permission_classes = [IsAuthenticated, IsPlatformAdmin]

    @extend_schema(
        operation_id="admin_update_user_status",
        summary="Activate or Deactivate User",
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "is_active": {"type": "boolean"},
                },
                "required": ["is_active"],
            }
        },
    )
    def patch(self, request, user_id):
        is_active = request.data.get("is_active")

        if not isinstance(is_active, bool):
            return Response(
                {"detail": "is_active must be true or false."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if str(request.user.pk) == str(user_id) and not is_active:
            return Response(
                {"detail": "You cannot deactivate your own account."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        with transaction.atomic():
            try:
                target_user = User.objects.select_for_update().get(
                    pk=user_id
                )
            except User.DoesNotExist:
                return Response(
                    {"detail": "User not found."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            if target_user.is_superuser:
                return Response(
                    {
                        "detail": (
                            "A superuser account cannot be changed here."
                        )
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            currently_admin = is_admin_user(target_user)

            if (
                target_user.is_active
                and not is_active
                and currently_admin
            ):
                other_active_admins = (
                    User.objects.filter(is_active=True)
                    .filter(
                        Q(is_staff=True)
                        | Q(is_superuser=True)
                        | Q(groups__name="Admin")
                    )
                    .exclude(pk=target_user.pk)
                    .distinct()
                    .count()
                )

                if other_active_admins == 0:
                    return Response(
                        {
                            "detail": (
                                "The last active Admin cannot be "
                                "deactivated."
                            )
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            target_user.is_active = is_active
            target_user.save(update_fields=["is_active"])

        return Response(
            {
                "message": (
                    "Account activated successfully."
                    if is_active
                    else "Account deactivated successfully."
                ),
                "user_id": target_user.id,
                "is_active": target_user.is_active,
            },
            status=status.HTTP_200_OK,
        )


# =====================================================
# STUDENT DASHBOARD
# =====================================================

class StudentDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated, IsStudent]

    def get(self, request):
        user = request.user

        return Response(
            {
                "student": {
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "full_name": (
                        f"{user.first_name} {user.last_name}".strip()
                        or user.get_username()
                    ),
                    "email": user.email,
                    "role": "Student",
                },
                "stats": {
                    "skills_assessed": 0,
                    "roadmap_progress": 0,
                    "tasks_completed": 0,
                    "total_tasks": 0,
                    "achievements": 0,
                },
                "tasks": [],
                "roadmap": [],
            },
            status=status.HTTP_200_OK,
        )


# =====================================================
# MENTOR DASHBOARD
# =====================================================

class MentorDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated, IsMentor]

    def get(self, request):
        mentor = request.user

        assignments = MentorStudentAssignment.objects.filter(
            mentor=mentor
        ).select_related("student")

        active_assignments = assignments.filter(status="Active")
        pending_assignments = assignments.filter(status="Pending")

        student_ids = active_assignments.values_list(
            "student_id",
            flat=True,
        ).distinct()

        assessment_count = AssessmentResult.objects.filter(
            user_id__in=student_ids
        ).count()

        students = [
            {
                "id": assignment.student.id,
                "name": (
                    assignment.student.get_full_name().strip()
                    or assignment.student.username
                ),
                "email": assignment.student.email,
                "assignment_status": assignment.status,
                "assigned_at": assignment.assigned_at,
            }
            for assignment in active_assignments
        ]

        recent_requests = pending_assignments.order_by(
            "-assigned_at"
        )[:5]

        recent_requests_data = [
            {
                "id": assignment.id,
                "student_id": assignment.student.id,
                "student_name": (
                    assignment.student.get_full_name().strip()
                    or assignment.student.username
                ),
                "student_email": assignment.student.email,
                "status": assignment.status,
                "assigned_at": assignment.assigned_at,
            }
            for assignment in recent_requests
        ]

        total_students = (
            assignments.exclude(status="Rejected")
            .values("student_id")
            .distinct()
            .count()
        )

        return Response(
            {
                "message": (
                    "Mentor dashboard data retrieved successfully."
                ),
                "role": "Mentor",
                "mentor": {
                    "id": mentor.id,
                    "name": (
                        mentor.get_full_name().strip()
                        or mentor.username
                    ),
                    "email": mentor.email,
                },
                "stats": {
                    "total_students": total_students,
                    "active_students": student_ids.distinct().count(),
                    "pending_requests": pending_assignments.count(),
                    "total_assessments": assessment_count,
                },
                "students": students,
                "recent_requests": recent_requests_data,
            },
            status=status.HTTP_200_OK,
        )


# =====================================================
# ADMIN DASHBOARD
# =====================================================

class AdminDashboardAPIView(APIView):
    permission_classes = [IsAuthenticated, IsPlatformAdmin]

    def get(self, request):
        total_users = User.objects.count()
        active_users = User.objects.filter(is_active=True).count()
        inactive_users = User.objects.filter(is_active=False).count()

        return Response(
            {
                "message": "Admin dashboard access granted.",
                "role": "Admin",
                "user_id": request.user.id,
                "stats": {
                    "total_users": total_users,
                    "active_users": active_users,
                    "inactive_users": inactive_users,
                },
            },
            status=status.HTTP_200_OK,
        )


# =====================================================
# ADMIN: SEND EMAIL
# =====================================================

class AdminSendEmailAPIView(APIView):
    permission_classes = [IsAuthenticated, IsPlatformAdmin]

    @extend_schema(
        operation_id="admin_send_email",
        summary="Send Email to a Recipient",
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "recipient_email": {
                        "type": "string",
                        "format": "email",
                    },
                    "subject": {"type": "string"},
                    "message": {"type": "string"},
                },
                "required": [
                    "recipient_email",
                    "subject",
                    "message",
                ],
            }
        },
        description="Allows an administrator to send an email.",
    )
    def post(self, request):
        recipient = request.data.get("recipient_email")
        subject = request.data.get("subject")
        message = request.data.get("message")

        if not all(
            isinstance(value, str)
            for value in [recipient, subject, message]
        ):
            return Response(
                {"detail": "All email fields must be strings."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        recipient = recipient.strip()
        subject = subject.strip()
        message = message.strip()

        if not recipient or not subject or not message:
            return Response(
                {"detail": "All email fields are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            validate_email(recipient)
        except ValidationError:
            return Response(
                {"detail": "Enter a valid recipient email address."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if len(subject) > 200 or len(message) > 10000:
            return Response(
                {"detail": "Subject or message exceeds the allowed length."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            sent = send_skillsphere_email(
                recipient=recipient,
                subject=subject,
                message=message,
            )

            if not sent:
                return Response(
                    {"detail": "Email could not be delivered."},
                    status=status.HTTP_503_SERVICE_UNAVAILABLE,
                )

        except Exception:
            return Response(
                {
                    "detail": (
                        "Unable to send email. "
                        "Please check the Brevo email configuration."
                    )
                },
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        return Response(
            {
                "message": "Email sent successfully.",
                "recipient_email": recipient,
            },
            status=status.HTTP_200_OK,
        )