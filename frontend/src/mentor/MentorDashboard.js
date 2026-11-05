
import React, { useState, useEffect, useCallback } from "react";
import { useNavigate, useLocation } from "react-router-dom";

import "./MentorDashboard.css";

import MentorProfile from "./MentorProfile";
import MyStudents from "./MyStudents";
import StudentProgress from "./StudentProgress";
import Assessments from "./Assessments";
import SkillAnalysis from "./SkillAnalysis";
import SkillGaps from "./SkillGap";
import Roadmaps from "./Roadmaps";
import LearningResources from "./LearningResources";
import MentorProjects from "./MentorProjects";
import MentorInterviewPrep from "./MentorInterviewPrep";
import FeedbackMessages from "./FeedbackMessages";
import MentorNotifications from "./MentorNotifications";
import MentorSettings from "./MentorSettings";

const API_BASE_URL = "http://127.0.0.1:8000";

// =====================================================
// MENTOR SIDEBAR MENU
// =====================================================

const menuItems = [
  "Dashboard",
  "My Profile",
  "My Students",
  "Student Progress",
  "Assessments",
  "Skill Analysis",
  "Skill Gaps",
  "Roadmaps",
  "Learning Resources",
  "Projects",
  "Interview Prep",
  "Feedback / Messages",
  "Notifications",
  "Settings",
  "Logout",
];

// =====================================================
// MENTOR ROUTES
// =====================================================

const mentorRoutes = {
  Dashboard: "/mentor/dashboard",
  "My Profile": "/mentor/profile",
  "My Students": "/mentor/students",
  "Student Progress": "/mentor/student-progress",
  Assessments: "/mentor/assessments",
  "Skill Analysis": "/mentor/skill-analysis",
  "Skill Gaps": "/mentor/skill-gaps",
  Roadmaps: "/mentor/roadmaps",
  "Learning Resources": "/mentor/resources",
  Projects: "/mentor/projects",
  "Interview Prep": "/mentor/interview-prep",
  "Feedback / Messages": "/mentor/messages",
  Notifications: "/mentor/notifications",
  Settings: "/mentor/settings",
};

const routeMenus = Object.fromEntries(
  Object.entries(mentorRoutes).map(([menu, path]) => [
    path,
    menu,
  ])
);

// =====================================================
// MENTOR DASHBOARD COMPONENT
// =====================================================

