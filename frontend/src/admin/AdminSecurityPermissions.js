
import React, { useEffect, useMemo, useState } from "react";
import { showToast } from "../components/ToastProvider";
import "./AdminSecurityPermissions.css";

const API_BASE_URL = "https://skillsphere-17hl.onrender.com";

const ROLE_PERMISSIONS = [
  {
    role: "Admin",
    description: "Platform administration",
    permissions: [
      "Manage users and roles",
      "Configure platform settings",
      "Manage platform content",
      "Review security configuration",
    ],
  },
  {
    role: "Mentor",
    description: "Learning guidance",
    permissions: [
      "Access mentor features",
      "Guide assigned students",
      "Support learning activities",
      "Manage permitted learning tasks",
    ],
  },
  {
    role: "Student",
    description: "Personal learning",
    permissions: [
      "Manage own profile",
      "Complete skill assessments",
      "View personal roadmap",
      "Track own learning progress",
    ],
  },
];

function getToken() {
  return (
    localStorage.getItem("access") ||
    localStorage.getItem("skillsphere_access") ||
    ""
  );
}

function AdminSecurityPermissions() {
  const [users, setUsers] = useState([]);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);
  const [savingId, setSavingId] = useState(null);
  const [selectedRoles, setSelectedRoles] = useState({});
  const [error, setError] = useState("");

  useEffect(() => {
    loadUsers();
  }, []);

  async function loadUsers() {
    setLoading(true);
    setError("");

    const token = getToken();

    if (!token) {
      setError("Your session has expired. Please log in again.");
      setLoading(false);
      return;
    }

    try {
      const response = await fetch(`${API_BASE_URL}/api/auth/users/`, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
      });

      const data = await response.json().catch(() => ({}));

      if (!response.ok) {
        throw new Error(
          data.detail ||
            data.message ||
            `Unable to load users (${response.status}).`
        );
      }

      const userList = Array.isArray(data)
        ? data
        : Array.isArray(data.results)
          ? data.results
          : [];

      setUsers(userList);

      const roles = {};
      userList.forEach((user) => {
        roles[user.id] = user.role || "Student";
      });
      setSelectedRoles(roles);
    } catch (err) {
      setError(err.message || "Unable to connect to the backend.");
    } finally {
      setLoading(false);
    }
  }

  const filteredUsers = useMemo(() => {
    const query = search.trim().toLowerCase();

    if (!query) return users;

    return users.filter((user) =>
      [
        user.first_name,
        user.last_name,
        user.username,
        user.email,
        user.role,
      ]
        .filter(Boolean)
        .join(" ")
        .toLowerCase()
        .includes(query)
    );
  }, [users, search]);

  async function saveRole(user) {
    const role = selectedRoles[user.id];

    if (!["Student", "Mentor", "Admin"].includes(role)) {
      showToast("Please select a valid role.", "error");
      return;
    }

    if (role === user.role) {
      showToast("No role changes to save.", "info");
      return;
    }

    const token = getToken();

    if (!token) {
      showToast("Your session has expired. Please log in again.", "error");
      return;
    }

    setSavingId(user.id);

    try {
      const response = await fetch(
        `${API_BASE_URL}/api/auth/users/${user.id}/role/`,
        {
          method: "POST",
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ role }),
        }
      );

      const data = await response.json().catch(() => ({}));

      if (!response.ok) {
        throw new Error(
          data.detail ||
            data.message ||
            `Role update failed (${response.status}).`
        );
      }

      showToast(data.message || "Role updated successfully.", "success");
      await loadUsers();
    } catch (err) {
      showToast(err.message || "Unable to update the role.", "error");
    } finally {
      setSavingId(null);
    }
  }

  const roleCounts = {
    Admin: users.filter((user) => user.role === "Admin").length,
    Mentor: users.filter((user) => user.role === "Mentor").length,
    Student: users.filter((user) => user.role === "Student").length,
  };

  return (
    <section className="asp-page">
      <header className="asp-header">
        <div>
          <span className="asp-eyebrow">PLATFORM CONTROL</span>
          <h1>Security &amp; Permissions</h1>
          <p>
            Review platform security and manage access according to user roles.
          </p>
        </div>

        <button
          type="button"
          className="asp-refresh-button"
          onClick={loadUsers}
          disabled={loading}
        >
          {loading ? "Loading..." : "↻ Refresh"}
        </button>
      </header>

      <div className="asp-security-banner">
        <span className="asp-shield" aria-hidden="true">✓</span>
        <div>
          <h2>Access control overview</h2>
          <p>
            Use authenticated API requests and server-side role checks to
            protect administrative actions. The information below summarizes
            the configured security approach.
          </p>
        </div>
      </div>

      <div className="asp-stat-grid">
        <article className="asp-stat-card">
          <span className="asp-stat-icon">♙</span>
          <span>Total accounts</span>
          <strong>{users.length}</strong>
        </article>

        <article className="asp-stat-card">
          <span className="asp-stat-icon">♜</span>
          <span>Administrators</span>
          <strong>{roleCounts.Admin}</strong>
        </article>

        <article className="asp-stat-card">
          <span className="asp-stat-icon">◇</span>
          <span>Mentors</span>
          <strong>{roleCounts.Mentor}</strong>
        </article>

        <article className="asp-stat-card">
          <span className="asp-stat-icon">♧</span>
          <span>Students</span>
          <strong>{roleCounts.Student}</strong>
        </article>
      </div>

      <section className="asp-panel">
        <div className="asp-panel-heading">
          <div>
            <h2>Role permissions</h2>
            <p>Expected access boundaries for each SkillSphere role.</p>
          </div>
        </div>

        <div className="asp-role-grid">
          {ROLE_PERMISSIONS.map((item) => (
            <article className="asp-role-card" key={item.role}>
              <div className="asp-role-top">
                <span className={`asp-role-badge asp-role-${item.role.toLowerCase()}`}>
                  {item.role}
                </span>
              </div>

              <h3>{item.description}</h3>

              <ul>
                {item.permissions.map((permission) => (
                  <li key={permission}>
                    <span aria-hidden="true">✓</span>
                    {permission}
                  </li>
                ))}
              </ul>
            </article>
          ))}
        </div>

        <p className="asp-note">
          Note: This matrix documents the intended access policy. Each API
          endpoint must enforce its permissions on the backend.
        </p>
      </section>

      <section className="asp-panel">
        <div className="asp-panel-heading asp-user-heading">
          <div>
            <h2>Account role management</h2>
            <p>Review registered accounts and update roles when authorized.</p>
          </div>

          <input
            type="search"
            className="asp-search"
            placeholder="Search name, email or role..."
            value={search}
            onChange={(event) => setSearch(event.target.value)}
            aria-label="Search accounts"
          />
        </div>

        {error && (
          <div className="asp-error" role="alert">
            <p>{error}</p>
            <button type="button" onClick={loadUsers}>Try again</button>
          </div>
        )}

        {loading ? (
          <div className="asp-empty">Loading registered accounts...</div>
        ) : !error && filteredUsers.length === 0 ? (
          <div className="asp-empty">No matching accounts found.</div>
        ) : (
          !error && (
            <div className="asp-table-wrap">
              <table className="asp-table">
                <thead>
                  <tr>
                    <th>Account</th>
                    <th>Email</th>
                    <th>Current role</th>
                    <th>Change role</th>
                    <th>Action</th>
                  </tr>
                </thead>

                <tbody>
                  {filteredUsers.map((user) => {
                    const fullName =
                      `${user.first_name || ""} ${user.last_name || ""}`.trim() ||
                      user.username ||
                      "User";

                    return (
                      <tr key={user.id}>
                        <td>
                          <div className="asp-account">
                            <span className="asp-avatar">
                              {fullName.charAt(0).toUpperCase()}
                            </span>
                            <span>{fullName}</span>
                          </div>
                        </td>

                        <td>{user.email || "—"}</td>

                        <td>
                          <span className="asp-current-role">
                            {user.role || "Unassigned"}
                          </span>
                        </td>

                        <td>
                          <select
                            className="asp-role-select"
                            value={selectedRoles[user.id] || "Student"}
                            onChange={(event) =>
                              setSelectedRoles((previous) => ({
                                ...previous,
                                [user.id]: event.target.value,
                              }))
                            }
                            aria-label={`Choose role for ${user.email || fullName}`}
                          >
                            <option value="Student">Student</option>
                            <option value="Mentor">Mentor</option>
                            <option value="Admin">Admin</option>
                          </select>
                        </td>

                        <td>
                          <button
                            type="button"
                            className="asp-save-button"
                            onClick={() => saveRole(user)}
                            disabled={
                              savingId === user.id ||
                              selectedRoles[user.id] === user.role
                            }
                          >
                            {savingId === user.id ? "Saving..." : "Save"}
                          </button>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          )
        )}
      </section>

      <section className="asp-panel">
        <div className="asp-panel-heading">
          <div>
            <h2>Security checklist</h2>
            <p>Important safeguards for the application.</p>
          </div>
        </div>

        <div className="asp-checklist">
          <div className="asp-check-row">
            <span className="asp-check-icon">✓</span>
            <div>
              <strong>JWT authentication</strong>
              <p>Protected requests should include a valid access token.</p>
            </div>
          </div>

          <div className="asp-check-row">
            <span className="asp-check-icon">✓</span>
            <div>
              <strong>Server-side role validation</strong>
              <p>Administrative APIs should verify the caller's role.</p>
            </div>
          </div>

          <div className="asp-check-row">
            <span className="asp-check-icon">✓</span>
            <div>
              <strong>Password protection</strong>
              <p>Passwords must be stored using Django's password hashing.</p>
            </div>
          </div>

          <div className="asp-check-row">
            <span className="asp-check-icon">✓</span>
            <div>
              <strong>Email verification</strong>
              <p>Registration should follow the existing email verification flow.</p>
            </div>
          </div>
        </div>

        <p className="asp-note">
          These checklist items describe required safeguards; their presence
          here does not independently verify every endpoint or setting.
        </p>
      </section>
    </section>
  );
}

export default AdminSecurityPermissions;
