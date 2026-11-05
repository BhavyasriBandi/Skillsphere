
from django.db import transaction
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import ManagedFile
from .serializers import ManagedFileSerializer
from accounts.views import get_user_role


class IsAdminUserRole(IsAuthenticated):

    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            return False

        return get_user_role(request.user) == "Admin"


class ManagedFileListCreateAPIView(generics.ListCreateAPIView):

    serializer_class = ManagedFileSerializer
    permission_classes = [IsAdminUserRole]

    def get_queryset(self):
        return ManagedFile.objects.select_related(
            "uploaded_by"
        ).order_by("-uploaded_at")

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)


class ManagedFileDetailAPIView(generics.RetrieveDestroyAPIView):

    serializer_class = ManagedFileSerializer
    permission_classes = [IsAdminUserRole]

    queryset = ManagedFile.objects.select_related(
        "uploaded_by"
    )

    http_method_names = ["get", "delete", "head", "options"]

    def perform_destroy(self, instance):

        # Save storage information before deleting the database record.
        file_name = instance.file.name if instance.file else None
        file_storage = instance.file.storage if instance.file else None

        # Delete the database record.
        super().perform_destroy(instance)

        # Delete the physical file after database transaction commits.
        if file_name and file_storage:
            transaction.on_commit(
                lambda storage=file_storage, name=file_name:
                    storage.delete(name)
            )


class ManagedFileDownloadAPIView(APIView):

    permission_classes = [IsAdminUserRole]

    def get(self, request, file_id):

        managed_file = get_object_or_404(
            ManagedFile,
            pk=file_id
        )

        if not managed_file.file:
            raise Http404("File not found.")

        try:
            managed_file.file.open("rb")

        except (OSError, ValueError):
            raise Http404("File not found.")

        filename = managed_file.original_filename

        response = FileResponse(
            managed_file.file,
            as_attachment=True,
            filename=filename,
        )

        response["X-Content-Type-Options"] = "nosniff"

        return response
