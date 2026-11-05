
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema

from .serializers import (
    LearningResourceSerializer,
    ResourceSearchSerializer,
)


LEARNING_RESOURCES = [
    {
        "id": 1,
        "title": "Official Python Tutorial",
        "description": "Learn Python programming fundamentals.",
        "skill": "Python",
        "resource_type": "Documentation",
        "url": "https://docs.python.org/3/tutorial/",
        "difficulty": "Beginner",
        "duration": "Self-paced",
    },
    {
        "id": 2,
        "title": "Django Documentation",
        "description": "Learn how to build web applications with Django.",
        "skill": "Django",
        "resource_type": "Documentation",
        "url": "https://docs.djangoproject.com/",
        "difficulty": "Intermediate",
        "duration": "Self-paced",
    },
    {
        "id": 3,
        "title": "MDN HTML Guide",
        "description": "Learn the structure of web pages using HTML.",
        "skill": "HTML",
        "resource_type": "Tutorial",
        "url": "https://developer.mozilla.org/en-US/docs/Web/HTML",
        "difficulty": "Beginner",
        "duration": "Self-paced",
    },
    {
        "id": 4,
        "title": "MDN CSS Guide",
        "description": "Learn styling and responsive web design.",
        "skill": "CSS",
        "resource_type": "Tutorial",
        "url": "https://developer.mozilla.org/en-US/docs/Web/CSS",
        "difficulty": "Beginner",
        "duration": "Self-paced",
    },
    {
        "id": 5,
        "title": "React Documentation",
        "description": "Learn React components, state, and interfaces.",
        "skill": "React",
        "resource_type": "Documentation",
        "url": "https://react.dev/learn",
        "difficulty": "Intermediate",
        "duration": "Self-paced",
    },
    {
        "id": 6,
        "title": "SQL Tutorial",
        "description": "Practice querying and managing relational data.",
        "skill": "SQL",
        "resource_type": "Tutorial",
        "url": "https://www.w3schools.com/sql/",
        "difficulty": "Beginner",
        "duration": "Self-paced",
    },
    {
        "id": 7,
        "title": "Java Documentation",
        "description": "Explore Java language concepts and APIs.",
        "skill": "Java",
        "resource_type": "Documentation",
        "url": "https://docs.oracle.com/en/java/",
        "difficulty": "Intermediate",
        "duration": "Self-paced",
    },
    {
        "id": 8,
        "title": "Machine Learning Course",
        "description": "Explore introductory machine learning concepts.",
        "skill": "Machine Learning",
        "resource_type": "Course",
        "url": "https://developers.google.com/machine-learning/crash-course",
        "difficulty": "Intermediate",
        "duration": "Self-paced",
    },
    {
        "id": 9,
        "title": "Git Documentation",
        "description": "Learn version control and Git workflows.",
        "skill": "Git",
        "resource_type": "Documentation",
        "url": "https://git-scm.com/doc",
        "difficulty": "Beginner",
        "duration": "Self-paced",
    },
    {
        "id": 10,
        "title": "Data Structures Learning",
        "description": "Study fundamental data structures and algorithms.",
        "skill": "Data Structures",
        "resource_type": "Tutorial",
        "url": "https://www.geeksforgeeks.org/data-structures/",
        "difficulty": "Intermediate",
        "duration": "Self-paced",
    },
]


def is_admin(user):
    return (
        user.is_superuser
        or user.groups.filter(name__iexact="Admin").exists()
    )


def find_resource(resource_id):
    return next(
        (
            item for item in LEARNING_RESOURCES
            if item["id"] == resource_id
        ),
        None,
    )


def validate_resource_data(data, partial=False):
    serializer = LearningResourceSerializer(
        data=data,
        partial=partial,
    )
    serializer.is_valid(raise_exception=True)
    return serializer


class LearningResourceListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="list_learning_resources",
        summary="List Learning Resources",
        parameters=[ResourceSearchSerializer],
        responses={200: LearningResourceSerializer(many=True)},
    )
    def get(self, request):
        query_serializer = ResourceSearchSerializer(
            data=request.query_params
        )
        query_serializer.is_valid(raise_exception=True)
        filters = query_serializer.validated_data

        results = LEARNING_RESOURCES

        if filters.get("skill"):
            skill = filters["skill"].casefold()
            results = [
                item for item in results
                if skill in item["skill"].casefold()
            ]

        if filters.get("resource_type"):
            resource_type = filters["resource_type"].casefold()
            results = [
                item for item in results
                if item["resource_type"].casefold() == resource_type
            ]

        if filters.get("difficulty"):
            difficulty = filters["difficulty"].casefold()
            results = [
                item for item in results
                if item["difficulty"].casefold() == difficulty
            ]

        serializer = LearningResourceSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        operation_id="create_learning_resource",
        summary="Create Learning Resource (Admin)",
        request=LearningResourceSerializer,
        responses={201: LearningResourceSerializer},
    )
    def post(self, request):
        if not is_admin(request.user):
            return Response(
                {"detail": "Only administrators can create resources."},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = validate_resource_data(request.data)
        data = dict(serializer.validated_data)

        new_id = max(
            (item["id"] for item in LEARNING_RESOURCES),
            default=0,
        ) + 1
        data["id"] = new_id
        LEARNING_RESOURCES.append(data)

        return Response(
            {
                "resource": LearningResourceSerializer(data).data,
                "message": "Resource added to temporary sample storage.",
            },
            status=status.HTTP_201_CREATED,
        )


class LearningResourceDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="get_learning_resource",
        summary="Get Learning Resource Details",
        responses={200: LearningResourceSerializer},
    )
    def get(self, request, resource_id):
        resource = find_resource(resource_id)

        if resource is None:
            return Response(
                {"detail": "Learning resource not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            LearningResourceSerializer(resource).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        operation_id="replace_learning_resource",
        summary="Replace Learning Resource (Admin)",
        request=LearningResourceSerializer,
        responses={200: LearningResourceSerializer},
    )
    def put(self, request, resource_id):
        if not is_admin(request.user):
            return Response(
                {"detail": "Only administrators can update resources."},
                status=status.HTTP_403_FORBIDDEN,
            )

        resource = find_resource(resource_id)
        if resource is None:
            return Response(
                {"detail": "Learning resource not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = validate_resource_data(request.data)
        updated_data = dict(serializer.validated_data)
        updated_data["id"] = resource_id

        resource.clear()
        resource.update(updated_data)

        return Response(
            {
                "resource": LearningResourceSerializer(resource).data,
                "message": "Resource replaced in temporary sample storage.",
            },
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        operation_id="partially_update_learning_resource",
        summary="Partially Update Learning Resource (Admin)",
        request=LearningResourceSerializer,
        responses={200: LearningResourceSerializer},
    )
    def patch(self, request, resource_id):
        if not is_admin(request.user):
            return Response(
                {"detail": "Only administrators can update resources."},
                status=status.HTTP_403_FORBIDDEN,
            )

        resource = find_resource(resource_id)
        if resource is None:
            return Response(
                {"detail": "Learning resource not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = validate_resource_data(
            request.data,
            partial=True,
        )

        resource.update(serializer.validated_data)

        return Response(
            {
                "resource": LearningResourceSerializer(resource).data,
                "message": "Resource updated in temporary sample storage.",
            },
            status=status.HTTP_200_OK,
        )

    @extend_schema(
        operation_id="delete_learning_resource",
        summary="Delete Learning Resource (Admin)",
        responses={204: None},
    )
    def delete(self, request, resource_id):
        if not is_admin(request.user):
            return Response(
                {"detail": "Only administrators can delete resources."},
                status=status.HTTP_403_FORBIDDEN,
            )

        resource = find_resource(resource_id)
        if resource is None:
            return Response(
                {"detail": "Learning resource not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        LEARNING_RESOURCES.remove(resource)

        return Response(status=status.HTTP_204_NO_CONTENT)


class RecommendedResourcesAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        operation_id="get_recommended_resources",
        summary="Get Recommended Learning Resources",
        responses={200: LearningResourceSerializer(many=True)},
        description=(
            "Returns sample resources matched to the skill query parameter. "
            "For example, use ?skill=Python. Recommendations are not "
            "persisted and do not use an external AI model."
        ),
    )
    def get(self, request):
        skill = request.query_params.get("skill", "").strip()

        if skill:
            results = [
                item for item in LEARNING_RESOURCES
                if skill.casefold() in item["skill"].casefold()
            ]
        else:
            results = [
                item for item in LEARNING_RESOURCES
                if item["difficulty"] == "Beginner"
            ]

        serializer = LearningResourceSerializer(results, many=True)

        return Response(
            {
                "user_id": request.user.pk,
                "count": len(results),
                "resources": serializer.data,
                "message": (
                    "Resources selected successfully."
                    if results
                    else "No matching resources found."
                ),
            },
            status=status.HTTP_200_OK,
        )
