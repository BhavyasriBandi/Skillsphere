
from rest_framework import serializers


class ProgressSummarySerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    skills_available = serializers.IntegerField()
    career_paths_available = serializers.IntegerField()
    assessment_attempts = serializers.IntegerField()
    completed_assessments = serializers.IntegerField()
    progress_percentage = serializers.FloatField()
    message = serializers.CharField()


class SkillProgressSerializer(serializers.Serializer):
    skill_name = serializers.CharField()
    current_level = serializers.CharField()
    progress_percentage = serializers.FloatField()
    status = serializers.CharField()


class CareerReadinessSerializer(serializers.Serializer):
    career_id = serializers.IntegerField()
    career_title = serializers.CharField()
    required_skills_count = serializers.IntegerField()
    matched_skills = serializers.ListField(
        child=serializers.CharField()
    )
    missing_skills = serializers.ListField(
        child=serializers.CharField()
    )
    readiness_percentage = serializers.FloatField()


class AchievementSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    status = serializers.CharField()
