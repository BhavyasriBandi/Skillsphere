
from rest_framework import serializers


class LearningResourceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    skill = serializers.CharField()
    resource_type = serializers.CharField()
    url = serializers.URLField()
    difficulty = serializers.CharField()
    duration = serializers.CharField()


class ResourceSearchSerializer(serializers.Serializer):
    skill = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=False,
    )
    resource_type = serializers.CharField(
        max_length=50,
        required=False,
        allow_blank=False,
    )
    difficulty = serializers.CharField(
        max_length=30,
        required=False,
        allow_blank=False,
    )