function MentorDashboard() {
  const navigate = useNavigate();
  const location = useLocation();

  const activeMenu =
    routeMenus[location.pathname] || "Dashboard";

  // ===================================================
  // STATES
  // ===================================================

  const [search, setSearch] = useState("");
  const [dashboardData, setDashboardData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  // Logout confirmation state
  const [showLogoutModal, setShowLogoutModal] = useState(false);

  // ===================================================
  // FETCH MENTOR DASHBOARD
  // ===================================================

  const fetchMentorDashboard = useCallback(async () => {
    try {
      setLoading(true);
      setError("");

      const token = localStorage.getItem(
        "skillsphere_access"
      );

      if (!token) {
        throw new Error(
          "Access token not found. Please login again."
        );
      }

      const response = await fetch(
        `${API_BASE_URL}/api/auth/mentor/dashboard/`,
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
        }
      );

      const data = await response.json();

      if (!response.ok) {
        if (response.status === 401) {
          throw new Error(
            "Session expired. Please login again."
          );
        }

        throw new Error(
          data.detail ||
          data.message ||
          "Unable to load dashboard."
        );
      }

      setDashboardData(data);
    } catch (err) {
      setError(
        err.message || "Something went wrong."
      );
    } finally {
      setLoading(false);
    }
  }, []);

  // ===================================================
  // LOAD DASHBOARD
  // ===================================================

  useEffect(() => {
    fetchMentorDashboard();
  }, [fetchMentorDashboard]);

  // ===================================================
  // DASHBOARD DATA
  // ===================================================

  const mentor = dashboardData?.mentor || {};
  const statsData = dashboardData?.stats || {};
  const students = dashboardData?.students || [];

  // ===================================================
  // DASHBOARD STATISTICS
  // ===================================================

  const stats = [
    {
      title: "Total Students",
      value: statsData.total_students ?? 0,
      icon: "👨‍🎓",
    },
    {
      title: "Active Students",
      value: statsData.active_students ?? 0,
      icon: "🟢",
    },
    {
      title: "Assessments",
      value: statsData.total_assessments ?? 0,
      icon: "📝",
    },
    {
      title: "Pending Reviews",
      value: statsData.pending_requests ?? 0,
      icon: "⏳",
    },
  ];

  // ===================================================
  // FILTER STUDENTS
  // ===================================================

  const filteredStudents = students.filter((student) => {
    const query = search.toLowerCase();

    return (
      (student.name || "")
        .toLowerCase()
        .includes(query) ||
      (student.email || "")
        .toLowerCase()
        .includes(query)
    );
  });

  // ===================================================
  // LOGOUT
  // ===================================================

  const handleLogout = () => {
    localStorage.removeItem("skillsphere_access");
    localStorage.removeItem("skillsphere_refresh");
    localStorage.removeItem("skillsphere_user");

    setShowLogoutModal(false);

    navigate("/login", {
      replace: true,
    });
  };

  // ===================================================
  // SIDEBAR NAVIGATION
  // ===================================================

  const handleMenuClick = (item) => {
    if (item === "Logout") {
      setShowLogoutModal(true);
      return;
    }

    if (mentorRoutes[item]) {
      navigate(mentorRoutes[item]);
    }
  };

  // ===================================================
  // LOADING
  // ===================================================

  if (loading) {
    return (
      <div className="mentor-placeholder">
        <h2>Loading Mentor Dashboard...</h2>
        <p>
          Please wait while we retrieve your dashboard information.
        </p>
      </div>
    );
  }

  // ===================================================
  // ERROR
  // ===================================================

  if (error) {
    return (
      <div className="mentor-placeholder">
        <div className="mentor-placeholder-icon">
          ⚠️
        </div>

        <h2>Unable to Load Dashboard</h2>
        <p>{error}</p>

        <button
          className="mentor-retry-button"
          onClick={fetchMentorDashboard}
        >
          Try Again
        </button>

        <button
          className="mentor-retry-button"
          onClick={handleLogout}
        >
          Back to Login
        </button>
      </div>
    );
  }

  // ===================================================
  // MAIN DASHBOARD UI
  // ===================================================

  return (
    <div className="mentor-layout">

      {/* SIDEBAR */}

      <aside className="mentor-sidebar">

        <div className="mentor-brand">
          <h2>SkillSphere</h2>
          <p>Mentor Workspace</p>
        </div>

        <nav className="mentor-navigation">
          {menuItems.map((item) => (
            <button
              key={item}
              type="button"
              className={
                activeMenu === item
                  ? "mentor-menu-item active"
                  : "mentor-menu-item"
              }
              onClick={() => handleMenuClick(item)}
            >
              <span>{item}</span>
            </button>
          ))}
        </nav>

        <div className="mentor-sidebar-footer">
          <p>SkillSphere © 2026</p>
        </div>

      </aside>

      {/* MAIN CONTENT */}

      <main className="mentor-main">

        {/* HEADER */}

        <header className="mentor-header">

          <div>
            <h2>{activeMenu}</h2>
            <p>Welcome to your Mentor Workspace</p>
          </div>

          <div className="mentor-header-actions">

            <input
              type="text"
              placeholder="Search students..."
              value={search}
              onChange={(event) =>
                setSearch(event.target.value)
              }
            />

            <button
              type="button"
              className="mentor-notification-button"
              onClick={() =>
                navigate("/mentor/notifications")
              }
              title="Notifications"
            >
              🔔
            </button>

            <div className="mentor-avatar">
              {(mentor.name || "Mentor")
                .charAt(0)
                .toUpperCase()}
            </div>

          </div>

        </header>

        {/* DASHBOARD HOME */}

        {activeMenu === "Dashboard" && (
          <section className="mentor-dashboard-content">

            {/* WELCOME SECTION */}

            <div className="mentor-welcome">
              <div>
                <h1>
                  Welcome Back, {mentor.name || "Mentor"}!
                </h1>

                <p>
                  Guide your students, track their progress
                  and help them achieve their career goals.
                </p>
              </div>

              <div className="mentor-welcome-icon">
                🎓
              </div>
            </div>

            {/* STATISTICS */}

            <div className="mentor-stats-grid">
              {stats.map((stat) => (
                <div
                  className="mentor-stat-card"
                  key={stat.title}
                >
                  <div className="mentor-stat-icon">
                    {stat.icon}
                  </div>

                  <div>
                    <p>{stat.title}</p>
                    <h2>{stat.value}</h2>
                  </div>
                </div>
              ))}
            </div>

            {/* DASHBOARD CONTENT */}

            <div className="mentor-content-grid">

              {/* STUDENT OVERVIEW */}

              <div className="mentor-panel mentor-students-panel">

                <div className="mentor-panel-heading">
                  <h3>Student Progress Overview</h3>

                  <button
                    type="button"
                    onClick={() =>
                      navigate("/mentor/students")
                    }
                  >
                    View All
                  </button>
                </div>

                {filteredStudents.length > 0 ? (
                  filteredStudents.map((student) => (
                    <div
                      className="mentor-student-row"
                      key={
                        student.assignment_id ||
                        student.id
                      }
                    >
                      <div className="mentor-student-avatar">
                        {(student.name || "S")
                          .charAt(0)
                          .toUpperCase()}
                      </div>

                      <div>
                        <strong>
                          {student.name || "Student"}
                        </strong>

                        <p>
                          {student.email || ""}
                        </p>
                      </div>
                    </div>
                  ))
                ) : (
                  <div className="mentor-empty-state">
                    <span>👨‍🎓</span>

                    <p>
                      {search
                        ? "No matching students found."
                        : "Student progress will appear here."}
                    </p>
                  </div>
                )}

              </div>

              {/* UPCOMING ACTIVITIES */}

              <div className="mentor-panel">
                <h3>Upcoming Activities</h3>

                <div className="mentor-empty-state">
                  <span>📅</span>
                  <p>No upcoming activities yet.</p>
                </div>
              </div>

              {/* SKILL GAP OVERVIEW */}

              <div className="mentor-panel">
                <h3>Skill Gap Overview</h3>

                <div className="mentor-empty-state">
                  <span>📊</span>

                  <p>
                    Student skill gap analysis will appear here.
                  </p>
                </div>
              </div>

              {/* QUICK ACTIONS */}

              <div className="mentor-panel">
                <h3>Quick Actions</h3>

                <div className="mentor-quick-actions">

                  <button
                    type="button"
                    onClick={() =>
                      navigate("/mentor/students")
                    }
                  >
                    My Students
                  </button>

                  <button
                    type="button"
                    onClick={() =>
                      navigate("/mentor/assessments")
                    }
                  >
                    Review Assessments
                  </button>

                  <button
                    type="button"
                    onClick={() =>
                      navigate("/mentor/roadmaps")
                    }
                  >
                    Manage Roadmaps
                  </button>

                  <button
                    type="button"
                    onClick={() =>
                      navigate("/mentor/messages")
                    }
                  >
                    Send Feedback
                  </button>

                </div>
              </div>

            </div>

          </section>
        )}

        {/* EXISTING DASHBOARD MODULES */}

        {activeMenu === "My Profile" && (
          <MentorProfile />
        )}

        {activeMenu === "My Students" && (
          <MyStudents />
        )}

        {activeMenu === "Student Progress" && (
          <StudentProgress />
        )}

        {activeMenu === "Assessments" && (
          <Assessments />
        )}

        {activeMenu === "Skill Analysis" && (
          <SkillAnalysis />
        )}

        {activeMenu === "Skill Gaps" && (
          <SkillGaps />
        )}

        {activeMenu === "Roadmaps" && (
          <Roadmaps />
        )}

        {activeMenu === "Learning Resources" && (
          <LearningResources />
        )}

        {activeMenu === "Projects" && (
          <MentorProjects />
        )}

        {activeMenu === "Interview Prep" && (
          <MentorInterviewPrep />
        )}

        {/* FEEDBACK / MESSAGES */}

        {activeMenu === "Feedback / Messages" && (
          <FeedbackMessages students={students} />
        )}

        {/* NOTIFICATIONS */}

        {activeMenu === "Notifications" && (
          <MentorNotifications />
        )}

        {/* SETTINGS */}

        {activeMenu === "Settings" && (
          <MentorSettings />
        )}

        {/* PLACEHOLDER FOR OTHER FUTURE MODULES */}

        {activeMenu !== "Dashboard" &&
          activeMenu !== "My Profile" &&
          activeMenu !== "My Students" &&
          activeMenu !== "Student Progress" &&
          activeMenu !== "Assessments" &&
          activeMenu !== "Skill Analysis" &&
          activeMenu !== "Skill Gaps" &&
          activeMenu !== "Roadmaps" &&
          activeMenu !== "Learning Resources" &&
          activeMenu !== "Projects" &&
          activeMenu !== "Interview Prep" &&
          activeMenu !== "Feedback / Messages" &&
          activeMenu !== "Notifications" &&
          activeMenu !== "Settings" && (

            <section className="mentor-placeholder">

              <div className="mentor-placeholder-icon">
                🚀
              </div>

              <h2>{activeMenu}</h2>

              <p>
                The {activeMenu} module will be developed next.
              </p>

            </section>
          )}

      </main>

      {/* =================================================
          LOGOUT CONFIRMATION MODAL
      ================================================= */}

      {showLogoutModal && (
        <div
          className="mentor-logout-overlay"
          onClick={() => setShowLogoutModal(false)}
        >
          <div
            className="mentor-logout-modal"
            role="dialog"
            aria-modal="true"
            aria-labelledby="mentor-logout-title"
            onClick={(event) => event.stopPropagation()}
          >

            <div className="mentor-logout-icon">
              🚪
            </div>

            <h2 id="mentor-logout-title">
              Confirm Logout
            </h2>

            <p>
              Are you sure you want to log out of your
              Mentor account?
            </p>

            <div className="mentor-logout-actions">

              <button
                type="button"
                className="mentor-logout-cancel"
                onClick={() => setShowLogoutModal(false)}
              >
                Cancel
              </button>

              <button
                type="button"
                className="mentor-logout-confirm"
                onClick={handleLogout}
              >
                Yes, Logout
              </button>

            </div>

          </div>
        </div>
      )}

    </div>
  );
}

export default MentorDashboard;
