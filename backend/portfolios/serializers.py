
from rest_framework import serializers

from .models import Portfolio


class PortfolioSerializer(serializers.ModelSerializer):
    # Keep the names expected by the existing React form.
    name = serializers.CharField(
        source="full_name",
        max_length=150,
    )
    headline = serializers.CharField(
        source="professional_title",
        max_length=150,
        required=False,
        default="Aspiring Software Developer",
    )
    objective = serializers.CharField(
        source="summary",
        max_length=2000,
        required=False,
        allow_blank=True,
        default="",
    )

    class Meta:
        model = Portfolio
        fields = [
            "id",
            "name",
            "headline",
            "email",
            "location",
            "phone",
            "objective",
            "skills",
            "education",
            "projects",
            "certifications",
            "resume_url",
            "portfolio_url",
            "github_url",
            "linkedin_url",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

    def validate_skills(self, value):
        if not isinstance(value, str):
            raise serializers.ValidationError(
                "Skills must be provided as text."
            )
        return value.strip()

    def validate_education(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError(
                "Education must be a list."
            )
        if len(value) > 30:
            raise serializers.ValidationError(
                "You can add a maximum of 30 education entries."
            )
        return value

    def validate_projects(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError(
                "Projects must be a list."
            )
        if len(value) > 50:
            raise serializers.ValidationError(
                "You can add a maximum of 50 projects."
            )
        return value
