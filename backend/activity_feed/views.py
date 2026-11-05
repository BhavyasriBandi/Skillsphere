from django.shortcuts import render

# Create your views here.

from datetime import datetime, timezone

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema

from .serializers import ActivityFeedSerializer


# Temporary in-memory storage; activities are not persisted.
ACTIVITIES = []
NEXT_ACTIVITY_ID = 1


class ActivityFeedAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Get My Recent Learning Activities",
        responses=ActivityFeedSerializer(many=True),
    )
    def get(self, request):
        activities = [
            activity
            for activity in ACTIVITIES
            if activity["user_id"] == request.user.pk
        ]

        activities.sort(
            key=lambda activity: activity["created_at"],
            reverse=True,
        )

        public_activities = [
            {
                key: value
                for key, value in activity.items()
                if key != "user_id"
            }
            for activity in activities
        ]

        serializer = ActivityFeedSerializer(
            public_activities,
            many=True,
        )

        return Response(
            {
                "count": len(serializer.data),
                "activities": serializer.data,
                "message": (
                    "Activities are temporary and are not saved "
                    "to the database."
                ),
            },
            status=status.HTTP_200_OK,
        )


class ActivityFeedCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Add a Learning Activity",
        request=ActivityFeedSerializer,
        responses={201: ActivityFeedSerializer},
    )
    def post(self, request):
        global NEXT_ACTIVITY_ID

        serializer = ActivityFeedSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        activity = {
            "id": NEXT_ACTIVITY_ID,
            "user_id": request.user.pk,
            **serializer.validated_data,
            "created_at": datetime.now(timezone.utc),
        }

        ACTIVITIES.append(activity)
        NEXT_ACTIVITY_ID += 1

        public_activity = {
            key: value
            for key, value in activity.items()
            if key != "user_id"
        }

        return Response(
            public_activity,
            status=status.HTTP_201_CREATED,
        )
