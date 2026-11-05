
import os
import zipfile

import magic

from rest_framework import serializers

from .models import ManagedFile


MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

ALLOWED_EXTENSIONS = {
    ".pdf", ".doc", ".docx", ".ppt", ".pptx",
    ".xls", ".xlsx", ".txt", ".csv",
    ".png", ".jpg", ".jpeg", ".webp", ".zip",
}

# Expected MIME types for supported extensions
ALLOWED_MIME_TYPES = {
    ".pdf": {"application/pdf"},
    ".doc": {"application/msword", "application/x-ole-storage"},
    ".docx": {
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        "application/zip",
    },
    ".ppt": {"application/vnd.ms-powerpoint", "application/x-ole-storage"},
    ".pptx": {
        "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        "application/zip",
    },
    ".xls": {"application/vnd.ms-excel", "application/x-ole-storage"},
    ".xlsx": {
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        "application/zip",
    },
    ".txt": {"text/plain"},
    ".csv": {"text/plain", "text/csv", "application/csv"},
    ".png": {"image/png"},
    ".jpg": {"image/jpeg"},
    ".jpeg": {"image/jpeg"},
    ".webp": {"image/webp"},
    ".zip": {"application/zip"},
}

OOXML_REQUIRED_FILES = {
    ".docx": "word/document.xml",
    ".pptx": "ppt/presentation.xml",
    ".xlsx": "xl/workbook.xml",
}


class ManagedFileSerializer(serializers.ModelSerializer):

    uploaded_by_email = serializers.EmailField(
        source="uploaded_by.email",
        read_only=True,
    )

    original_filename = serializers.CharField(read_only=True)

    file = serializers.FileField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = ManagedFile

        fields = [
            "id",
            "title",
            "file",
            "original_filename",
            "category",
            "uploaded_by",
            "uploaded_by_email",
            "uploaded_at",
        ]

        read_only_fields = [
            "id",
            "uploaded_by",
            "uploaded_by_email",
            "uploaded_at",
            "original_filename",
        ]

    def validate_title(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "File title cannot be empty."
            )

        if len(value) > 200:
            raise serializers.ValidationError(
                "File title cannot exceed 200 characters."
            )

        return value

    def validate_category(self, value):
        allowed_categories = {
            choice[0]
            for choice in ManagedFile.CATEGORY_CHOICES
        }

        if value not in allowed_categories:
            raise serializers.ValidationError(
                "Invalid file category."
            )

        return value

    def validate_file(self, value):

        # 1. Reject empty files
        if value.size == 0:
            raise serializers.ValidationError(
                "Empty files cannot be uploaded."
            )

        # 2. Check file size
        if value.size > MAX_FILE_SIZE:
            raise serializers.ValidationError(
                "File size must not exceed 10 MB."
            )

        # 3. Check extension
        extension = os.path.splitext(value.name)[1].lower()

        if extension not in ALLOWED_EXTENSIONS:
            raise serializers.ValidationError(
                "Unsupported file type."
            )

        # 4. Detect actual MIME type
        try:
            file_header = value.read(8192)
            value.seek(0)

            detected_mime = magic.from_buffer(
                file_header,
                mime=True,
            )

        except Exception:
            value.seek(0)

            raise serializers.ValidationError(
                "Unable to verify file content."
            )

        if detected_mime not in ALLOWED_MIME_TYPES[extension]:
            raise serializers.ValidationError(
                "File content does not match its extension."
            )

        # 5. Verify Office Open XML archive structure
        if extension in OOXML_REQUIRED_FILES:

            try:
                value.seek(0)

                with zipfile.ZipFile(value, "r") as archive:
                    required_file = OOXML_REQUIRED_FILES[extension]

                    if required_file not in archive.namelist():
                        raise serializers.ValidationError(
                            "Invalid Office document structure."
                        )

                    if "[Content_Types].xml" not in archive.namelist():
                        raise serializers.ValidationError(
                            "Invalid Office document structure."
                        )

            except zipfile.BadZipFile:
                raise serializers.ValidationError(
                    "Invalid or corrupted Office document."
                )

            finally:
                value.seek(0)

        return value
