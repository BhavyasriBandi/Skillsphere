
from rest_framework import generics
from rest_framework.permissions import BasePermission, IsAuthenticated

from .models import StudentProject
from .serializers import (
    StudentProjectSerializer,
    AdminStudentProjectSerializer,
)
from achievements.views import evaluate_achievements


def update_project_achievements(student):
    """Recalculate achievements using completed projects."""
    completed_count = StudentProject.objects.filter(
        student=student,
        status="Completed",
    ).count()

    evaluate_achievements(
        student=student,
        activity_counts={"project": completed_count},
    )


class IsStaffAdminOrReadOnly(BasePermission):
    """Only staff users can create, update, or delete admin projects."""

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True

        return request.user.is_staff


# Existing student APIs — preserved.

class StudentProjectListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = StudentProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return StudentProject.objects.filter(
            student=self.request.user
        ).order_by("-created_at", "-id")

    def perform_create(self, serializer):
        project = serializer.save(student=self.request.user)
        update_project_achievements(project.student)


class StudentProjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentProjectSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        return StudentProject.objects.filter(
            student=self.request.user
        )

    def perform_update(self, serializer):
        project = serializer.save()
        update_project_achievements(project.student)


# New admin APIs.

class AdminProjectListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsStaffAdminOrReadOnly]

    def get_serializer_class(self):
        return AdminStudentProjectSerializer

    def get_queryset(self):
        queryset = StudentProject.objects.select_related("student").all()

        search = self.request.query_params.get("search", "").strip()
        status = self.request.query_params.get("status", "").strip()
        category = self.request.query_params.get("category", "").strip()

        if search:
            queryset = queryset.filter(title__icontains=search)

        if status:
            queryset = queryset.filter(status=status)

        if category:
            queryset = queryset.filter(category=category)

        return queryset.order_by("-created_at", "-id")

    def perform_create(self, serializer):
        project = serializer.save()
        update_project_achievements(project.student)


class AdminProjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AdminStudentProjectSerializer
    permission_classes = [IsAuthenticated, IsStaffAdminOrReadOnly]
    queryset = StudentProject.objects.select_related("student").all()
    lookup_field = "id"

    def perform_update(self, serializer):
        old_student = serializer.instance.student
        project = serializer.save()

        update_project_achievements(old_student)

        if project.student_id != old_student.id:
            update_project_achievements(project.student)

    def perform_destroy(self, instance):
        student = instance.student
        instance.delete()
        update_project_achievements(student)
