import React, { useEffect, useMemo, useState } from "react";
import { showToast } from "../components/ToastProvider";
import {
  getLearningHubProgress,
  saveLearningHubProgress,
} from "./learningHubApi";
import "./LearningHub.css";

const STORAGE_KEY = "skillsphere_learning_hub_progress";

const INITIAL_PROGRESS = {
  completedLessons: [],
  savedCourses: [],
};

const COURSES = [
  {
    id: "python",
    title: "Python Programming",
    category: "Programming",
    level: "Beginner",
    duration: "4 weeks",
    icon: "🐍",
    color: "purple",
    description:
      "Learn Python fundamentals, functions, collections, and object-oriented programming through practical examples.",
    skills: ["Variables", "Functions", "OOP", "Problem Solving"],
    lessons: [
      {
        id: "py1",
        title: "Introduction to Python",
        duration: "15 min",
        type: "Reading",
        content:
          "Python is a beginner-friendly programming language used in web development, automation, data science, and AI. Start by understanding Python's purpose, installing Python, and running your first print() statement.",
        example: 'print("Hello, SkillSphere!")',
      },
      {
        id: "py2",
        title: "Variables and Data Types",
        duration: "20 min",
        type: "Practice",
        content:
          "Variables store values. Common data types include int, float, str, and bool. Use type() to inspect a value and input() to receive user input.",
        example:
          'name = "Bhavya"\nage = 20\nprint(name)\nprint(type(age))',
      },
      {
        id: "py3",
        title: "Conditions and Loops",
        duration: "25 min",
        type: "Practice",
        content:
          "Use if, elif, and else to make decisions. Use for and while loops to repeat operations. Indentation defines Python code blocks.",
        example: "for number in range(1, 6):\n    print(number)",
      },
      {
        id: "py4",
        title: "Functions and Collections",
        duration: "30 min",
        type: "Practice",
        content:
          "Functions organize reusable logic. Lists store ordered items, tuples are immutable, dictionaries store key-value pairs, and sets contain unique items.",
        example:
          "def square(number):\n    return number * number\n\nprint(square(5))",
      },
      {
        id: "py5",
        title: "Object-Oriented Programming",
        duration: "30 min",
        type: "Reading",
        content:
          "Classes define objects and their behavior. Learn about constructors, instance attributes, methods, inheritance, and encapsulation.",
        example:
          'class Student:\n    def __init__(self, name):\n        self.name = name\n\nstudent = Student("Bhavya")\nprint(student.name)',
      },
    ],
    resources: [
      {
        label: "Official Python Tutorial",
        url: "https://docs.python.org/3/tutorial/",
      },
      {
        label: "Python Beginner Guide",
        url: "https://www.python.org/about/gettingstarted/",
      },
    ],
  },
    {
    id: "java",
    title: "Java Programming",
    category: "Programming",
    level: "Beginner",
    duration: "5 weeks",
    icon: "☕",
    color: "orange",
    description:
      "Understand Java syntax, control flow, classes, objects, inheritance, and exception handling.",
    skills: ["Java Syntax", "OOP", "Collections", "Exceptions"],
    lessons: [
      {
        id: "ja1",
        title: "Introduction to Java",
        duration: "15 min",
        type: "Reading",
        content:
          "Java is a general-purpose, class-based programming language. Understand the JDK, JVM, source files, compilation, and program execution.",
        example:
          'public class Main {\n    public static void main(String[] args) {\n        System.out.println("Hello, SkillSphere!");\n    }\n}',
      },
      {
        id: "ja2",
        title: "Variables and Data Types",
        duration: "20 min",
        type: "Practice",
        content:
          "Java has primitive types such as int, double, char, and boolean, as well as reference types such as String and arrays.",
        example:
          'String name = "Bhavya";\nint score = 90;\nSystem.out.println(name + ": " + score);',
      },
      {
        id: "ja3",
        title: "Conditions and Loops",
        duration: "25 min",
        type: "Practice",
        content:
          "Use if-else and switch for decisions. Use for, while, and do-while loops to repeat tasks.",
        example:
          "for (int i = 1; i <= 5; i++) {\n    System.out.println(i);\n}",
      },
      {
        id: "ja4",
        title: "Classes and Objects",
        duration: "30 min",
        type: "Practice",
        content:
          "A class defines fields and methods. An object is an instance of a class. Constructors initialize objects, and access modifiers control visibility.",
        example:
          "class Student {\n    String name;\n    Student(String name) {\n        this.name = name;\n    }\n}",
      },
      {
        id: "ja5",
        title: "Inheritance and Exceptions",
        duration: "30 min",
        type: "Reading",
        content:
          "Inheritance lets a class extend another class. Exception handling uses try, catch, finally, throw, and throws to handle exceptional situations.",
        example:
          'try {\n    int result = 10 / 2;\n    System.out.println(result);\n} catch (ArithmeticException e) {\n    System.out.println("Invalid calculation");\n}',
      },
    ],
    resources: [
      {
        label: "Official Java Tutorials",
        url: "https://dev.java/learn/",
      },
      {
        label: "Java Documentation",
        url: "https://docs.oracle.com/en/java/",
      },
    ],
  },
  {
    id: "c",
    title: "C Programming",
    category: "Programming",
    level: "Beginner",
    duration: "3 weeks",
    icon: "💻",
    color: "blue",
    description:
      "Build strong programming foundations with C syntax, arrays, functions, pointers, and memory concepts.",
    skills: ["C Basics", "Arrays", "Pointers", "Functions"],
    lessons: [
      {
        id: "c1",
        title: "Your First C Program",
        duration: "15 min",
        type: "Reading",
        content:
          "C is a compiled programming language. Learn the role of main(), header files, printf(), compilation, and execution.",
        example:
          '#include <stdio.h>\n\nint main(void) {\n    printf("Hello, SkillSphere!\\n");\n    return 0;\n}',
      },
      {
        id: "c2",
        title: "Variables and Operators",
        duration: "20 min",
        type: "Practice",
        content:
          "Learn int, float, char, arithmetic operators, relational operators, logical operators, and formatted input/output.",
        example:
          '#include <stdio.h>\n\nint main(void) {\n    int a = 10, b = 5;\n    printf("%d", a + b);\n    return 0;\n}',
      },
      {
        id: "c3",
        title: "Conditions and Loops",
        duration: "25 min",
        type: "Practice",
        content:
          "Use if-else and switch to make decisions. Use for, while, and do-while to repeat instructions.",
        example:
          'for (int i = 1; i <= 5; i++) {\n    printf("%d\\n", i);\n}',
      },
      {
        id: "c4",
        title: "Arrays and Functions",
        duration: "30 min",
        type: "Practice",
        content:
          "Arrays store multiple values of the same type. Functions separate logic into reusable blocks and can accept parameters and return values.",
        example: "int add(int a, int b) {\n    return a + b;\n}",
      },
      {
        id: "c5",
        title: "Pointers and Structures",
        duration: "35 min",
        type: "Reading",
        content:
          "Pointers store memory addresses. Structures group related fields into one type. Practice carefully with addresses and pointer dereferencing.",
        example: 'int number = 10;\nint *ptr = &number;\nprintf("%d", *ptr);',
      },
    ],
    resources: [
      {
        label: "C Language Reference",
        url: "https://en.cppreference.com/w/c",
      },
      {
        label: "GNU C Documentation",
        url: "https://gcc.gnu.org/onlinedocs/",
      },
    ],
  },
  {
    id: "sql",
    title: "SQL and Databases",
    category: "Database",
    level: "Beginner",
    duration: "3 weeks",
    icon: "🗄️",
    color: "green",
    description:
      "Learn relational database concepts, SQL queries, joins, aggregation, and data manipulation.",
    skills: ["SELECT", "JOIN", "GROUP BY", "Database Design"],
    lessons: [
      {
        id: "sq1",
        title: "Database Fundamentals",
        duration: "15 min",
        type: "Reading",
        content:
          "A relational database stores structured information in tables. Learn tables, rows, columns, primary keys, and foreign keys.",
        example:
          "CREATE TABLE students (\n    id INTEGER PRIMARY KEY,\n    name VARCHAR(100),\n    email VARCHAR(150)\n);",
      },
      {
        id: "sq2",
        title: "SELECT and Filtering",
        duration: "20 min",
        type: "Practice",
        content:
          "SELECT retrieves data. WHERE filters rows, ORDER BY sorts results, and LIMIT restricts how many rows are returned.",
        example:
          "SELECT name, email\nFROM students\nWHERE id > 1\nORDER BY name;",
      },
      {
        id: "sq3",
        title: "INSERT, UPDATE, DELETE",
        duration: "25 min",
        type: "Practice",
        content:
          "INSERT adds rows, UPDATE modifies existing rows, and DELETE removes rows. Always use appropriate WHERE conditions when changing data.",
        example:
          "INSERT INTO students (id, name)\nVALUES (1, 'Bhavya');",
      },
      {
        id: "sq4",
        title: "Joins and Relationships",
        duration: "30 min",
        type: "Practice",
        content:
          "JOIN combines related records from tables. Learn INNER JOIN and LEFT JOIN, and understand how keys connect tables.",
        example:
          "SELECT students.name, courses.title\nFROM students\nINNER JOIN enrollments\nON students.id = enrollments.student_id\nINNER JOIN courses\nON enrollments.course_id = courses.id;",
      },
      {
        id: "sq5",
        title: "Aggregate Functions",
        duration: "25 min",
        type: "Reading",
        content:
          "COUNT, SUM, AVG, MIN, and MAX summarize data. GROUP BY creates groups, while HAVING filters aggregated results.",
        example:
          "SELECT department, COUNT(*) AS total\nFROM employees\nGROUP BY department;",
      },
    ],
    resources: [
      {
        label: "PostgreSQL Documentation",
        url: "https://www.postgresql.org/docs/",
      },
      {
        label: "SQL Tutorial",
        url: "https://www.w3schools.com/sql/",
      },
    ],
  },
  {
    id: "react",
    title: "React.js Fundamentals",
    category: "Web Development",
    level: "Intermediate",
    duration: "4 weeks",
    icon: "⚛️",
    color: "cyan",
    description:
      "Create reusable user interfaces with components, props, state, events, and React hooks.",
    skills: ["Components", "Props", "State", "Hooks"],
    lessons: [
      {
        id: "re1",
        title: "React and Components",
        duration: "20 min",
        type: "Reading",
        content:
          "React builds interfaces from reusable components. Components are JavaScript functions that return JSX. Keep components focused and reusable.",
        example:
          'function Welcome() {\n    return <h1>Welcome to SkillSphere</h1>;\n}\n\nexport default Welcome;',
      },
      {
        id: "re2",
        title: "JSX and Props",
        duration: "25 min",
        type: "Practice",
        content:
          "JSX describes UI using JavaScript expressions and markup-like syntax. Props pass information from parent components to child components.",
        example:
          'function Greeting({ name }) {\n    return <p>Hello, {name}!</p>;\n}',
      },
      {
        id: "re3",
        title: "State and Events",
        duration: "30 min",
        type: "Practice",
        content:
          "useState stores component state. State updates cause React to render the component again. Event handlers respond to clicks, typing, and other interactions.",
        example:
          'const [count, setCount] = useState(0);\n\n<button onClick={() => setCount(count + 1)}>\n    Count: {count}\n</button>',
      },
      {
        id: "re4",
        title: "Lists and Conditional UI",
        duration: "25 min",
        type: "Practice",
        content:
          "Use map() to render lists and give each item a stable key. Use conditions to show different content depending on application state.",
        example:
          'const topics = ["HTML", "CSS", "React"];\n\n{topics.map(topic => (\n    <p key={topic}>{topic}</p>\n))}',
      },
      {
        id: "re5",
        title: "Effects and Data Flow",
        duration: "35 min",
        type: "Reading",
        content:
          "useEffect synchronizes a component with external systems. Specify dependencies carefully and clean up subscriptions or timers when needed.",
        example:
          'useEffect(() => {\n    document.title = "SkillSphere";\n}, []);',
      },
    ],
    resources: [
      {
        label: "Official React Documentation",
        url: "https://react.dev/learn",
      },
      {
        label: "React API Reference",
        url: "https://react.dev/reference/react",
      },
    ],
  },
    {
    id: "django",
    title: "Django and REST APIs",
    category: "Web Development",
    level: "Intermediate",
    duration: "5 weeks",
    icon: "🌐",
    color: "green",
    description:
      "Understand Django applications, models, views, serializers, API endpoints, and backend fundamentals.",
    skills: ["Django", "Models", "DRF", "REST APIs"],
    lessons: [
      {
        id: "dj1",
        title: "Django Project Structure",
        duration: "20 min",
        type: "Reading",
        content:
          "A Django project contains configuration, while apps organize related features. Learn manage.py, settings.py, urls.py, and app structure.",
        example:
          "python -m django --version\npython manage.py startapp courses",
      },
      {
        id: "dj2",
        title: "Models and Migrations",
        duration: "30 min",
        type: "Practice",
        content:
          "Models describe database tables using Python classes. makemigrations creates migration files; migrate applies them to the database.",
        example:
          "from django.db import models\n\nclass Course(models.Model):\n    title = models.CharField(max_length=150)\n    description = models.TextField(blank=True)",
      },
      {
        id: "dj3",
        title: "Views and URLs",
        duration: "25 min",
        type: "Practice",
        content:
          "Views process requests and return responses. URL patterns route incoming paths to the correct views.",
        example:
          'from django.http import JsonResponse\n\ndef health_check(request):\n    return JsonResponse({"status": "ok"})',
      },
      {
        id: "dj4",
        title: "Serializers and API Views",
        duration: "35 min",
        type: "Practice",
        content:
          "Django REST Framework serializers convert model instances to representations and validate incoming data. API views handle HTTP requests and responses.",
        example:
          "from rest_framework import serializers\n\nclass CourseSerializer(serializers.Serializer):\n    title = serializers.CharField(max_length=150)",
      },
      {
        id: "dj5",
        title: "Testing REST Endpoints",
        duration: "30 min",
        type: "Reading",
        content:
          "Test API endpoints with suitable HTTP methods, status codes, request payloads, permissions, and validation. Avoid exposing secrets in responses.",
        example:
          "GET /api/courses/\nPOST /api/courses/\nContent-Type: application/json",
      },
    ],
    resources: [
      {
        label: "Official Django Tutorial",
        url: "https://docs.djangoproject.com/en/stable/intro/tutorial01/",
      },
      {
        label: "Django REST Framework Guide",
        url: "https://www.django-rest-framework.org/",
      },
    ],
  },
  {
    id: "dsa",
    title: "Data Structures and Algorithms",
    category: "Computer Science",
    level: "Intermediate",
    duration: "6 weeks",
    icon: "🧠",
    color: "pink",
    description:
      "Improve problem-solving with arrays, linked lists, stacks, queues, searching, sorting, and complexity analysis.",
    skills: ["Arrays", "Stacks", "Queues", "Algorithms"],
    lessons: [
      {
        id: "ds1",
        title: "Complexity Basics",
        duration: "20 min",
        type: "Reading",
        content:
          "Time complexity describes how running time grows with input size. Space complexity describes additional memory use. Learn common Big-O categories.",
        example:
          "O(1) — constant\nO(log n) — logarithmic\nO(n) — linear\nO(n log n) — linearithmic\nO(n²) — quadratic",
      },
      {
        id: "ds2",
        title: "Arrays and Searching",
        duration: "25 min",
        type: "Practice",
        content:
          "Arrays store ordered elements. Linear search checks elements one by one. Binary search works on sorted data by repeatedly halving the search range.",
        example:
          "def linear_search(items, target):\n    for index, item in enumerate(items):\n        if item == target:\n            return index\n    return -1",
      },
      {
        id: "ds3",
        title: "Stacks and Queues",
        duration: "25 min",
        type: "Practice",
        content:
          "A stack follows last-in, first-out. A queue follows first-in, first-out. These structures are useful in parsing, scheduling, and breadth-first search.",
        example:
          "stack = []\nstack.append(10)\nstack.append(20)\nlast = stack.pop()",
      },
      {
        id: "ds4",
        title: "Sorting Algorithms",
        duration: "30 min",
        type: "Reading",
        content:
          "Sorting arranges data in order. Learn the ideas behind bubble sort, insertion sort, merge sort, and quicksort, including their trade-offs.",
        example: "numbers = [5, 2, 4, 1]\nnumbers.sort()\nprint(numbers)",
      },
      {
        id: "ds5",
        title: "Linked Lists and Trees",
        duration: "35 min",
        type: "Reading",
        content:
          "Linked lists connect nodes using references. Trees organize data hierarchically. Learn nodes, traversal, and basic binary search tree operations.",
        example:
          "class Node:\n    def __init__(self, value):\n        self.value = value\n        self.next = None",
      },
    ],
    resources: [
      {
        label: "VisuAlgo — Algorithm Visualizations",
        url: "https://visualgo.net/en",
      },
      {
        label: "Open Data Structures Book",
        url: "https://opendatastructures.org/",
      },
    ],
  },
  {
    id: "htmlcss",
    title: "HTML and CSS Essentials",
    category: "Web Development",
    level: "Beginner",
    duration: "2 weeks",
    icon: "🎨",
    color: "orange",
    description:
      "Build the foundation of the web with semantic HTML, forms, responsive layouts, Flexbox, and CSS Grid.",
    skills: ["HTML", "CSS", "Flexbox", "Responsive Design"],
    lessons: [
      {
        id: "hc1",
        title: "HTML Document Structure",
        duration: "15 min",
        type: "Reading",
        content:
          "HTML structures web content. Learn headings, paragraphs, links, images, semantic elements, and how a document is organized.",
        example:
          "<main>\n  <h1>My Learning Journey</h1>\n  <p>Welcome to SkillSphere.</p>\n</main>",
      },
      {
        id: "hc2",
        title: "Forms and Accessibility",
        duration: "20 min",
        type: "Practice",
        content:
          "Forms collect user input. Associate labels with controls, use appropriate input types, and provide clear instructions and error messages.",
        example:
          '<label for="email">Email</label>\n<input id="email" type="email" required />',
      },
      {
        id: "hc3",
        title: "CSS Selectors and Box Model",
        duration: "25 min",
        type: "Practice",
        content:
          "CSS controls presentation. Learn selectors, specificity, margin, border, padding, width, and box-sizing.",
        example:
          ".card {\n  padding: 20px;\n  border-radius: 12px;\n  box-sizing: border-box;\n}",
      },
      {
        id: "hc4",
        title: "Flexbox and Grid",
        duration: "30 min",
        type: "Practice",
        content:
          "Flexbox is useful for one-dimensional layouts. CSS Grid supports rows and columns for two-dimensional layouts.",
        example:
          ".container {\n  display: grid;\n  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));\n  gap: 16px;\n}",
      },
      {
        id: "hc5",
        title: "Responsive Design",
        duration: "25 min",
        type: "Reading",
        content:
          "Responsive design adapts layouts to different screens. Use flexible units, responsive grids, suitable images, and media queries.",
        example:
          "@media (max-width: 600px) {\n  .sidebar {\n    display: none;\n  }\n}",
      },
    ],
    resources: [
      {
        label: "MDN HTML Guide",
        url: "https://developer.mozilla.org/en-US/docs/Web/HTML",
      },
      {
        label: "MDN CSS Guide",
        url: "https://developer.mozilla.org/en-US/docs/Web/CSS",
      },
    ],
  },
];

