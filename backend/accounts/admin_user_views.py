
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.db import IntegrityError, transaction
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.password_validation import validate_password

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsPlatformAdmin


User = get_user_model()
ROLES = ("Student", "Mentor", "Admin")


def user_role(user):
    if user.is_superuser or user.is_staff:
        return "Admin"

    for role in ("Admin", "Mentor", "Student"):
        if user.groups.filter(name=role).exists():
            return role

    return "Unassigned"


def user_data(user):
    return {
        "id": user.id,
        "username": user.get_username(),
        "first_name": user.first_name,
        "last_name": user.last_name,
        "name": user.get_full_name().strip() or user.email,
        "email": user.email,
        "role": user_role(user),
        "is_active": user.is_active,
        "status": "Active" if user.is_active else "Inactive",
        "date_joined": user.date_joined,
        "joined": (
            user.date_joined.date().isoformat()
            if user.date_joined
            else None
        ),
    }


def assign_role(user, role):
    if role not in ROLES:
        raise ValueError("Choose Student, Mentor, or Admin.")

    role_groups = Group.objects.filter(name__in=ROLES)
    user.groups.remove(*role_groups)

    group, _ = Group.objects.get_or_create(name=role)
    user.groups.add(group)

    user.is_staff = role == "Admin"


def error_response(message, code=status.HTTP_400_BAD_REQUEST):
    return Response({"detail": message}, status=code)


class AdminUserListAPIView(APIView):
    permission_classes = [IsAuthenticated, IsPlatformAdmin]

    def get(self, request):
        users = (
            User.objects
            .exclude(email_verification_codes__is_used=False)
            .distinct()
            .order_by("-date_joined")
        )
        results = [user_data(user) for user in users]

        return Response(
            {"count": len(results), "results": results},
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        name = str(request.data.get("name", "")).strip()
        email = str(request.data.get("email", "")).strip().lower()
        role = str(request.data.get("role", "Student")).strip().title()

        if not name or not email:
            return error_response("Name and email are required.")

        try:
            validate_email(email)
        except ValidationError:
            return error_response("Enter a valid email address.")

        if role not in ROLES:
            return error_response("Choose Student, Mentor, or Admin.")

        if User.objects.filter(email__iexact=email).exists():
            return error_response(
                "A user with this email already exists.",
                status.HTTP_409_CONFLICT,
            )

        frontend_url = getattr(settings, "FRONTEND_URL", "").rstrip("/")
        if not frontend_url:
            return error_response(
                "Frontend URL is not configured.",
                status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        parts = name.split()
        first_name = parts[0]
        last_name = " ".join(parts[1:])

        try:
            with transaction.atomic():
                user = User(
                    username=email,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    is_active=False,
                    is_staff=(role == "Admin"),
                )
                user.set_unusable_password()
                user.save()

                group, _ = Group.objects.get_or_create(name=role)
                user.groups.add(group)

                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)
                setup_url = (
                    f"{frontend_url}/set-password/{uid}/{token}"
                )

                subject = "Set up your SkillSphere account"
                message = (
                    f"Hello {first_name},\n\n"
                    "Your SkillSphere account has been created by an "
                    "administrator.\n\n"
                    "Click the secure link below to set your password "
                    "and activate your account:\n\n"
                    f"{setup_url}\n\n"
                    "If you did not expect this email, please ignore it.\n\n"
                    "SkillSphere Team"
                )

                sent = send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )

                if sent != 1:
                    raise RuntimeError("Setup email could not be sent.")

        except IntegrityError:
            return error_response(
                "A user with this email or username already exists.",
                status.HTTP_409_CONFLICT,
            )
        except Exception:
            return error_response(
                "User creation email failed. Check the server email configuration.",
                status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        return Response(
            {
                "message": "User created. Password setup email sent.",
                "user": user_data(user),
            },
            status=status.HTTP_201_CREATED,
        )


class AdminUserDetailAPIView(APIView):
    permission_classes = [IsAuthenticated, IsPlatformAdmin]

    def get_object(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def patch(self, request, user_id):
        with transaction.atomic():
            try:
                user = User.objects.select_for_update().get(pk=user_id)
            except User.DoesNotExist:
                return error_response(
                    "User not found.", status.HTTP_404_NOT_FOUND
                )

            if user.is_superuser:
                return error_response(
                    "Superuser accounts cannot be modified here."
                )

            if user.pk == request.user.pk:
                return error_response(
                    "You cannot edit your own account here."
                )

            name = request.data.get("name")
            email = request.data.get("email")

            if name is not None:
                name = str(name).strip()
                if not name:
                    return error_response("Name cannot be empty.")

                parts = name.split()
                user.first_name = parts[0]
                user.last_name = " ".join(parts[1:])

            if email is not None:
                email = str(email).strip().lower()
                try:
                    validate_email(email)
                except ValidationError:
                    return error_response("Enter a valid email address.")

                if User.objects.filter(
                    email__iexact=email
                ).exclude(pk=user.pk).exists():
                    return error_response(
                        "This email is already in use.",
                        status.HTTP_409_CONFLICT,
                    )

                if User.objects.filter(
                    username__iexact=email
                ).exclude(pk=user.pk).exists():
                    return error_response(
                        "This username is already in use.",
                        status.HTTP_409_CONFLICT,
                    )

                user.email = email
                user.username = email

            user.save()

        return Response(
            {
                "message": "User updated successfully.",
                "user": user_data(user),
            },
            status=status.HTTP_200_OK,
        )

    def delete(self, request, user_id):
        if str(request.user.pk) == str(user_id):
            return error_response("You cannot delete your own account.")

        with transaction.atomic():
            try:
                user = User.objects.select_for_update().get(pk=user_id)
            except User.DoesNotExist:
                return error_response(
                    "User not found.", status.HTTP_404_NOT_FOUND
                )

            if user.is_superuser:
                return error_response(
                    "Superuser accounts cannot be deleted here."
                )

            if user.is_active and user_role(user) == "Admin":
                other_admins = (
                    User.objects.filter(is_active=True)
                    .filter(
                        groups__name="Admin"
                    )
                    .exclude(pk=user.pk)
                    .distinct()
                    .count()
                )

                if other_admins == 0:
                    return error_response(
                        "The last active Admin cannot be deleted."
                    )

            user.delete()

        return Response(
            {"message": "User deleted successfully."},
            status=status.HTTP_200_OK,
        )


class AdminSetPasswordAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        uid = request.data.get("uid")
        token = request.data.get("token")
        password = request.data.get("password")
        confirm_password = request.data.get("confirm_password")

        if not all([uid, token, password, confirm_password]):
            return error_response("All fields are required.")

        if password != confirm_password:
            return error_response("Passwords do not match.")

        try:
            user_id = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=user_id)
        except (
            TypeError,
            ValueError,
            OverflowError,
            User.DoesNotExist,
        ):
            return error_response("Invalid or expired setup link.")

        if user.is_active or user.has_usable_password():
            return error_response(
                "This account has already been activated."
            )

        if not default_token_generator.check_token(user, token):
            return error_response(
                "Invalid or expired setup link. Contact your administrator."
            )

        try:
            validate_password(password, user)
        except ValidationError as exc:
            return error_response({"password": exc.messages})

        user.set_password(password)
        user.is_active = True
        user.save(update_fields=["password", "is_active"])

        return Response(
            {
                "message": (
                    "Password set successfully. You can now log in."
                )
            },
            status=status.HTTP_200_OK,
        )
