
from rest_framework.permissions import BasePermission


class IsInGroup(BasePermission):
    """
    Allows access only to authenticated users
    who belong to the required group.
    """

    required_group = None

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        if not self.required_group:
            return False

        return user.groups.filter(
            name=self.required_group
        ).exists()


class IsStudent(IsInGroup):
    required_group = "Student"


class IsMentor(IsInGroup):
    required_group = "Mentor"


class IsPlatformAdmin(BasePermission):
    """
    Allows access to staff, superusers, or users
    explicitly assigned to the Admin group.
    """

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        return bool(
            user.is_staff
            or user.is_superuser
            or user.groups.filter(name="Admin").exists()
        )