const CATEGORIES = [
  "All",
  "Programming",
  "Web Development",
  "Database",
  "Computer Science",
];


function LearningHub() {
  const [progress, setProgress] = useState(INITIAL_PROGRESS);
  const [progressLoaded, setProgressLoaded] = useState(false);

  const [search, setSearch] = useState("");
  const [category, setCategory] = useState("All");
  const [level, setLevel] = useState("All Levels");
  const [activeTab, setActiveTab] = useState("Explore");
  const [selectedCourseId, setSelectedCourseId] = useState(null);
  const [selectedLessonId, setSelectedLessonId] = useState(null);

  // Load the student's saved learning progress from Django.
  useEffect(() => {
    let isMounted = true;

    async function loadProgress() {
      try {
        const data = await getLearningHubProgress();

        if (isMounted) {
          setProgress({
            completedLessons: Array.isArray(data.completedLessons)
              ? data.completedLessons
              : [],
            savedCourses: Array.isArray(data.savedCourses)
              ? data.savedCourses
              : [],
          });
        }
      } catch (error) {
        if (isMounted) {
          showToast(
            error.message || "Failed to load learning progress.",
            "error"
          );
        }
      } finally {
        if (isMounted) {
          setProgressLoaded(true);
        }
      }
    }

    loadProgress();

    return () => {
      isMounted = false;
    };
  }, []);

  // Save changes to the browser and Django after the initial load.
  useEffect(() => {
    if (!progressLoaded) return;

    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
    } catch {
      showToast(
        "Progress could not be saved in browser storage.",
        "error"
      );
    }

    let isMounted = true;

    async function saveProgress() {
      try {
        await saveLearningHubProgress(progress);
      } catch (error) {
        if (isMounted) {
          showToast(
            error.message || "Failed to save learning progress.",
            "error"
          );
        }
      }
    }

    saveProgress();

    return () => {
      isMounted = false;
    };
  }, [progress, progressLoaded]);

  const completedSet = useMemo(
    () => new Set(progress.completedLessons),
    [progress.completedLessons]
  );

  const completedCount = progress.completedLessons.length;

  const getCourseProgress = (course) => {
    const completed = course.lessons.filter((lesson) =>
      completedSet.has(lesson.id)
    ).length;

    return {
      completed,
      total: course.lessons.length,
      percentage: Math.round((completed / course.lessons.length) * 100),
    };
  };

  const filteredCourses = useMemo(() => {
    const query = search.trim().toLowerCase();

    return COURSES.filter((course) => {
      const matchesSearch =
        !query ||
        course.title.toLowerCase().includes(query) ||
        course.description.toLowerCase().includes(query) ||
        course.skills.some((skill) => skill.toLowerCase().includes(query));

      const matchesCategory =
        category === "All" || course.category === category;

      const matchesLevel =
        level === "All Levels" || course.level === level;

      const courseProgress = course.lessons.filter((lesson) =>
        completedSet.has(lesson.id)
      ).length;

      const matchesTab =
        activeTab !== "My Learning" ||
        progress.savedCourses.includes(course.id) ||
        courseProgress > 0;

      return (
        matchesSearch &&
        matchesCategory &&
        matchesLevel &&
        matchesTab
      );
    });
  }, [
    search,
    category,
    level,
    activeTab,
    progress.savedCourses,
    completedSet,
  ]);

  const selectedCourse = COURSES.find(
    (course) => course.id === selectedCourseId
  );

  const selectedLesson = selectedCourse?.lessons.find(
    (lesson) => lesson.id === selectedLessonId
  );

  const openCourse = (course) => {
    setSelectedCourseId(course.id);

    const firstIncomplete = course.lessons.find(
      (lesson) => !completedSet.has(lesson.id)
    );

    setSelectedLessonId(
      firstIncomplete?.id || course.lessons[0]?.id || null
    );
  };

  const closeCourse = () => {
    setSelectedCourseId(null);
    setSelectedLessonId(null);
  };

  const toggleSaved = (courseId) => {
    const isSaved = progress.savedCourses.includes(courseId);

    setProgress((previous) => ({
      ...previous,
      savedCourses: isSaved
        ? previous.savedCourses.filter((id) => id !== courseId)
        : [...previous.savedCourses, courseId],
    }));

    showToast(
      isSaved
        ? "Course removed from My Learning."
        : "Course saved to My Learning.",
      isSaved ? "info" : "success"
    );
  };

  const toggleLessonComplete = (lessonId) => {
    const alreadyComplete = completedSet.has(lessonId);

    setProgress((previous) => ({
      ...previous,
      completedLessons: alreadyComplete
        ? previous.completedLessons.filter((id) => id !== lessonId)
        : [...previous.completedLessons, lessonId],
    }));

    showToast(
      alreadyComplete
        ? "Lesson marked incomplete."
        : "Lesson completed! Great work.",
      alreadyComplete ? "info" : "success"
    );
  };

  const resetFilters = () => {
    setSearch("");
    setCategory("All");
    setLevel("All Levels");
  };

  const startNextLesson = () => {
    if (!selectedCourse) return;

    const currentIndex = selectedCourse.lessons.findIndex(
      (lesson) => lesson.id === selectedLessonId
    );

    const nextLesson = selectedCourse.lessons
      .slice(currentIndex + 1)
      .find((lesson) => !completedSet.has(lesson.id));

    if (nextLesson) {
      setSelectedLessonId(nextLesson.id);
    } else {
      const firstIncomplete = selectedCourse.lessons.find(
        (lesson) => !completedSet.has(lesson.id)
      );

      if (firstIncomplete) {
        setSelectedLessonId(firstIncomplete.id);
      } else {
        showToast(
          "You've completed every lesson in this course!",
          "success"
        );
      }
    }
  };

  const totalLessons = COURSES.reduce(
    (total, course) => total + course.lessons.length,
    0
  );

  const overallProgress = Math.round(
    (completedCount / totalLessons) * 100
  );
    return (
    <div className="learning-hub">
      <header className="lh-hero">
        <div className="lh-hero-copy">
          <span className="lh-eyebrow">
            <span className="lh-eyebrow-dot" />
            SKILLSPHERE LEARNING HUB
          </span>

          <h1>
            Learn something <span>extraordinary.</span>
          </h1>

          <p>
            Build in-demand skills, explore guided lessons, and keep moving
            towards your career goals — one lesson at a time.
          </p>

          <button
            type="button"
            className="lh-primary-button"
            onClick={() => {
              setActiveTab("Explore");
              setCategory("All");
              setLevel("All Levels");
              setSearch("");
              document.getElementById("lh-course-library")?.scrollIntoView({
                behavior: "smooth",
                block: "start",
              });
            }}
          >
            Explore courses <span aria-hidden="true">→</span>
          </button>
        </div>

        <div className="lh-hero-art" aria-hidden="true">
          <div className="lh-orbit lh-orbit-one" />
          <div className="lh-orbit lh-orbit-two" />
          <div className="lh-hero-book">📚</div>
          <div className="lh-float-card lh-float-top">
            <span>✦</span> Keep growing
          </div>
          <div className="lh-float-card lh-float-bottom">
            <span>✓</span> One step at a time
          </div>
        </div>
      </header>

      <section className="lh-stats" aria-label="Learning statistics">
        <div className="lh-stat-card">
          <span className="lh-stat-icon lh-stat-blue">📘</span>
          <div>
            <strong>{COURSES.length}</strong>
            <span>Learning paths</span>
          </div>
        </div>

        <div className="lh-stat-card">
          <span className="lh-stat-icon lh-stat-purple">✓</span>
          <div>
            <strong>{completedCount}</strong>
            <span>Lessons completed</span>
          </div>
        </div>

        <div className="lh-stat-card">
          <span className="lh-stat-icon lh-stat-green">🎯</span>
          <div>
            <strong>{overallProgress}%</strong>
            <span>Overall completion</span>
          </div>
        </div>

        <div className="lh-stat-card">
          <span className="lh-stat-icon lh-stat-orange">🔖</span>
          <div>
            <strong>{progress.savedCourses.length}</strong>
            <span>Saved courses</span>
          </div>
        </div>
      </section>

      <section className="lh-progress-banner">
        <div className="lh-progress-symbol">🚀</div>

        <div className="lh-progress-info">
          <div className="lh-progress-heading">
            <div>
              <h2>Your learning journey</h2>
              <p>Small steps today. Stronger skills tomorrow.</p>
            </div>
            <strong>{overallProgress}%</strong>
          </div>

          <div
            className="lh-progress-track"
            role="progressbar"
            aria-label="Overall learning progress"
            aria-valuenow={overallProgress}
            aria-valuemin={0}
            aria-valuemax={100}
          >
            <div style={{ width: `${overallProgress}%` }} />
          </div>

          <span className="lh-progress-caption">
            {completedCount} of {totalLessons} lessons completed across all
            courses
          </span>
        </div>
      </section>

      <section className="lh-library" id="lh-course-library">
        <div className="lh-section-heading">
          <div>
            <span className="lh-section-label">YOUR NEXT OPPORTUNITY</span>
            <h2>Discover your next skill</h2>
            <p>Choose a learning path and grow at your own pace.</p>
          </div>
        </div>

        <div className="lh-tabs" role="tablist" aria-label="Course views">
          <button
            type="button"
            role="tab"
            aria-selected={activeTab === "Explore"}
            className={activeTab === "Explore" ? "active" : ""}
            onClick={() => setActiveTab("Explore")}
          >
            Explore courses
          </button>

          <button
            type="button"
            role="tab"
            aria-selected={activeTab === "My Learning"}
            className={activeTab === "My Learning" ? "active" : ""}
            onClick={() => setActiveTab("My Learning")}
          >
            My learning
            <span className="lh-tab-count">
              {progress.savedCourses.length}
            </span>
          </button>
        </div>

        <div className="lh-filters">
          <label className="lh-search">
            <span aria-hidden="true">⌕</span>
            <input
              type="search"
              placeholder="Search courses, skills..."
              value={search}
              onChange={(event) => setSearch(event.target.value)}
              aria-label="Search courses"
            />

            {search && (
              <button
                type="button"
                onClick={() => setSearch("")}
                aria-label="Clear search"
              >
                ×
              </button>
            )}
          </label>

          <label className="lh-filter-select">
            <span className="lh-sr-only">Filter by category</span>
            <select
              value={category}
              onChange={(event) => setCategory(event.target.value)}
            >
              {CATEGORIES.map((item) => (
                <option key={item} value={item}>
                  {item === "All" ? "All categories" : item}
                </option>
              ))}
            </select>
          </label>

          <label className="lh-filter-select">
            <span className="lh-sr-only">Filter by level</span>
            <select
              value={level}
              onChange={(event) => setLevel(event.target.value)}
            >
              <option>All Levels</option>
              <option>Beginner</option>
              <option>Intermediate</option>
              <option>Advanced</option>
            </select>
          </label>

          {(search || category !== "All" || level !== "All Levels") && (
            <button
              type="button"
              className="lh-reset-filters"
              onClick={resetFilters}
            >
              Clear filters
            </button>
          )}
        </div>

        {activeTab === "My Learning" && (
          <div className="lh-my-learning-note">
            <span>🔖</span>
            <p>
              Your saved courses and courses you've started appear here.
              Save a course or complete a lesson to add it to this list.
            </p>
          </div>
        )}

        <div className="lh-course-grid">
          {filteredCourses.map((course) => {
            const courseProgress = getCourseProgress(course);
            const isSaved = progress.savedCourses.includes(course.id);

            return (
              <article className="lh-course-card" key={course.id}>
                <div className={`lh-course-cover ${course.color}`}>
                  <div className="lh-course-cover-top">
                    <span className="lh-course-category">
                      {course.category}
                    </span>

                    <button
                      type="button"
                      className={`lh-bookmark ${isSaved ? "saved" : ""}`}
                      onClick={() => toggleSaved(course.id)}
                      aria-label={
                        isSaved
                          ? `Remove ${course.title} from saved courses`
                          : `Save ${course.title}`
                      }
                      title={isSaved ? "Remove saved course" : "Save course"}
                    >
                      {isSaved ? "★" : "☆"}
                    </button>
                  </div>

                  <span className="lh-course-emoji" aria-hidden="true">
                    {course.icon}
                  </span>

                  <span className="lh-cover-decoration" aria-hidden="true">
                    ✦
                  </span>
                </div>

                <div className="lh-course-body">
                  <div className="lh-course-meta">
                    <span className={`lh-level ${course.level.toLowerCase()}`}>
                      {course.level}
                    </span>
                    <span>◷ {course.duration}</span>
                  </div>

                  <h3>{course.title}</h3>
                  <p className="lh-course-description">{course.description}</p>

                  <div className="lh-skill-tags">
                    {course.skills.slice(0, 3).map((skill) => (
                      <span key={skill}>{skill}</span>
                    ))}

                    {course.skills.length > 3 && (
                      <span>+{course.skills.length - 3}</span>
                    )}
                  </div>

                  <div className="lh-course-progress">
                    <div className="lh-course-progress-label">
                      <span>
                        {courseProgress.completed}/{courseProgress.total} lessons
                      </span>
                      <strong>{courseProgress.percentage}%</strong>
                    </div>

                    <div className="lh-mini-track">
                      <div
                        style={{ width: `${courseProgress.percentage}%` }}
                      />
                    </div>
                  </div>

                  <button
                    type="button"
                    className="lh-course-button"
                    onClick={() => openCourse(course)}
                  >
                    {courseProgress.percentage === 100
                      ? "Review course"
                      : courseProgress.percentage > 0
                      ? "Continue learning"
                      : "Start learning"}
                    <span aria-hidden="true">→</span>
                  </button>
                </div>
              </article>
            );
          })}
        </div>

        {filteredCourses.length === 0 && (
          <div className="lh-empty-state">
            <span>🔎</span>
            <h3>No courses found</h3>
            <p>
              {activeTab === "My Learning"
                ? "You haven't saved or started any courses matching these filters yet."
                : "Try a different search term or change your filters."}
            </p>
            <button type="button" onClick={resetFilters}>
              Reset filters
            </button>
          </div>
        )}
      </section>
            <section className="lh-resource-section">
        <div className="lh-section-heading">
          <div>
            <span className="lh-section-label">KEEP EXPLORING</span>
            <h2>Trusted learning resources</h2>
            <p>Go deeper with official documentation and references.</p>
          </div>
        </div>

        <div className="lh-resource-grid">
          {[
            {
              icon: "📖",
              title: "Official Documentation",
              description:
                "Learn directly from the official guides and reference material.",
              links: [
                { label: "Python", url: "https://docs.python.org/3/" },
                { label: "React", url: "https://react.dev/learn" },
                {
                  label: "Django",
                  url: "https://docs.djangoproject.com/en/stable/",
                },
              ],
            },
            {
              icon: "🧩",
              title: "Practice and Visualize",
              description:
                "Strengthen your problem-solving skills with guided practice.",
              links: [
                { label: "Visual Algorithms", url: "https://visualgo.net/en" },
                {
                  label: "SQL Tutorial",
                  url: "https://www.w3schools.com/sql/",
                },
              ],
            },
          ].map((resource) => (
            <article className="lh-resource-card" key={resource.title}>
              <div className="lh-resource-icon">{resource.icon}</div>

              <div className="lh-resource-content">
                <h3>{resource.title}</h3>
                <p>{resource.description}</p>

                <div className="lh-resource-links">
                  {resource.links.map((link) => (
                    <a
                      href={link.url}
                      key={link.label}
                      target="_blank"
                      rel="noreferrer"
                    >
                      {link.label} <span aria-hidden="true">↗</span>
                    </a>
                  ))}
                </div>
              </div>
            </article>
          ))}
        </div>
      </section>

      {selectedCourse && (
        <div
          className="lh-modal-backdrop"
          role="presentation"
          onMouseDown={(event) => {
            if (event.target === event.currentTarget) closeCourse();
          }}
        >
          <section
            className="lh-course-modal"
            role="dialog"
            aria-modal="true"
            aria-labelledby="lh-modal-title"
          >
            <div className="lh-modal-header">
              <div className={`lh-modal-course-icon ${selectedCourse.color}`}>
                {selectedCourse.icon}
              </div>

              <div className="lh-modal-heading">
                <span>{selectedCourse.category}</span>
                <h2 id="lh-modal-title">{selectedCourse.title}</h2>
                <p>
                  {selectedCourse.level} · {selectedCourse.duration} ·{" "}
                  {getCourseProgress(selectedCourse).completed}/
                  {selectedCourse.lessons.length} lessons complete
                </p>
              </div>

              <button
                type="button"
                className="lh-modal-close"
                onClick={closeCourse}
                aria-label="Close course"
              >
                ×
              </button>
            </div>

            <div className="lh-modal-progress">
              <div
                style={{
                  width: `${getCourseProgress(selectedCourse).percentage}%`,
                }}
              />
            </div>

            <div className="lh-modal-layout">
              <aside className="lh-lesson-sidebar">
                <h3>Course lessons</h3>

                {selectedCourse.lessons.map((lesson, index) => {
                  const isComplete = completedSet.has(lesson.id);

                  return (
                    <button
                      type="button"
                      key={lesson.id}
                      className={`lh-lesson-nav ${
                        selectedLessonId === lesson.id ? "active" : ""
                      }`}
                      onClick={() => setSelectedLessonId(lesson.id)}
                    >
                      <span
                        className={`lh-lesson-number ${
                          isComplete ? "complete" : ""
                        }`}
                      >
                        {isComplete ? "✓" : String(index + 1).padStart(2, "0")}
                      </span>

                      <span className="lh-lesson-nav-copy">
                        <strong>{lesson.title}</strong>
                        <small>{lesson.duration}</small>
                      </span>
                    </button>
                  );
                })}
              </aside>

              <div className="lh-lesson-content">
                {selectedLesson ? (
                  <>
                    <div className="lh-lesson-labels">
                      <span>
                        LESSON{" "}
                        {selectedCourse.lessons.findIndex(
                          (lesson) => lesson.id === selectedLesson.id
                        ) + 1}
                      </span>
                      <span>◷ {selectedLesson.duration}</span>
                      <span>{selectedLesson.type}</span>
                    </div>

                    <h3>{selectedLesson.title}</h3>

                    <p className="lh-lesson-description">
                      {selectedLesson.content}
                    </p>

                    <div className="lh-example-box">
                      <div className="lh-example-header">
                        <span>Example</span>
                        <span>Code sample</span>
                      </div>

                      <pre>
                        <code>{selectedLesson.example}</code>
                      </pre>

                      <p>
                        Study the example and try running or adapting it in
                        your own coding environment.
                      </p>
                    </div>

                    <div className="lh-lesson-tip">
                      <span>💡</span>
                      <p>
                        <strong>Learning tip:</strong> Don't just read the
                        example. Type it yourself, experiment with it, and
                        explain the result in your own words.
                      </p>
                    </div>

                    <div className="lh-lesson-actions">
                      <button
                        type="button"
                        className={`lh-complete-button ${
                          completedSet.has(selectedLesson.id) ? "completed" : ""
                        }`}
                        onClick={() =>
                          toggleLessonComplete(selectedLesson.id)
                        }
                      >
                        {completedSet.has(selectedLesson.id)
                          ? "✓ Completed — mark incomplete"
                          : "✓ Mark lesson complete"}
                      </button>

                      <button
                        type="button"
                        className="lh-next-button"
                        onClick={startNextLesson}
                      >
                        Next lesson →
                      </button>
                    </div>

                    <div className="lh-course-resources">
                      <h4>Recommended references</h4>

                      {selectedCourse.resources.map((resource) => (
                        <a
                          key={resource.url}
                          href={resource.url}
                          target="_blank"
                          rel="noreferrer"
                        >
                          {resource.label} <span aria-hidden="true">↗</span>
                        </a>
                      ))}
                    </div>
                  </>
                ) : (
                  <p>Select a lesson to begin.</p>
                )}
              </div>
            </div>
          </section>
        </div>
      )}
    </div>
  );
}

export default LearningHub;