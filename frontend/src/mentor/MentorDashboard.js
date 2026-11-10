
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

const menuItems = [
  "Dashboard",  "My Students", "Student Progress",
  "Assessments", "Skill Analysis", "Skill Gaps", "Roadmaps",
  "Learning Resources", "Projects", "Interview Prep",
  "Feedback / Messages", "Notifications","My Profile", "Settings", "Logout",
];

const menuIcons = {
  Dashboard: "▦", "My Profile": "◉", "My Students": "♧",
  "Student Progress": "↗", Assessments: "▤", "Skill Analysis": "◫",
  "Skill Gaps": "⌁", Roadmaps: "⌖", "Learning Resources": "▱",
  Projects: "◇", "Interview Prep": "✧", "Feedback / Messages": "✉",
  Notifications: "♢", Settings: "⚙", Logout: "⇥",
};

const mentorRoutes = {
  Dashboard: "/mentor/dashboard", "My Profile": "/mentor/profile",
  "My Students": "/mentor/students", "Student Progress": "/mentor/student-progress",
  Assessments: "/mentor/assessments", "Skill Analysis": "/mentor/skill-analysis",
  "Skill Gaps": "/mentor/skill-gaps", Roadmaps: "/mentor/roadmaps",
  "Learning Resources": "/mentor/resources", Projects: "/mentor/projects",
  "Interview Prep": "/mentor/interview-prep", "Feedback / Messages": "/mentor/messages",
  Notifications: "/mentor/notifications", Settings: "/mentor/settings",
};

const routeMenus = Object.fromEntries(
  Object.entries(mentorRoutes).map(([menu, path]) => [path, menu])
);

function formatDate(value) {
  if (!value) return "Date not available";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return "Date not available";
  return date.toLocaleDateString(undefined, {
    day: "numeric",
    month: "short",
    year: "numeric",
  });
}

