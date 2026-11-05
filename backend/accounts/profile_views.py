from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema

from .models import StudentProfile
from .profile_serializers import (
    ProfileSerializer,
    ChangePasswordSerializer,
)
from .serializers import StudentProfileSerializer

User = get_user_model()


class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_student_profile(self, user):
        profile, _ = StudentProfile.objects.get_or_create(user=user)
        return profile

    def get_combined_profile(self, user):
        student_profile = self.get_student_profile(user)

        account_data = dict(ProfileSerializer(user).data)
        student_data = StudentProfileSerializer(student_profile).data

        account_data.update(student_data)

        return account_data

    @extend_schema(
        operation_id="get_profile",
        summary="Get My Profile",
    )
    def get(self, request):
        data = self.get_combined_profile(request.user)

        return Response(data, status=status.HTTP_200_OK)

    @extend_schema(
        operation_id="update_profile",
        summary="Update My Profile",
        request=StudentProfileSerializer,
    )
    def patch(self, request):
        user = request.user
        student_profile = self.get_student_profile(user)

        account_fields = {
            "first_name",
            "last_name",
            "email",
        }

        account_data = {
            key: value
            for key, value in request.data.items()
            if key in account_fields
        }

        student_fields = {
            "fullName",
            "phone",
            "college",
            "qualification",
            "branch",
            "graduationYear",
            "location",
            "careerInterest",
            "bio",
        }

        student_data = {
            key: value
            for key, value in request.data.items()
            if key in student_fields
        }

        account_serializer = ProfileSerializer(
            user,
            data=account_data,
            partial=True,
        )

        student_serializer = StudentProfileSerializer(
            student_profile,
            data=student_data,
            partial=True,
        )

        account_serializer.is_valid(raise_exception=True)
        student_serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            account_serializer.save()
            student_serializer.save()

        return Response(
            {
                "message": "Profile updated successfully.",
                **self.get_combined_profile(user),
            },
            status=status.HTTP_200_OK,
        )


class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="change_password",
        summary="Change Password",
        request=ChangePasswordSerializer,
    )
    def post(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data,
            context={"request": request},
        )

        serializer.is_valid(raise_exception=True)

        user = request.user
        user.set_password(serializer.validated_data["new_password"])
        user.save(update_fields=["password"])

        return Response(
            {
                "message": (
                    "Password changed successfully. "
                    "Please log in again with your new password."
                )
            },
            status=status.HTTP_200_OK,
        )