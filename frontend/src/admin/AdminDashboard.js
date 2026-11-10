import React, { useEffect, useMemo, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { showToast } from "../components/ToastProvider";
import "./AdminDashboard.css";

import UserManagement from "./UserManagement";
import Students from "./Students";
import Mentors from "./Mentors";
import SkillsManagement from "./SkillsManagement";
import AdminAssessments from "./AdminAssessments";
import AdminLearningResources from "./AdminLearningResources";
import AdminRoadmaps from "./AdminRoadmaps";
import AdminChallenges from "./AdminChallenges";
import AdminProjects from "./AdminProjects";
import AdminInterviewPreparation from "./AdminInterviewPreparation";
import AdminAchievements from "./AdminAchievements";
import ReportsAnalytics from "./ReportsAnalytics";
import Notifications from "./AdminNotifications";
import AdminEmailManagement from "./AdminEmailManagement";
import AdminFileManagement from "./AdminFileManagement";
import AdminSystemSettings from "./AdminSystemSettings";
import AdminSecurityPermissions from "./AdminSecurityPermissions";
import AdminAssessmentResults from "./AdminAssessmentResults";
import { useAuth } from "../auth/AuthContext";
const ADMIN_DASHBOARD_API =
  "https://skillsphere-17hl.onrender.com/api/auth/admin/dashboard/";

const MENU_GROUPS = [
  {
    title: "OVERVIEW",
    items: [{ id: "dashboard", label: "Dashboard", icon: "⌂" }],
  },
  {
    title: "USER MANAGEMENT",
    items: [
      { id: "users", label: "User Management", icon: "♙" },
      { id: "students", label: "Students", icon: "♧" },
      { id: "mentors", label: "Mentors", icon: "♙" },
      { id: "assessment-results", label: "Assessment Results", icon: "▥" },
    ],
  },
  {
    title: "LEARNING MANAGEMENT",
    items: [
      { id: "skills", label: "Skills & Categories", icon: "◇" },
      { id: "assessments", label: "Assessments", icon: "▤" },
      { id: "resources", label: "Learning Resources", icon: "▣" },
      { id: "roadmaps", label: "Roadmaps", icon: "↗" },
      { id: "challenges", label: "Challenges", icon: "♢" },
      { id: "projects", label: "Projects", icon: "▧" },
      { id: "interviews", label: "Interview Preparation", icon: "▤" },
      { id: "achievements", label: "Achievements", icon: "☆" },
    ],
  },
  {
    title: "SYSTEM",
    items: [
      { id: "reports", label: "Reports & Analytics", icon: "▥" },
      { id: "notifications", label: "Notifications", icon: "♧" },
      { id: "email", label: "Email Management", icon: "✉" },
      { id: "files", label: "File Management", icon: "▱" },
      { id: "settings", label: "System Settings", icon: "⚙" },
      { id: "security", label: "Security & Permissions", icon: "♧" },
    ],
  },
];

const SECTION_DETAILS = {
  achievements: {
    title: "Achievements",
    description:
      "Manage achievement categories and recognition milestones.",
    icon: "☆",
    features: [
      "Achievement types",
      "Milestone categories",
      "Recognition criteria",
    ],
  },
  reports: {
    title: "Reports & Analytics",
    description:
      "Review SkillSphere platform activity and analytics.",
    icon: "▥",
    features: [
      "Platform activity reports",
      "Learning progress",
      "System usage",
    ],
  },
  notifications: {
    title: "Notifications",
    description:
      "Manage platform announcements and notifications.",
    icon: "♧",
    features: [
      "Notification categories",
      "Announcements",
      "Delivery preferences",
    ],
  },
  email: {
    title: "Email Management",
    description: "Manage platform email communication.",
    icon: "✉",
    features: [
      "Email templates",
      "Communication types",
      "Email preferences",
    ],
  },
  files: {
    title: "File Management",
    description: "Review uploaded files and learning resources.",
    icon: "▱",
    features: [
      "File categories",
      "Uploaded materials",
      "Access rules",
    ],
  },
  settings: {
    title: "System Settings",
    description: "Review general SkillSphere configuration options.",
    icon: "⚙",
    features: [
      "Platform configuration",
      "General preferences",
      "Application settings",
    ],
  },
  security: {
    title: "Security & Permissions",
    description: "Review access control and security settings.",
    icon: "♧",
    features: [
      "Role permissions",
      "Access control",
      "Security configuration",
    ],
  },
};

function getSectionFromPath(pathname) {
  const path = pathname.replace(/\/+$/, "") || "/";

  if (path === "/admin" || path === "/admin/dashboard") {
    return "dashboard";
  }

  if (path.startsWith("/admin/")) {
    return path.split("/").filter(Boolean).pop() || "dashboard";
  }

  return "dashboard";
}

function getAdminName() {
  try {
    const savedUser =
      localStorage.getItem("skillsphere_user") ||
      localStorage.getItem("user");

    if (!savedUser) return "Administrator";

    const user = JSON.parse(savedUser);

    return (
      user.first_name ||
      user.firstName ||
      user.username ||
      user.name ||
      user.email?.split("@")[0] ||
      "Administrator"
    );
  } catch {
    return "Administrator";
  }
}

function getInitials(name) {
  return (
    String(name || "Administrator")
      .split(/[\s._-]+/)
      .filter(Boolean)
      .slice(0, 2)
      .map((part) => part.charAt(0).toUpperCase())
      .join("") || "AD"
  );
}

function AdminDashboard() {
  const navigate = useNavigate();
  const location = useLocation();

  const [activeSection, setActiveSection] = useState(() =>
    getSectionFromPath(window.location.pathname)
  );

  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [searchTerm, setSearchTerm] = useState("");
  const [profileOpen, setProfileOpen] = useState(false);
  const [logoutPending, setLogoutPending] = useState(false);
  const [showLogoutConfirm, setShowLogoutConfirm] = useState(false);

  const [adminData, setAdminData] = useState(null);
  const [dashboardLoading, setDashboardLoading] = useState(true);
  const [dashboardError, setDashboardError] = useState("");

  const adminName = useMemo(() => getAdminName(), []);

  useEffect(() => {
    const section = getSectionFromPath(location.pathname);

    setActiveSection(section);
    setSidebarOpen(false);
    setSearchTerm("");
    setProfileOpen(false);

    document.title =
      section === "dashboard"
        ? "Admin Dashboard | SkillSphere"
        : `${
            section.charAt(0).toUpperCase() + section.slice(1)
          } | SkillSphere`;
  }, [location.pathname]);

  async function loadAdminDashboard() {
    const token =
      localStorage.getItem("skillsphere_access") ||
      localStorage.getItem("access");

    if (!token) {
      setDashboardError(
        "Your session has expired. Please log in again."
      );
      setDashboardLoading(false);
      return;
    }

    setDashboardLoading(true);
    setDashboardError("");

    try {
      const response = await fetch(ADMIN_DASHBOARD_API, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${token}`,
          Accept: "application/json",
        },
      });

      const data = await response.json().catch(() => ({}));

      if (!response.ok) {
        throw new Error(
          data.detail ||
            data.message ||
            `Unable to load dashboard data (${response.status}).`
        );
      }

      setAdminData(data);
    } catch (error) {
      setDashboardError(
        error.message || "Unable to connect to the backend."
      );
    } finally {
      setDashboardLoading(false);
    }
  }

  useEffect(() => {
    loadAdminDashboard();
  }, []);

  const allItems = useMemo(
    () => MENU_GROUPS.flatMap((group) => group.items),
    []
  );

  const activeItem = allItems.find(
    (item) => item.id === activeSection
  );

  const sectionDetails = SECTION_DETAILS[activeSection];

  const filteredGroups = useMemo(() => {
    const query = searchTerm.trim().toLowerCase();

    if (!query) return MENU_GROUPS;

    return MENU_GROUPS.map((group) => ({
      ...group,
      items: group.items.filter((item) =>
        item.label.toLowerCase().includes(query)
      ),
    })).filter((group) => group.items.length > 0);
  }, [searchTerm]);

  function handleNavigation(item) {
    if (!item) return;

    setSidebarOpen(false);
    setSearchTerm("");
    setProfileOpen(false);

    const targetPath =
      item.id === "dashboard"
        ? "/admin/dashboard"
        : `/admin/${item.id}`;

    if (location.pathname !== targetPath) {
      navigate(targetPath);
    } else {
      setActiveSection(item.id);
    }
  }

  function handleLogout() {
    if (logoutPending) return;

    showToast("Logged out successfully.", "error");

    setLogoutPending(true);

    [
      "access",
      "refresh",
      "role",
      "user",
      "skillsphere_access",
      "skillsphere_refresh",
      "skillsphere_user",
      "skillsphere_saved_email",
    ].forEach((key) => localStorage.removeItem(key));

    setShowLogoutConfirm(false);

    showToast(
      "You have been logged out of SkillSphere.",
      "success"
    );

    navigate("/login", { replace: true });
  }

  function renderDashboardOverview() {
    const stats = adminData?.stats || {};

    return (
      <>
        <section className="admin-welcome-panel">
          <div className="admin-welcome-copy">
            <span className="admin-eyebrow">
              ADMINISTRATION
            </span>

            <h2>Welcome back, {adminName}!</h2>

            <p>
              Manage your SkillSphere platform, learning content, and
              system configuration from one place.
            </p>
          </div>

          <div
            className="admin-welcome-art"
            aria-hidden="true"
          >
            <div className="admin-art-orbit admin-art-orbit-one" />
            <div className="admin-art-orbit admin-art-orbit-two" />
            <div className="admin-art-core">S</div>
            <span className="admin-art-star">✦</span>
            <span className="admin-art-dot admin-art-dot-one" />
            <span className="admin-art-dot admin-art-dot-two" />
          </div>
        </section>

        <div className="admin-section-heading">
          <div>
            <h2>Platform Overview</h2>
            <p>Your administration workspace at a glance.</p>
          </div>

          <button
            type="button"
            className="admin-secondary-button"
            onClick={loadAdminDashboard}
            disabled={dashboardLoading}
          >
            ↻ {dashboardLoading ? "Refreshing..." : "Refresh"}
          </button>
        </div>

        {dashboardError && (
          <div
            className="admin-placeholder-notice"
            role="alert"
          >
            <span>ⓘ</span>
            <p>{dashboardError}</p>
          </div>
        )}

        <section
          className="admin-stat-grid"
          aria-label="Platform overview"
        >
          <article className="admin-stat-card">
            <div className="admin-stat-top">
              <span className="admin-stat-icon stat-icon-blue">
                ♙
              </span>
              <span className="admin-stat-label">Users</span>
            </div>

            <strong>
              {dashboardLoading
                ? "…"
                : stats.total_users ?? "—"}
            </strong>

            <p>
              {dashboardLoading
                ? "Loading from backend..."
                : `${stats.active_users ?? 0} active · ${
                    stats.inactive_users ?? 0
                  } inactive`}
            </p>
          </article>

          <article className="admin-stat-card">
            <div className="admin-stat-top">
              <span className="admin-stat-icon stat-icon-purple">
                ◇
              </span>
              <span className="admin-stat-label">Skills</span>
            </div>
            <strong>—</strong>
            <p>Skills statistics API not connected</p>
          </article>

          <article className="admin-stat-card">
            <div className="admin-stat-top">
              <span className="admin-stat-icon stat-icon-orange">
                ▤
              </span>
              <span className="admin-stat-label">
                Assessments
              </span>
            </div>
            <strong>—</strong>
            <p>Assessment statistics API not connected</p>
          </article>

          <article className="admin-stat-card">
            <div className="admin-stat-top">
              <span className="admin-stat-icon stat-icon-green">
                ↗
              </span>
              <span className="admin-stat-label">Roadmaps</span>
            </div>
            <strong>—</strong>
            <p>Roadmap statistics API not connected</p>
          </article>
        </section>

        <div className="admin-content-grid">
          <section className="admin-panel admin-quick-panel">
            <div className="admin-panel-heading">
              <div>
                <h2>Quick Access</h2>
                <p>Jump directly to a platform section.</p>
              </div>
              <span className="admin-panel-heading-icon">
                ✦
              </span>
            </div>

            <div className="admin-quick-grid">
              {[
                {
                  id: "users",
                  title: "User Management",
                  icon: "♙",
                  color: "blue",
                },
                {
                  id: "students",
                  title: "Students",
                  icon: "🎓",
                  color: "purple",
                },
                {
                  id: "mentors",
                  title: "Mentors",
                  icon: "♧",
                  color: "orange",
                },
                {
                  id: "interviews",
                  title: "Interview Preparation",
                  icon: "▤",
                  color: "green",
                },
              ].map((item) => (
                <button
                  type="button"
                  className="admin-quick-link"
                  key={item.id}
                  onClick={() => handleNavigation(item)}
                >
                  <span
                    className={`admin-quick-icon quick-${item.color}`}
                  >
                    {item.icon}
                  </span>

                  <span>{item.title}</span>

                  <span
                    className="admin-quick-arrow"
                    aria-hidden="true"
                  >
                    ↗
                  </span>
                </button>
              ))}
            </div>
          </section>

          <section className="admin-panel admin-status-panel">
            <div className="admin-panel-heading">
              <div>
                <h2>System Status</h2>
                <p>Application connection information.</p>
              </div>
              <span className="admin-status-indicator" />
            </div>

            <div className="admin-status-row">
              <span className="admin-status-symbol">✓</span>
              <div>
                <strong>Admin interface</strong>
                <p>The dashboard interface is loaded.</p>
              </div>
              <span className="admin-status-pill">Ready</span>
            </div>

            <div className="admin-status-row">
              <span className="admin-status-symbol status-symbol-muted">
                ↔
              </span>
              <div>
                <strong>Backend connection</strong>
                <p>
                  {dashboardLoading
                    ? "Loading dashboard statistics..."
                    : dashboardError
                    ? "Please check your backend and session."
                    : "Dashboard API responded successfully."}
                </p>
              </div>
              <span className="admin-status-pill">
                {dashboardLoading
                  ? "Loading"
                  : dashboardError
                  ? "Error"
                  : "Connected"}
              </span>
            </div>
          </section>
        </div>

        <section className="admin-panel admin-modules-panel">
          <div className="admin-panel-heading">
            <div>
              <h2>Administration Modules</h2>
              <p>
                Explore the tools available in your workspace.
              </p>
            </div>
          </div>

          <div className="admin-module-list">
            {[
              [
                "User management",
                "Students, mentors, and platform accounts",
              ],
              [
                "Learning content",
                "Skills, assessments, resources, and roadmaps",
              ],
              [
                "Practice & growth",
                "Challenges, projects, and interview preparation",
              ],
            ].map(([title, description]) => (
              <div className="admin-module-row" key={title}>
                <span className="admin-module-check">✓</span>
                <div>
                  <strong>{title}</strong>
                  <p>{description}</p>
                </div>
                <span className="admin-module-arrow">→</span>
              </div>
            ))}
          </div>
        </section>
      </>
    );
  }

  function renderSectionPlaceholder() {
    if (!sectionDetails) {
      return (
        <section className="admin-section-placeholder">
          <div className="admin-placeholder-icon">◇</div>
          <span className="admin-eyebrow">ADMIN MODULE</span>
          <h2>Section not configured</h2>
          <p className="admin-placeholder-description">
            This section does not have a connected component yet.
          </p>
          <button
            type="button"
            className="admin-primary-button"
            onClick={() =>
              handleNavigation({ id: "dashboard" })
            }
          >
            ← Back to Dashboard
          </button>
        </section>
      );
    }

    return (
      <section className="admin-section-placeholder">
        <div className="admin-placeholder-icon">
          {sectionDetails.icon}
        </div>

        <span className="admin-eyebrow">ADMIN MODULE</span>
        <h2>{sectionDetails.title}</h2>

        <p className="admin-placeholder-description">
          {sectionDetails.description}
        </p>

        <div className="admin-placeholder-notice">
          <span aria-hidden="true">ⓘ</span>
          <p>
            The page is available, but its data and actions need a
            dedicated component and backend API connection.
          </p>
        </div>

        <div className="admin-placeholder-features">
          {sectionDetails.features.map((feature) => (
            <div
              className="admin-placeholder-feature"
              key={feature}
            >
              <span>✓</span>
              {feature}
            </div>
          ))}
        </div>

        <button
          type="button"
          className="admin-primary-button"
          onClick={() =>
            handleNavigation({ id: "dashboard" })
          }
        >
          ← Back to Dashboard
        </button>
      </section>
    );
  }

  function renderActiveSection() {
    switch (activeSection) {
      case "dashboard":
        return renderDashboardOverview();

      case "users":
        return <UserManagement />;

      case "students":
        return <Students />;

      case "mentors":
        return <Mentors />;

      case "skills":
        return <SkillsManagement />;

      case "assessments":
        return <AdminAssessments />;

      case "resources":
        return <AdminLearningResources />;

      case "roadmaps":
        return <AdminRoadmaps />;

      case "challenges":
        return <AdminChallenges />;

      case "projects":
        return <AdminProjects />;

      case "interviews":
        return <AdminInterviewPreparation />;

      case "achievements":
        return <AdminAchievements />;

      // Connected Reports & Analytics component.
      case "reports":
        return <ReportsAnalytics />;

        case "notifications":
  return <Notifications />;

  case "email":
  return <AdminEmailManagement />;

  case "files":
  return <AdminFileManagement />;



case "settings":
  return <AdminSystemSettings />;


case "security":
  return <AdminSecurityPermissions />;

  case "assessment-results":
  return <AdminAssessmentResults />;


      default:
        return renderSectionPlaceholder();
    }
  }

  return (
    <div className="admin-layout">
      {sidebarOpen && (
        <button
          type="button"
          className="admin-mobile-overlay"
          aria-label="Close navigation menu"
          onClick={() => setSidebarOpen(false)}
        />
      )}

      <aside
        className={`admin-sidebar ${
          sidebarOpen ? "admin-sidebar-open" : ""
        }`}
      >
        <div className="admin-brand">
          <div className="admin-brand-mark">S</div>

          <div className="admin-brand-copy">
            <strong>SkillSphere</strong>
            <span>ADMIN CONSOLE</span>
          </div>

          <button
            type="button"
            className="admin-sidebar-close"
            aria-label="Close navigation"
            onClick={() => setSidebarOpen(false)}
          >
            ×
          </button>
        </div>

        <div className="admin-sidebar-search">
          <span aria-hidden="true">⌕</span>

          <input
            type="search"
            value={searchTerm}
            onChange={(event) => setSearchTerm(event.target.value)}
            placeholder="Find a section..."
            aria-label="Find a dashboard section"
          />

          {searchTerm && (
            <button
              type="button"
              aria-label="Clear search"
              onClick={() => setSearchTerm("")}
            >
              ×
            </button>
          )}
        </div>

        <nav
          className="admin-navigation"
          aria-label="Admin navigation"
        >
          {filteredGroups.length === 0 ? (
            <p className="admin-no-results">
              No matching sections found.
            </p>
          ) : (
            filteredGroups.map((group) => (
              <div className="admin-nav-group" key={group.title}>
                <p className="admin-nav-heading">{group.title}</p>

                {group.items.map((item) => (
                  <button
                    type="button"
                    key={item.id}
                    className={`admin-nav-item ${
                      activeSection === item.id
                        ? "admin-nav-item-active"
                        : ""
                    }`}
                    onClick={() => handleNavigation(item)}
                    aria-current={
                      activeSection === item.id
                        ? "page"
                        : undefined
                    }
                    title={item.label}
                  >
                    <span
                      className="admin-nav-icon"
                      aria-hidden="true"
                    >
                      {item.icon}
                    </span>

                    <span className="admin-nav-label">
                      {item.label}
                    </span>

                    {activeSection === item.id && (
                      <span className="admin-active-indicator" />
                    )}
                  </button>
                ))}
              </div>
            ))
          )}
        </nav>

        <div className="admin-sidebar-bottom">
          <div className="admin-help-card">
            <div className="admin-help-icon">?</div>
            <strong>Need assistance?</strong>
            <p>
              Manage your platform from this admin workspace.
            </p>

            <button
              type="button"
              onClick={() =>
                showToast(
                  "For technical assistance, contact your SkillSphere project administrator.",
                  "info"
                )
              }
            >
              View help <span aria-hidden="true">↗</span>
            </button>
          </div>

          <button
            type="button"
            className="admin-logout-button"
            onClick={() => setShowLogoutConfirm(true)}
            disabled={logoutPending}
          >
            <span className="admin-nav-icon" aria-hidden="true">
              ⇥
            </span>
            <span>
              {logoutPending ? "Signing out..." : "Logout"}
            </span>
          </button>

          <div className="admin-sidebar-profile">
            <div className="admin-avatar">
              {getInitials(adminName)}
            </div>

            <div className="admin-profile-details">
              <strong>{adminName}</strong>
              <span>Administrator</span>
            </div>

            <button
              type="button"
              className="admin-profile-menu-button"
              aria-label="Profile options"
              aria-expanded={profileOpen}
              onClick={() =>
                setProfileOpen((open) => !open)
              }
            >
              ⋯
            </button>

            {profileOpen && (
              <div className="admin-profile-menu">
                <button
                  type="button"
                  onClick={() => {
                    setProfileOpen(false);
                    showToast(
                      "Administrator profile details are not available in this dashboard yet.",
                      "info"
                    );
                  }}
                >
                  Profile details
                </button>

                <button
                  type="button"
                  onClick={() => {
                    setProfileOpen(false);
                    setShowLogoutConfirm(true);
                  }}
                >
                  Sign out
                </button>
              </div>
            )}
          </div>
        </div>
      </aside>

      <main className="admin-main">
        <header className="admin-topbar">
          <div className="admin-topbar-left">
            <button
              type="button"
              className="admin-menu-toggle"
              aria-label="Open navigation menu"
              onClick={() => setSidebarOpen(true)}
            >
              ☰
            </button>

            <div className="admin-breadcrumb">
              <span>SkillSphere</span>
              <span className="admin-breadcrumb-separator">/</span>
              <strong>{activeItem?.label || "Dashboard"}</strong>
            </div>
          </div>

          <div className="admin-topbar-right">
            <div className="admin-topbar-status">
              <span className="admin-online-dot" />
              Admin workspace
            </div>

            <div className="admin-topbar-divider" />

            <div className="admin-topbar-user">
              <div className="admin-avatar admin-avatar-small">
                {getInitials(adminName)}
              </div>

              <div className="admin-topbar-user-copy">
                <strong>{adminName}</strong>
                <span>Administrator</span>
              </div>
            </div>
          </div>
        </header>

        <div className="admin-page-content">
          <div className="admin-page-heading">
            <div>
              <span className="admin-page-kicker">
                SKILLSPHERE / ADMIN
              </span>

              <h1>{activeItem?.label || "Dashboard"}</h1>

              <p>
                {activeSection === "dashboard"
                  ? "Your platform overview and administration tools."
                  : activeSection === "users"
                  ? "View and manage SkillSphere users."
                  : sectionDetails?.description ||
                    `Manage ${
                      activeItem?.label || "your platform"
                    } in SkillSphere.`}
              </p>
            </div>

            <div className="admin-date-label">
              <span aria-hidden="true">▦</span>
              {new Date().toLocaleDateString(undefined, {
                month: "short",
                day: "numeric",
                year: "numeric",
              })}
            </div>
          </div>

          {renderActiveSection()}

          <footer className="admin-footer">
            <span>
              © {new Date().getFullYear()} SkillSphere
            </span>
            <span>Learn · Build · Grow</span>
          </footer>
        </div>
      </main>

      {showLogoutConfirm && (
        <div
          className="admin-logout-overlay"
          onClick={(event) => {
            if (event.target === event.currentTarget) {
              setShowLogoutConfirm(false);
            }
          }}
        >
          <section
            className="admin-logout-modal"
            role="dialog"
            aria-modal="true"
            aria-labelledby="admin-logout-title"
          >
            <div
              className="admin-logout-modal-icon"
              aria-hidden="true"
            >
              ⇥
            </div>

            <h2 id="admin-logout-title">Confirm Logout</h2>

            <p>
              Are you sure you want to log out of SkillSphere?
            </p>

            <div className="admin-logout-modal-actions">
              <button
                type="button"
                className="admin-logout-cancel"
                onClick={() => setShowLogoutConfirm(false)}
              >
                Cancel
              </button>

              <button
                type="button"
                className="admin-logout-confirm"
                onClick={handleLogout}
                disabled={logoutPending}
              >
                Yes, Logout
              </button>
            </div>
          </section>
        </div>
      )}
    </div>
  );
}

export default AdminDashboard;
