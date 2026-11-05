
import os
import uuid

from django.conf import settings
from django.db import models


def file_upload_path(instance, filename):
    extension = os.path.splitext(filename)[1].lower()
    return f"file_management/{uuid.uuid4().hex}{extension}"


class ManagedFile(models.Model):
    CATEGORY_CHOICES = [
        ("document", "Document"),
        ("learning", "Learning Material"),
        ("project", "Project File"),
        ("other", "Other"),
    ]

    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="managed_files",
    )
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to=file_upload_path)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="other",
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def original_filename(self):
        return os.path.basename(self.file.name)
