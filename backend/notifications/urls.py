
from django.urls import path

from .views import (
    NotificationListAPIView,
    UnreadNotificationsAPIView,
    MarkNotificationReadAPIView,
    MarkAllNotificationsReadAPIView,
)


urlpatterns = [
    path(
        "",
        NotificationListAPIView.as_view(),
        name="notification-list",
    ),
    path(
        "unread/",
        UnreadNotificationsAPIView.as_view(),
        name="unread-notifications",
    ),
    path(
        "read-all/",
        MarkAllNotificationsReadAPIView.as_view(),
        name="mark-all-notifications-read",
    ),
    path(
        "<int:notification_id>/read/",
        MarkNotificationReadAPIView.as_view(),
        name="mark-notification-read",
    ),
   
]
