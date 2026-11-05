
from datetime import date

from rest_framework import serializers

from .models import LearningGoal, CareerGoal


class LearningGoalSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = LearningGoal
        fields = [
            "id",
            "title",
            "description",
            "target_date",
            "status",
            "progress_percentage",
        ]

    def validate_target_date(self, value):
        if value < date.today():
            raise serializers.ValidationError(
                "Target date cannot be in the past."
            )
        return value


class CareerGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerGoal
        fields = [
            "career_role",
            "domain",
            "experience_level",
            "target_date",
            "objective",
        ]

    def validate_target_date(self, value):
        if value is not None and value < date.today():
            raise serializers.ValidationError(
                "Target date cannot be in the past."
            )
        return value
