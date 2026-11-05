
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsMentor

from .models import (
    MentorStudentAssignment,
    MentorFeedback,
    MentorMessage,
)

from .serializers import (
    MentorStudentFeedbackSerializer,
    MentorMessageSerializer,
)


User = get_user_model()


# =====================================================
# HELPER: GET ACTIVELY ASSIGNED STUDENTS
# =====================================================

def get_active_mentor_students(mentor):
    return User.objects.filter(
        student_mentor_assignments__mentor=mentor,
        student_mentor_assignments__status="Active",
    ).distinct()


def is_active_mentor_student(mentor, student):
    return MentorStudentAssignment.objects.filter(
        mentor=mentor,
        student=student,
        status="Active",
    ).exists()


# =====================================================
# MENTOR TO STUDENT FEEDBACK API
# GET  - View feedback
# POST - Give feedback
# =====================================================

class MentorStudentFeedbackAPIView(APIView):

    permission_classes = [IsAuthenticated, IsMentor]

    def get(self, request):

        student_id = request.query_params.get("student_id")

        feedbacks = MentorFeedback.objects.filter(
            mentor=request.user,
            student__in=get_active_mentor_students(request.user),
        ).select_related(
            "mentor",
            "student",
        )

        if student_id:
            try:
                student_id = int(student_id)
            except (TypeError, ValueError):
                return Response(
                    {"detail": "Invalid student ID."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            feedbacks = feedbacks.filter(
                student_id=student_id
            )

        serializer = MentorStudentFeedbackSerializer(
            feedbacks,
            many=True,
        )

        return Response(
            {
                "count": feedbacks.count(),
                "feedbacks": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request):

        # Accept either student_id or student.
        student_id = (
            request.data.get("student_id")
            or request.data.get("student")
        )

        if not student_id:
            return Response(
                {"student": ["This field is required."]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            student_id = int(student_id)
        except (TypeError, ValueError):
            return Response(
                {"student": ["Invalid student ID."]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        student = get_object_or_404(
            User,
            pk=student_id,
        )

        if not is_active_mentor_student(
            request.user,
            student,
        ):
            return Response(
                {
                    "detail": (
                        "You can give feedback only to "
                        "actively assigned students."
                    )
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        # Add student before serializer validation.
        feedback_data = request.data.copy()
        feedback_data["student"] = student.pk

        serializer = MentorStudentFeedbackSerializer(
            data=feedback_data,
        )

        serializer.is_valid(raise_exception=True)

        feedback = serializer.save(
            mentor=request.user,
            student=student,
        )

        return Response(
            {
                "detail": "Feedback submitted successfully.",
                "feedback": MentorStudentFeedbackSerializer(
                    feedback
                ).data,
            },
            status=status.HTTP_201_CREATED,
        )


# =====================================================
# MENTOR MESSAGES API
# GET  - Retrieve messages/conversation
# POST - Send message
# =====================================================

class MentorMessagesAPIView(APIView):

    permission_classes = [IsAuthenticated, IsMentor]

    def get(self, request):

        student_id = request.query_params.get("student_id")

        active_students = get_active_mentor_students(
            request.user
        )

        messages = (
            MentorMessage.objects.filter(
                sender=request.user,
                recipient__in=active_students,
            )
            |
            MentorMessage.objects.filter(
                recipient=request.user,
                sender__in=active_students,
            )
        )

        messages = messages.select_related(
            "sender",
            "recipient",
        ).order_by("created_at")

        if student_id:

            try:
                student_id = int(student_id)
            except (TypeError, ValueError):
                return Response(
                    {"detail": "Invalid student ID."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            student = get_object_or_404(
                active_students,
                pk=student_id,
            )

            messages = messages.filter(
                sender__in=[request.user, student],
                recipient__in=[request.user, student],
            )

            # Mark incoming student messages as read
            # when the mentor opens the conversation.
            MentorMessage.objects.filter(
                sender=student,
                recipient=request.user,
                is_read=False,
            ).update(is_read=True)

            messages = messages.order_by("created_at")

        serializer = MentorMessageSerializer(
            messages,
            many=True,
        )

        unread_count = MentorMessage.objects.filter(
            recipient=request.user,
            sender__in=active_students,
            is_read=False,
        ).count()

        return Response(
            {
                "count": messages.count(),
                "unread_count": unread_count,
                "messages": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request):

        student_id = request.data.get("student_id")

        if not student_id:
            return Response(
                {"detail": "Student ID is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            student_id = int(student_id)
        except (TypeError, ValueError):
            return Response(
                {"detail": "Invalid student ID."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        student = get_object_or_404(
            User,
            pk=student_id,
        )

        if not is_active_mentor_student(
            request.user,
            student,
        ):
            return Response(
                {
                    "detail": (
                        "You can message only actively "
                        "assigned students."
                    )
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        # IMPORTANT:
        # Add recipient before serializer validation.
        message_data = request.data.copy()
        message_data["recipient"] = student.pk

        serializer = MentorMessageSerializer(
            data=message_data,
        )

        serializer.is_valid(raise_exception=True)

        message = serializer.save(
            sender=request.user,
            recipient=student,
        )

        return Response(
            {
                "detail": "Message sent successfully.",
                "message": MentorMessageSerializer(
                    message
                ).data,
            },
            status=status.HTTP_201_CREATED,
        )


# =====================================================
# MARK MESSAGE AS READ API
# PATCH - Mark individual message as read
# =====================================================

class MentorMessageReadAPIView(APIView):

    permission_classes = [IsAuthenticated, IsMentor]

    def patch(self, request, message_id):

        message = get_object_or_404(
            MentorMessage,
            pk=message_id,
            recipient=request.user,
        )

        # Only messages from actively assigned students
        # can be marked as read by this mentor.
        if not is_active_mentor_student(
            request.user,
            message.sender,
        ):
            return Response(
                {
                    "detail": (
                        "You cannot access this message."
                    )
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        message.is_read = True

        message.save(
            update_fields=["is_read"]
        )

        return Response(
            {
                "detail": "Message marked as read.",
                "message_id": message.id,
                "is_read": message.is_read,
            },
            status=status.HTTP_200_OK,
        )
