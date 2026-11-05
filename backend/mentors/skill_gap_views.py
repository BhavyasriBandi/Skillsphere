
from collections import defaultdict

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from accounts.permissions import IsMentor
from mentors.models import MentorStudentAssignment
from skills.models import StudentSkill


class MentorSkillGapsAPIView(APIView):
    permission_classes = [IsAuthenticated, IsMentor]

    def get(self, request):
        assignments = (
            MentorStudentAssignment.objects
            .filter(
                mentor=request.user,
                status="Active",
            )
            .select_related("student")
            .order_by("-assigned_at")
        )

        students_data = []
        total_students = 0
        total_skills = 0
        completed_skills = 0
        incomplete_skills = 0

        proficiency_summary = {
            "beginner": 0,
            "intermediate": 0,
            "advanced": 0,
        }

        skill_summary = defaultdict(
            lambda: {
                "student_count": 0,
                "beginner": 0,
                "intermediate": 0,
                "advanced": 0,
                "completed": 0,
                "incomplete": 0,
            }
        )

        for assignment in assignments:
            student = assignment.student
            total_students += 1

            student_skills = (
                StudentSkill.objects
                .filter(user=student)
                .select_related("skill", "skill__category")
                .order_by("skill__name")
            )

            skills_data = []
            student_completed = 0
            student_incomplete = 0

            for item in student_skills:
                proficiency = item.proficiency.lower()
                is_completed = item.is_completed

                total_skills += 1

                if proficiency in proficiency_summary:
                    proficiency_summary[proficiency] += 1

                skill_data = skill_summary[item.skill.name]
                skill_data["student_count"] += 1

                if proficiency in skill_data:
                    skill_data[proficiency] += 1

                if is_completed:
                    completed_skills += 1
                    student_completed += 1
                    skill_data["completed"] += 1
                else:
                    incomplete_skills += 1
                    student_incomplete += 1
                    skill_data["incomplete"] += 1

                skills_data.append({
                    "id": item.id,
                    "skill_id": item.skill_id,
                    "skill_name": item.skill.name,
                    "category": item.skill.category.name,
                    "proficiency": item.proficiency,
                    "is_completed": is_completed,
                    "gap_status": (
                        "Completed" if is_completed else "Needs Improvement"
                    ),
                    "updated_at": item.updated_at,
                })

            student_total = len(skills_data)

            completion_percentage = (
                round((student_completed / student_total) * 100, 2)
                if student_total else 0
            )

            gap_percentage = (
                round((student_incomplete / student_total) * 100, 2)
                if student_total else 0
            )

            students_data.append({
                "student": {
                    "id": student.id,
                    "name": (
                        student.get_full_name() or student.username
                    ),
                    "email": student.email,
                },
                "assignment_id": assignment.id,
                "total_skills": student_total,
                "completed_skills": student_completed,
                "incomplete_skills": student_incomplete,
                "completion_percentage": completion_percentage,
                "skill_gap_percentage": gap_percentage,
                "skills": skills_data,
            })

        skill_breakdown = []

        for skill_name, values in sorted(skill_summary.items()):
            skill_total = values["student_count"]

            gap_percentage = (
                round(
                    (values["incomplete"] / skill_total) * 100,
                    2,
                )
                if skill_total else 0
            )

            skill_breakdown.append({
                "skill_name": skill_name,
                "student_count": skill_total,
                "beginner": values["beginner"],
                "intermediate": values["intermediate"],
                "advanced": values["advanced"],
                "completed": values["completed"],
                "incomplete": values["incomplete"],
                "gap_percentage": gap_percentage,
            })

        return Response(
            {
                "student_count": total_students,
                "summary": {
                    "total_skills": total_skills,
                    "completed_skills": completed_skills,
                    "incomplete_skills": incomplete_skills,
                    "overall_gap_percentage": (
                        round(
                            (incomplete_skills / total_skills) * 100,
                            2,
                        )
                        if total_skills else 0
                    ),
                    "proficiency": proficiency_summary,
                },
                "skill_breakdown": skill_breakdown,
                "students": students_data,
            },
            status=status.HTTP_200_OK,
        )
