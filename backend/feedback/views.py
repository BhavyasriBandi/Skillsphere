from django.shortcuts import render

# Create your views here.

from datetime import datetime, timezone

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema

from .serializers import FeedbackSerializer


# Temporary in-memory storage; not persistent.
FEEDBACK_ENTRIES = []
NEXT_FEEDBACK_ID = 1


class FeedbackListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="List My Feedback",
        responses=FeedbackSerializer(many=True),
    )
    def get(self, request):
        entries = [
            {
                key: value
                for key, value in entry.items()
                if key != "user_id"
            }
            for entry in FEEDBACK_ENTRIES
            if entry["user_id"] == request.user.pk
        ]

        return Response({
            "count": len(entries),
            "feedback": entries,
        })

    @extend_schema(
        summary="Submit Feedback",
        request=FeedbackSerializer,
    )
    def post(self, request):
        global NEXT_FEEDBACK_ID

        serializer = FeedbackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        entry = {
            "id": NEXT_FEEDBACK_ID,
            "user_id": request.user.pk,
            **serializer.validated_data,
            "created_at": datetime.now(timezone.utc),
        }

        FEEDBACK_ENTRIES.append(entry)
        NEXT_FEEDBACK_ID += 1

        public_entry = {
            key: value
            for key, value in entry.items()
            if key != "user_id"
        }

        return Response(
            public_entry,
            status=status.HTTP_201_CREATED,
        )


class FeedbackDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_feedback(self, request, feedback_id):
        return next(
            (
                entry for entry in FEEDBACK_ENTRIES
                if entry["id"] == feedback_id
                and entry["user_id"] == request.user.pk
            ),
            None,
        )

    @extend_schema(
        summary="Retrieve My Feedback",
        responses=FeedbackSerializer,
    )
    def get(self, request, feedback_id):
        entry = self.get_feedback(request, feedback_id)

        if entry is None:
            return Response(
                {"detail": "Feedback not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response({
            key: value
            for key, value in entry.items()
            if key != "user_id"
        })

    @extend_schema(summary="Delete My Feedback")
    def delete(self, request, feedback_id):
        entry = self.get_feedback(request, feedback_id)

        if entry is None:
            return Response(
                {"detail": "Feedback not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        FEEDBACK_ENTRIES.remove(entry)

        return Response(
            {"message": "Feedback deleted successfully."},
            status=status.HTTP_200_OK,
        )
