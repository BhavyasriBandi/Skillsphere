
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db import IntegrityError, transaction

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
            {
                "count": len(results),
                "results": results,
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        name = str(request.data.get("name", "")).strip()
        email = str(request.data.get("email", "")).strip().lower()
        role = str(request.data.get("role", "Student")).strip().title()
        password = request.data.get("password", "")
        confirm_password = request.data.get("confirm_password", "")

        if not name or not email or not password or not confirm_password:
            return error_response(
                "Name, email, password and confirm password are required."
            )

        try:
            validate_email(email)
        except ValidationError:
            return error_response("Enter a valid email address.")

        if role not in ROLES:
            return error_response("Choose Student, Mentor, or Admin.")

        if password != confirm_password:
            return error_response("Passwords do not match.")

        if User.objects.filter(email__iexact=email).exists():
            return error_response(
                "A user with this email already exists.",
                status.HTTP_409_CONFLICT,
            )

        if User.objects.filter(username__iexact=email).exists():
            return error_response(
                "A user with this username already exists.",
                status.HTTP_409_CONFLICT,
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
                    is_active=True,
                    is_staff=False,
                )

                validate_password(password, user)
                user.set_password(password)
                user.save()

                assign_role(user, role)
                user.save(update_fields=["is_staff"])

        except ValidationError as exc:
            return error_response(
                {"password": exc.messages},
                status.HTTP_400_BAD_REQUEST,
            )

        except IntegrityError:
            return error_response(
                "A user with this email or username already exists.",
                status.HTTP_409_CONFLICT,
            )

        return Response(
            {
                "message": "User created successfully. The account is active and ready to log in.",
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
                    "User not found.",
                    status.HTTP_404_NOT_FOUND,
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

                if (
                    User.objects.filter(email__iexact=email)
                    .exclude(pk=user.pk)
                    .exists()
                ):
                    return error_response(
                        "This email is already in use.",
                        status.HTTP_409_CONFLICT,
                    )

                if (
                    User.objects.filter(username__iexact=email)
                    .exclude(pk=user.pk)
                    .exists()
                ):
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
                    "User not found.",
                    status.HTTP_404_NOT_FOUND,
                )

            if user.is_superuser:
                return error_response(
                    "Superuser accounts cannot be deleted here."
                )

            if user.is_active and user_role(user) == "Admin":
                other_admins = (
                    User.objects.filter(
                        is_active=True,
                        groups__name="Admin",
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
    """
    Legacy endpoint retained temporarily so existing URL imports
    do not break. Admin-created users now receive their password
    directly during account creation. Email setup links are disabled.
    """

    permission_classes = [AllowAny]

    def post(self, request):
        return error_response(
            "Email-based password setup is disabled. Contact your administrator.",
            status.HTTP_410_GONE,
        )
