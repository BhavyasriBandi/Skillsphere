
from collections import defaultdict
from decimal import Decimal

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from accounts.permissions import IsMentor
from mentors.models import MentorStudentAssignment
from skills.models import StudentSkill, SkillAssessmentResult


class MentorSkillAnalysisAPIView(APIView):
    permission_classes = [IsAuthenticated, IsMentor]

    def get(self, request):
        assignments = (
            MentorStudentAssignment.objects
            .filter(mentor=request.user, status="Active")
            .select_related("student")
            .order_by("-assigned_at")
        )

        students = []
        student_ids = list(
            assignments.values_list("student_id", flat=True).distinct()
        )

        proficiency_summary = {
            "beginner": 0,
            "intermediate": 0,
            "advanced": 0,
        }

        total_skills = 0
        completed_skills = 0
        skill_summary = defaultdict(
            lambda: {
                "student_count": 0,
                "beginner": 0,
                "intermediate": 0,
                "advanced": 0,
                "completed": 0,
                "incomplete": 0,
                "assessment_count": 0,
                "assessment_percentages": [],
            }
        )

        for assignment in assignments:
            student = assignment.student

            student_skills = (
                StudentSkill.objects
                .filter(user=student)
                .select_related("skill", "skill__category")
                .order_by("skill__name")
            )

            skill_assessments = (
                SkillAssessmentResult.objects
                .filter(user=student)
                .select_related("skill")
                .order_by("-completed_at")
            )

            assessments_by_skill = defaultdict(list)

            for result in skill_assessments:
                assessments_by_skill[result.skill_id].append({
                    "id": result.id,
                    "score": result.score,
                    "total_questions": result.total_questions,
                    "percentage": str(result.percentage),
                    "completed_at": result.completed_at,
                })

            student_skill_data = []

            for item in student_skills:
                proficiency = item.proficiency.lower()
                is_completed = item.is_completed

                total_skills += 1

                if proficiency in proficiency_summary:
                    proficiency_summary[proficiency] += 1

                if is_completed:
                    completed_skills += 1

                summary = skill_summary[item.skill.name]
                summary["student_count"] += 1

                if proficiency in summary:
                    summary[proficiency] += 1

                if is_completed:
                    summary["completed"] += 1
                else:
                    summary["incomplete"] += 1

                results = assessments_by_skill.get(item.skill_id, [])

                summary["assessment_count"] += len(results)
                summary["assessment_percentages"].extend(
                    [Decimal(result["percentage"]) for result in results]
                )

                student_skill_data.append({
                    "id": item.id,
                    "skill_id": item.skill_id,
                    "skill_name": item.skill.name,
                    "category": item.skill.category.name,
                    "proficiency": item.proficiency,
                    "is_completed": is_completed,
                    "assessment_count": len(results),
                    "assessment_results": results,
                    "updated_at": item.updated_at,
                })

            students.append({
                "student": {
                    "id": student.id,
                    "name": (
                        student.get_full_name() or student.username
                    ),
                    "email": student.email,
                },
                "total_skills": len(student_skill_data),
                "completed_skills": sum(
                    1 for item in student_skill_data
                    if item["is_completed"]
                ),
                "incomplete_skills": sum(
                    1 for item in student_skill_data
                    if not item["is_completed"]
                ),
                "skills": student_skill_data,
            })

        skill_breakdown = []

        for skill_name, values in sorted(skill_summary.items()):
            percentages = values["assessment_percentages"]

            average_percentage = (
                sum(percentages) / len(percentages)
                if percentages else None
            )

            skill_breakdown.append({
                "skill_name": skill_name,
                "student_count": values["student_count"],
                "beginner": values["beginner"],
                "intermediate": values["intermediate"],
                "advanced": values["advanced"],
                "completed": values["completed"],
                "incomplete": values["incomplete"],
                "assessment_count": values["assessment_count"],
                "average_assessment_percentage": (
                    str(round(average_percentage, 2))
                    if average_percentage is not None else None
                ),
            })

        return Response(
            {
                "student_count": len(student_ids),
                "summary": {
                    "total_skills": total_skills,
                    "completed_skills": completed_skills,
                    "incomplete_skills": (
                        total_skills - completed_skills
                    ),
                    "proficiency": proficiency_summary,
                },
                "skill_breakdown": skill_breakdown,
                "students": students,
            },
            status=status.HTTP_200_OK,
        )
