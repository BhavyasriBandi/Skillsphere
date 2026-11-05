
from django.db.models import Q

from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsMentor
from mentors.models import MentorStudentAssignment
from projects.models import StudentProject


class MentorProjectSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    student_email = serializers.EmailField(
        source="student.email",
        read_only=True,
    )

    class Meta:
        model = StudentProject
        fields = [
            "id",
            "student",
            "student_name",
            "student_email",
            "title",
            "description",
            "category",
            "technologies",
            "status",
            "github",
            "live_demo",
            "created_at",
            "updated_at",
        ]

    def get_student_name(self, obj):
        return obj.student.get_full_name() or obj.student.email


class MentorProjectsAPIView(APIView):
    permission_classes = [IsAuthenticated, IsMentor]

    def get(self, request):
        # Get only students actively assigned to this mentor.
        assigned_student_ids = MentorStudentAssignment.objects.filter(
            mentor=request.user,
            status="Active",
        ).values_list("student_id", flat=True)

        # Get projects belonging to those assigned students.
        queryset = StudentProject.objects.filter(
            student_id__in=assigned_student_ids
        ).select_related("student")

        # Search by project title, description, or student email.
        search = request.query_params.get("search", "").strip()

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search)
                | Q(description__icontains=search)
                | Q(student__email__icontains=search)
            )

        # Filter by project status.
        project_status = request.query_params.get("status", "").strip()

        if project_status:
            queryset = queryset.filter(status=project_status)

        # Filter by project category.
        category = request.query_params.get("category", "").strip()

        if category:
            queryset = queryset.filter(category=category)

        queryset = queryset.order_by("-created_at", "-id")

        serializer = MentorProjectSerializer(
            queryset,
            many=True,
        )

        return Response(
            {
                "count": queryset.count(),
                "projects": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
