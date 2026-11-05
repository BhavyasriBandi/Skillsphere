
from django.utils import timezone
from rest_framework import serializers

from .models import InterviewQuestion, InterviewPractice


class InterviewQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewQuestion
        fields = [
            "id",
            "question",
            "category",
            "difficulty",
            "suggested_answer",
            "explanation",
            "keywords",
            "is_active",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class InterviewPracticeSerializer(serializers.ModelSerializer):
    question_details = InterviewQuestionSerializer(
        source="question",
        read_only=True,
    )

    question_id = serializers.PrimaryKeyRelatedField(
        source="question",
        queryset=InterviewQuestion.objects.filter(is_active=True),
        write_only=True,
        required=False,
    )

    class Meta:
        model = InterviewPractice
        fields = [
            "id",
            "question_id",
            "question_details",
            "student_answer",
            "is_practiced",
            "is_bookmarked",
            "last_practiced_at",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "last_practiced_at",
            "created_at",
            "updated_at",
        ]

    def validate(self, attrs):
        question = attrs.get(
            "question",
            getattr(self.instance, "question", None),
        )

        if question is not None and self.instance is None:
            request = self.context.get("request")

            if request and InterviewPractice.objects.filter(
                student=request.user,
                question=question,
            ).exists():
                raise serializers.ValidationError({
                    "question_id": (
                        "You already have a practice record for this question."
                    )
                })

        return attrs

    def create(self, validated_data):
        if validated_data.get("is_practiced"):
            validated_data["last_practiced_at"] = timezone.now()

        return super().create(validated_data)

    def update(self, instance, validated_data):
        if validated_data.get("is_practiced") is True:
            validated_data["last_practiced_at"] = timezone.now()

        return super().update(instance, validated_data)
