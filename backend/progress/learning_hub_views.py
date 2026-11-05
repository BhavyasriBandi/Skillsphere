from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import LearningHubProgress
from .learning_hub_serializers import LearningHubProgressSerializer


class LearningHubProgressAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="get_learning_hub_progress",
        summary="Get Learning Hub Progress",
        responses={200: LearningHubProgressSerializer},
    )
    def get(self, request):
        progress, _ = LearningHubProgress.objects.get_or_create(
            user=request.user
        )

        serializer = LearningHubProgressSerializer(progress)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        operation_id="update_learning_hub_progress",
        summary="Update Learning Hub Progress",
        request=LearningHubProgressSerializer,
        responses={200: LearningHubProgressSerializer},
    )
    def patch(self, request):
        progress, _ = LearningHubProgress.objects.get_or_create(
            user=request.user
        )

        serializer = LearningHubProgressSerializer(
            progress,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)