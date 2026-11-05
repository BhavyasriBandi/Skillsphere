from rest_framework import serializers
from .models import LearningResource


class LearningResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningResource
        fields = [
            "id",
            "title",
            "category",
            "skill",
            "level",
            "resource_type",
            "description",
            "url",
            "is_active",
            "created_at",
        ]
