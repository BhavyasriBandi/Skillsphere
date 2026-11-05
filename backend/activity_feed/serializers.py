
from rest_framework import serializers


class ActivityFeedSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    activity_type = serializers.ChoiceField(
        choices=[
            "skill",
            "assessment",
            "career",
            "learning_goal",
            "study_session",
        ]
    )
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(
        required=False,
        allow_blank=True,
        default="",
    )
    created_at = serializers.DateTimeField(read_only=True)
