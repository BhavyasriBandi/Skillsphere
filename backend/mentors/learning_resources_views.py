
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from accounts.permissions import IsMentor


# Reuses the same course catalogue currently displayed in Student Learning Hub.
# These are static React catalogue entries, not database records.

LEARNING_RESOURCES = [
    {
        "id": "python",
        "title": "Python Programming",
        "category": "Programming",
        "level": "Beginner",
        "duration": "4 weeks",
        "icon": "🐍",
        "description": "Learn Python fundamentals, functions, collections, and object-oriented programming through practical examples.",
        "skills": ["Variables", "Functions", "OOP", "Problem Solving"],
        "lesson_count": 5,
        "resources": [
            {
                "label": "Official Python Tutorial",
                "url": "https://docs.python.org/3/tutorial/",
            },
            {
                "label": "Python Beginner Guide",
                "url": "https://www.python.org/about/gettingstarted/",
            },
        ],
    },
    {
        "id": "java",
        "title": "Java Programming",
        "category": "Programming",
        "level": "Beginner",
        "duration": "5 weeks",
        "icon": "☕",
        "description": "Understand Java syntax, control flow, classes, objects, inheritance, and exception handling.",
        "skills": ["Java Syntax", "OOP", "Collections", "Exceptions"],
        "lesson_count": 5,
        "resources": [
            {
                "label": "Official Java Tutorials",
                "url": "https://dev.java/learn/",
            },
            {
                "label": "Java Documentation",
                "url": "https://docs.oracle.com/en/java/",
            },
        ],
    },
    {
        "id": "c",
        "title": "C Programming",
        "category": "Programming",
        "level": "Beginner",
        "duration": "3 weeks",
        "icon": "💻",
        "description": "Build strong programming foundations with C syntax, arrays, functions, pointers, and memory concepts.",
        "skills": ["C Basics", "Arrays", "Pointers", "Functions"],
        "lesson_count": 5,
        "resources": [
            {
                "label": "C Language Reference",
                "url": "https://en.cppreference.com/w/c",
            },
            {
                "label": "GNU C Documentation",
                "url": "https://gcc.gnu.org/onlinedocs/",
            },
        ],
    },
    {
        "id": "sql",
        "title": "SQL and Databases",
        "category": "Database",
        "level": "Beginner",
        "duration": "3 weeks",
        "icon": "🗄️",
        "description": "Learn relational database concepts, SQL queries, joins, aggregation, and data manipulation.",
        "skills": ["SELECT", "JOIN", "GROUP BY", "Database Design"],
        "lesson_count": 5,
        "resources": [
            {
                "label": "PostgreSQL Documentation",
                "url": "https://www.postgresql.org/docs/",
            },
            {
                "label": "SQL Tutorial",
                "url": "https://www.w3schools.com/sql/",
            },
        ],
    },
    {
        "id": "react",
        "title": "React.js Fundamentals",
        "category": "Web Development",
        "level": "Intermediate",
        "duration": "4 weeks",
        "icon": "⚛️",
        "description": "Create reusable user interfaces with components, props, state, events, and React hooks.",
        "skills": ["Components", "Props", "State", "Hooks"],
        "lesson_count": 5,
        "resources": [
            {
                "label": "Official React Documentation",
                "url": "https://react.dev/learn",
            },
            {
                "label": "React API Reference",
                "url": "https://react.dev/reference/react",
            },
        ],
    },
    {
        "id": "django",
        "title": "Django and REST APIs",
        "category": "Web Development",
        "level": "Intermediate",
        "duration": "5 weeks",
        "icon": "🌐",
        "description": "Understand Django applications, models, views, serializers, API endpoints, and backend fundamentals.",
        "skills": ["Django", "Models", "DRF", "REST APIs"],
        "lesson_count": 5,
        "resources": [
            {
                "label": "Official Django Tutorial",
                "url": "https://docs.djangoproject.com/en/stable/intro/tutorial01/",
            },
            {
                "label": "Django REST Framework Guide",
                "url": "https://www.django-rest-framework.org/",
            },
        ],
    },
    {
        "id": "dsa",
        "title": "Data Structures and Algorithms",
        "category": "Computer Science",
        "level": "Intermediate",
        "duration": "6 weeks",
        "icon": "🧠",
        "description": "Improve problem-solving with arrays, linked lists, stacks, queues, searching, sorting, and complexity analysis.",
        "skills": ["Arrays", "Stacks", "Queues", "Algorithms"],
        "lesson_count": 5,
        "resources": [
            {
                "label": "VisuAlgo — Algorithm Visualizations",
                "url": "https://visualgo.net/en",
            },
            {
                "label": "Open Data Structures Book",
                "url": "https://opendatastructures.org/",
            },
        ],
    },
    {
        "id": "htmlcss",
        "title": "HTML and CSS Essentials",
        "category": "Web Development",
        "level": "Beginner",
        "duration": "2 weeks",
        "icon": "🎨",
        "description": "Build the foundation of the web with semantic HTML, forms, responsive layouts, Flexbox, and CSS Grid.",
        "skills": ["HTML", "CSS", "Flexbox", "Responsive Design"],
        "lesson_count": 5,
        "resources": [
            {
                "label": "MDN HTML Guide",
                "url": "https://developer.mozilla.org/en-US/docs/Web/HTML",
            },
            {
                "label": "MDN CSS Guide",
                "url": "https://developer.mozilla.org/en-US/docs/Web/CSS",
            },
        ],
    },
]


class MentorLearningResourcesAPIView(APIView):
    permission_classes = [IsAuthenticated, IsMentor]

    def get(self, request):
        resources = LEARNING_RESOURCES.copy()

        search = request.query_params.get("search", "").strip().casefold()
        category = request.query_params.get("category", "").strip()
        level = request.query_params.get("level", "").strip()

        if search:
            resources = [
                item for item in resources
                if search in item["title"].casefold()
                or search in item["description"].casefold()
                or any(search in skill.casefold() for skill in item["skills"])
            ]

        if category and category.casefold() != "all":
            resources = [
                item for item in resources
                if item["category"].casefold() == category.casefold()
            ]

        if level and level.casefold() != "all levels":
            resources = [
                item for item in resources
                if item["level"].casefold() == level.casefold()
            ]

        return Response(
            {
                "count": len(resources),
                "categories": [
                    "Programming",
                    "Web Development",
                    "Database",
                    "Computer Science",
                ],
                "levels": ["Beginner", "Intermediate", "Advanced"],
                "resources": resources,
            },
            status=status.HTTP_200_OK,
        )
