
from rest_framework import serializers

from .models import (
    SkillCategory,
    Skill,
    StudentSkill,
    SkillAssessmentResult,
)


class SkillCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillCategory
        fields = ["id", "name", "description", "created_at"]
        read_only_fields = ["id", "created_at"]


class SkillSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source="category.name",
        read_only=True,
    )

    class Meta:
        model = Skill
        fields = [
            "id",
            "name",
            "description",
            "category",
            "category_name",
            "is_active",
            "created_at",
        ]
        read_only_fields = ["id", "category_name", "created_at"]


class StudentSkillSerializer(serializers.ModelSerializer):
    skill_name = serializers.CharField(
        source="skill.name",
        read_only=True,
    )
    category_name = serializers.CharField(
        source="skill.category.name",
        read_only=True,
    )

    class Meta:
        model = StudentSkill
        fields = [
            "id",
            "user",
            "skill",
            "skill_name",
            "category_name",
            "proficiency",
            "is_completed",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "user",
            "skill_name",
            "category_name",
            "created_at",
            "updated_at",
        ]


class SkillAssessmentSerializer(serializers.Serializer):
    skill_name = serializers.CharField(
        max_length=100,
        trim_whitespace=True,
    )
    answers = serializers.ListField(
        child=serializers.IntegerField(min_value=0, max_value=3),
        allow_empty=False,
    )
    score = serializers.IntegerField(min_value=0, required=True)
    total_questions = serializers.IntegerField(min_value=1, required=True)
    percentage = serializers.DecimalField(
        max_digits=5,
        decimal_places=2,
        min_value=0,
        max_value=100,
        required=True,
    )

    def validate_skill_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError(
                "Skill name cannot be empty."
            )
        return value

    def validate(self, attrs):
        answers = attrs["answers"]
        score = attrs["score"]
        total = attrs["total_questions"]
        percentage = attrs["percentage"]

        if total != 10:
            raise serializers.ValidationError({
                "total_questions": "An assessment must contain 10 questions."
            })

        if len(answers) != total:
            raise serializers.ValidationError({
                "answers": "Please submit answers to all 10 questions."
            })

        if score > total:
            raise serializers.ValidationError({
                "score": "Score cannot exceed the total questions."
            })

        expected_percentage = round((score / total) * 100, 2)

        if round(float(percentage), 2) != expected_percentage:
            raise serializers.ValidationError({
                "percentage": "Percentage does not match the submitted score."
            })

        return attrs


class AssessmentStartSerializer(serializers.Serializer):
    skill_name = serializers.CharField(
        max_length=100,
        trim_whitespace=True,
    )
    difficulty = serializers.ChoiceField(
        choices=["beginner", "intermediate", "advanced"],
        default="intermediate",
    )

    def validate_skill_name(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Skill name cannot be empty."
            )
        return value.strip()


class AssessmentSubmitSerializer(serializers.Serializer):
    attempt_id = serializers.IntegerField(min_value=1)
    answers = serializers.ListField(
        child=serializers.IntegerField(min_value=0, max_value=3),
        min_length=10,
        max_length=10,
    )


class SkillProgressQuerySerializer(serializers.Serializer):
    skill_name = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=False,
        trim_whitespace=True,
    )


class SkillAssessmentResultSerializer(serializers.ModelSerializer):
    skill_name = serializers.CharField(
        source="skill.name",
        read_only=True,
    )

    class Meta:
        model = SkillAssessmentResult
        fields = [
            "id",
            "user",
            "skill",
            "skill_name",
            "score",
            "total_questions",
            "percentage",
            "answers",
            "completed_at",
        ]
        read_only_fields = [
            "id",
            "user",
            "skill_name",
            "percentage",
            "completed_at",
        ]
