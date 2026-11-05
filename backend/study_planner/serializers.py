
from rest_framework import serializers


class StudySessionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    subject = serializers.CharField(max_length=100)
    study_date = serializers.DateField()
    start_time = serializers.TimeField()
    duration_minutes = serializers.IntegerField(
        min_value=15,
        max_value=720,
    )
    notes = serializers.CharField(
        required=False,
        allow_blank=True,
        default="",
    )
    status = serializers.ChoiceField(
        choices=["Scheduled", "Completed", "Skipped"],
        default="Scheduled",
    )