function MentorDashboard() {
  const navigate = useNavigate();
  const location = useLocation();
  const activeMenu = routeMenus[location.pathname] || "Dashboard";

  const [search, setSearch] = useState("");
  const [dashboardData, setDashboardData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [showLogoutModal, setShowLogoutModal] = useState(false);
  const [sidebarOpen, setSidebarOpen] = useState(false);

  // Close drawer when the page changes.
  useEffect(() => {
    setSidebarOpen(false);
  }, [location.pathname]);

  // Prevent background scrolling while mobile drawer is open.
  useEffect(() => {
    document.body.style.overflow = sidebarOpen ? "hidden" : "";

    return () => {
      document.body.style.overflow = "";
    };
  }, [sidebarOpen]);

  // Close drawer using Escape key.
  useEffect(() => {
    const handleEscape = (event) => {
      if (event.key === "Escape") {
        setSidebarOpen(false);
      }
    };

    window.addEventListener("keydown", handleEscape);
    return () => window.removeEventListener("keydown", handleEscape);
  }, []);

  const fetchMentorDashboard = useCallback(async () => {
    try {
      setLoading(true);
      setError("");

      const token = localStorage.getItem("skillsphere_access");

      if (!token) {
        throw new Error("Access token not found. Please login again.");
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
          throw new Error("Session expired. Please login again.");
        }

        throw new Error(
          data.detail || data.message || "Unable to load dashboard."
        );
      }

      setDashboardData(data);
    } catch (err) {
      setError(err.message || "Something went wrong.");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchMentorDashboard();
  }, [fetchMentorDashboard]);

  const mentor = dashboardData?.mentor || {};
  const statsData = dashboardData?.stats || {};

  const students = Array.isArray(dashboardData?.students)
    ? dashboardData.students
    : [];

  const requests = Array.isArray(dashboardData?.recent_requests)
    ? dashboardData.recent_requests
    : [];

  const filteredStudents = students.filter((student) => {
    const query = search.trim().toLowerCase();

    return (
      !query ||
      `${student.name || ""} ${student.email || ""}`
        .toLowerCase()
        .includes(query)
    );
  });

  const stats = [
    {
      title: "Total Students",
      value: statsData.total_students ?? 0,
      icon: "♧",
      tone: "blue",
      note: "All assigned students",
    },
    {
      title: "Active Students",
      value: statsData.active_students ?? 0,
      icon: "◉",
      tone: "green",
      note: "Currently working with you",
    },
    {
      title: "Assessments",
      value: statsData.total_assessments ?? 0,
      icon: "▤",
      tone: "violet",
      note: "Completed by your students",
    },
    {
      title: "Pending Requests",
      value: statsData.pending_requests ?? 0,
      icon: "◷",
      tone: "orange",
      note: "Awaiting your attention",
    },
  ];

  const handleLogout = () => {
    localStorage.removeItem("skillsphere_access");
    localStorage.removeItem("skillsphere_refresh");
    localStorage.removeItem("skillsphere_user");

    setShowLogoutModal(false);
    setSidebarOpen(false);
    navigate("/login", { replace: true });
  };

  const handleMenuClick = (item) => {
    setSidebarOpen(false);

    if (item === "Logout") {
      setShowLogoutModal(true);
      return;
    }

    if (mentorRoutes[item]) {
      navigate(mentorRoutes[item]);
    }
  };

  if (loading) {
    return (
      <div className="mentor-state-screen">
        <div className="mentor-loader" />
        <h2>Preparing your workspace</h2>
        <p>Loading your students and mentoring activity...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="mentor-state-screen">
        <div className="mentor-state-icon">!</div>
        <h2>Unable to load dashboard</h2>
        <p>{error}</p>
        <div className="mentor-state-actions">
          <button
            className="mentor-primary-button"
            onClick={fetchMentorDashboard}
          >
            Try Again
          </button>
          <button
            className="mentor-secondary-button"
            onClick={handleLogout}
          >
            Back to Login
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="mentor-layout">

      {/* Mobile drawer overlay */}
      {sidebarOpen && (
        <button
          type="button"
          className="mentor-mobile-overlay"
          aria-label="Close navigation"
          onClick={() => setSidebarOpen(false)}
        />
      )}

      {/* ORIGINAL SIDEBAR */}
      <aside
        className={`mentor-sidebar ${
          sidebarOpen ? "mentor-sidebar-open" : ""
        }`}
      >
        <div className="mentor-brand">
          <div className="mentor-brand-mark">S</div>

          <div>
            <h2>SkillSphere</h2>
            <p>MENTOR WORKSPACE</p>
          </div>

          <button
            type="button"
            className="mentor-sidebar-close"
            aria-label="Close navigation"
            onClick={() => setSidebarOpen(false)}
          >
            ×
          </button>
        </div>

        <div className="mentor-nav-label">WORKSPACE</div>

        <nav className="mentor-navigation">
          {menuItems.map((item) => (
            <button
              key={item}
              type="button"
              className={`mentor-menu-item ${
                activeMenu === item ? "active" : ""
              } ${item === "Logout" ? "mentor-logout-menu" : ""}`}
              onClick={() => handleMenuClick(item)}
            >
              <span className="mentor-menu-icon">
                {menuIcons[item]}
              </span>

              <span>{item}</span>

              {item === "Notifications" && (
                <span className="mentor-menu-dot" />
              )}
            </button>
          ))}
        </nav>

        <div className="mentor-sidebar-help">
          <div className="mentor-help-symbol">?</div>
          <div>
            <strong>Need assistance?</strong>
            <span>Visit support centre</span>
          </div>
          <span className="mentor-help-arrow">↗</span>
        </div>

        <div className="mentor-sidebar-footer">
          © 2026 SkillSphere <span>•</span> Empowering growth
        </div>
      </aside>

      {/* ORIGINAL MAIN CONTENT */}
      <main className="mentor-main">

        <header className="mentor-header">

          {/* Mobile hamburger */}
          <button
            type="button"
            className="mentor-mobile-menu-button"
            aria-label="Open navigation"
            aria-expanded={sidebarOpen}
            onClick={() => setSidebarOpen(true)}
          >
            <span />
            <span />
            <span />
          </button>

          <div className="mentor-breadcrumb">
            <span>Workspace</span>
            <b>/</b>
            <strong>{activeMenu}</strong>
            <p>
              {activeMenu === "Dashboard"
                ? "Your mentoring overview at a glance"
                : `Manage your ${activeMenu.toLowerCase()} workspace`}
            </p>
          </div>

          <div className="mentor-header-actions">
            <label className="mentor-search">
              <span>⌕</span>
              <input
                aria-label="Search students"
                type="search"
                placeholder="Search students..."
                value={search}
                onChange={(event) => setSearch(event.target.value)}
              />
            </label>

            <button
              type="button"
              className="mentor-notification-button"
              onClick={() => navigate("/mentor/notifications")}
              aria-label="Open notifications"
            >
              <span>♢</span>
              <i />
            </button>

            <button
              type="button"
              className="mentor-profile-chip"
              onClick={() => navigate("/mentor/profile")}
            >
              <span className="mentor-avatar">
                {(mentor.name || "M").charAt(0).toUpperCase()}
              </span>

              <span className="mentor-profile-name">
                <strong>{mentor.name || "Mentor"}</strong>
                <small>Mentor</small>
              </span>

              <span className="mentor-chevron">⌄</span>
            </button>
          </div>
        </header>

        {/* ORIGINAL DASHBOARD UI - PRESERVED */}
        {activeMenu === "Dashboard" && (
          <section className="mentor-dashboard-content">

            <div className="mentor-welcome">
              <div className="mentor-welcome-copy">
                <span className="mentor-eyebrow">
                  YOUR MENTORING OVERVIEW
                </span>

                <h1>
                  Welcome back, {mentor.name || "Mentor"} <span>✦</span>
                </h1>

                <p>
                  Great things happen when you guide with purpose.
                  Here's what's happening with your students today.
                </p>

                <div className="mentor-welcome-actions">
                  <button
                    type="button"
                    onClick={() => navigate("/mentor/students")}
                  >
                    Explore my students <span>→</span>
                  </button>

                  <span className="mentor-welcome-caption">
                    Make every learning moment count.
                  </span>
                </div>
              </div>

              <div className="mentor-welcome-art" aria-hidden="true">
                <div className="mentor-art-orbit orbit-one" />
                <div className="mentor-art-orbit orbit-two" />
                <div className="mentor-art-circle">✦</div>

                <div className="mentor-art-card art-card-one">
                  <span>↗</span>
                  <div>
                    <b>Growth</b>
                    <small>Starts with guidance</small>
                  </div>
                </div>

                <div className="mentor-art-card art-card-two">
                  <span>✓</span>
                  <div>
                    <b>Keep inspiring</b>
                    <small>One student at a time</small>
                  </div>
                </div>
              </div>
            </div>

            <div className="mentor-section-heading">
              <div>
                <span className="mentor-section-kicker">AT A GLANCE</span>
                <h2>Your mentoring snapshot</h2>
              </div>

              <span className="mentor-live-label">
                <i /> Live dashboard data
              </span>
            </div>

            <div className="mentor-stats-grid">
              {stats.map((stat) => (
                <article className="mentor-stat-card" key={stat.title}>
                  <div className={`mentor-stat-icon ${stat.tone}`}>
                    {stat.icon}
                  </div>

                  <div className="mentor-stat-info">
                    <p>{stat.title}</p>
                    <h2>{stat.value}</h2>
                    <span>{stat.note}</span>
                  </div>

                  <div className={`mentor-stat-accent ${stat.tone}`} />
                </article>
              ))}
            </div>

            <div className="mentor-section-heading mentor-section-heading-spaced">
              <div>
                <span className="mentor-section-kicker">
                  YOUR STUDENTS
                </span>
                <h2>Stay connected and guide progress</h2>
              </div>
            </div>

            <div className="mentor-content-grid">

              <section className="mentor-panel mentor-students-panel">
                <div className="mentor-panel-heading">
                  <div>
                    <h3>Your students</h3>
                    <p>Students currently connected with you</p>
                  </div>

                  <span className="mentor-count-badge">
                    {students.length}
                  </span>
                </div>

                {filteredStudents.length > 0 ? (
                  <div className="mentor-student-list">
                    {filteredStudents.slice(0, 6).map((student) => (
                      <div
                        className="mentor-student-row"
                        key={student.assignment_id || student.id}
                      >
                        <div className="mentor-student-avatar">
                          {(student.name || "S")
                            .charAt(0)
                            .toUpperCase()}
                        </div>

                        <div className="mentor-student-details">
                          <strong>{student.name || "Student"}</strong>
                          <p>{student.email || "Email not available"}</p>
                        </div>

                        <div className="mentor-student-date">
                          {formatDate(student.assigned_at)}
                        </div>
                      </div>
                    ))}
                  </div>
                ) : (
                  <div className="mentor-empty-state">
                    <span className="mentor-empty-icon">♧</span>
                    <strong>
                      {search ? "No matching students" : "No active students yet"}
                    </strong>
                    <p>
                      {search
                        ? "Try another name or email address."
                        : "Students assigned to you will appear here."}
                    </p>
                  </div>
                )}

                {filteredStudents.length > 6 && (
                  <button
                    className="mentor-list-more"
                    onClick={() => navigate("/mentor/students")}
                  >
                    See all {filteredStudents.length} students →
                  </button>
                )}
              </section>

              <section className="mentor-panel mentor-requests-panel">
                <div className="mentor-panel-heading">
                  <div>
                    <h3>Pending student requests</h3>
                    <p>Recent requests that need your attention</p>
                  </div>

                  <span className="mentor-count-badge">
                    {statsData.pending_requests ?? requests.length}
                  </span>
                </div>

                {requests.length > 0 ? (
                  <div className="mentor-request-list">
                    {requests.map((request) => (
                      <div className="mentor-request-row" key={request.id}>
                        <div className="mentor-request-avatar">
                          {(request.student_name || "S")
                            .charAt(0)
                            .toUpperCase()}
                        </div>

                        <div className="mentor-request-details">
                          <strong>
                            {request.student_name || "Student"}
                          </strong>
                          <p>
                            {request.student_email || "Email not available"}
                          </p>
                          <small>
                            Requested {formatDate(request.assigned_at)}
                          </small>
                        </div>

                        <span className="mentor-pending-pill">
                          Pending
                        </span>
                      </div>
                    ))}
                  </div>
                ) : (
                  <div className="mentor-empty-state mentor-request-empty">
                    <span className="mentor-empty-icon">✓</span>
                    <strong>You're all caught up</strong>
                    <p>New student requests will appear here.</p>
                  </div>
                )}

                <button
                  className="mentor-panel-footer-link"
                  type="button"
                  onClick={() => navigate("/mentor/students")}
                >
                  Manage student connections <span>→</span>
                </button>
              </section>

              <section className="mentor-panel mentor-quick-panel">
                <div className="mentor-panel-heading">
                  <div>
                    <h3>Quick actions</h3>
                    <p>Jump into your mentoring tools</p>
                  </div>

                  <span className="mentor-quick-spark">✦</span>
                </div>

                <div className="mentor-quick-actions">
                  <button onClick={() => navigate("/mentor/students")}>
                    <span className="quick-action-icon blue">♧</span>
                    <span>
                      <strong>My students</strong>
                      <small>View learner profiles</small>
                    </span>
                    <b>→</b>
                  </button>

                  <button onClick={() => navigate("/mentor/assessments")}>
                    <span className="quick-action-icon violet">▤</span>
                    <span>
                      <strong>Assessments</strong>
                      <small>Review student results</small>
                    </span>
                    <b>→</b>
                  </button>

                  <button onClick={() => navigate("/mentor/roadmaps")}>
                    <span className="quick-action-icon green">⌖</span>
                    <span>
                      <strong>Learning roadmaps</strong>
                      <small>Guide the next steps</small>
                    </span>
                    <b>→</b>
                  </button>

                  <button onClick={() => navigate("/mentor/messages")}>
                    <span className="quick-action-icon orange">✉</span>
                    <span>
                      <strong>Send feedback</strong>
                      <small>Stay in touch</small>
                    </span>
                    <b>→</b>
                  </button>
                </div>
              </section>

              <section className="mentor-insight-panel">
                <div className="mentor-insight-top">
                  <span className="mentor-insight-icon">✧</span>
                  <span>MENTOR NOTE</span>
                </div>

                <h3>Small guidance. Big growth.</h3>

                <p>
                  Consistent feedback and clear learning goals help
                  students build confidence and move forward.
                </p>

                <button
                  type="button"
                  onClick={() => navigate("/mentor/student-progress")}
                >
                  Review student progress <span>→</span>
                </button>

                <div className="mentor-insight-decoration">✦</div>
              </section>

            </div>
          </section>
        )}

        {/* ALL ORIGINAL MODULES */}
        {activeMenu === "My Profile" && <MentorProfile />}
        {activeMenu === "My Students" && <MyStudents />}
        {activeMenu === "Student Progress" && <StudentProgress />}
        {activeMenu === "Assessments" && <Assessments />}
        {activeMenu === "Skill Analysis" && <SkillAnalysis />}
        {activeMenu === "Skill Gaps" && <SkillGaps />}
        {activeMenu === "Roadmaps" && <Roadmaps />}
        {activeMenu === "Learning Resources" && <LearningResources />}
        {activeMenu === "Projects" && <MentorProjects />}
        {activeMenu === "Interview Prep" && <MentorInterviewPrep />}
        {activeMenu === "Feedback / Messages" && (
          <FeedbackMessages students={students} />
        )}
        {activeMenu === "Notifications" && <MentorNotifications />}
        {activeMenu === "Settings" && <MentorSettings />}

      </main>

      {/* ORIGINAL LOGOUT CONFIRMATION */}
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
            <div className="mentor-logout-icon">⇥</div>
            <span className="mentor-modal-eyebrow">
              ENDING YOUR SESSION
            </span>
            <h2 id="mentor-logout-title">Confirm logout</h2>
            <p>
              Are you sure you want to log out of your Mentor account?
            </p>

            <div className="mentor-logout-actions">
              <button
                type="button"
                className="mentor-logout-cancel"
                onClick={() => setShowLogoutModal(false)}
              >
                Stay logged in
              </button>

              <button
                type="button"
                className="mentor-logout-confirm"
                onClick={handleLogout}
              >
                Yes, log out
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default MentorDashboard;
