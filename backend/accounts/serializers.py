
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError

from rest_framework import serializers

from .models import StudentProfile


User = get_user_model()


# ============================================================
# REGISTRATION SERIALIZER
# Public registration: Student and Mentor only
# ============================================================

class RegisterSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(
        write_only=True,
        trim_whitespace=False,
    )

    role = serializers.ChoiceField(
        choices=[
            ("Student", "Student"),
            ("Mentor", "Mentor"),
        ],
        default="Student",
        error_messages={
            "invalid_choice": (
                "Public registration is allowed only for Student and Mentor."
            )
        },
    )

    class Meta:
        model = User

        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "confirm_password",
            "role",
        ]

        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            "email": {"required": True},
            "password": {
                "write_only": True,
                "min_length": 8,
            },
        }

    def validate_first_name(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "First name is required."
            )

        return value

    def validate_last_name(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Last name is required."
            )

        return value

    def validate_email(self, value):
        email = value.strip().lower()

        if not email:
            raise serializers.ValidationError(
                "Email is required."
            )

        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError(
                "An account with this email already exists."
            )

        return email

    def validate_password(self, value):
        try:
            validate_password(value)
        except DjangoValidationError as error:
            raise serializers.ValidationError(error.messages)

        return value

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError({
                "confirm_password": "Passwords do not match."
            })

        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password")

        role = validated_data.pop("role", "Student")
        email = validated_data.pop("email").lower()
        password = validated_data.pop("password")

        user = User(
            username=email,
            email=email,
            **validated_data,
        )

        user.set_password(password)

        # Account remains inactive until email verification.
        user.is_active = False
        user.is_staff = False
        user.is_superuser = False

        user.save()

        group, _ = Group.objects.get_or_create(name=role)
        user.groups.add(group)

        return user


# ============================================================
# PROFILE UPDATE SERIALIZER
# ============================================================

class ProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = [
            "first_name",
            "last_name",
        ]

        extra_kwargs = {
            "first_name": {
                "required": False,
                "allow_blank": False,
            },
            "last_name": {
                "required": False,
                "allow_blank": False,
            },
        }


# ============================================================
# CHANGE PASSWORD SERIALIZER
# ============================================================

class ChangePasswordSerializer(serializers.Serializer):

    current_password = serializers.CharField(
        write_only=True,
        trim_whitespace=False,
    )

    new_password = serializers.CharField(
        write_only=True,
        min_length=8,
        trim_whitespace=False,
    )

    confirm_new_password = serializers.CharField(
        write_only=True,
        trim_whitespace=False,
    )

    def validate_current_password(self, value):
        user = self.context["request"].user

        if not user.check_password(value):
            raise serializers.ValidationError(
                "Current password is incorrect."
            )

        return value

    def validate(self, attrs):
        if attrs["new_password"] != attrs["confirm_new_password"]:
            raise serializers.ValidationError({
                "confirm_new_password": "New passwords do not match."
            })

        user = self.context["request"].user

        try:
            validate_password(
                attrs["new_password"],
                user=user,
            )
        except DjangoValidationError as error:
            raise serializers.ValidationError({
                "new_password": error.messages
            })

        if user.check_password(attrs["new_password"]):
            raise serializers.ValidationError({
                "new_password": (
                    "New password must be different from the current password."
                )
            })

        return attrs


# ============================================================
# STUDENT PROFILE SERIALIZER
# ============================================================

class StudentProfileSerializer(serializers.Serializer):

    fullName = serializers.CharField(
        required=False,
        allow_blank=False,
        max_length=150,
    )

    email = serializers.EmailField(read_only=True)

    phone = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=30,
    )

    college = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
    )

    qualification = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=120,
    )

    branch = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=120,
    )

    graduationYear = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=4,
    )

    location = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
    )

    careerInterest = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255,
    )

    bio = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=500,
    )

    def to_representation(self, instance):
        user = instance.user

        full_name = (
            f"{user.first_name} {user.last_name}".strip()
            or user.username
        )

        return {
            "fullName": full_name,
            "email": user.email,
            "phone": instance.phone,
            "college": instance.college,
            "qualification": instance.qualification,
            "branch": instance.branch,
            "graduationYear": instance.graduation_year,
            "location": instance.location,
            "careerInterest": instance.career_interest,
            "bio": instance.bio,
        }

    def update(self, instance, validated_data):
        full_name = validated_data.pop("fullName", None)

        if full_name is not None:
            name_parts = full_name.strip().split(maxsplit=1)

            instance.user.first_name = name_parts[0]

            instance.user.last_name = (
                name_parts[1]
                if len(name_parts) > 1
                else ""
            )

            instance.user.save(
                update_fields=[
                    "first_name",
                    "last_name",
                ]
            )

        field_mapping = {
            "phone": "phone",
            "college": "college",
            "qualification": "qualification",
            "branch": "branch",
            "graduationYear": "graduation_year",
            "location": "location",
            "careerInterest": "career_interest",
            "bio": "bio",
        }

        for api_field, model_field in field_mapping.items():
            if api_field in validated_data:
                setattr(
                    instance,
                    model_field,
                    validated_data[api_field],
                )

        instance.save()

        return instance
