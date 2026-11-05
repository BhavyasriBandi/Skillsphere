
import random

from django.core.cache import cache

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import AssessmentResult
from .serializers import (
    AssessmentSubmitSerializer,
    SkillGapSerializer,
)
from .assessment_question_bank import RAW_QUESTIONS


# ============================================================
# CONFIGURATION
# ============================================================

QUESTIONS_PER_ATTEMPT = 10
ASSESSMENT_CACHE_TIMEOUT = 2 * 60 * 60  # Two hours


# ============================================================
# SHARED ASSESSMENT QUESTION BANK
# All 50 questions per skill are loaded from the question bank.
# Correct answers and explanations are kept on the backend.
# ============================================================

ASSESSMENT_QUESTIONS = {
    skill.casefold(): [
        {
            "id": str(question_id),
            "skill": "C" if skill.casefold() == "c" else skill.title(),
            "question": question,
            "options": options,
            "correct_answer": answer_index,
            "explanation": explanation,
        }
        for question_id, question, options, answer_index, explanation
        in rows
    ]
    for skill, rows in RAW_QUESTIONS.items()
}


def get_assessment_cache_key(user_id, skill):
    """Return the cache key for a user's current assessment skill."""
    return f"skillsphere_assessment_{user_id}_{skill}"


def normalize_skill(value):
    """Normalize supported skill names consistently."""
    skill = str(value).strip().casefold()

    if skill in ASSESSMENT_QUESTIONS:
        return skill

    return None


# ============================================================
# CAREER REQUIREMENTS
# Existing skill-gap functionality preserved.
# ============================================================

CAREER_REQUIREMENTS = {
    1: {
        "title": "Python Developer",
        "required_skills": [
            "Python",
            "Django",
            "REST API",
            "SQL",
            "Git",
        ],
    },
    2: {
        "title": "Full-Stack Developer",
        "required_skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Python",
            "Django",
            "SQL",
        ],
    },
    3: {
        "title": "Data Analyst",
        "required_skills": [
            "Python",
            "SQL",
            "Excel",
            "Statistics",
            "Data Visualization",
        ],
    },
    4: {
        "title": "Java Developer",
        "required_skills": [
            "Java",
            "OOP",
            "Data Structures",
            "SQL",
            "Git",
        ],
    },
    5: {
        "title": "AI and Machine Learning Engineer",
        "required_skills": [
            "Python",
            "Statistics",
            "Linear Algebra",
            "Machine Learning",
            "Data Structures",
        ],
    },
}


# ============================================================
# GET ASSESSMENT QUESTIONS
# GET /api/.../?skill=Python
#
# Returns 10 randomly selected questions.
# Correct answers and explanations are never exposed.
# The issued question IDs are cached for answer validation.
# ============================================================

class AssessmentQuestionsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="get_assessment_questions",
        summary="Get 10 Random Assessment Questions",
        parameters=[
            OpenApiParameter(
                name="skill",
                type=str,
                location=OpenApiParameter.QUERY,
                required=True,
                description="Supported skills: Python, Java, C and SQL.",
            ),
        ],
        responses={200: dict},
    )
    def get(self, request):
        requested_skill = request.query_params.get("skill", "")
        skill = normalize_skill(requested_skill)

        if not requested_skill.strip():
            return Response(
                {
                    "detail": (
                        "Provide a skill query parameter, "
                        "for example ?skill=Python."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if skill is None:
            return Response(
                {
                    "detail": (
                        "Unsupported skill. Choose Python, Java, C or SQL."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        all_questions = ASSESSMENT_QUESTIONS[skill]

        if len(all_questions) < QUESTIONS_PER_ATTEMPT:
            return Response(
                {
                    "detail": (
                        f"At least {QUESTIONS_PER_ATTEMPT} questions "
                        "are required for this assessment."
                    )
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        # Randomly select 10 different questions from the bank of 50.
        selected_questions = random.sample(
            all_questions,
            QUESTIONS_PER_ATTEMPT,
        )

        # Remember which IDs were issued so answers for unrelated
        # question IDs cannot be submitted for this user and skill.
        cache_key = get_assessment_cache_key(request.user.pk, skill)

        cache.set(
            cache_key,
            [question["id"] for question in selected_questions],
            timeout=ASSESSMENT_CACHE_TIMEOUT,
        )

        # Do not expose correct_answer or explanation to React.
        public_questions = [
            {
                "id": question["id"],
                "skill": question["skill"],
                "question": question["question"],
                "options": question["options"],
            }
            for question in selected_questions
        ]

        return Response(
            public_questions,
            status=status.HTTP_200_OK,
        )


# ============================================================
# SUBMIT ASSESSMENT
# Scores submitted answers and saves the result.
# ============================================================

class AssessmentSubmitAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="submit_assessment",
        summary="Submit Assessment and Save Result",
        request=AssessmentSubmitSerializer,
    )
    def post(self, request):
        serializer = AssessmentSubmitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        requested_skill = serializer.validated_data["skill"]
        skill = normalize_skill(requested_skill)

        if skill is None:
            return Response(
                {
                    "detail": (
                        "Unsupported skill. Choose Python, Java, C or SQL."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        answers = serializer.validated_data["answers"]

        if not answers:
            return Response(
                {"detail": "Submit at least one answer."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Retrieve the question IDs that were issued to this user.
        cache_key = get_assessment_cache_key(request.user.pk, skill)
        issued_ids = cache.get(cache_key)

        if not issued_ids:
            return Response(
                {
                    "detail": (
                        "Your assessment has expired or was not started. "
                        "Fetch a new set of questions and try again."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        question_map = {
            question["id"]: question
            for question in ASSESSMENT_QUESTIONS[skill]
        }

        normalized_answers = {
            str(question_id): answer
            for question_id, answer in answers.items()
        }

        submitted_ids = set(normalized_answers.keys())
        allowed_ids = set(issued_ids)

        # Reject question IDs that were not issued for this attempt.
        invalid_ids = submitted_ids - allowed_ids

        if invalid_ids:
            return Response(
                {
                    "detail": (
                        "One or more submitted question IDs were not "
                        "included in your current assessment."
                    ),
                    "invalid_question_ids": sorted(invalid_ids),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Validate answer indexes before calculating the score.
        for question_id, answer in normalized_answers.items():
            options = question_map[question_id]["options"]

            if (
                not isinstance(answer, int)
                or isinstance(answer, bool)
                or answer < 0
                or answer >= len(options)
            ):
                return Response(
                    {
                        "detail": (
                            f"Invalid answer option for question "
                            f"{question_id}."
                        )
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        # Score only the answers submitted for this assessment.
        correct_count = sum(
            normalized_answers[question_id]
            == question_map[question_id]["correct_answer"]
            for question_id in normalized_answers
        )

        total = len(normalized_answers)
        percentage = round((correct_count / total) * 100, 2)

        if percentage >= 80:
            level = "Advanced"
        elif percentage >= 50:
            level = "Intermediate"
        else:
            level = "Beginner"

        # Preserve the existing AssessmentResult model fields.
        result = AssessmentResult.objects.create(
            user=request.user,
            skill=question_map[next(iter(normalized_answers))]["skill"],
            total_questions=total,
            correct_answers=correct_count,
            score_percentage=percentage,
            estimated_level=level,
        )

        return Response(
            {
                "id": result.pk,
                "user_id": request.user.pk,
                "skill": result.skill,
                "total_questions": result.total_questions,
                "correct_answers": result.correct_answers,
                "score_percentage": float(result.score_percentage),
                "estimated_level": result.estimated_level,
                "created_at": result.created_at,
                "message": "Assessment evaluated and saved successfully.",
            },
            status=status.HTTP_200_OK,
        )


# ============================================================
# ASSESSMENT HISTORY
# Existing functionality preserved.
# ============================================================

class AssessmentHistoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="get_assessment_history",
        summary="Get My Assessment History",
        responses={200: dict},
    )
    def get(self, request):
        results = AssessmentResult.objects.filter(
            user=request.user
        ).order_by("-created_at")

        history = [
            {
                "id": result.pk,
                "skill": result.skill,
                "total_questions": result.total_questions,
                "correct_answers": result.correct_answers,
                "score_percentage": float(result.score_percentage),
                "estimated_level": result.estimated_level,
                "created_at": result.created_at,
            }
            for result in results
        ]

        return Response(
            {
                "count": len(history),
                "results": history,
            },
            status=status.HTTP_200_OK,
        )


# ============================================================
# SKILL GAP ANALYSIS
# Existing functionality preserved.
# ============================================================

class SkillGapAnalysisAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="analyze_career_skill_gap",
        summary="Analyze Career Skill Gap",
        request=SkillGapSerializer,
    )
    def post(self, request):
        serializer = SkillGapSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        career_id = serializer.validated_data["career_id"]
        current_skills = serializer.validated_data["current_skills"]

        career = CAREER_REQUIREMENTS.get(career_id)

        if career is None:
            return Response(
                {"detail": "Career path not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        current_normalized = {
            skill.strip().casefold()
            for skill in current_skills
        }

        matched = [
            skill
            for skill in career["required_skills"]
            if skill.casefold() in current_normalized
        ]

        missing = [
            skill
            for skill in career["required_skills"]
            if skill.casefold() not in current_normalized
        ]

        total = len(career["required_skills"])
        coverage = round((len(matched) / total) * 100, 2)

        return Response(
            {
                "user_id": request.user.pk,
                "career_id": career_id,
                "career_title": career["title"],
                "matched_skills": matched,
                "missing_skills": missing,
                "skill_coverage_percentage": coverage,
                "message": (
                    "Skill gap analysis completed. "
                    "This analysis is not saved."
                ),
            },
            status=status.HTTP_200_OK,
        )
