from django.shortcuts import render

# Create your views here.

from datetime import date

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema

from .serializers import StudySessionSerializer


# Temporary storage only; data is not saved to the database.
STUDY_SESSIONS = []
NEXT_SESSION_ID = 1


def serialize_session(session):
    return {
        key: value
        for key, value in session.items()
        if key != "user_id"
    }


class StudySessionListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="List My Study Sessions",
        responses=StudySessionSerializer(many=True),
    )
    def get(self, request):
        sessions = [
            serialize_session(session)
            for session in STUDY_SESSIONS
            if session["user_id"] == request.user.pk
        ]

        return Response({
            "count": len(sessions),
            "sessions": sessions,
        })

    @extend_schema(
        summary="Create a Study Session",
        request=StudySessionSerializer,
    )
    def post(self, request):
        global NEXT_SESSION_ID

        serializer = StudySessionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.validated_data["study_date"] < date.today():
            return Response(
                {"study_date": "Study date cannot be in the past."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        session = {
            "id": NEXT_SESSION_ID,
            "user_id": request.user.pk,
            **serializer.validated_data,
        }

        STUDY_SESSIONS.append(session)
        NEXT_SESSION_ID += 1

        return Response(
            serialize_session(session),
            status=status.HTTP_201_CREATED,
        )


class StudySessionDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_session(self, request, session_id):
        return next(
            (
                session for session in STUDY_SESSIONS
                if session["id"] == session_id
                and session["user_id"] == request.user.pk
            ),
            None,
        )

    @extend_schema(
        summary="Retrieve a Study Session",
        responses=StudySessionSerializer,
    )
    def get(self, request, session_id):
        session = self.get_session(request, session_id)

        if session is None:
            return Response(
                {"detail": "Study session not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(serialize_session(session))

    @extend_schema(
        summary="Replace a Study Session",
        request=StudySessionSerializer,
    )
    def put(self, request, session_id):
        session = self.get_session(request, session_id)

        if session is None:
            return Response(
                {"detail": "Study session not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = StudySessionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.validated_data["study_date"] < date.today():
            return Response(
                {"study_date": "Study date cannot be in the past."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        session.update(serializer.validated_data)

        return Response(serialize_session(session))

    @extend_schema(
        summary="Partially Update a Study Session",
        request=StudySessionSerializer,
    )
    def patch(self, request, session_id):
        session = self.get_session(request, session_id)

        if session is None:
            return Response(
                {"detail": "Study session not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = StudySessionSerializer(
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)

        if (
            "study_date" in serializer.validated_data
            and serializer.validated_data["study_date"] < date.today()
        ):
            return Response(
                {"study_date": "Study date cannot be in the past."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        session.update(serializer.validated_data)

        return Response(serialize_session(session))

    @extend_schema(summary="Delete a Study Session")
    def delete(self, request, session_id):
        session = self.get_session(request, session_id)

        if session is None:
            return Response(
                {"detail": "Study session not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        STUDY_SESSIONS.remove(session)

        return Response(
            {"message": "Study session deleted successfully."},
            status=status.HTTP_200_OK,
        )
