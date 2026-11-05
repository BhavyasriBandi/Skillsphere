import React, { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { useAuth } from "../auth/AuthContext";

import Toast from "./Toast";
import CareerGoal from "./CareerGoal";
import "./StudentDashboard.css";

import SkillAssessment from "./SkillAssessment";
import SkillAnalysis from "./SkillAnalysis";
import SkillGap from "./SkillGap";
import MyRoadmap from "./MyRoadmap";
import LearningHub from "./LearningHub";
import Challenges from "./Challenges";
import Projects from "./Projects";
import InterviewPrep from "./InterviewPrep";
import MyProgress from "./MyProgress";
import Achievements from "./Achievements";
import MyPortfolio from "./MyPortfolio";
import Notifications from "./Notifications";
import Settings from "./Settings";
import StudentProfile from "./StudentProfile";

// Sidebar menu groups
const menuGroups = [
  {
    title: "MY SPACE",
    items: [
      { label: "Dashboard", icon: "⌂" },
      { label: "Career Goal", icon: "◎" },
    ],
  },
  {
    title: "SKILL DEVELOPMENT",
    items: [
      { label: "Skill Assessment", icon: "✳" },
      { label: "Skill Analysis", icon: "◈" },
      { label: "Skill Gap", icon: "△" },
      { label: "My Roadmap", icon: "⇢" },
      { label: "Learning Hub", icon: "▤" },
      { label: "Challenges", icon: "⚡" },
    ],
  },
  {
    title: "CAREER GROWTH",
    items: [
      { label: "Projects", icon: "▣" },
      { label: "Interview Prep", icon: "▥" },
      { label: "My Progress", icon: "↗" },
      { label: "Achievements", icon: "♛" },
      { label: "My Portfolio", icon: "▧" },
    ],
  },
  {
    title: "ACCOUNT",
    items: [
      { label: "My Profile", icon: "◉" },
      { label: "Notifications", icon: "♧" },
      { label: "Settings", icon: "⚙" },
    ],
  },
];

const allMenuItems = menuGroups.flatMap((group) => group.items);

const studentRoutes = {
  Dashboard: "/student/dashboard",
  "My Profile": "/student/profile",
  "Career Goal": "/student/career-goal",
  "Skill Assessment": "/student/skill-assessment",
  "Skill Analysis": "/student/skill-analysis",
  "Skill Gap": "/student/skill-gap",
  "My Roadmap": "/student/roadmap",
  "Learning Hub": "/student/learning-hub",
  Challenges: "/student/challenges",
  Projects: "/student/projects",
  "Interview Prep": "/student/interview-prep",
  "My Progress": "/student/progress",
  Achievements: "/student/achievements",
  "My Portfolio": "/student/portfolio",
  Notifications: "/student/notifications",
  Settings: "/student/settings",
};

const studentRouteLabels = Object.fromEntries(
  Object.entries(studentRoutes).map(([label, path]) => [path, label])
);

function getStudentSectionFromPath(pathname) {
  return studentRouteLabels[pathname] || "Dashboard";
}

const initialTasks = [
  {
    id: 1,
    title: "Complete Python fundamentals",
    detail: "Learning Hub · 30 minutes",
    done: false,
  },
  {
    id: 2,
    title: "Practice five data structure problems",
    detail: "Challenges · 45 minutes",
    done: false,
  },
  {
    id: 3,
    title: "Update your career goal",
    detail: "Career Goal · 10 minutes",
    done: false,
  },
];

function getRegisteredEmail() {
  try {
    return (
      sessionStorage.getItem("skillsphere_email") ||
      localStorage.getItem("skillsphere_saved_email") ||
      localStorage.getItem("email") ||
      ""
    );
  } catch {
    return "";
  }
}

function getSavedProfile() {
  try {
    const savedProfile = localStorage.getItem(
      "skillsphere_student_profile"
    );

    if (savedProfile) {
      return JSON.parse(savedProfile);
    }
  } catch {
    // Use the default profile when saved data cannot be read.
  }

  return {
    fullName: "",
    email: getRegisteredEmail(),
    phone: "",
    college: "",
    qualification: "",
    branch: "",
    graduationYear: "",
    location: "",
    careerInterest: "",
    bio: "",
  };
}

// Get the current authenticated user's name.
function getAuthenticatedName(user) {
  if (!user || typeof user !== "object") return "";

  const source = user.user || user.profile || user;

  const firstName =
    source.first_name || source.firstName || "";

  const lastName =
    source.last_name || source.lastName || "";

  return (
    source.full_name ||
    source.fullName ||
    source.name ||
    [firstName, lastName].filter(Boolean).join(" ") ||
    source.username ||
    ""
  ).toString().trim();
}

// Get the current authenticated user's email.
function getAuthenticatedEmail(user) {
  if (!user || typeof user !== "object") return "";

  const source = user.user || user.profile || user;

  return (
    source.email ||
    source.user_email ||
    ""
  ).toString().trim();
}

function getInitials(name) {
  if (!name || !name.trim()) {
    return "S";
  }

  return name
    .trim()
    .split(/\s+/)
    .slice(0, 2)
    .map((part) => part.charAt(0).toUpperCase())
    .join("");
}

function StudentDashboard() {
  const navigate = useNavigate();

  const { logout, user: authUser } = useAuth();

  const location = useLocation();

  const [activeItem, setActiveItem] = useState(() =>
    getStudentSectionFromPath(location.pathname)
  );

  const [sidebarOpen, setSidebarOpen] = useState(false);

  const [showLogoutConfirm, setShowLogoutConfirm] =
    useState(false);

  const [profileName, setProfileName] = useState("");

  const [profileEmail, setProfileEmail] =
    useState(getRegisteredEmail);

  const [tasks, setTasks] = useState(() => {
    try {
      const savedTasks = localStorage.getItem(
        "skillsphere_student_tasks"
      );

      return savedTasks
        ? JSON.parse(savedTasks)
        : initialTasks;
    } catch {
      return initialTasks;
    }
  });

  // Update active sidebar item.
  useEffect(() => {
    setActiveItem(
      getStudentSectionFromPath(location.pathname)
    );
  }, [location.pathname]);

  // Sync the current authenticated student's profile.
  useEffect(() => {
    function syncProfile() {
      const authenticatedName =
        getAuthenticatedName(authUser);

      const authenticatedEmail =
        getAuthenticatedEmail(authUser);

      let saved = getSavedProfile();

      // Do not display another student's cached profile.
      const savedEmail = (saved.email || "")
        .trim()
        .toLowerCase();

      const currentEmail = authenticatedEmail
        .trim()
        .toLowerCase();

      if (
        !currentEmail ||
        !savedEmail ||
        savedEmail !== currentEmail
      ) {
        saved = {
          fullName: "",
          email: authenticatedEmail,
        };
      }

      setProfileName(
        authenticatedName || saved.fullName || ""
      );

      setProfileEmail(
        authenticatedEmail || saved.email || ""
      );
    }

    syncProfile();

    window.addEventListener("storage", syncProfile);

    return () => {
      window.removeEventListener("storage", syncProfile);
    };
  }, [authUser, activeItem]);

  const completedTasks = tasks.filter(
    (task) => task.done
  ).length;

  const initials = getInitials(profileName);

  // Sidebar navigation.
  function handleMenuClick(label) {
    if (label === "Logout") {
      setShowLogoutConfirm(true);
      setSidebarOpen(false);
      return;
    }

    const targetRoute = studentRoutes[label];

    if (targetRoute) {
      navigate(targetRoute);
    }

    setSidebarOpen(false);
  }

  // Logout confirmation.
  async function confirmLogout() {
    try {
      await logout();
    } finally {
      sessionStorage.removeItem("skillsphere_email");

      localStorage.removeItem("access");
      localStorage.removeItem("refresh");
      localStorage.removeItem("email");
      localStorage.removeItem("user");

      setShowLogoutConfirm(false);

      navigate("/login", { replace: true });
    }
  }

  // Update learning tasks.
  function toggleTask(id) {
    setTasks((currentTasks) => {
      const updatedTasks = currentTasks.map((task) =>
        task.id === id
          ? { ...task, done: !task.done }
          : task
      );

      try {
        localStorage.setItem(
          "skillsphere_student_tasks",
          JSON.stringify(updatedTasks)
        );
      } catch {
        // Tasks remain available during the current page session.
      }

      return updatedTasks;
    });
  }

  // Dashboard overview.
  function renderOverview() {
    return (
      <>
        <section className="student-welcome">
          <div className="welcome-copy">
            <span className="eyebrow">
              YOUR PERSONAL LEARNING SPACE
            </span>

            <h1>
              Shape your future, one skill at a time.
            </h1>

            <p>
              Every skill you build brings you closer to your career goals.
              Keep learning, keep growing.
            </p>

            <button
              type="button"
              className="primary-button"
              onClick={() =>
                handleMenuClick("Skill Assessment")
              }
            >
              Continue your journey <span>→</span>
            </button>
          </div>

          <div className="welcome-art" aria-hidden="true">
            <div className="art-orbit orbit-one" />
            <div className="art-orbit orbit-two" />
            <div className="art-center">S</div>
            <span className="art-bubble bubble-one">✦</span>
            <span className="art-bubble bubble-two">↗</span>
            <span className="art-bubble bubble-three">✓</span>
          </div>
        </section>

        <section className="student-stats">
          <article className="stat-card">
            <span className="stat-icon blue-icon">✳</span>
            <span className="stat-label">Skills assessed</span>
            <strong>08</strong>
            <span className="stat-note">
              Build your skill profile
            </span>
          </article>

          <article className="stat-card">
            <span className="stat-icon purple-icon">⇢</span>
            <span className="stat-label">Roadmap progress</span>
            <strong>35%</strong>
            <div className="progress-track">
              <span style={{ width: "35%" }} />
            </div>
          </article>

          <article className="stat-card">
            <span className="stat-icon green-icon">✓</span>
            <span className="stat-label">Tasks completed</span>
            <strong>
              {completedTasks}/{tasks.length}
            </strong>
            <span className="stat-note">
              Keep your momentum going
            </span>
          </article>

          <article className="stat-card">
            <span className="stat-icon orange-icon">♛</span>
            <span className="stat-label">Achievements</span>
            <strong>04</strong>
            <span className="stat-note">
              Celebrate your progress
            </span>
          </article>
        </section>

        <div className="student-content-grid">
          <section className="student-panel">
            <div className="panel-heading">
              <div>
                <span className="eyebrow">
                  YOUR NEXT STEPS
                </span>
                <h2>Learning tasks</h2>
              </div>

              <button
                type="button"
                className="text-button"
                onClick={() => handleMenuClick("Learning Hub")}
              >
                View all →
              </button>
            </div>

            <div className="task-list">
              {tasks.map((task) => (
                <label className="task-row" key={task.id}>
                  <input
                    type="checkbox"
                    checked={task.done}
                    onChange={() => toggleTask(task.id)}
                  />

                  <span className="task-copy">
                    <strong
                      className={task.done ? "task-done" : ""}
                    >
                      {task.title}
                    </strong>

                    <small>{task.detail}</small>
                  </span>

                  <span className="task-arrow">→</span>
                </label>
              ))}
            </div>

            <div className="task-footer">
              <span>
                {completedTasks} of {tasks.length} tasks completed
              </span>

              <span className="task-footer-progress">
                <span
                  style={{
                    width: `${
                      tasks.length
                        ? (completedTasks / tasks.length) * 100
                        : 0
                    }%`,
                  }}
                />
              </span>
            </div>
          </section>

          <section className="student-panel roadmap-panel">
            <div className="panel-heading">
              <div>
                <span className="eyebrow">
                  YOUR CAREER PATH
                </span>
                <h2>Learning roadmap</h2>
              </div>

              <button
                type="button"
                className="text-button"
                onClick={() => handleMenuClick("My Roadmap")}
              >
                Details →
              </button>
            </div>

            <div className="roadmap-steps">
              <div className="roadmap-step step-complete">
                <span className="roadmap-marker">✓</span>

                <div>
                  <strong>Discover your interests</strong>
                  <small>Understand your strengths</small>
                </div>

                <span className="roadmap-tag">Done</span>
              </div>

              <div className="roadmap-step step-current">
                <span className="roadmap-marker">2</span>

                <div>
                  <strong>Assess your skills</strong>
                  <small>Identify your current level</small>
                </div>

                <span className="roadmap-tag">Current</span>
              </div>

              <div className="roadmap-step">
                <span className="roadmap-marker">3</span>

                <div>
                  <strong>Close your skill gaps</strong>
                  <small>Follow a personalized plan</small>
                </div>
              </div>

              <div className="roadmap-step">
                <span className="roadmap-marker">4</span>

                <div>
                  <strong>Become career ready</strong>
                  <small>Build projects and prepare</small>
                </div>
              </div>
            </div>
          </section>
        </div>

        <section className="student-project-banner">
          <div>
            <span className="eyebrow">
              YOUR NEXT OPPORTUNITY
            </span>

            <h2>
              Turn your knowledge into real projects.
            </h2>

            <p>
              Build practical experience and showcase what you can do.
            </p>
          </div>

          <button
            type="button"
            className="primary-button"
            onClick={() => handleMenuClick("Projects")}
          >
            Explore projects →
          </button>
        </section>
      </>
    );
  }

  // Render selected dashboard section.
  function renderSection() {
    switch (activeItem) {
      case "Dashboard":
        return renderOverview();

      case "My Profile":
        return <StudentProfile />;

      case "Career Goal":
        return <CareerGoal />;

      case "Skill Assessment":
        return <SkillAssessment />;

      case "Skill Analysis":
        return <SkillAnalysis />;

      case "Skill Gap":
        return <SkillGap />;

      case "My Roadmap":
        return <MyRoadmap />;

      case "Learning Hub":
        return <LearningHub />;

      case "Challenges":
        return <Challenges />;

      case "Projects":
        return <Projects />;

      case "Interview Prep":
        return <InterviewPrep />;

      case "My Progress":
        return <MyProgress />;

      case "Achievements":
        return <Achievements />;

      case "My Portfolio":
        return <MyPortfolio />;

      case "Notifications":
        return <Notifications />;

      case "Settings":
        return <Settings />;

      default:
        return renderOverview();
    }
  }

  return (
    <div className="student-dashboard">
      {sidebarOpen && (
        <button
          type="button"
          className="sidebar-overlay"
          aria-label="Close navigation"
          onClick={() => setSidebarOpen(false)}
        />
      )}

      <aside
        className={`student-sidebar ${
          sidebarOpen ? "is-open" : ""
        }`}
      >
        <a
          className="student-brand"
          href="/student/dashboard"
          onClick={(event) => {
            event.preventDefault();
            handleMenuClick("Dashboard");
          }}
        >
          <span className="brand-symbol">S</span>

          <span className="brand-wordmark">
            <strong>SkillSphere</strong>
            <small>KNOW · GROW · ACHIEVE</small>
          </span>
        </a>

        <div className="sidebar-workspace">
          <span className="workspace-dot" />
          <span>STUDENT WORKSPACE</span>
        </div>

        <nav
          className="student-sidebar-nav"
          aria-label="Student navigation"
        >
          {menuGroups.map((group) => (
            <div
              className="student-nav-group"
              key={group.title}
            >
              <h3 className="student-nav-heading">
                {group.title}
              </h3>

              {group.items.map((item) => (
                <button
                  type="button"
                  key={item.label}
                  className={`student-nav-link ${
                    activeItem === item.label ? "active" : ""
                  }`}
                  onClick={() => handleMenuClick(item.label)}
                  aria-current={
                    activeItem === item.label
                      ? "page"
                      : undefined
                  }
                >
                  <span
                    className="student-nav-icon"
                    aria-hidden="true"
                  >
                    {item.icon}
                  </span>

                  <span className="student-nav-label">
                    {item.label}
                  </span>

                  {activeItem === item.label && (
                    <span className="active-indicator" />
                  )}
                </button>
              ))}
            </div>
          ))}
        </nav>

        <div className="sidebar-help-card">
          <span className="help-sparkle">✦</span>
          <strong>Keep growing!</strong>

          <p>
            Small steps today create big opportunities tomorrow.
          </p>

          <button
            type="button"
            onClick={() => handleMenuClick("My Roadmap")}
          >
            View my roadmap →
          </button>
        </div>

        <div className="sidebar-profile">
          <div className="profile-avatar">{initials}</div>

          <div className="profile-details">
            <strong>{profileName || "Student"}</strong>
            <small>
              {profileEmail || "Student account"}
            </small>
          </div>

          <button
            className="profile-menu-button"
            type="button"
            aria-label="Open settings"
            onClick={() => handleMenuClick("Settings")}
          >
            ⋯
          </button>
        </div>

        <button
          type="button"
          className="student-nav-link logout-link"
          onClick={() => handleMenuClick("Logout")}
        >
          <span className="student-nav-icon" aria-hidden="true">
            ↪
          </span>

          <span className="student-nav-label">
            Logout
          </span>
        </button>
      </aside>

      <main className="student-main">
        <header className="student-topbar">
          <div className="topbar-left">
            <button
              className="mobile-menu-button"
              type="button"
              aria-label="Open navigation menu"
              onClick={() => setSidebarOpen(true)}
            >
              ☰
            </button>

            <div>
              <span className="topbar-breadcrumb">
                Student workspace
              </span>

              <span className="breadcrumb-divider">/</span>

              <strong>{activeItem}</strong>
            </div>
          </div>

          <div className="topbar-actions">
            <span className="topbar-status">
              <span /> Your growth journey
            </span>

            <button
              type="button"
              className="notification-button"
              aria-label="View notifications"
              onClick={() => handleMenuClick("Notifications")}
            >
              ♧
              <span className="notification-dot" />
            </button>

            <button
              type="button"
              className="topbar-avatar"
              aria-label="View profile"
              onClick={() => handleMenuClick("My Profile")}
            >
              {initials}
            </button>
          </div>
        </header>

        <div className="student-page-content">
          {activeItem === "Dashboard" && (
            <div className="page-intro">
              <div>
                <span className="eyebrow">
                  YOUR JOURNEY, YOUR FUTURE
                </span>

                <h1>
                  Welcome back, {profileName || "Student"}{" "}
                  <span>✦</span>
                </h1>

                <p>
                  Here's a look at your learning journey today.
                </p>
              </div>

              <span className="today-label">
                LEARN SOMETHING NEW TODAY
              </span>
            </div>
          )}

          {renderSection()}

          <footer className="student-footer">
            <span>
              © {new Date().getFullYear()} SkillSphere
            </span>

            <span>
              Know Your Skills. Shape Your Future.
            </span>
          </footer>
        </div>
      </main>

      {showLogoutConfirm && (
        <div
          className="logout-modal-overlay"
          onClick={() => setShowLogoutConfirm(false)}
        >
          <div
            className="logout-modal"
            role="dialog"
            aria-modal="true"
            aria-labelledby="logout-modal-title"
            onClick={(event) => event.stopPropagation()}
          >
            <div
              className="logout-modal-icon"
              aria-hidden="true"
            >
              ↪
            </div>

            <h2 id="logout-modal-title">
              Log out?
            </h2>

            <p>
              Are you sure you want to log out of SkillSphere?
            </p>

            <div className="logout-modal-actions">
              <button
                type="button"
                className="logout-cancel-button"
                onClick={() => setShowLogoutConfirm(false)}
              >
                Cancel
              </button>

              <button
                type="button"
                className="logout-confirm-button"
                onClick={confirmLogout}
              >
                Log out
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default StudentDashboard;