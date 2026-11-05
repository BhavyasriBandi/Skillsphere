from rest_framework import serializers

from .models import LearningHubProgress


class LearningHubProgressSerializer(serializers.ModelSerializer):
    completedLessons = serializers.ListField(
        child=serializers.CharField(max_length=100),
        required=False,
    )

    savedCourses = serializers.ListField(
        child=serializers.CharField(max_length=100),
        required=False,
    )

    class Meta:
        model = LearningHubProgress
        fields = [
            "completedLessons",
            "savedCourses",
        ]

    def to_representation(self, instance):
        return {
            "completedLessons": instance.completed_lessons,
            "savedCourses": instance.saved_courses,
        }

    def update(self, instance, validated_data):
        if "completedLessons" in validated_data:
            instance.completed_lessons = validated_data["completedLessons"]

        if "savedCourses" in validated_data:
            instance.saved_courses = validated_data["savedCourses"]

        instance.save()
        return instance