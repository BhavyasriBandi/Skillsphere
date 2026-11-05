
from datetime import date

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema

from .models import LearningGoal, CareerGoal
from .serializers import (
    LearningGoalSerializer,
    CareerGoalSerializer,
)


class LearningGoalListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="List My Learning Goals",
        responses=LearningGoalSerializer(many=True),
    )
    def get(self, request):
        goals = LearningGoal.objects.filter(user=request.user)
        serializer = LearningGoalSerializer(goals, many=True)

        return Response({
            "count": goals.count(),
            "goals": serializer.data,
        })

    @extend_schema(
        summary="Create a Learning Goal",
        request=LearningGoalSerializer,
        responses=LearningGoalSerializer,
    )
    def post(self, request):
        serializer = LearningGoalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )


class LearningGoalDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_goal(self, request, goal_id):
        return get_object_or_404(
            LearningGoal,
            pk=goal_id,
            user=request.user,
        )

    @extend_schema(
        summary="Retrieve a Learning Goal",
        responses=LearningGoalSerializer,
    )
    def get(self, request, goal_id):
        goal = self.get_goal(request, goal_id)
        return Response(LearningGoalSerializer(goal).data)

    @extend_schema(
        summary="Replace a Learning Goal",
        request=LearningGoalSerializer,
        responses=LearningGoalSerializer,
    )
    def put(self, request, goal_id):
        goal = self.get_goal(request, goal_id)
        serializer = LearningGoalSerializer(
            goal,
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    @extend_schema(
        summary="Partially Update a Learning Goal",
        request=LearningGoalSerializer,
        responses=LearningGoalSerializer,
    )
    def patch(self, request, goal_id):
        goal = self.get_goal(request, goal_id)
        serializer = LearningGoalSerializer(
            goal,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    @extend_schema(summary="Delete a Learning Goal")
    def delete(self, request, goal_id):
        goal = self.get_goal(request, goal_id)
        goal.delete()

        return Response(
            {"message": "Learning goal deleted successfully."},
            status=status.HTTP_200_OK,
        )


class CareerGoalAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Get My Career Goal",
        responses=CareerGoalSerializer,
    )
    def get(self, request):
        goal = CareerGoal.objects.filter(user=request.user).first()

        if goal is None:
            return Response({
                "career_role": "",
                "domain": "",
                "experience_level": "Beginner",
                "target_date": None,
                "objective": "",
            })

        return Response(CareerGoalSerializer(goal).data)

    @extend_schema(
        summary="Create or Save My Career Goal",
        request=CareerGoalSerializer,
        responses=CareerGoalSerializer,
    )
    def post(self, request):
        existing_goal = CareerGoal.objects.filter(
            user=request.user
        ).first()

        serializer = CareerGoalSerializer(
            existing_goal,
            data=request.data,
            partial=existing_goal is not None,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(
            serializer.data,
            status=(
                status.HTTP_200_OK
                if existing_goal is not None
                else status.HTTP_201_CREATED
            ),
        )

    @extend_schema(
        summary="Update My Career Goal",
        request=CareerGoalSerializer,
        responses=CareerGoalSerializer,
    )
    def patch(self, request):
        goal = CareerGoal.objects.filter(user=request.user).first()

        if goal is None:
            serializer = CareerGoalSerializer(data=request.data)
        else:
            serializer = CareerGoalSerializer(
                goal,
                data=request.data,
                partial=True,
            )

        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(serializer.data)
