from django.shortcuts import render

# Create your views here.
from datetime import date, timedelta

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import StudyStreakSerializer


# Temporary in-memory storage; data disappears on server restart.
STUDY_DAYS = {}


class StudyStreakView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.user.id
        today = date.today()

        # Store unique study dates for each authenticated user.
        dates = STUDY_DAYS.get(user_id, set())

        if not dates:
            data = {
                "current_streak": 0,
                "longest_streak": 0,
                "total_study_days": 0,
                "last_activity_date": None,
            }
            return Response(StudyStreakSerializer(data).data)

        sorted_dates = sorted(dates)
        longest_streak = 1
        running_streak = 1

        for index in range(1, len(sorted_dates)):
            if sorted_dates[index] == (
                sorted_dates[index - 1] + timedelta(days=1)
            ):
                running_streak += 1
            else:
                running_streak = 1

            longest_streak = max(
                longest_streak,
                running_streak,
            )

        last_date = max(dates)

        # A streak remains active if the last study day was
        # today or yesterday.
        current_streak = 0

        if last_date >= today - timedelta(days=1):
            current_streak = 1
            check_date = last_date - timedelta(days=1)

            while check_date in dates:
                current_streak += 1
                check_date -= timedelta(days=1)

        data = {
            "current_streak": current_streak,
            "longest_streak": longest_streak,
            "total_study_days": len(dates),
            "last_activity_date": last_date,
        }

        return Response(StudyStreakSerializer(data).data)


class RecordStudyDayView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.user.id
        today = date.today()

        if user_id not in STUDY_DAYS:
            STUDY_DAYS[user_id] = set()

        STUDY_DAYS[user_id].add(today)

        return Response({
            "message": "Today's study activity recorded.",
            "study_date": today,
        })