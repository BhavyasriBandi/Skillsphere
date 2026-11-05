
from django.utils import timezone

from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsPlatformAdmin

from .models import InterviewQuestion, InterviewPractice
from .serializers import (
    InterviewQuestionSerializer,
    InterviewPracticeSerializer,
)


class InterviewQuestionListView(generics.ListAPIView):
    """List active questions for student practice."""

    serializer_class = InterviewQuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = InterviewQuestion.objects.filter(is_active=True)

        category = self.request.query_params.get("category")
        difficulty = self.request.query_params.get("difficulty")
        search = self.request.query_params.get("search")

        if category:
            queryset = queryset.filter(category__iexact=category)

        if difficulty:
            queryset = queryset.filter(difficulty__iexact=difficulty)

        if search:
            queryset = queryset.filter(question__icontains=search)

        return queryset


class InterviewPracticeListCreateView(generics.ListCreateAPIView):
    """List or create the authenticated student's practice records."""

    serializer_class = InterviewPracticeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return InterviewPractice.objects.filter(
            student=self.request.user
        ).select_related("question")

    def perform_create(self, serializer):
        question = serializer.validated_data["question"]

        if InterviewPractice.objects.filter(
            student=self.request.user,
            question=question,
        ).exists():
            raise ValidationError({
                "question_id": (
                    "You already have a practice record for this question."
                )
            })

        serializer.save(student=self.request.user)


class InterviewPracticeDetailView(
    generics.RetrieveUpdateDestroyAPIView
):
    """Manage only the authenticated student's own practice record."""

    serializer_class = InterviewPracticeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return InterviewPractice.objects.filter(
            student=self.request.user
        ).select_related("question")


class InterviewPracticeMarkView(APIView):
    """Mark the authenticated student's practice record as practiced."""

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            practice = InterviewPractice.objects.get(
                pk=pk,
                student=request.user,
            )
        except InterviewPractice.DoesNotExist:
            raise NotFound("Practice record not found.")

        practice.is_practiced = True
        practice.last_practiced_at = timezone.now()
        practice.save(
            update_fields=[
                "is_practiced",
                "last_practiced_at",
                "updated_at",
            ]
        )

        return Response(
            InterviewPracticeSerializer(
                practice,
                context={"request": request},
            ).data
        )


# ADMIN: LIST AND CREATE QUESTIONS

class AdminInterviewQuestionListCreateView(
    generics.ListCreateAPIView
):
    """Allow platform admins to list and create interview questions."""

    serializer_class = InterviewQuestionSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsPlatformAdmin,
    ]

    def get_queryset(self):
        queryset = InterviewQuestion.objects.all()

        category = self.request.query_params.get("category")
        difficulty = self.request.query_params.get("difficulty")
        search = self.request.query_params.get("search")
        active = self.request.query_params.get("is_active")

        if category:
            queryset = queryset.filter(category__iexact=category)

        if difficulty:
            queryset = queryset.filter(difficulty__iexact=difficulty)

        if search:
            queryset = queryset.filter(question__icontains=search)

        if active is not None:
            if active.lower() in ("true", "1", "yes"):
                queryset = queryset.filter(is_active=True)
            elif active.lower() in ("false", "0", "no"):
                queryset = queryset.filter(is_active=False)

        return queryset


# ADMIN: RETRIEVE, UPDATE AND DELETE QUESTIONS

class AdminInterviewQuestionDetailView(
    generics.RetrieveUpdateDestroyAPIView
):
    """Allow platform admins to retrieve, update or delete a question."""

    serializer_class = InterviewQuestionSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsPlatformAdmin,
    ]
    queryset = InterviewQuestion.objects.all()
