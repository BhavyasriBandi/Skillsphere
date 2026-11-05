
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser

from .models import AssessmentQuestion
from .serializers import AdminAssessmentQuestionSerializer


SKILL_QUESTION_NAME_MAP = {
    "c programming": "C",
    "java": "Java",
    "python": "Python",
    "sql & databases": "Sql",
}


class AdminQuestionPagination(PageNumberPagination):
    page_size = 500
    page_size_query_param = "page_size"
    max_page_size = 1000


class AdminQuestionListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AdminAssessmentQuestionSerializer
    pagination_class = AdminQuestionPagination

    def get_queryset(self):
        queryset = AssessmentQuestion.objects.all().order_by("id")

        skill = self.request.query_params.get("skill", "").strip()

        if skill and skill.casefold() != "all skills":
            normalized_skill = skill.casefold()
            question_skill = SKILL_QUESTION_NAME_MAP.get(
                normalized_skill,
                skill
            )
            queryset = queryset.filter(skill__iexact=question_skill)

        return queryset


class AdminQuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AdminAssessmentQuestionSerializer
    queryset = AssessmentQuestion.objects.all()
