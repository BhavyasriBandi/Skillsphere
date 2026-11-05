
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema

from accounts.permissions import IsMentor

from .models import MentorStudentAssignment, MentorProfile

from assessments.models import AssessmentResult
from skills.models import StudentSkill, SkillAssessmentResult
from progress.models import LearningHubProgress, ChallengeProgress

from .serializers import (
    MentorSerializer,
    MentorshipRequestSerializer,
    MentorFeedbackSerializer,
    MentorStudentAssignmentSerializer,
    MentorAssignmentDecisionSerializer,
    MentorProfileSerializer,
)

User = get_user_model()


DEFAULT_EXPERTISE = [
    "Career Guidance",
    "Skill Development",
    "Interview Preparation",
]


# =====================================================
# HELPER FUNCTIONS
# =====================================================

def get_mentor_users():
    """Return active users assigned to the Mentor group."""

    try:
        mentor_group = Group.objects.get(name__iexact="Mentor")
    except Group.DoesNotExist:
        return User.objects.none()

    return (
        User.objects.filter(
            groups=mentor_group,
            is_active=True,
        )
        .distinct()
        .order_by("username")
    )


def serialize_mentor(user):
    full_name = user.get_full_name().strip()

    return {
        "id": user.pk,
        "username": user.username,
        "full_name": full_name or user.username,
        "email": user.email or "",
        "expertise": DEFAULT_EXPERTISE,
    }


# =====================================================
# 1. LIST MENTORS
# =====================================================

class MentorListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="list_mentors",
        summary="List Available Mentors",
        responses={200: MentorSerializer(many=True)},
    )
    def get(self, request):

        mentors = [
            serialize_mentor(user)
            for user in get_mentor_users()
        ]

        return Response(
            {
                "count": len(mentors),
                "mentors": mentors,
                "message": (
                    "Mentors are listed using Django users "
                    "assigned to the Mentor group."
                ),
            },
            status=status.HTTP_200_OK,
        )


# =====================================================
# 2. MENTOR DETAILS
# =====================================================

class MentorDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="get_mentor_details",
        summary="Get Mentor Details",
        responses={200: MentorSerializer},
    )
    def get(self, request, mentor_id):

        mentor = get_mentor_users().filter(
            pk=mentor_id
        ).first()

        if mentor is None:
            return Response(
                {"detail": "Mentor not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            serialize_mentor(mentor),
            status=status.HTTP_200_OK,
        )


# =====================================================
# 3. STUDENT SUBMITS MENTORSHIP REQUEST
# =====================================================

class MentorshipRequestAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="create_mentorship_request",
        summary="Submit Mentorship Request",
        request=MentorshipRequestSerializer,
    )
    def post(self, request):

        # Only students can submit requests.
        if not request.user.groups.filter(
            name__iexact="Student"
        ).exists():

            return Response(
                {
                    "detail": (
                        "Only students can request mentorship."
                    )
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = MentorshipRequestSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        mentor_id = serializer.validated_data["mentor_id"]

        mentor = get_mentor_users().filter(
            pk=mentor_id
        ).first()

        if mentor is None:
            return Response(
                {"detail": "Mentor not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        assignment, created = (
            MentorStudentAssignment.objects.get_or_create(
                mentor=mentor,
                student=request.user,
                defaults={
                    "status": "Pending",
                    "source": "Student Request",
                },
            )
        )

        if not created:

            if assignment.status == "Active":
                return Response(
                    {
                        "detail": (
                            "You already have an active "
                            "assignment with this mentor."
                        )
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if assignment.status == "Pending":
                return Response(
                    {
                        "detail": (
                            "Your mentorship request "
                            "is already pending."
                        )
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Allow a student to request again
            # after a previous rejection.
            assignment.status = "Pending"
            assignment.source = "Student Request"

            assignment.save(
                update_fields=[
                    "status",
                    "source",
                    "updated_at",
                ]
            )

        return Response(
            {
                "message": (
                    "Mentorship request submitted successfully."
                ),
                "request": MentorStudentAssignmentSerializer(
                    assignment
                ).data,
            },
            status=status.HTTP_201_CREATED,
        )


# =====================================================
# 4. STUDENT VIEW REQUEST HISTORY
# =====================================================

class MyMentorshipRequestsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="list_my_mentorship_requests",
        summary="List My Mentorship Requests",
    )
    def get(self, request):

        requests = (
            MentorStudentAssignment.objects.filter(
                student=request.user
            )
            .select_related("mentor", "student")
        )

        serializer = MentorStudentAssignmentSerializer(
            requests,
            many=True,
        )

        return Response(
            {
                "student_id": request.user.pk,
                "count": requests.count(),
                "requests": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


# =====================================================
# 5. SUBMIT MENTOR FEEDBACK
# =====================================================

class MentorFeedbackAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="submit_mentor_feedback",
        summary="Submit Mentor Feedback",
        request=MentorFeedbackSerializer,
    )
    def post(self, request):

        serializer = MentorFeedbackSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        mentor_id = serializer.validated_data["mentor_id"]

        mentor = get_mentor_users().filter(
            pk=mentor_id
        ).first()

        if mentor is None:
            return Response(
                {"detail": "Mentor not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Existing feedback behavior is preserved.
        # Persistent feedback storage will be implemented separately.

        return Response(
            {
                "feedback_id": None,
                "student_id": request.user.pk,
                "mentor_id": mentor.pk,
                "rating": serializer.validated_data["rating"],
                "feedback": serializer.validated_data["feedback"],
                "notice": (
                    "Feedback was accepted for this request only. "
                    "It is not saved to a database."
                ),
            },
            status=status.HTTP_201_CREATED,
        )


# =====================================================
# 6. MENTOR MANAGES ASSIGNED STUDENTS AND REQUESTS
# =====================================================

class MentorAssignmentManagementAPIView(APIView):
    permission_classes = [
        IsAuthenticated,
        IsMentor,
    ]

    @extend_schema(
        operation_id="mentor_list_assignments",
        summary="List Mentor Students and Requests",
        responses={
            200: MentorStudentAssignmentSerializer(many=True)
        },
    )
    def get(self, request):

        assignments = (
            MentorStudentAssignment.objects.filter(
                mentor=request.user
            )
            .select_related("student", "mentor")
        )

        serializer = MentorStudentAssignmentSerializer(
            assignments,
            many=True,
        )

        return Response(
            {
                "count": assignments.count(),
                "assignments": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        operation_id="mentor_decide_assignment",
        summary="Accept or Reject Mentorship Request",
        request=MentorAssignmentDecisionSerializer,
        responses={
            200: MentorStudentAssignmentSerializer,
        },
    )
    def patch(self, request, assignment_id):

        serializer = MentorAssignmentDecisionSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        assignment = (
            MentorStudentAssignment.objects.filter(
                id=assignment_id,
                mentor=request.user,
                status="Pending",
            )
            .select_related("student", "mentor")
            .first()
        )

        if assignment is None:
            return Response(
                {
                    "detail": (
                        "Pending mentorship request not found."
                    )
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        assignment.status = serializer.validated_data["status"]

        assignment.save(
            update_fields=[
                "status",
                "updated_at",
            ]
        )

        return Response(
            {
                "message": (
                    "Mentorship request updated successfully."
                ),
                "assignment": MentorStudentAssignmentSerializer(
                    assignment
                ).data,
            },
            status=status.HTTP_200_OK,
        )

# =====================================================
# 7. MENTOR PROFILE API
# =====================================================

class MentorProfileAPIView(APIView):
    permission_classes = [
        IsAuthenticated,
        IsMentor,
    ]

    @extend_schema(
        operation_id="get_mentor_profile",
        summary="Get My Mentor Profile",
        responses={200: MentorProfileSerializer},
    )
    def get(self, request):
        profile, created = MentorProfile.objects.get_or_create(
            mentor=request.user
        )

        serializer = MentorProfileSerializer(profile)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        operation_id="update_mentor_profile",
        summary="Update My Mentor Profile",
        request=MentorProfileSerializer,
        responses={200: MentorProfileSerializer},
    )
    def patch(self, request):
        profile, created = MentorProfile.objects.get_or_create(
            mentor=request.user
        )

        serializer = MentorProfileSerializer(
            profile,
            data=request.data,
            partial=True,
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Mentor profile updated successfully.",
                "profile": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


# =========================================================
# MENTOR STUDENT PROGRESS API
# =========================================================

class MentorStudentProgressAPIView(APIView):

    permission_classes = [IsAuthenticated, IsMentor]

    def get(self, request):

        assignments = (
            MentorStudentAssignment.objects
            .filter(
                mentor=request.user,
                status="Active"
            )
            .select_related("student")
            .order_by("-assigned_at")
        )

        students_data = []

        for assignment in assignments:

            student = assignment.student

            # ---------------------------------------------
            # STUDENT SKILLS
            # ---------------------------------------------

            student_skills = (
                StudentSkill.objects
                .filter(user=student)
                .select_related("skill", "skill__category")
            )

            skills_data = []

            for item in student_skills:
                skills_data.append({
                    "id": item.id,
                    "skill_name": item.skill.name,
                    "category": item.skill.category.name,
                    "proficiency": item.proficiency,
                    "is_completed": item.is_completed,
                    "created_at": item.created_at,
                    "updated_at": item.updated_at,
                })

            total_skills = student_skills.count()

            completed_skills = student_skills.filter(
                is_completed=True
            ).count()

            # ---------------------------------------------
            # OVERALL ASSESSMENT RESULTS
            # ---------------------------------------------

            assessment_results = (
                AssessmentResult.objects
                .filter(user=student)
                .order_by("-created_at")
            )

            assessments_data = []

            for item in assessment_results:
                assessments_data.append({
                    "id": item.id,
                    "skill": item.skill,
                    "total_questions": item.total_questions,
                    "correct_answers": item.correct_answers,
                    "score_percentage": str(item.score_percentage),
                    "estimated_level": item.estimated_level,
                    "created_at": item.created_at,
                })

            # ---------------------------------------------
            # SKILL ASSESSMENT RESULTS
            # ---------------------------------------------

            skill_assessment_results = (
                SkillAssessmentResult.objects
                .filter(user=student)
                .select_related("skill")
                .order_by("-completed_at")
            )

            skill_assessments_data = []

            for item in skill_assessment_results:
                skill_assessments_data.append({
                    "id": item.id,
                    "skill": item.skill.name,
                    "score": item.score,
                    "total_questions": item.total_questions,
                    "percentage": str(item.percentage),
                    "completed_at": item.completed_at,
                })

            # ---------------------------------------------
            # LEARNING HUB PROGRESS
            # ---------------------------------------------

            learning_progress = (
                LearningHubProgress.objects
                .filter(user=student)
                .first()
            )

            completed_lessons = (
                learning_progress.completed_lessons
                if learning_progress else []
            )

            saved_courses = (
                learning_progress.saved_courses
                if learning_progress else []
            )

            # ---------------------------------------------
            # CHALLENGE PROGRESS
            # ---------------------------------------------

            challenge_progress = (
                ChallengeProgress.objects
                .filter(user=student)
                .first()
            )

            completed_challenges = (
                challenge_progress.completed_ids
                if challenge_progress else []
            )

            # ---------------------------------------------
            # FINAL STUDENT RESPONSE
            # ---------------------------------------------

            students_data.append({

                "student": {
                    "id": student.id,
                    "name": (
                        student.get_full_name()
                        or student.username
                    ),
                    "email": student.email,
                },

                "assignment": {
                    "id": assignment.id,
                    "status": assignment.status,
                    "assigned_at": assignment.assigned_at,
                },

                "skill_progress": {
                    "total_skills": total_skills,
                    "completed_skills": completed_skills,
                    "incomplete_skills": (
                        total_skills - completed_skills
                    ),
                    "skills": skills_data,
                },

                "assessments": {
                    "total_assessments": len(assessments_data),
                    "results": assessments_data,
                },

                "skill_assessments": {
                    "total_assessments": len(
                        skill_assessments_data
                    ),
                    "results": skill_assessments_data,
                },

                "learning_hub": {
                    "completed_lessons": completed_lessons,
                    "completed_lessons_count": len(
                        completed_lessons
                    ),
                    "saved_courses": saved_courses,
                    "saved_courses_count": len(
                        saved_courses
                    ),
                },

                "challenges": {
                    "completed_ids": completed_challenges,
                    "completed_count": len(
                        completed_challenges
                    ),
                },

            })

        return Response(
            {
                "count": len(students_data),
                "students": students_data,
            },
            status=status.HTTP_200_OK
        )
