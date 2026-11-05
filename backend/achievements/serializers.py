
from rest_framework import serializers

from .models import Achievement, StudentAchievement


class AchievementSerializer(serializers.ModelSerializer):
    badge_type = serializers.CharField(
        source="achievement.tier",
        read_only=True,
    )
    title = serializers.CharField(
        source="achievement.title",
        read_only=True,
    )
    description = serializers.CharField(
        source="achievement.description",
        read_only=True,
    )
    points = serializers.IntegerField(
        source="achievement.points",
        read_only=True,
    )

    class Meta:
        model = StudentAchievement
        fields = [
            "id",
            "title",
            "description",
            "badge_type",
            "points",
            "earned_at",
            "is_earned",
            "is_saved",
            "saved_at",
        ]
        read_only_fields = fields


class AchievementDefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = [
            "id",
            "badge_key",
            "title",
            "description",
            "icon",
            "category",
            "tier",
            "requirement",
            "target",
            "points",
            "is_active",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    def validate_badge_key(self, value):
        value = value.strip().lower()

        queryset = Achievement.objects.filter(badge_key=value)

        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError(
                "This badge key already exists."
            )

        return value

    def validate_target(self, value):
        if value < 1:
            raise serializers.ValidationError(
                "Target must be at least 1."
            )
        return value

    def validate_points(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Points cannot be negative."
            )
        return value
