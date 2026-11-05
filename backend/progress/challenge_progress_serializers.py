
from rest_framework import serializers

from .models import ChallengeProgress


class ChallengeProgressSerializer(serializers.ModelSerializer):
    completedIds = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        source="completed_ids",
        required=False,
    )

    class Meta:
        model = ChallengeProgress
        fields = ["completedIds", "updated_at"]
        read_only_fields = ["updated_at"]

    def validate_completedIds(self, value):
        if len(value) != len(set(value)):
            raise serializers.ValidationError(
                "Duplicate completed challenge IDs are not allowed."
            )

        if len(value) > 14:
            raise serializers.ValidationError(
                "No more than 14 challenge IDs are allowed."
            )

        return value
