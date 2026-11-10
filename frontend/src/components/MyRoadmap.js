import React, { useEffect, useMemo, useState } from "react";
import { apiFetch } from "../auth/AuthContext";
import Toast from "./Toast";
import "./MyRoadmap.css";

const GOAL_KEY = "skillsphere_student_career_goal";
const GAP_KEY = "skillsphere_student_skill_gap";
const ROADMAP_KEY = "skillsphere_student_roadmap_progress";
const ROADMAP_API_URL =
  "https://skillsphere-u93o.onrender.com/api/careers/roadmap-progress/";

const CAREER_PLANS = {
  "Full Stack Developer": [
    {
      phase: "Phase 1",
      title: "Build your foundations",
      duration: "Week 1–2",
      description: "Learn the essential building blocks of web development.",
      skills: ["HTML & CSS", "JavaScript"],
      tasks: [
        "Learn HTML structure, forms, and semantic elements",
        "Practise CSS layouts, Flexbox, and responsive design",
        "Understand JavaScript variables, functions, and arrays",
        "Build a responsive personal webpage",
      ],
    },
    {
      phase: "Phase 2",
      title: "Master frontend development",
      duration: "Week 3–4",
      description: "Create interactive user interfaces using React.",
      skills: ["React.js"],
      tasks: [
        "Learn components, props, and state",
        "Practise hooks and event handling",
        "Build forms with validation",
        "Create a small React dashboard",
      ],
    },
    {
      phase: "Phase 3",
      title: "Develop backend skills",
      duration: "Week 5–6",
      description: "Build application logic and connect APIs.",
      skills: ["Python", "Django / REST APIs"],
      tasks: [
        "Practise Python functions, collections, and classes",
        "Understand Django models, views, and serializers",
        "Create REST API endpoints",
        "Test API requests and validation",
      ],
    },
    {
      phase: "Phase 4",
      title: "Work with databases",
      duration: "Week 7",
      description: "Store, query, and manage application data.",
      skills: ["SQL & Databases"],
      tasks: [
        "Practise SELECT, INSERT, UPDATE, and DELETE",
        "Understand primary and foreign keys",
        "Connect your application to a database",
        "Practise joins and filtering",
      ],
    },
    {
      phase: "Phase 5",
      title: "Build and publish a project",
      duration: "Week 8",
      description: "Combine your knowledge in a complete application.",
      skills: ["Git & GitHub", "Testing & Debugging"],
      tasks: [
        "Use Git to track project changes",
        "Test forms and API endpoints",
        "Fix errors and validate edge cases",
        "Document and demonstrate your finished project",
      ],
    },
  ],

  "Python Developer": [
    {
      phase: "Phase 1",
      title: "Python fundamentals",
      duration: "Week 1–2",
      description: "Develop confidence with core Python programming.",
      skills: ["Python"],
      tasks: [
        "Practise variables, conditions, and loops",
        "Write functions and use modules",
        "Work with lists, tuples, sets, and dictionaries",
        "Build a command-line mini project",
      ],
    },
    {
      phase: "Phase 2",
      title: "Problem-solving and OOP",
      duration: "Week 3–4",
      description: "Strengthen programming logic and code organization.",
      skills: ["Data Structures", "Object-Oriented Programming"],
      tasks: [
        "Practise strings, lists, stacks, and queues",
        "Solve beginner coding problems",
        "Learn classes, inheritance, and encapsulation",
        "Build a small object-oriented application",
      ],
    },
    {
      phase: "Phase 3",
      title: "Backend development",
      duration: "Week 5–6",
      description: "Create APIs and server-side functionality.",
      skills: ["Django / REST APIs"],
      tasks: [
        "Learn Django project and app structure",
        "Create models, serializers, and API views",
        "Implement validation and authentication",
        "Test endpoints with Postman",
      ],
    },
    {
      phase: "Phase 4",
      title: "Database and tools",
      duration: "Week 7",
      description: "Store application data and manage your code.",
      skills: ["SQL & Databases", "Git & GitHub"],
      tasks: [
        "Practise SQL queries and joins",
        "Connect Django to a database",
        "Practise Git commits and branches",
        "Push your project to GitHub",
      ],
    },
    {
      phase: "Phase 5",
      title: "Test and demonstrate",
      duration: "Week 8",
      description: "Prepare a reliable project for your portfolio.",
      skills: ["Testing & Debugging"],
      tasks: [
        "Write tests for important application behavior",
        "Debug common exceptions",
        "Add clear project documentation",
        "Complete and demonstrate a Python project",
      ],
    },
  ],

  "Java Developer": [
    {
      phase: "Phase 1",
      title: "Java fundamentals",
      duration: "Week 1–2",
      description: "Learn Java syntax and core programming concepts.",
      skills: ["Java"],
      tasks: [
        "Practise variables, data types, and operators",
        "Write conditional statements and loops",
        "Create methods and work with arrays",
        "Build a console-based mini project",
      ],
    },
    {
      phase: "Phase 2",
      title: "Object-oriented programming",
      duration: "Week 3–4",
      description: "Structure Java programs using reusable classes.",
      skills: ["Object-Oriented Programming"],
      tasks: [
        "Learn classes, objects, and constructors",
        "Practise inheritance and polymorphism",
        "Understand interfaces and abstraction",
        "Build a simple object-oriented application",
      ],
    },
    {
      phase: "Phase 3",
      title: "Data structures",
      duration: "Week 5",
      description: "Improve coding logic and problem-solving.",
      skills: ["Data Structures"],
      tasks: [
        "Practise arrays and strings",
        "Learn lists, stacks, and queues",
        "Understand searching and sorting",
        "Solve coding exercises",
      ],
    },
    {
      phase: "Phase 4",
      title: "APIs and databases",
      duration: "Week 6–7",
      description: "Connect Java applications to external services and data.",
      skills: ["SQL & Databases", "REST APIs"],
      tasks: [
        "Practise SQL queries and joins",
        "Understand database connectivity concepts",
        "Learn HTTP methods and API responses",
        "Build a small database-backed application",
      ],
    },
    {
      phase: "Phase 5",
      title: "Quality and version control",
      duration: "Week 8",
      description: "Test your application and present your work.",
      skills: ["Git & GitHub", "Testing & Debugging"],
      tasks: [
        "Practise Git commits and branches",
        "Test important methods and inputs",
        "Debug exceptions",
        "Document and publish your project",
      ],
    },
  ],

  "Data Analyst": [
    {
      phase: "Phase 1",
      title: "Understand data",
      duration: "Week 1–2",
      description: "Build a foundation in spreadsheets and statistics.",
      skills: ["Excel", "Statistics"],
      tasks: [
        "Practise spreadsheet formulas and functions",
        "Learn sorting, filtering, and pivot tables",
        "Understand mean, median, and distributions",
        "Explore a small sample dataset",
      ],
    },
    {
      phase: "Phase 2",
      title: "Query databases",
      duration: "Week 3–4",
      description: "Retrieve and organize information with SQL.",
      skills: ["SQL & Databases"],
      tasks: [
        "Practise SELECT, WHERE, and ORDER BY",
        "Learn aggregation and GROUP BY",
        "Practise joins and subqueries",
        "Answer questions using a sample database",
      ],
    },
    {
      phase: "Phase 3",
      title: "Analyse with Python",
      duration: "Week 5–6",
      description: "Clean datasets and identify useful patterns.",
      skills: ["Python", "Data Cleaning"],
      tasks: [
        "Practise Python data structures and functions",
        "Explore data using pandas",
        "Handle missing values and duplicates",
        "Summarize patterns in a dataset",
      ],
    },
    {
      phase: "Phase 4",
      title: "Communicate insights",
      duration: "Week 7",
      description: "Present findings through clear visualizations.",
      skills: ["Data Visualization", "Power BI / Tableau"],
      tasks: [
        "Choose appropriate charts for different questions",
        "Build a simple interactive dashboard",
        "Write a concise findings summary",
        "Explain trends and limitations",
      ],
    },
    {
      phase: "Phase 5",
      title: "Complete an analysis project",
      duration: "Week 8",
      description: "Show your complete data analysis workflow.",
      skills: [],
      tasks: [
        "Choose a dataset and define a question",
        "Clean and analyse the data",
        "Create charts and a dashboard",
        "Document conclusions and recommendations",
      ],
    },
  ],

  "AI / Machine Learning Engineer": [
    {
      phase: "Phase 1",
      title: "Programming foundations",
      duration: "Week 1–2",
      description: "Prepare to work with data and algorithms.",
      skills: ["Python", "Data Structures"],
      tasks: [
        "Practise Python functions and collections",
        "Solve basic algorithm exercises",
        "Learn NumPy array operations",
        "Write reusable data-processing functions",
      ],
    },
    {
      phase: "Phase 2",
      title: "Mathematics for data",
      duration: "Week 3–4",
      description: "Understand the mathematical ideas behind models.",
      skills: ["Statistics & Probability", "Linear Algebra"],
      tasks: [
        "Learn averages, variance, and probability",
        "Practise vectors and matrices",
        "Understand correlation and distributions",
        "Explore a dataset with descriptive statistics",
      ],
    },
    {
      phase: "Phase 3",
      title: "Prepare datasets",
      duration: "Week 5",
      description: "Clean and transform data for analysis.",
      skills: ["Data Processing"],
      tasks: [
        "Load data with pandas",
        "Handle missing values and duplicates",
        "Explore features and target variables",
        "Separate training and test data",
      ],
    },
    {
      phase: "Phase 4",
      title: "Machine learning fundamentals",
      duration: "Week 6–7",
      description: "Train and evaluate introductory machine learning models.",
      skills: ["Machine Learning Fundamentals", "Model Evaluation"],
      tasks: [
        "Understand supervised and unsupervised learning",
        "Train a simple classification or regression model",
        "Compare predictions with actual values",
        "Learn appropriate evaluation metrics",
      ],
    },
    {
      phase: "Phase 5",
      title: "Build a demonstrable project",
      duration: "Week 8",
      description: "Document your experiment and make results reproducible.",
      skills: ["Git & GitHub"],
      tasks: [
        "Choose a suitable dataset",
        "Create a reproducible notebook or script",
        "Record model limitations",
        "Publish code and a project README",
      ],
    },
  ],

  "Frontend Developer": [
    {
      phase: "Phase 1",
      title: "Web foundations",
      duration: "Week 1–2",
      description: "Create accessible, structured web pages.",
      skills: ["HTML & CSS"],
      tasks: [
        "Practise semantic HTML",
        "Build layouts using Flexbox and Grid",
        "Create responsive pages",
        "Use accessible labels and navigation",
      ],
    },
    {
      phase: "Phase 2",
      title: "JavaScript essentials",
      duration: "Week 3–4",
      description: "Make interfaces interactive and dynamic.",
      skills: ["JavaScript"],
      tasks: [
        "Practise variables, arrays, and objects",
        "Write functions and event handlers",
        "Understand asynchronous requests",
        "Build an interactive mini application",
      ],
    },
    {
      phase: "Phase 3",
      title: "Responsive user experiences",
      duration: "Week 5",
      description: "Improve usability across screen sizes.",
      skills: ["Responsive Design", "Accessibility"],
      tasks: [
        "Test layouts on mobile and desktop sizes",
        "Use keyboard-friendly interactions",
        "Improve color contrast and form labels",
        "Review loading and empty states",
      ],
    },
    {
      phase: "Phase 4",
      title: "Build with React",
      duration: "Week 6–7",
      description: "Create reusable components and interactive pages.",
      skills: ["React.js"],
      tasks: [
        "Practise components, props, and state",
        "Use hooks and controlled forms",
        "Fetch and display API data",
        "Build a multi-page interface",
      ],
    },
    {
      phase: "Phase 5",
      title: "Polish and publish",
      duration: "Week 8",
      description: "Test and present your frontend project.",
      skills: ["Git & GitHub", "Testing & Debugging"],
      tasks: [
        "Use Git to track changes",
        "Test interactions and responsive layouts",
        "Fix console errors",
        "Document and publish the project",
      ],
    },
  ],

  "Backend Developer": [
    {
      phase: "Phase 1",
      title: "Programming foundations",
      duration: "Week 1–2",
      description: "Strengthen programming and problem-solving skills.",
      skills: ["Python", "Data Structures"],
      tasks: [
        "Practise functions and core Python collections",
        "Solve basic algorithm exercises",
        "Understand time complexity at a basic level",
        "Build a command-line application",
      ],
    },
    {
      phase: "Phase 2",
      title: "Backend APIs",
      duration: "Week 3–4",
      description: "Build server-side application logic.",
      skills: ["Django / REST APIs"],
      tasks: [
        "Learn Django models, views, and serializers",
        "Build REST endpoints",
        "Validate request data",
        "Test API responses with Postman",
      ],
    },
    {
      phase: "Phase 3",
      title: "Databases",
      duration: "Week 5",
      description: "Design and query structured application data.",
      skills: ["SQL & Databases"],
      tasks: [
        "Practise SQL queries and joins",
        "Understand relationships and constraints",
        "Create and run migrations",
        "Test database-backed endpoints",
      ],
    },
    {
      phase: "Phase 4",
      title: "Security and reliability",
      duration: "Week 6–7",
      description: "Protect endpoints and handle failures gracefully.",
      skills: ["Authentication & Security", "Testing & Debugging"],
      tasks: [
        "Understand authentication and authorization",
        "Protect endpoints using permissions",
        "Validate input and handle errors",
        "Test successful and unsuccessful requests",
      ],
    },
    {
      phase: "Phase 5",
      title: "Version control and delivery",
      duration: "Week 8",
      description: "Package your backend project for demonstration.",
      skills: ["Git & GitHub"],
      tasks: [
        "Use Git commits and branches",
        "Document API endpoints",
        "Prepare setup instructions",
        "Publish your code repository",
      ],
    },
  ],
};

