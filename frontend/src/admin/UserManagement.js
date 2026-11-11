
import React, {
  useCallback,
  useEffect,
  useMemo,
  useState,
} from "react";

import { apiFetch } from "../auth/AuthContext";
import { showToast } from "../components/ToastProvider";
import "./UserManagement.css";

const emptyForm = {
  name: "",
  email: "",
  role: "Student",
  status: "Active",
};

// =====================================================
// NORMALIZE USER DATA
// =====================================================

function normalizeUser(user) {
  const name =
    user.name ||
    `${user.first_name || ""} ${user.last_name || ""}`.trim() ||
    user.email ||
    "Unnamed User";

  return {
    id: user.id,
    name,
    email: user.email || "",
    role: user.role || "Unassigned",
    status:
      user.status ||
      (user.is_active ? "Active" : "Inactive"),
    joined:
      user.joined ||
      (user.date_joined
        ? user.date_joined.slice(0, 10)
        : ""),
  };
}

// =====================================================
// AUTHENTICATED API REQUEST
// =====================================================

async function apiRequest(path = "", options = {}) {
  const response = await apiFetch(
    `/api/auth/users/${path}`,
    options
  );

  const data = await response.json().catch(() => ({}));

  if (!response.ok) {
    if (
      response.status === 401 ||
      response.status === 403
    ) {
      throw new Error(
        data.detail ||
          data.message ||
          "Access denied. Please log in with an administrator account."
      );
    }

    const detail =
      data.detail ||
      data.email?.[0] ||
      data.name?.[0] ||
      data.role?.[0] ||
      data.status?.[0] ||
      data.error;

    throw new Error(
      detail || `Request failed (${response.status}).`
    );
  }

  return data;
}

// =====================================================
// USER MANAGEMENT COMPONENT
// =====================================================

