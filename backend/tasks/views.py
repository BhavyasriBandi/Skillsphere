
from datetime import date

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema

from .serializers import (
    TaskSerializer,
    TaskCreateSerializer,
    AssignmentSubmissionSerializer,
    TaskReviewSerializer,
)


SAMPLE_TASKS = [
    {
        "id": 1,
        "title": "Python Fundamentals",
        "description": "Write five Python programs using functions and loops.",
        "assigned_by": 3,
        "due_date": date(2026, 11, 5),
        "status": "Pending",
    },
    {
        "id": 2,
        "title": "SQL Practice",
        "description": "Write SQL queries using SELECT, WHERE, and JOIN.",
        "assigned_by": 3,
        "due_date": date(2026, 11, 10),
        "status": "Pending",
    },
]


def user_has_group(user, group_name):
    return user.groups.filter(name__iexact=group_name).exists()


def mentor_required(request):
    return user_has_group(request.user, "Mentor") or request.user.is_superuser


def student_required(request):
    return user_has_group(request.user, "Student") or request.user.is_superuser


def find_task(task_id):
    return next(
        (task for task in SAMPLE_TASKS if task["id"] == task_id),
        None,
    )


def serialize_task(task):
    return TaskSerializer(task).data


class TaskListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="list_tasks",
        summary="List Available Tasks",
        responses={200: TaskSerializer(many=True)},
    )
    def get(self, request):
        serializer = TaskSerializer(SAMPLE_TASKS, many=True)
        return Response(
            {
                "count": len(SAMPLE_TASKS),
                "tasks": serializer.data,
                "message": "These are sample tasks, not persisted records.",
            },
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        operation_id="create_task",
        summary="Create and Assign a Task",
        request=TaskCreateSerializer,
    )
    def post(self, request):
        if not mentor_required(request):
            return Response(
                {"detail": "Only mentors or administrators can create tasks."},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = TaskCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        from django.contrib.auth import get_user_model

        User = get_user_model()
        student_id = serializer.validated_data["student_id"]
        student = User.objects.filter(
            pk=student_id,
            is_active=True,
        ).first()

        if student is None or not user_has_group(student, "Student"):
            return Response(
                {"detail": "An active student with that ID was not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        data = serializer.validated_data
        new_id = max((task["id"] for task in SAMPLE_TASKS), default=0) + 1

        task = {
            "id": new_id,
            "title": data["title"],
            "description": data["description"],
            "assigned_by": request.user.pk,
            "due_date": data.get("due_date"),
            "status": "Pending",
        }
        SAMPLE_TASKS.append(task)

        return Response(
            {
                "task": serialize_task(task),
                "student_id": student.pk,
                "message": (
                    "Task created in temporary sample storage. "
                    "It is not saved to the database."
                ),
            },
            status=status.HTTP_201_CREATED,
        )


class TaskDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="update_task",
        summary="Replace Task Details",
        request=TaskCreateSerializer,
        responses={200: TaskSerializer},
    )
    def put(self, request, task_id):
        if not mentor_required(request):
            return Response(
                {"detail": "Only mentors or administrators can update tasks."},
                status=status.HTTP_403_FORBIDDEN,
            )

        task = find_task(task_id)
        if task is None:
            return Response(
                {"detail": "Task not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = TaskCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        from django.contrib.auth import get_user_model

        User = get_user_model()
        student = User.objects.filter(
            pk=data["student_id"],
            is_active=True,
        ).first()

        if student is None or not user_has_group(student, "Student"):
            return Response(
                {"detail": "An active student with that ID was not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        task.update(
            {
                "title": data["title"],
                "description": data["description"],
                "assigned_by": request.user.pk,
                "due_date": data.get("due_date"),
                "status": "Pending",
            }
        )

        return Response(
            {
                "task": serialize_task(task),
                "student_id": student.pk,
                "message": "Task replaced in temporary sample storage.",
            },
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        operation_id="partially_update_task",
        summary="Partially Update Task Details",
        request=TaskSerializer,
        responses={200: TaskSerializer},
    )
    def patch(self, request, task_id):
        if not mentor_required(request):
            return Response(
                {"detail": "Only mentors or administrators can update tasks."},
                status=status.HTTP_403_FORBIDDEN,
            )

        task = find_task(task_id)
        if task is None:
            return Response(
                {"detail": "Task not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        allowed_fields = {"title", "description", "due_date", "status"}
        updates = {}

        for field in allowed_fields:
            if field in request.data:
                updates[field] = request.data[field]

        if not updates:
            return Response(
                {"detail": "Provide at least one supported field to update."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if "title" in updates and (
            not isinstance(updates["title"], str)
            or not updates["title"].strip()
        ):
            return Response(
                {"title": "Title must be a non-empty string."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if "description" in updates and not isinstance(
            updates["description"], str
        ):
            return Response(
                {"description": "Description must be a string."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if "status" in updates and updates["status"] not in {
            "Pending", "In Progress", "Completed"
        }:
            return Response(
                {"status": "Choose Pending, In Progress, or Completed."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if "due_date" in updates:
            value = updates["due_date"]
            if value in ("", None):
                updates["due_date"] = None
            else:
                try:
                    updates["due_date"] = date.fromisoformat(value)
                except (TypeError, ValueError):
                    return Response(
                        {"due_date": "Use YYYY-MM-DD format."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

        for field, value in updates.items():
            task[field] = value.strip() if field in {
                "title", "description"
            } and isinstance(value, str) else value

        return Response(
            {
                "task": serialize_task(task),
                "message": "Task updated in temporary sample storage.",
            },
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        operation_id="delete_task",
        summary="Delete a Task",
        responses={204: None},
    )
    def delete(self, request, task_id):
        if not mentor_required(request):
            return Response(
                {"detail": "Only mentors or administrators can delete tasks."},
                status=status.HTTP_403_FORBIDDEN,
            )

        task = find_task(task_id)
        if task is None:
            return Response(
                {"detail": "Task not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        SAMPLE_TASKS.remove(task)

        return Response(status=status.HTTP_204_NO_CONTENT)


class AssignmentSubmissionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="submit_assignment",
        summary="Submit an Assignment",
        request=AssignmentSubmissionSerializer,
    )
    def post(self, request, task_id):
        if not student_required(request):
            return Response(
                {"detail": "Only students can submit assignments."},
                status=status.HTTP_403_FORBIDDEN,
            )

        task = find_task(task_id)
        if task is None:
            return Response(
                {"detail": "Task not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = AssignmentSubmissionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            {
                "task_id": task_id,
                "student_id": request.user.pk,
                "submission_text": serializer.validated_data[
                    "submission_text"
                ],
                "message": "Submission validated successfully but not saved.",
            },
            status=status.HTTP_201_CREATED,
        )


class TaskReviewAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="review_task_submission",
        summary="Review an Assignment",
        request=TaskReviewSerializer,
    )
    def patch(self, request, task_id):
        if not mentor_required(request):
            return Response(
                {"detail": "Only mentors or administrators can review tasks."},
                status=status.HTTP_403_FORBIDDEN,
            )

        task = find_task(task_id)
        if task is None:
            return Response(
                {"detail": "Task not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = TaskReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            {
                "task_id": task_id,
                "reviewed_by": request.user.pk,
                "feedback": serializer.validated_data["feedback"],
                "score": serializer.validated_data["score"],
                "message": "Review validated successfully but not saved.",
            },
            status=status.HTTP_200_OK,
        )
