
from rest_framework import serializers


class AssessmentQuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    skill = serializers.CharField()
    question = serializers.CharField()
    options = serializers.ListField(
        child=serializers.CharField()
    )


class AssessmentSubmitSerializer(serializers.Serializer):
    skill = serializers.CharField(max_length=100)
    answers = serializers.DictField(
        child=serializers.IntegerField(min_value=0),
        allow_empty=False,
    )

    def validate_skill(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError(
                "Skill name is required."
            )
        return value


class SkillGapSerializer(serializers.Serializer):
    current_skills = serializers.ListField(
        child=serializers.CharField(max_length=100),
        allow_empty=True,
    )
    career_id = serializers.IntegerField(min_value=1)
from rest_framework import serializers
from .models import AssessmentQuestion


class AdminAssessmentQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentQuestion
        fields = [
            "id",
            "legacy_id",
            "skill",
            "question",
            "options",
            "correct_answer",
            "explanation",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "legacy_id",
            "created_at",
            "updated_at",
        ]

    def validate_skill(self, value):
        allowed_skills = {"python", "java", "c", "sql"}
        if value.strip().lower() not in allowed_skills:
            raise serializers.ValidationError(
                "Skill must be Python, Java, C, or SQL."
            )
        return "C" if value.strip().lower() == "c" else value.strip().title()

    def validate_options(self, value):
        if not isinstance(value, list) or len(value) < 2:
            raise serializers.ValidationError(
                "Provide at least two answer options."
            )

        if not all(isinstance(option, str) and option.strip() for option in value):
            raise serializers.ValidationError(
                "Every option must be a non-empty string."
            )

        return value

    def validate(self, attrs):
        options = attrs.get(
            "options",
            self.instance.options if self.instance else [],
        )
        correct_answer = attrs.get(
            "correct_answer",
            self.instance.correct_answer if self.instance else None,
        )

        if correct_answer is not None and not (
            isinstance(correct_answer, int)
            and 0 <= correct_answer < len(options)
        ):
            raise serializers.ValidationError({
                "correct_answer": "Must be a valid zero-based option index."
            })

        return attrs