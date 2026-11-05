from rest_framework import serializers


class StudyStreakSerializer(serializers.Serializer):
    current_streak = serializers.IntegerField(min_value=0)
    longest_streak = serializers.IntegerField(min_value=0)
    total_study_days = serializers.IntegerField(min_value=0)
    last_activity_date = serializers.DateField(
        allow_null=True
    )