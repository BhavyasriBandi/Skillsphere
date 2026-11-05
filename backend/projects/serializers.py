
from rest_framework import serializers

from .models import StudentProject


class StudentProjectSerializer(serializers.ModelSerializer):
    student = serializers.IntegerField(
        source="student_id",
        read_only=True,
    )

    class Meta:
        model = StudentProject
        fields = [
            "id",
            "student",
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
        read_only_fields = [
            "id",
            "student",
            "created_at",
            "updated_at",
        ]

    def validate_title(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError(
                "Project title is required."
            )
        return value

    def validate_technologies(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError(
                "Technologies must be a list."
            )

        cleaned = []
        for technology in value:
            if not isinstance(technology, str):
                raise serializers.ValidationError(
                    "Each technology must be text."
                )

            technology = technology.strip()
            if technology and technology not in cleaned:
                cleaned.append(technology)

        return cleaned

    def validate_github(self, value):
        return value.strip()

    def validate_live_demo(self, value):
        return value.strip()


class AdminStudentProjectSerializer(StudentProjectSerializer):
    student = serializers.PrimaryKeyRelatedField(
        queryset=StudentProject._meta.get_field("student").remote_field.model.objects.all()
    )

    class Meta(StudentProjectSerializer.Meta):
        read_only_fields = ["id", "created_at", "updated_at"]
