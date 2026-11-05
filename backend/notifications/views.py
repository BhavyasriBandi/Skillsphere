
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Notification
from .serializers import NotificationSerializer


class NotificationListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="list_notifications",
        summary="List My Notifications",
        responses={200: NotificationSerializer(many=True)},
    )
    def get(self, request):
        notifications = Notification.objects.filter(
            user=request.user
        )

        serializer = NotificationSerializer(
            notifications,
            many=True,
        )

        return Response(
            {
                "count": notifications.count(),
                "unread_count": notifications.filter(
                    is_read=False
                ).count(),
                "notifications": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class UnreadNotificationsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="list_unread_notifications",
        summary="List Unread Notifications",
    )
    def get(self, request):
        notifications = Notification.objects.filter(
            user=request.user,
            is_read=False,
        )

        serializer = NotificationSerializer(
            notifications,
            many=True,
        )

        return Response(
            {
                "count": notifications.count(),
                "notifications": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class MarkNotificationReadAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="mark_notification_read",
        summary="Mark Notification as Read",
    )
    def patch(self, request, notification_id):
        try:
            notification = Notification.objects.get(
                id=notification_id,
                user=request.user,
            )
        except Notification.DoesNotExist:
            return Response(
                {"detail": "Notification not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        notification.is_read = True
        notification.save(update_fields=["is_read"])

        return Response(
            {
                "notification_id": notification.id,
                "is_read": notification.is_read,
                "message": "Notification marked as read.",
            },
            status=status.HTTP_200_OK,
        )


class MarkAllNotificationsReadAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="mark_all_notifications_read",
        summary="Mark All Notifications as Read",
    )
    def patch(self, request):
        updated_count = Notification.objects.filter(
            user=request.user,
            is_read=False,
        ).update(is_read=True)

        return Response(
            {
                "updated_count": updated_count,
                "message": "All notifications marked as read.",
            },
            status=status.HTTP_200_OK,
        )
