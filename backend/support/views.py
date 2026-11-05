from django.shortcuts import render

# Create your views here.
from datetime import datetime, timezone

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SupportTicketSerializer


# Temporary in-memory storage; data is lost on server restart.
SUPPORT_TICKETS = []
NEXT_TICKET_ID = 1


class SupportTicketListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tickets = [
            {
                key: value
                for key, value in ticket.items()
                if key != "user_id"
            }
            for ticket in SUPPORT_TICKETS
            if ticket["user_id"] == request.user.id
        ]

        return Response(
            SupportTicketSerializer(tickets, many=True).data
        )

    def post(self, request):
        global NEXT_TICKET_ID

        serializer = SupportTicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        ticket = {
            "id": NEXT_TICKET_ID,
            "user_id": request.user.id,
            "subject": data["subject"],
            "category": data["category"],
            "description": data["description"],
            "priority": data.get("priority", "Medium"),
            "status": "Open",
            "created_at": datetime.now(timezone.utc),
        }

        SUPPORT_TICKETS.append(ticket)
        NEXT_TICKET_ID += 1

        response_data = {
            key: value
            for key, value in ticket.items()
            if key != "user_id"
        }

        return Response(
            SupportTicketSerializer(response_data).data,
            status=status.HTTP_201_CREATED,
        )


class SupportTicketDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_ticket(self, request, ticket_id):
        return next(
            (
                ticket
                for ticket in SUPPORT_TICKETS
                if ticket["id"] == ticket_id
                and ticket["user_id"] == request.user.id
            ),
            None,
        )

    def get(self, request, ticket_id):
        ticket = self.get_ticket(request, ticket_id)

        if ticket is None:
            return Response(
                {"error": "Support ticket not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        response_data = {
            key: value
            for key, value in ticket.items()
            if key != "user_id"
        }

        return Response(
            SupportTicketSerializer(response_data).data
        )


class SupportTicketCancelView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, ticket_id):
        ticket = next(
            (
                item for item in SUPPORT_TICKETS
                if item["id"] == ticket_id
                and item["user_id"] == request.user.id
            ),
            None,
        )

        if ticket is None:
            return Response(
                {"error": "Support ticket not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        SUPPORT_TICKETS.remove(ticket)

        return Response(
            {"message": "Support ticket deleted successfully."},
            status=status.HTTP_200_OK,
        )