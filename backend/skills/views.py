import logging
import random
from decimal import Decimal

from django.db import transaction
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (
    SkillCategory,
    Skill,
    StudentSkill,
    SkillAssessmentResult,
    AssessmentQuestion,
    AssessmentAttempt,
)

from .serializers import (
    SkillCategorySerializer,
    SkillSerializer,
    StudentSkillSerializer,
    SkillAssessmentSerializer,
    SkillProgressQuerySerializer,
    SkillAssessmentResultSerializer,
    AssessmentStartSerializer,
    AssessmentSubmitSerializer,
)


logger = logging.getLogger(__name__)

ASSESSMENT_QUESTION_COUNT = 10


# =========================================================
# SKILL CATEGORIES
# =========================================================

class SkillCategoriesAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        categories = SkillCategory.objects.all().order_by("name")
        serializer = SkillCategorySerializer(categories, many=True)

        return Response(
            {"categories": serializer.data},
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        if not request.user.is_authenticated or not request.user.is_staff:
            return Response(
                {"detail": "Only administrators can create categories."},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = SkillCategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Category created successfully.",
                    "category": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class SkillCategoryDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        category = get_object_or_404(SkillCategory, pk=pk)

        return Response(
            SkillCategorySerializer(category).data,
            status=status.HTTP_200_OK,
        )

    def put(self, request, pk):
        if not request.user.is_staff:
            return Response(
                {"detail": "Only administrators can update categories."},
                status=status.HTTP_403_FORBIDDEN,
            )

        category = get_object_or_404(SkillCategory, pk=pk)
        serializer = SkillCategorySerializer(category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Category updated successfully.",
                    "category": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def patch(self, request, pk):
        if not request.user.is_staff:
            return Response(
                {"detail": "Only administrators can update categories."},
                status=status.HTTP_403_FORBIDDEN,
            )

        category = get_object_or_404(SkillCategory, pk=pk)

        serializer = SkillCategorySerializer(
            category,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Category updated successfully.",
                    "category": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk):
        if not request.user.is_staff:
            return Response(
                {"detail": "Only administrators can delete categories."},
                status=status.HTTP_403_FORBIDDEN,
            )

        category = get_object_or_404(SkillCategory, pk=pk)

        try:
            category.delete()
        except ProtectedError:
            return Response(
                {
                    "detail": (
                        "This category cannot be deleted because skills "
                        "are associated with it. Move or remove those "
                        "skills first."
                    )
                },
                status=status.HTTP_409_CONFLICT,
            )

        return Response(
            {"message": "Category deleted successfully."},
            status=status.HTTP_200_OK,
        )


# =========================================================
# SKILLS
# =========================================================

class SkillsListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        skills = (
            Skill.objects.filter(is_active=True)
            .select_related("category")
            .order_by("name")
        )

        category_id = request.query_params.get("category")

        if category_id:
            if not category_id.isdigit():
                return Response(
                    {
                        "detail": (
                            "The category parameter must be an integer."
                        )
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            skills = skills.filter(category_id=int(category_id))

        serializer = SkillSerializer(skills, many=True)

        return Response(
            {"skills": serializer.data},
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        if not request.user.is_authenticated or not request.user.is_staff:
            return Response(
                {"detail": "Only administrators can create skills."},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = SkillSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Skill created successfully.",
                    "skill": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class SkillDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        skill = get_object_or_404(Skill, pk=pk)

        return Response(
            SkillSerializer(skill).data,
            status=status.HTTP_200_OK,
        )

    def put(self, request, pk):
        if not request.user.is_staff:
            return Response(
                {"detail": "Only administrators can update skills."},
                status=status.HTTP_403_FORBIDDEN,
            )

        skill = get_object_or_404(Skill, pk=pk)
        serializer = SkillSerializer(skill, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Skill updated successfully.",
                    "skill": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def patch(self, request, pk):
        if not request.user.is_staff:
            return Response(
                {"detail": "Only administrators can update skills."},
                status=status.HTTP_403_FORBIDDEN,
            )

        skill = get_object_or_404(Skill, pk=pk)

        serializer = SkillSerializer(
            skill,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Skill updated successfully.",
                    "skill": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk):
        if not request.user.is_staff:
            return Response(
                {"detail": "Only administrators can update skills."},
                status=status.HTTP_403_FORBIDDEN,
            )

        skill = get_object_or_404(Skill, pk=pk)
        skill.is_active = False
        skill.save(update_fields=["is_active"])

        return Response(
            {"message": "Skill deactivated successfully."},
            status=status.HTTP_200_OK,
        )


# =========================================================
# MY SKILLS
# =========================================================

class MySkillsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        student_skills = (
            StudentSkill.objects.filter(user=request.user)
            .select_related("skill", "skill__category")
        )

        serializer = StudentSkillSerializer(
            student_skills,
            many=True,
        )

        return Response(
            {"my_skills": serializer.data},
            status=status.HTTP_200_OK,
        )


# =========================================================
# START SKILL ASSESSMENT
# Uses pre-generated questions stored in the database.
# Ollama is NOT called when a student starts an assessment.
# =========================================================

class SkillAssessmentStartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AssessmentStartSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        skill_name = serializer.validated_data["skill_name"].strip()
        difficulty = serializer.validated_data["difficulty"]

        skill = Skill.objects.filter(
            name__iexact=skill_name,
            is_active=True,
        ).first()

        if skill is None:
            return Response(
                {"detail": "The requested skill was not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Find questions already shown to this student for this skill.
        used_question_ids = AssessmentAttempt.objects.filter(
            user=request.user,
            skill=skill,
        ).values_list("questions__id", flat=True)

        # Get active questions that the student has not seen before.
        available_questions = list(
            AssessmentQuestion.objects.filter(
                skill=skill,
                difficulty=difficulty,
                is_active=True,
            )
            .exclude(id__in=used_question_ids)
            .distinct()
        )

        # At least 10 questions must be available.
        if len(available_questions) < ASSESSMENT_QUESTION_COUNT:
            return Response(
                {
                    "detail": (
                        "Not enough unseen questions are available for this "
                        "skill and difficulty. Please try again after the "
                        "question bank has been updated."
                    ),
                    "available_questions": len(available_questions),
                    "required_questions": ASSESSMENT_QUESTION_COUNT,
                },
                status=status.HTTP_409_CONFLICT,
            )

        # Randomly select exactly 10 questions.
        selected_questions = random.sample(
            available_questions,
            ASSESSMENT_QUESTION_COUNT,
        )

        try:
            with transaction.atomic():
                attempt = AssessmentAttempt.objects.create(
                    user=request.user,
                    skill=skill,
                    total_questions=ASSESSMENT_QUESTION_COUNT,
                )

                attempt.questions.set(selected_questions)

                attempt.question_order = [
                    question.id for question in selected_questions
                ]

                attempt.save(update_fields=["question_order"])

        except Exception:
            logger.exception("Unable to create assessment attempt.")

            return Response(
                {
                    "detail": (
                        "Unable to start assessment. Please try again."
                    )
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        # Do not send correct answers or explanations to React yet.
        response_questions = [
            {
                "id": question.id,
                "question_text": question.question_text,
                "options": question.options,
            }
            for question in selected_questions
        ]

        return Response(
            {
                "message": "Assessment started successfully.",
                "attempt_id": attempt.id,
                "skill": skill.name,
                "difficulty": difficulty,
                "total_questions": ASSESSMENT_QUESTION_COUNT,
                "questions": response_questions,
            },
            status=status.HTTP_201_CREATED,
        )


# =========================================================
# SUBMIT SKILL ASSESSMENT
# =========================================================

class SkillAssessmentSubmitAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AssessmentSubmitSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        attempt_id = serializer.validated_data["attempt_id"]
        answers = serializer.validated_data["answers"]

        try:
            with transaction.atomic():
                attempt = (
                    AssessmentAttempt.objects
                    .select_for_update()
                    .filter(
                        pk=attempt_id,
                        user=request.user,
                    )
                    .first()
                )

                if attempt is None:
                    return Response(
                        {"detail": "Assessment attempt not found."},
                        status=status.HTTP_404_NOT_FOUND,
                    )

                if attempt.is_completed:
                    return Response(
                        {
                            "detail": (
                                "This assessment has already been submitted."
                            )
                        },
                        status=status.HTTP_409_CONFLICT,
                    )

                question_order = attempt.question_order

                if (
                    not isinstance(question_order, list)
                    or len(question_order) != ASSESSMENT_QUESTION_COUNT
                ):
                    return Response(
                        {
                            "detail": (
                                "The assessment question order is invalid."
                            )
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                if len(answers) != ASSESSMENT_QUESTION_COUNT:
                    return Response(
                        {"detail": "Exactly 10 answers are required."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                questions = AssessmentQuestion.objects.filter(
                    id__in=question_order,
                    skill=attempt.skill,
                )

                question_map = {
                    question.id: question
                    for question in questions
                }

                attempt_question_ids = set(
                    attempt.questions.values_list("id", flat=True)
                )

                if (
                    len(question_map) != ASSESSMENT_QUESTION_COUNT
                    or set(question_order) != attempt_question_ids
                ):
                    return Response(
                        {
                            "detail": (
                                "Assessment questions could not be verified."
                            )
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                ordered_questions = [
                    question_map[question_id]
                    for question_id in question_order
                ]

                # Calculate score on the server.
                score = sum(
                    1
                    for question, selected_answer in zip(
                        ordered_questions,
                        answers,
                    )
                    if question.correct_answer == selected_answer
                )

                percentage = (
                    Decimal(score)
                    * Decimal("100")
                    / Decimal(ASSESSMENT_QUESTION_COUNT)
                ).quantize(Decimal("0.01"))

                if percentage >= Decimal("80"):
                    level = "Advanced"
                    proficiency = "advanced"

                elif percentage >= Decimal("60"):
                    level = "Intermediate"
                    proficiency = "intermediate"

                else:
                    level = "Beginner"
                    proficiency = "beginner"

                submitted_data = []
                review_data = []

                for question, selected_answer in zip(
                    ordered_questions,
                    answers,
                ):
                    submitted_data.append(
                        {
                            "question_id": question.id,
                            "selected_answer": selected_answer,
                        }
                    )

                    review_data.append(
                        {
                            "question_id": question.id,
                            "question_text": question.question_text,
                            "options": question.options,
                            "selected_answer": selected_answer,
                            "correct_answer": question.correct_answer,
                            "is_correct": (
                                selected_answer == question.correct_answer
                            ),
                            "explanation": question.explanation,
                        }
                    )

                # Save assessment attempt.
                attempt.score = score
                attempt.total_questions = ASSESSMENT_QUESTION_COUNT
                attempt.percentage = percentage
                attempt.submitted_answers = submitted_data
                attempt.is_completed = True
                attempt.completed_at = timezone.now()

                attempt.save(
                    update_fields=[
                        "score",
                        "total_questions",
                        "percentage",
                        "submitted_answers",
                        "is_completed",
                        "completed_at",
                    ]
                )

                # Save assessment result.
                result = SkillAssessmentResult.objects.create(
                    user=request.user,
                    skill=attempt.skill,
                    score=score,
                    total_questions=ASSESSMENT_QUESTION_COUNT,
                    percentage=percentage,
                    answers=review_data,
                )

                # Update student proficiency.
                student_skill, created = StudentSkill.objects.get_or_create(
                    user=request.user,
                    skill=attempt.skill,
                    defaults={
                        "proficiency": proficiency,
                    },
                )

                if not created:
                    student_skill.proficiency = proficiency
                    student_skill.save(
                        update_fields=["proficiency"]
                    )

        except Exception:
            logger.exception("Assessment submission failed.")

            return Response(
                {
                    "detail": (
                        "Unable to submit assessment. Please try again."
                    )
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        result_data = SkillAssessmentResultSerializer(result).data

        return Response(
            {
                "message": "Assessment submitted successfully.",
                "result": result_data,
                "correct_answers": score,
                "total_questions": ASSESSMENT_QUESTION_COUNT,
                "percentage": float(percentage),
                "level": level,
                "review": review_data,
            },
            status=status.HTTP_200_OK,
        )


# =========================================================
# SKILL ASSESSMENT HISTORY
# =========================================================

class SkillAssessmentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        assessments = (
            SkillAssessmentResult.objects.filter(user=request.user)
            .select_related("skill")
            .order_by("-completed_at")
        )

        serializer = SkillAssessmentResultSerializer(
            assessments,
            many=True,
        )

        return Response(
            {
                "assessments": serializer.data,
                "count": assessments.count(),
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        return Response(
            {
                "detail": (
                    "Direct score submission is no longer supported. "
                    "Start an assessment using /assessments/start/ "
                    "and submit answers using /assessments/submit/."
                )
            },
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )


# =========================================================
# SKILL PROGRESS - SKILL GAP CHECKLIST
# =========================================================

class SkillProgressAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query_serializer = SkillProgressQuerySerializer(
            data=request.query_params,
        )

        if not query_serializer.is_valid():
            return Response(
                query_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        progress = (
            StudentSkill.objects.filter(user=request.user)
            .select_related("skill", "skill__category")
        )

        skill_name = query_serializer.validated_data.get("skill_name")

        if skill_name:
            progress = progress.filter(
                skill__name__iexact=skill_name.strip(),
            )

        serializer = StudentSkillSerializer(
            progress,
            many=True,
        )

        return Response(
            {
                "progress": serializer.data,
                "count": progress.count(),
            },
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        skill_name = request.data.get("skill_name")
        is_completed = request.data.get("is_completed")

        if not isinstance(skill_name, str) or not skill_name.strip():
            return Response(
                {"detail": "A valid skill_name is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not isinstance(is_completed, bool):
            return Response(
                {"detail": "is_completed must be true or false."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        skill_name = skill_name.strip()

        skill = Skill.objects.filter(
            name__iexact=skill_name,
            is_active=True,
        ).first()

        if skill is None:
            category, _ = SkillCategory.objects.get_or_create(
                name="Career Skills",
                defaults={
                    "description": (
                        "Skills used by career readiness checklists."
                    )
                },
            )

            skill, _ = Skill.objects.get_or_create(
                name=skill_name,
                defaults={
                    "category": category,
                    "description": "Career readiness checklist skill.",
                    "is_active": True,
                },
            )

            if not skill.is_active:
                return Response(
                    {"detail": "This skill is currently inactive."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        student_skill, created = StudentSkill.objects.get_or_create(
            user=request.user,
            skill=skill,
            defaults={
                "is_completed": is_completed,
            },
        )

        if not created:
            student_skill.is_completed = is_completed
            student_skill.save(
                update_fields=["is_completed", "updated_at"],
            )

        serializer = StudentSkillSerializer(student_skill)

        return Response(
            {
                "message": (
                    "Skill progress saved successfully."
                    if is_completed
                    else "Skill marked as not completed."
                ),
                "progress": serializer.data,
            },
            status=(
                status.HTTP_201_CREATED
                if created
                else status.HTTP_200_OK
            ),
        )