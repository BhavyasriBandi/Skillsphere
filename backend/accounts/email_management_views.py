
from django.conf import settings
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema

from .views import get_user_role


class AdminEmailManagementAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Send an email from SkillSphere Admin",
        description="Send a plain-text email to one recipient. "
                    "Restricted to platform administrators.",
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "recipient_email": {
                        "type": "string",
                        "format": "email",
                    },
                    "subject": {"type": "string"},
                    "message": {"type": "string"},
                },
                "required": [
                    "recipient_email",
                    "subject",
                    "message",
                ],
            }
        },
    )
    def post(self, request):
        if get_user_role(request.user) != "Admin":
            return Response(
                {"detail": "Only platform administrators can send emails."},
                status=status.HTTP_403_FORBIDDEN,
            )

        recipient = request.data.get("recipient_email", "")
        subject = request.data.get("subject", "")
        message = request.data.get("message", "")

        if not all(
            isinstance(value, str)
            for value in (recipient, subject, message)
        ):
            return Response(
                {"detail": "All fields must be text."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        recipient = recipient.strip()
        subject = subject.strip()
        message = message.strip()

        try:
            validate_email(recipient)
        except ValidationError:
            return Response(
                {"detail": "Enter a valid recipient email address."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not subject or len(subject) > 200:
            return Response(
                {"detail": "Subject is required and must be at most 200 characters."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not message or len(message) > 10000:
            return Response(
                {"detail": "Message is required and must be at most 10000 characters."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if (
            settings.EMAIL_BACKEND
            != "django.core.mail.backends.smtp.EmailBackend"
            or not settings.EMAIL_HOST_USER
            or not settings.EMAIL_HOST_PASSWORD
        ):
            return Response(
                {"detail": "SMTP email is not configured."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

        try:
            sent_count = send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[recipient],
                fail_silently=False,
            )
        except Exception:
            return Response(
                {"detail": "Unable to send email. Check the SMTP configuration."},
                status=status.HTTP_502_BAD_GATEWAY,
            )

        if sent_count != 1:
            return Response(
                {"detail": "The email was not accepted for sending."},
                status=status.HTTP_502_BAD_GATEWAY,
            )

        return Response(
            {
                "message": "Email accepted by the email server.",
                "recipient_email": recipient,
            },
            status=status.HTTP_200_OK,
        )