function readJSON(key, fallback) {
  try {
    const value = localStorage.getItem(key);
    return value ? JSON.parse(value) : fallback;
  } catch {
    return fallback;
  }
}

function getCareerName(goal) {
  if (!goal || typeof goal !== "object") return "";

  const values = [
    goal.role,
    goal.career,
    goal.careerGoal,
    goal.targetRole,
    goal.targetCareer,
    goal.goal,
    goal.title,
  ];

  const aliases = {
    "full stack": "Full Stack Developer",
    "full-stack developer": "Full Stack Developer",
    "fullstack developer": "Full Stack Developer",
    python: "Python Developer",
    "python development": "Python Developer",
    java: "Java Developer",
    "java development": "Java Developer",
    "data analysis": "Data Analyst",
    "data analytics": "Data Analyst",
    frontend: "Frontend Developer",
    "front-end developer": "Frontend Developer",
    backend: "Backend Developer",
    "back-end developer": "Backend Developer",
    "ai engineer": "AI / Machine Learning Engineer",
    "machine learning engineer": "AI / Machine Learning Engineer",
  };

  for (const value of values) {
    if (typeof value !== "string") continue;

    const normalized = value.trim().toLowerCase();

    if (aliases[normalized]) return aliases[normalized];

    const exact = Object.keys(CAREER_PLANS).find(
      (careerName) => careerName.toLowerCase() === normalized
    );

    if (exact) return exact;
  }

  return "";
}

