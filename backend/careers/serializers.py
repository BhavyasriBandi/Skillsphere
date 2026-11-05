from rest_framework import serializers

from .models import RoadmapTaskProgress


class CareerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    required_skills = serializers.ListField(
        child=serializers.CharField()
    )
    opportunities = serializers.ListField(
        child=serializers.CharField()
    )
    learning_duration = serializers.CharField()


class CareerRecommendationRequestSerializer(serializers.Serializer):
    skills = serializers.ListField(
        child=serializers.CharField(max_length=100),
        allow_empty=False,
    )
    interests = serializers.ListField(
        child=serializers.CharField(max_length=100),
        required=False,
        default=list,
    )

    def validate_skills(self, value):
        cleaned = [
            skill.strip()
            for skill in value
            if skill.strip()
        ]

        if not cleaned:
            raise serializers.ValidationError(
                "Provide at least one valid skill."
            )

        return cleaned

    def validate_interests(self, value):
        return [
            interest.strip()
            for interest in value
            if interest.strip()
        ]


class CareerProgressQuerySerializer(serializers.Serializer):
    career_id = serializers.IntegerField(
        required=False,
        min_value=1,
    )


class RoadmapTaskProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadmapTaskProgress
        fields = [
            "id",
            "career",
            "task_id",
            "task_name",
            "is_completed",
            "updated_at",
        ]
        read_only_fields = ["id", "updated_at"]