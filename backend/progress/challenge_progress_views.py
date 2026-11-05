
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ChallengeProgress
from .challenge_progress_serializers import ChallengeProgressSerializer


class ChallengeProgressAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="get_challenge_progress",
        summary="Get Student Challenge Progress",
        responses={200: ChallengeProgressSerializer},
    )
    def get(self, request):
        progress, _ = ChallengeProgress.objects.get_or_create(
            user=request.user
        )

        serializer = ChallengeProgressSerializer(progress)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        operation_id="update_challenge_progress",
        summary="Update Student Challenge Progress",
        request=ChallengeProgressSerializer,
        responses={200: ChallengeProgressSerializer},
    )
    def patch(self, request):
        progress, _ = ChallengeProgress.objects.get_or_create(
            user=request.user
        )

        serializer = ChallengeProgressSerializer(
            progress,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