export default function UserManagement() {
  const [users, setUsers] = useState([]);
  const [search, setSearch] = useState("");
  const [roleFilter, setRoleFilter] = useState("All");
  const [statusFilter, setStatusFilter] = useState("All");

  const [modalOpen, setModalOpen] = useState(false);
  const [editingId, setEditingId] = useState(null);
  const [form, setForm] = useState(emptyForm);

  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [pageError, setPageError] = useState("");

  // ===================================================
  // LOAD USERS
  // ===================================================

  const loadUsers = useCallback(async () => {
    setLoading(true);
    setPageError("");

    try {
      const data = await apiRequest();

      const results = Array.isArray(data)
        ? data
        : data.results;

      if (!Array.isArray(results)) {
        throw new Error(
          "The server returned an unexpected user list."
        );
      }

      setUsers(results.map(normalizeUser));
    } catch (err) {
      setPageError(
        err.message || "Could not load users."
      );
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadUsers();
  }, [loadUsers]);

  // ===================================================
  // SEARCH AND FILTER
  // ===================================================

  const filteredUsers = useMemo(() => {
    const query = search.trim().toLowerCase();

    return users.filter((user) => {
      const matchesSearch =
        user.name.toLowerCase().includes(query) ||
        user.email.toLowerCase().includes(query);

      const matchesRole =
        roleFilter === "All" ||
        user.role === roleFilter;

      const matchesStatus =
        statusFilter === "All" ||
        user.status === statusFilter;

      return (
        matchesSearch &&
        matchesRole &&
        matchesStatus
      );
    });
  }, [users, search, roleFilter, statusFilter]);

  // ===================================================
  // STATISTICS
  // ===================================================

  const activeCount = users.filter(
    (user) => user.status === "Active"
  ).length;

  const studentCount = users.filter(
    (user) => user.role === "Student"
  ).length;

  const mentorCount = users.filter(
    (user) => user.role === "Mentor"
  ).length;

  // ===================================================
  // ADD USER
  // ===================================================

  function openAddModal() {
    setEditingId(null);
    setForm({ ...emptyForm });
    setError("");
    setModalOpen(true);
  }

  // ===================================================
  // EDIT USER
  // ===================================================

  function openEditModal(user) {
    setEditingId(user.id);

    setForm({
      name: user.name,
      email: user.email,
      role: user.role,
      status: user.status,
    });

    setError("");
    setModalOpen(true);
  }

  // ===================================================
  // CLOSE MODAL
  // ===================================================

  function closeModal() {
    if (saving) return;

    setModalOpen(false);
    setEditingId(null);
    setForm({ ...emptyForm });
    setError("");
  }

  // ===================================================
  // ADD / UPDATE USER
  // ===================================================

  async function handleSubmit(event) {
    event.preventDefault();

    const name = form.name.trim();
    const email = form.email.trim().toLowerCase();

    if (!name || !email) {
      setError("Please enter both name and email.");
      return;
    }

    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!emailPattern.test(email)) {
      setError("Please enter a valid email address.");
      return;
    }

    const emailExists = users.some(
      (user) =>
        user.email.toLowerCase() === email &&
        String(user.id) !== String(editingId)
    );

    if (emailExists) {
      setError("A user with this email already exists.");
      return;
    }

    setSaving(true);
    setError("");

    try {
      if (editingId !== null) {
        const originalUser = users.find(
          (user) =>
            String(user.id) === String(editingId)
        );

        // Update name and email.
        await apiRequest(`${editingId}/`, {
          method: "PATCH",
          body: JSON.stringify({
            name,
            email,
          }),
        });

        // Update role using the existing role endpoint.
        if (
          originalUser &&
          originalUser.role !== form.role
        ) {
          await apiRequest(`${editingId}/role/`, {
            method: "POST",
            body: JSON.stringify({
              role: form.role,
            }),
          });
        }

        // Update account status using the existing endpoint.
        if (
          originalUser &&
          originalUser.status !== form.status
        ) {
          await apiRequest(`${editingId}/status/`, {
            method: "PATCH",
            body: JSON.stringify({
              is_active: form.status === "Active",
            }),
          });
        }

        showToast(
          "User details updated successfully!",
          "success"
        );
      } else {
        // Backend must create the account and send
        // a secure password setup email.
        await apiRequest("", {
          method: "POST",
          body: JSON.stringify({
            name,
            email,
            role: form.role,
          }),
        });

        showToast(
          "User created. Password setup email sent successfully!",
          "success"
        );
      }

      setModalOpen(false);
      setEditingId(null);
      setForm({ ...emptyForm });

      await loadUsers();
    } catch (err) {
      setError(
        err.message || "Could not save user."
      );
    } finally {
      setSaving(false);
    }
  }

  // ===================================================
  // ACTIVATE / DEACTIVATE USER
  // ===================================================

  async function toggleStatus(user) {
    const nextStatus =
      user.status === "Active"
        ? "Inactive"
        : "Active";

    const confirmed = window.confirm(
      `${nextStatus === "Active" ? "Activate" : "Deactivate"} ${user.name}'s account?`
    );

    if (!confirmed) return;

    try {
      await apiRequest(`${user.id}/status/`, {
        method: "PATCH",
        body: JSON.stringify({
          is_active: nextStatus === "Active",
        }),
      });

      showToast(
        nextStatus === "Active"
          ? "User account activated successfully!"
          : "User account deactivated successfully!",
        "success"
      );

      await loadUsers();
    } catch (err) {
      showToast(
        err.message || "Could not update user status.",
        "error"
      );
    }
  }

  // ===================================================
  // DELETE USER
  // ===================================================

  async function deleteUser(user) {
    const confirmed = window.confirm(
      `Are you sure you want to delete ${user.name}? This action cannot be undone.`
    );

    if (!confirmed) return;

    try {
      await apiRequest(`${user.id}/`, {
        method: "DELETE",
      });

      showToast(
        "User deleted successfully!",
        "success"
      );

      await loadUsers();
    } catch (err) {
      showToast(
        err.message || "Could not delete user.",
        "error"
      );
    }
  }

  // ===================================================
  // UI
  // ===================================================

  return (
    <main className="um-page">

      {/* HEADER */}

      <header className="um-header">
        <div>
          <span className="um-eyebrow">
            ADMINISTRATION
          </span>

          <h1>User Management</h1>

          <p>
            Manage SkillSphere users, roles, and account access.
          </p>
        </div>

        <button
          className="um-primary-btn"
          onClick={openAddModal}
        >
          <span aria-hidden="true">＋</span> Add User
        </button>
      </header>

      {/* STATISTICS */}

      <section className="um-stats">

        <article className="um-stat-card">
          <div className="um-stat-icon um-icon-blue">
            ◉
          </div>

          <div>
            <p>Total Users</p>
            <h2>{users.length}</h2>
            <span>All registered accounts</span>
          </div>
        </article>

        <article className="um-stat-card">
          <div className="um-stat-icon um-icon-green">
            ✓
          </div>

          <div>
            <p>Active Users</p>
            <h2>{activeCount}</h2>
            <span>Currently marked active</span>
          </div>
        </article>

        <article className="um-stat-card">
          <div className="um-stat-icon um-icon-purple">
            ◈
          </div>

          <div>
            <p>Students</p>
            <h2>{studentCount}</h2>
            <span>Student accounts</span>
          </div>
        </article>

        <article className="um-stat-card">
          <div className="um-stat-icon um-icon-orange">
            ★
          </div>

          <div>
            <p>Mentors</p>
            <h2>{mentorCount}</h2>
            <span>Mentor accounts</span>
          </div>
        </article>

      </section>

      {/* USERS TABLE */}

      <section className="um-table-card">

        <div className="um-table-heading">
          <div>
            <h2>All Users</h2>
            <p>
              Search and manage registered accounts.
            </p>
          </div>

          <span className="um-result-count">
            {filteredUsers.length} results
          </span>
        </div>

        {/* FILTERS */}

        <div className="um-filters">

          <label className="um-search">
            <span aria-hidden="true">⌕</span>

            <input
              type="search"
              placeholder="Search by name or email..."
              value={search}
              onChange={(event) =>
                setSearch(event.target.value)
              }
            />
          </label>

          <select
            aria-label="Filter by role"
            value={roleFilter}
            onChange={(event) =>
              setRoleFilter(event.target.value)
            }
          >
            <option value="All">All Roles</option>
            <option value="Student">Students</option>
            <option value="Mentor">Mentors</option>
            <option value="Admin">Admins</option>
          </select>

          <select
            aria-label="Filter by status"
            value={statusFilter}
            onChange={(event) =>
              setStatusFilter(event.target.value)
            }
          >
            <option value="All">All Statuses</option>
            <option value="Active">Active</option>
            <option value="Inactive">Inactive</option>
          </select>

        </div>

        {/* ERROR */}

        {pageError && (
          <div
            role="alert"
            className="um-form-error"
          >
            {pageError}

            <button
              type="button"
              onClick={loadUsers}
            >
              Retry
            </button>
          </div>
        )}

        {/* TABLE */}

        <div className="um-table-wrapper">
          <table className="um-table">

            <thead>
              <tr>
                <th>User</th>
                <th>Role</th>
                <th>Status</th>
                <th>Date Joined</th>
                <th>Actions</th>
              </tr>
            </thead>

            <tbody>

              {loading ? (
                <tr>
                  <td
                    colSpan="5"
                    className="um-empty"
                  >
                    Loading users from database...
                  </td>
                </tr>
              ) : (
                <>
                  {filteredUsers.map((user) => (
                    <tr key={user.id}>

                      <td>
                        <div className="um-user-cell">

                          <div className="um-avatar">
                            {user.name
                              .split(" ")
                              .filter(Boolean)
                              .map((part) => part[0])
                              .join("")
                              .slice(0, 2)
                              .toUpperCase()}
                          </div>

                          <div className="um-user-info">
                            <strong>{user.name}</strong>
                            <span>{user.email}</span>
                          </div>

                        </div>
                      </td>

                      <td>
                        <span
                          className={`um-role um-role-${user.role.toLowerCase()}`}
                        >
                          {user.role}
                        </span>
                      </td>

                      <td>
                        <span
                          className={`um-status um-status-${user.status.toLowerCase()}`}
                        >
                          <span className="um-status-dot" />
                          {user.status}
                        </span>
                      </td>

                      <td>
                        {user.joined
                          ? new Date(
                              `${user.joined}T00:00:00`
                            ).toLocaleDateString("en-IN", {
                              day: "2-digit",
                              month: "short",
                              year: "numeric",
                            })
                          : "—"}
                      </td>

                      <td>
                        <div className="um-actions">

                          <button
                            type="button"
                            className="um-action-btn"
                            onClick={() =>
                              openEditModal(user)
                            }
                            aria-label={`Edit ${user.name}`}
                            title="Edit user"
                          >
                            ✎
                          </button>

                          <button
                            type="button"
                            className="um-action-btn"
                            onClick={() =>
                              toggleStatus(user)
                            }
                            aria-label={`Change status for ${user.name}`}
                            title={
                              user.status === "Active"
                                ? "Deactivate user"
                                : "Activate user"
                            }
                          >
                            {user.status === "Active"
                              ? "◉"
                              : "✓"}
                          </button>

                          <button
                            type="button"
                            className="um-action-btn um-delete-btn"
                            onClick={() =>
                              deleteUser(user)
                            }
                            aria-label={`Delete ${user.name}`}
                            title="Delete user"
                          >
                            ×
                          </button>

                        </div>
                      </td>

                    </tr>
                  ))}

                  {filteredUsers.length === 0 && (
                    <tr>
                      <td
                        colSpan="5"
                        className="um-empty"
                      >
                        <div>⌕</div>
                        <strong>No users found</strong>
                        <span>
                          Try changing your search or filters.
                        </span>
                      </td>
                    </tr>
                  )}
                </>
              )}

            </tbody>
          </table>
        </div>

        <div className="um-table-footer">
          Showing {filteredUsers.length} of {users.length} users
        </div>

      </section>

      {/* ADD / EDIT MODAL */}

      {modalOpen && (
        <div
          className="um-modal-backdrop"
          onMouseDown={(event) => {
            if (event.target === event.currentTarget) {
              closeModal();
            }
          }}
        >
          <section
            className="um-modal"
            role="dialog"
            aria-modal="true"
            aria-labelledby="um-modal-title"
          >

            <div className="um-modal-header">
              <div>
                <span className="um-eyebrow">
                  USER ADMINISTRATION
                </span>

                <h2 id="um-modal-title">
                  {editingId !== null
                    ? "Edit User"
                    : "Add New User"}
                </h2>
              </div>

              <button
                type="button"
                className="um-modal-close"
                onClick={closeModal}
                aria-label="Close dialog"
              >
                ×
              </button>
            </div>

            <form onSubmit={handleSubmit}>

              <label className="um-form-field">
                Full Name

                <input
                  type="text"
                  value={form.name}
                  onChange={(event) =>
                    setForm({
                      ...form,
                      name: event.target.value,
                    })
                  }
                  placeholder="Enter full name"
                  required
                  autoFocus
                />
              </label>

              <label className="um-form-field">
                Email Address

                <input
                  type="email"
                  value={form.email}
                  onChange={(event) =>
                    setForm({
                      ...form,
                      email: event.target.value,
                    })
                  }
                  placeholder="name@example.com"
                  required
                />
              </label>

              <div className="um-form-row">

                <label className="um-form-field">
                  Role

                  <select
                    value={form.role}
                    onChange={(event) =>
                      setForm({
                        ...form,
                        role: event.target.value,
                      })
                    }
                  >
                    <option value="Student">Student</option>
                    <option value="Mentor">Mentor</option>
                    <option value="Admin">Admin</option>
                  </select>
                </label>

                <label className="um-form-field">
                  Status

                  <select
                    value={form.status}
                    onChange={(event) =>
                      setForm({
                        ...form,
                        status: event.target.value,
                      })
                    }
                  >
                    <option value="Active">Active</option>
                    <option value="Inactive">Inactive</option>
                  </select>
                </label>

              </div>

              {error && (
                <p className="um-form-error">
                  {error}
                </p>
              )}

              <div className="um-modal-actions">

                <button
                  type="button"
                  className="um-secondary-btn"
                  onClick={closeModal}
                  disabled={saving}
                >
                  Cancel
                </button>

                <button
                  type="submit"
                  className="um-primary-btn"
                  disabled={saving}
                >
                  {saving
                    ? "Saving..."
                    : editingId !== null
                      ? "Save Changes"
                      : "Create User"}
                </button>

              </div>

            </form>

          </section>
        </div>
      )}

    </main>
  );
}