function getStepId(career, phaseIndex) {
  return `${career}::${phaseIndex}`;
}

function MyRoadmap() {
  const [career, setCareer] = useState("Full Stack Developer");
  const [completedTasks, setCompletedTasks] = useState({});
  const [expandedPhases, setExpandedPhases] = useState({ 0: true });
  const [toast, setToast] = useState({
    message: "",
    type: "success",
  });

  function showToast(message, type = "success") {
    setToast({ message, type });
  }

  function closeToast() {
    setToast({ message: "", type: "success" });
  }

  useEffect(() => {
    if (!toast.message) return undefined;

    const timer = window.setTimeout(() => {
      setToast({ message: "", type: "success" });
    }, 3500);

    return () => window.clearTimeout(timer);
  }, [toast.message, toast.type]);

  useEffect(() => {
    let isMounted = true;

    async function loadRoadmapProgress() {
      const goal = readJSON(GOAL_KEY, {});
      const savedCareer = getCareerName(goal);

      if (savedCareer && isMounted) {
        setCareer(savedCareer);
      }

      const localProgress = readJSON(ROADMAP_KEY, {});

      if (
        localProgress &&
        typeof localProgress === "object" &&
        !Array.isArray(localProgress) &&
        isMounted
      ) {
        setCompletedTasks(localProgress);
      }

      try {
        const response = await apiFetch(ROADMAP_API_URL, {
          method: "GET",
          headers: { "Content-Type": "application/json" },
        });

        if (!response.ok) {
          const detail = await response.text();
          throw new Error(
            `Could not load roadmap progress (${response.status}). ${detail}`
          );
        }

        const records = await response.json();
        const mergedProgress = { ...(localProgress || {}) };

        records.forEach((record) => {
          if (record && typeof record.task_id === "string") {
            mergedProgress[record.task_id] = Boolean(record.is_completed);
          }
        });

        if (isMounted) {
          setCompletedTasks(mergedProgress);
          localStorage.setItem(
            ROADMAP_KEY,
            JSON.stringify(mergedProgress)
          );
        }
      } catch (error) {
        console.error("Roadmap progress load error:", error);

        if (isMounted) {
          showToast(
            "Could not sync with Django. Showing saved browser progress.",
            "error"
          );
        }
      }
    }

    loadRoadmapProgress();

    return () => {
      isMounted = false;
    };
  }, []);

  const phases =
    CAREER_PLANS[career] || CAREER_PLANS["Full Stack Developer"];

  const allTasks = phases.flatMap((phase, phaseIndex) =>
    phase.tasks.map((task, taskIndex) => ({
      id: `${getStepId(career, phaseIndex)}::${taskIndex}`,
      phaseIndex,
      taskIndex,
      task,
    }))
  );

  const completedCount = allTasks.filter(
    (task) => Boolean(completedTasks[task.id])
  ).length;

  const totalTasks = allTasks.length;

  const progress = totalTasks
    ? Math.round((completedCount / totalTasks) * 100)
    : 0;

  const phaseProgress = useMemo(
    () =>
      phases.map((phase, phaseIndex) => {
        const tasks = phase.tasks.map(
          (_, taskIndex) =>
            `${getStepId(career, phaseIndex)}::${taskIndex}`
        );

        const completed = tasks.filter(
          (taskId) => completedTasks[taskId]
        ).length;

        return {
          total: tasks.length,
          completed,
          percentage: tasks.length
            ? Math.round((completed / tasks.length) * 100)
            : 0,
        };
      }),
    [career, phases, completedTasks]
  );

  const nextTask = allTasks.find(
    (task) => !completedTasks[task.id]
  );

  async function toggleTask(taskId) {
    const taskDetails = allTasks.find(
      (item) => item.id === taskId
    );

    if (!taskDetails) return;

    const wasCompleted = Boolean(completedTasks[taskId]);
    const nextCompleted = !wasCompleted;
    const previousProgress = completedTasks;

    const updated = {
      ...completedTasks,
      [taskId]: nextCompleted,
    };

    setCompletedTasks(updated);
    localStorage.setItem(ROADMAP_KEY, JSON.stringify(updated));

    try {
      const response = await apiFetch(ROADMAP_API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          career,
          task_id: taskId,
          task_name: taskDetails.task,
          is_completed: nextCompleted,
        }),
      });

      if (!response.ok) {
        const detail = await response.text();
        throw new Error(
          `Save failed (${response.status}). ${detail}`
        );
      }

      const savedRecord = await response.json();

      const confirmedProgress = {
        ...updated,
        [savedRecord.task_id]: Boolean(savedRecord.is_completed),
      };

      setCompletedTasks(confirmedProgress);
      localStorage.setItem(
        ROADMAP_KEY,
        JSON.stringify(confirmedProgress)
      );

      showToast(
        nextCompleted
          ? "Task completed and saved to Django."
          : "Task marked incomplete and saved to Django.",
        "success"
      );
    } catch (error) {
      console.error("Roadmap task save error:", error);

      setCompletedTasks(previousProgress);
      localStorage.setItem(
        ROADMAP_KEY,
        JSON.stringify(previousProgress)
      );

      showToast(
        "Could not save this task to Django. Please check your login and try again.",
        "error"
      );
    }
  }

  function togglePhase(index) {
    setExpandedPhases((current) => ({
      ...current,
      [index]: !current[index],
    }));
  }

  async function resetRoadmap() {
    try {
      const response = await apiFetch(
        `${ROADMAP_API_URL}?career=${encodeURIComponent(career)}`,
        {
          method: "DELETE",
          headers: { "Content-Type": "application/json" },
        }
      );

      if (!response.ok) {
        const detail = await response.text();
        throw new Error(
          `Reset failed (${response.status}). ${detail}`
        );
      }

      const updated = { ...completedTasks };

      allTasks.forEach((task) => {
        delete updated[task.id];
      });

      setCompletedTasks(updated);
      localStorage.setItem(ROADMAP_KEY, JSON.stringify(updated));
      setExpandedPhases({ 0: true });

      showToast(
        "Progress for this roadmap has been reset in Django.",
        "info"
      );
    } catch (error) {
      console.error("Roadmap reset error:", error);

      showToast(
        "Could not reset progress in Django. Please check your login and try again.",
        "error"
      );
    }
  }

  function changeCareer(event) {
    const nextCareer = event.target.value;

    setCareer(nextCareer);
    setExpandedPhases({ 0: true });

    showToast(
      `Switched to the ${nextCareer} roadmap.`,
      "info"
    );
  }

  return (
    <div className="my-roadmap-page">
      <Toast
        message={toast.message}
        type={toast.type}
        onClose={closeToast}
      />

      <header className="roadmap-header">
        <div>
          <span className="roadmap-eyebrow">
            YOUR GOALS · YOUR JOURNEY · YOUR FUTURE
          </span>
          <h1>My Roadmap</h1>
          <p>
            Turn your career ambition into manageable steps. Learn, practise,
            and track your progress one task at a time.
          </p>
        </div>

        <div className="roadmap-header-art" aria-hidden="true">
          <span className="roadmap-art-path">↗</span>
          <span className="roadmap-art-dot" />
        </div>
      </header>

      <section className="roadmap-career-card">
        <div className="roadmap-career-content">
          <span className="roadmap-label">
            YOUR LEARNING DESTINATION
          </span>
          <h2>{career}</h2>
          <p>
            Follow the phases below at your own pace. Your completed tasks sync
            with your Django account.
          </p>
        </div>

        <div className="roadmap-career-controls">
          <label htmlFor="roadmap-career-select">
            Target career
          </label>
          <select
            id="roadmap-career-select"
            value={career}
            onChange={changeCareer}
          >
            {Object.keys(CAREER_PLANS).map((name) => (
              <option key={name} value={name}>
                {name}
              </option>
            ))}
          </select>
        </div>
      </section>

      <section className="roadmap-overview-grid">
        <article className="roadmap-overview-card">
          <span className="roadmap-stat-icon blue">↗</span>
          <div>
            <span>Overall progress</span>
            <strong>{progress}%</strong>
          </div>
        </article>

        <article className="roadmap-overview-card">
          <span className="roadmap-stat-icon green">✓</span>
          <div>
            <span>Tasks completed</span>
            <strong>
              {completedCount}
              <small> / {totalTasks}</small>
            </strong>
          </div>
        </article>

        <article className="roadmap-overview-card">
          <span className="roadmap-stat-icon purple">▤</span>
          <div>
            <span>Learning phases</span>
            <strong>{phases.length}</strong>
          </div>
        </article>
      </section>

      <section className="roadmap-main-panel">
        <div className="roadmap-panel-heading">
          <div>
            <h2>Your learning journey</h2>
            <p>
              Complete each task to move towards your career goal.
            </p>
          </div>

          <button
            type="button"
            className="roadmap-reset-button"
            onClick={resetRoadmap}
            disabled={completedCount === 0}
          >
            Reset progress
          </button>
        </div>

        <div className="roadmap-overall-progress">
          <div className="roadmap-overall-progress-label">
            <span>Journey completion</span>
            <strong>
              {completedCount} of {totalTasks} tasks
            </strong>
          </div>

          <div
            className="roadmap-progress-track"
            role="progressbar"
            aria-label="Overall roadmap progress"
            aria-valuemin={0}
            aria-valuemax={100}
            aria-valuenow={progress}
          >
            <div
              className="roadmap-progress-fill"
              style={{ width: `${progress}%` }}
            />
          </div>
        </div>

        {nextTask && (
          <div className="roadmap-next-task">
            <span className="roadmap-next-task-icon">→</span>
            <div>
              <span>NEXT TASK TO COMPLETE</span>
              <strong>{nextTask.task}</strong>
              <small>
                {phases[nextTask.phaseIndex].title}
              </small>
            </div>
          </div>
        )}

        {!nextTask && (
          <div className="roadmap-finished-banner">
            <span>✓</span>
            <div>
              <strong>
                You've completed every roadmap task!
              </strong>
              <p>
                Review your projects and continue building practical
                experience.
              </p>
            </div>
          </div>
        )}

        <div className="roadmap-timeline">
          {phases.map((phase, phaseIndex) => {
            const phaseId = getStepId(career, phaseIndex);
            const isExpanded = Boolean(expandedPhases[phaseIndex]);
            const stats = phaseProgress[phaseIndex];
            const isComplete =
              stats.total > 0 && stats.completed === stats.total;

            return (
              <article
                className={`roadmap-phase ${
                  isComplete ? "phase-complete" : ""
                }`}
                key={phaseId}
              >
                <div className="roadmap-timeline-marker">
                  <span>
                    {isComplete ? "✓" : phaseIndex + 1}
                  </span>
                </div>

                <div className="roadmap-phase-card">
                  <button
                    type="button"
                    className="roadmap-phase-toggle"
                    onClick={() => togglePhase(phaseIndex)}
                    aria-expanded={isExpanded}
                  >
                    <div className="roadmap-phase-heading">
                      <span className="roadmap-phase-label">
                        {phase.phase}
                      </span>
                      <span className="roadmap-duration">
                        {phase.duration}
                      </span>
                    </div>

                    <div className="roadmap-phase-title-row">
                      <div>
                        <h3>{phase.title}</h3>
                        <p>{phase.description}</p>
                      </div>

                      <span className="roadmap-expand-icon">
                        {isExpanded ? "−" : "+"}
                      </span>
                    </div>

                    <div className="roadmap-phase-progress-row">
                      <div className="roadmap-phase-progress-track">
                        <div
                          className="roadmap-phase-progress-fill"
                          style={{
                            width: `${stats.percentage}%`,
                          }}
                        />
                      </div>
                      <span>
                        {stats.completed}/{stats.total} tasks
                      </span>
                    </div>
                  </button>

                  {isExpanded && (
                    <div className="roadmap-phase-details">
                      {phase.skills.length > 0 && (
                        <div className="roadmap-skills">
                          <span className="roadmap-detail-label">
                            SKILLS IN THIS PHASE
                          </span>
                          <div className="roadmap-skill-chips">
                            {phase.skills.map((skill) => (
                              <span key={skill}>{skill}</span>
                            ))}
                          </div>
                        </div>
                      )}

                      <div className="roadmap-tasks">
                        <span className="roadmap-detail-label">
                          TASK CHECKLIST
                        </span>

                        {phase.tasks.map((task, taskIndex) => {
                          const taskId = `${phaseId}::${taskIndex}`;
                          const isChecked = Boolean(
                            completedTasks[taskId]
                          );

                          return (
                            <label
                              key={taskId}
                              className={`roadmap-task ${
                                isChecked ? "task-completed" : ""
                              }`}
                            >
                              <input
                                type="checkbox"
                                checked={isChecked}
                                onChange={() => toggleTask(taskId)}
                              />
                              <span className="roadmap-custom-checkbox">
                                {isChecked ? "✓" : ""}
                              </span>
                              <span className="roadmap-task-text">
                                {task}
                              </span>
                            </label>
                          );
                        })}
                      </div>
                    </div>
                  )}
                </div>
              </article>
            );
          })}
        </div>
      </section>

      <footer className="roadmap-footer">
        <span>i</span>
        This is a suggested eight-week learning structure, not a deadline.
        Adjust the pace to your schedule. Task completion is saved to your
        authenticated Django account, with browser storage used as a fallback.
      </footer>
    </div>
  );
}

export default MyRoadmap;