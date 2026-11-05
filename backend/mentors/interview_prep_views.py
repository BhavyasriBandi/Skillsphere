
from django.db.models import Q

from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsMentor
from mentors.models import MentorStudentAssignment
from interview_prep.models import InterviewPractice


class MentorInterviewPracticeSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    student_email = serializers.EmailField(
        source="student.email",
        read_only=True,
    )
    question_details = serializers.SerializerMethodField()

    class Meta:
        model = InterviewPractice
        fields = [
            "id",
            "student",
            "student_name",
            "student_email",
            "question_details",
            "student_answer",
            "is_practiced",
            "is_bookmarked",
            "last_practiced_at",
            "created_at",
            "updated_at",
        ]

    def get_student_name(self, obj):
        return obj.student.get_full_name() or obj.student.email

    def get_question_details(self, obj):
        question = obj.question

        return {
            "id": question.id,
            "question": question.question,
            "category": question.category,
            "difficulty": question.difficulty,
            "suggested_answer": question.suggested_answer,
            "explanation": question.explanation,
            "keywords": question.keywords,
        }


class MentorInterviewPrepAPIView(APIView):
    permission_classes = [IsAuthenticated, IsMentor]

    def get(self, request):
        assigned_student_ids = MentorStudentAssignment.objects.filter(
            mentor=request.user,
            status="Active",
        ).values_list("student_id", flat=True)

        queryset = InterviewPractice.objects.filter(
            student_id__in=assigned_student_ids
        ).select_related("student", "question")

        search = request.query_params.get("search", "").strip()
        category = request.query_params.get("category", "").strip()
        difficulty = request.query_params.get("difficulty", "").strip()
        practiced = request.query_params.get("practiced", "").strip()
        bookmarked = request.query_params.get("bookmarked", "").strip()

        if search:
            queryset = queryset.filter(
                Q(question__question__icontains=search)
                | Q(student_answer__icontains=search)
                | Q(student__email__icontains=search)
            )

        if category:
            queryset = queryset.filter(
                question__category__iexact=category
            )

        if difficulty:
            queryset = queryset.filter(
                question__difficulty__iexact=difficulty
            )

        if practiced.lower() in ("true", "1", "yes"):
            queryset = queryset.filter(is_practiced=True)
        elif practiced.lower() in ("false", "0", "no"):
            queryset = queryset.filter(is_practiced=False)

        if bookmarked.lower() in ("true", "1", "yes"):
            queryset = queryset.filter(is_bookmarked=True)
        elif bookmarked.lower() in ("false", "0", "no"):
            queryset = queryset.filter(is_bookmarked=False)

        queryset = queryset.order_by("-updated_at", "-id")

        total = queryset.count()
        practiced_count = queryset.filter(is_practiced=True).count()
        pending_count = queryset.filter(is_practiced=False).count()
        bookmarked_count = queryset.filter(is_bookmarked=True).count()

        serializer = MentorInterviewPracticeSerializer(
            queryset,
            many=True,
        )

        return Response(
            {
                "count": total,
                "statistics": {
                    "total_practices": total,
                    "practiced": practiced_count,
                    "pending": pending_count,
                    "bookmarked": bookmarked_count,
                },
                "practices": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
