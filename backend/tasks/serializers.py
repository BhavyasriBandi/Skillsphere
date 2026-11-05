
from rest_framework import serializers


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    assigned_by = serializers.IntegerField()
    due_date = serializers.DateField(allow_null=True)
    status = serializers.ChoiceField(
        choices=["Pending", "Submitted", "Reviewed"]
    )


class TaskCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=2000)
    due_date = serializers.DateField(required=False, allow_null=True)
    student_id = serializers.IntegerField(min_value=1)

    def validate_title(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Task title is required.")
        return value

    def validate_description(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError(
                "Task description is required."
            )
        return value


class AssignmentSubmissionSerializer(serializers.Serializer):
    submission_text = serializers.CharField(max_length=5000)

    def validate_submission_text(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError(
                "Submission text cannot be empty."
            )
        return value


class TaskReviewSerializer(serializers.Serializer):
    feedback = serializers.CharField(max_length=2000)
    score = serializers.IntegerField(min_value=0, max_value=100)

    def validate_feedback(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError(
                "Review feedback cannot be empty."
            )
        return value
