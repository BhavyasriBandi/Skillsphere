from django.urls import path

from .views import (
    SupportTicketListCreateView,
    SupportTicketDetailView,
    SupportTicketCancelView,
)

urlpatterns = [
    path(
        "",
        SupportTicketListCreateView.as_view(),
        name="support-ticket-list-create",
    ),
    path(
        "<int:ticket_id>/",
        SupportTicketDetailView.as_view(),
        name="support-ticket-detail",
    ),
    path(
        "<int:ticket_id>/delete/",
        SupportTicketCancelView.as_view(),
        name="support-ticket-delete",
    ),
]