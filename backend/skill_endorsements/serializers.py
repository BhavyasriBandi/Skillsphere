
from rest_framework import serializers


class SkillEndorsementSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    student_id = serializers.IntegerField()
    skill_name = serializers.CharField(max_length=100)
    message = serializers.CharField(
        max_length=500,
        required=False,
        allow_blank=True,
        default="",
    )
    endorsed_at = serializers.DateTimeField(read_only=True)
