
from rest_framework import serializers

from .models import (
    MentorStudentAssignment,
    MentorProfile,
    MentorFeedback,
    MentorMessage,
)


# =====================================================
# MENTOR SERIALIZER
# =====================================================

class MentorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    full_name = serializers.CharField()
    email = serializers.EmailField(allow_blank=True)
    expertise = serializers.ListField(
        child=serializers.CharField()
    )


# =====================================================
# MENTORSHIP REQUEST SERIALIZER
# =====================================================

class MentorshipRequestSerializer(serializers.Serializer):
    mentor_id = serializers.IntegerField(min_value=1)

    message = serializers.CharField(
        max_length=1000,
        allow_blank=False,
    )

    def validate_message(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Please enter a mentorship request message."
            )

        return value


# =====================================================
# STUDENT TO MENTOR FEEDBACK SERIALIZER
# EXISTING FUNCTIONALITY - PRESERVED
# =====================================================

class MentorFeedbackSerializer(serializers.Serializer):
    mentor_id = serializers.IntegerField(min_value=1)

    rating = serializers.IntegerField(
        min_value=1,
        max_value=5,
    )

    feedback = serializers.CharField(
        max_length=1000,
        allow_blank=False,
    )

    def validate_feedback(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Please enter feedback."
            )

        return value


# =====================================================
# MENTOR TO STUDENT FEEDBACK SERIALIZER
# =====================================================

class MentorStudentFeedbackSerializer(serializers.ModelSerializer):

    student_name = serializers.CharField(
        source="student.get_full_name",
        read_only=True,
    )

    student_email = serializers.EmailField(
        source="student.email",
        read_only=True,
    )

    mentor_name = serializers.CharField(
        source="mentor.get_full_name",
        read_only=True,
    )

    class Meta:
        model = MentorFeedback

        fields = [
            "id",
            "mentor",
            "mentor_name",
            "student",
            "student_name",
            "student_email",
            "subject",
            "feedback",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "mentor",
            "mentor_name",
            "student_name",
            "student_email",
            "created_at",
            "updated_at",
        ]

    def validate_subject(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Please enter a feedback subject."
            )

        return value

    def validate_feedback(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Please enter feedback."
            )

        return value


# =====================================================
# MENTOR MESSAGE SERIALIZER
# =====================================================

class MentorMessageSerializer(serializers.ModelSerializer):

    sender_name = serializers.CharField(
        source="sender.get_full_name",
        read_only=True,
    )

    recipient_name = serializers.CharField(
        source="recipient.get_full_name",
        read_only=True,
    )

    sender_email = serializers.EmailField(
        source="sender.email",
        read_only=True,
    )

    recipient_email = serializers.EmailField(
        source="recipient.email",
        read_only=True,
    )

    class Meta:
        model = MentorMessage

        fields = [
            "id",
            "sender",
            "sender_name",
            "sender_email",
            "recipient",
            "recipient_name",
            "recipient_email",
            "message",
            "is_read",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "sender",
            "sender_name",
            "sender_email",
            "recipient_name",
            "recipient_email",
            "is_read",
            "created_at",
        ]

    def validate_message(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Please enter a message."
            )

        return value


# =====================================================
# MENTOR STUDENT ASSIGNMENT SERIALIZER
# =====================================================

class MentorStudentAssignmentSerializer(serializers.ModelSerializer):

    mentor_name = serializers.CharField(
        source="mentor.get_full_name",
        read_only=True,
    )

    student_name = serializers.CharField(
        source="student.get_full_name",
        read_only=True,
    )

    student_email = serializers.EmailField(
        source="student.email",
        read_only=True,
    )

    class Meta:
        model = MentorStudentAssignment

        fields = [
            "id",
            "mentor",
            "mentor_name",
            "student",
            "student_name",
            "student_email",
            "status",
            "source",
            "assigned_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "mentor",
            "student",
            "status",
            "source",
            "assigned_at",
            "updated_at",
        ]


# =====================================================
# MENTOR ASSIGNMENT DECISION SERIALIZER
# =====================================================

class MentorAssignmentDecisionSerializer(serializers.Serializer):

    status = serializers.ChoiceField(
        choices=["Active", "Rejected"]
    )


# =====================================================
# MENTOR PROFILE SERIALIZER
# =====================================================

class MentorProfileSerializer(serializers.ModelSerializer):

    mentor_name = serializers.CharField(
        source="mentor.get_full_name",
        read_only=True,
    )

    email = serializers.EmailField(
        source="mentor.email",
        read_only=True,
    )

    class Meta:
        model = MentorProfile

        fields = [
            "id",
            "mentor_name",
            "email",
            "phone",
            "location",
            "qualification",
            "college",
            "specialization",
            "expertise",
            "skills",
            "experience",
            "bio",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "mentor_name",
            "email",
            "created_at",
            "updated_at",
        ]

    def validate_experience(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Experience cannot be negative."
            )

        if value > 60:
            raise serializers.ValidationError(
                "Please enter a valid experience value."
            )

        return value
