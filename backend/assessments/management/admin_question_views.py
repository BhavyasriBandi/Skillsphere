
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import AssessmentQuestion
from .serializers import AdminAssessmentQuestionSerializer


class AdminQuestionListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AdminAssessmentQuestionSerializer

    def get_queryset(self):
        queryset = AssessmentQuestion.objects.all().order_by("id")

        skill = self.request.query_params.get("skill", "").strip()
        if skill:
            queryset = queryset.filter(skill__iexact=skill)

        return queryset


class AdminQuestionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AdminAssessmentQuestionSerializer
    queryset = AssessmentQuestion.objects.all()
