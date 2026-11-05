
from rest_framework import serializers


class FeedbackSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    category = serializers.ChoiceField(
        choices=[
            "Platform",
            "Mentor",
            "Learning Resource",
        ]
    )
    rating = serializers.IntegerField(min_value=1, max_value=5)
    comments = serializers.CharField(
        max_length=1000,
        required=False,
        allow_blank=True,
        default="",
    )
    created_at = serializers.DateTimeField(read_only=True)
