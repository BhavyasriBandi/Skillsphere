from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import JobOpportunitySerializer


# Sample data only. These are not verified live vacancies.
JOBS = [
    {
        "id": 1,
        "title": "Junior Python Developer",
        "company": "Sample Technology Company",
        "career_path": "Python Developer",
        "required_skills": [
            "Python",
            "Django",
            "SQL",
            "Git",
        ],
        "experience_level": "Fresher",
        "work_mode": "Hybrid",
        "location": "Hyderabad",
        "apply_url": "",
    },
    {
        "id": 2,
        "title": "Junior Data Analyst",
        "company": "Sample Analytics Company",
        "career_path": "Data Analyst",
        "required_skills": [
            "SQL",
            "Python",
            "Excel",
            "Statistics",
        ],
        "experience_level": "Fresher",
        "work_mode": "On-site",
        "location": "Bengaluru",
        "apply_url": "",
    },
    {
        "id": 3,
        "title": "Frontend Developer Intern",
        "company": "Sample Software Company",
        "career_path": "Frontend Developer",
        "required_skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
        ],
        "experience_level": "Fresher",
        "work_mode": "Remote",
        "location": "India",
        "apply_url": "",
    },
]


class JobOpportunityListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        jobs = JOBS.copy()

        career_path = request.query_params.get("career_path")
        experience = request.query_params.get("experience_level")
        work_mode = request.query_params.get("work_mode")
        search = request.query_params.get("search")

        if career_path:
            jobs = [
                job for job in jobs
                if career_path.lower() in job["career_path"].lower()
            ]

        if experience:
            jobs = [
                job for job in jobs
                if job["experience_level"].lower()
                == experience.lower()
            ]

        if work_mode:
            jobs = [
                job for job in jobs
                if job["work_mode"].lower() == work_mode.lower()
            ]

        if search:
            keyword = search.lower()
            jobs = [
                job for job in jobs
                if keyword in job["title"].lower()
                or keyword in job["company"].lower()
                or any(
                    keyword in skill.lower()
                    for skill in job["required_skills"]
                )
            ]

        serializer = JobOpportunitySerializer(jobs, many=True)

        return Response({
            "count": len(jobs),
            "results": serializer.data,
            "notice": (
                "Sample listings only. Verify vacancies and application "
                "links with employers before applying."
            ),
        })


class JobOpportunityDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, job_id):
        job = next(
            (item for item in JOBS if item["id"] == job_id),
            None,
        )

        if job is None:
            return Response(
                {"error": "Job opportunity not found."},
                status=404,
            )

        return Response(JobOpportunitySerializer(job).data)