
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import IntegrityError, transaction
from django.utils import timezone

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsPlatformAdmin


User = get_user_model()
ROLES = ("Student", "Mentor", "Admin")


def user_role(user):
    if user.is_staff or user.is_superuser:
        return "Admin"

    for role in ROLES:
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

    # Admin API access requires is_staff=True.
    if role == "Admin":
        user.is_staff = True
    elif user.is_staff and not user.is_superuser:
        user.is_staff = False


def error_response(message, code=status.HTTP_400_BAD_REQUEST):
    return Response({"detail": message}, status=code)


class AdminUsersAPIView(APIView):
    permission_classes = [IsAuthenticated, IsPlatformAdmin]

    def get(self, request):
        users = User.objects.all().order_by("-date_joined")
        results = [user_data(user) for user in users]

        return Response(
            {"count": len(results), "results": results},
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        name = str(request.data.get("name", "")).strip()
        email = str(request.data.get("email", "")).strip().lower()
        role = request.data.get("role", "Student")
        account_status = request.data.get("status", "Active")

        if not name or not email:
            return error_response("Name and email are required.")

        if "@" not in email or "." not in email.rsplit("@", 1)[-1]:
            return error_response("Enter a valid email address.")

        if role not in ROLES:
            return error_response("Choose a valid role.")

        if account_status not in ("Active", "Inactive"):
            return error_response("Choose Active or Inactive status.")

        if User.objects.filter(email__iexact=email).exists():
            return error_response("A user with this email already exists.")

        name_parts = name.split(maxsplit=1)
        first_name = name_parts[0]
        last_name = name_parts[1] if len(name_parts) > 1 else ""

        # Generate an unusable-password account. No password is exposed
        # or invented by the admin interface.
        try:
            with transaction.atomic():
                user = User(
                    username=email,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    is_active=(account_status == "Active"),
                    is_staff=False,
                )
                user.set_unusable_password()
                user.save()
                assign_role(user, role)
                user.save()

        except IntegrityError:
            return error_response(
                "A user with this email or username already exists."
            )
        except ValueError as exc:
            return error_response(str(exc))

        return Response(
            {
                "message": "User created successfully.",
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
        user = self.get_object(user_id)

        if user is None:
            return error_response("User not found.", status.HTTP_404_NOT_FOUND)

        if user.is_superuser:
            return error_response(
                "Superuser accounts cannot be modified here."
            )

        if user.pk == request.user.pk:
            return error_response(
                "You cannot change your own account through this screen."
            )

        name = request.data.get("name")
        email = request.data.get("email")
        role = request.data.get("role")
        account_status = request.data.get("status")

        if name is not None:
            name = str(name).strip()
            if not name:
                return error_response("Name cannot be empty.")

        if email is not None:
            email = str(email).strip().lower()
            if (
                not email
                or "@" not in email
                or "." not in email.rsplit("@", 1)[-1]
            ):
                return error_response("Enter a valid email address.")

            if User.objects.filter(email__iexact=email).exclude(
                pk=user.pk
            ).exists():
                return error_response(
                    "A user with this email already exists."
                )

            if (
                User.objects.filter(username__iexact=email)
                .exclude(pk=user.pk)
                .exists()
            ):
                return error_response(
                    "A user with this username already exists."
                )

        if role is not None and role not in ROLES:
            return error_response("Choose a valid role.")

        if account_status is not None and account_status not in (
            "Active",
            "Inactive",
        ):
            return error_response("Choose Active or Inactive status.")

        try:
            with transaction.atomic():
                if name is not None:
                    name_parts = name.split(maxsplit=1)
                    user.first_name = name_parts[0]
                    user.last_name = (
                        name_parts[1] if len(name_parts) > 1 else ""
                    )

                if email is not None:
                    user.email = email

                    # Keep the standard Django username aligned with email.
                    if hasattr(user, "username"):
                        user.username = email

                if account_status is not None:
                    user.is_active = account_status == "Active"

                if role is not None:
                    assign_role(user, role)

                user.save()

        except IntegrityError:
            return error_response(
                "A user with this email or username already exists."
            )
        except ValueError as exc:
            return error_response(str(exc))

        return Response(
            {
                "message": "User updated successfully.",
                "user": user_data(user),
            },
            status=status.HTTP_200_OK,
        )

    def delete(self, request, user_id):
        user = self.get_object(user_id)

        if user is None:
            return error_response("User not found.", status.HTTP_404_NOT_FOUND)

        if user.is_superuser:
            return error_response(
                "Superuser accounts cannot be deleted here."
            )

        if user.pk == request.user.pk:
            return error_response(
                "You cannot delete your own account."
            )

        email = user.email
        user.delete()

        return Response(
            {"message": f"User {email} deleted successfully."},
            status=status.HTTP_200_OK,
        )
