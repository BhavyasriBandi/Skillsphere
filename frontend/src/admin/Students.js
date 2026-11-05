
import React, {
  useCallback,
  useEffect,
  useMemo,
  useState,
} from "react";

import { apiFetch } from "../auth/AuthContext";
import "./Students.css";

const USERS_API = "/api/auth/users/";

// =====================================================
// GET USER ROLE
// =====================================================

function getRole(user) {
  if (typeof user?.role === "string") return user.role;
  if (typeof user?.user_role === "string") return user.user_role;
  if (typeof user?.account_type === "string") return user.account_type;

  if (Array.isArray(user?.groups)) {
    const group = user.groups.find((item) => {
      const name = typeof item === "string" ? item : item?.name;
      return name?.toLowerCase() === "student";
    });

    if (group) {
      return typeof group === "string" ? group : group.name;
    }
  }

  return "";
}

// =====================================================
// GET USER NAME
// =====================================================

function getName(user) {
  return (
    user?.name ||
    [user?.first_name, user?.last_name].filter(Boolean).join(" ") ||
    user?.full_name ||
    user?.username ||
    user?.email ||
    "Unnamed student"
  );
}

// =====================================================
// EXTRACT USERS FROM API RESPONSE
// =====================================================

function getUsers(data) {
  if (Array.isArray(data)) return data;
  if (Array.isArray(data?.results)) return data.results;
  if (Array.isArray(data?.users)) return data.users;
  if (Array.isArray(data?.data)) return data.data;
  return [];
}

// =====================================================
// FORMAT DATE
// =====================================================

function formatDate(value) {
  if (!value) return "—";

  const date = new Date(value);

  if (Number.isNaN(date.getTime())) return "—";

  return date.toLocaleDateString("en-IN", {
    month: "short",
    day: "numeric",
    year: "numeric",
  });
}

// =====================================================
// API REQUEST
// =====================================================

async function apiRequest(path, options = {}) {
  const response = await apiFetch(path, options);
  const data = await response.json().catch(() => ({}));

  if (!response.ok) {
    throw new Error(
      data?.detail ||
        data?.message ||
        data?.error ||
        `Request failed with status ${response.status}.`
    );
  }

  return data;
}

// =====================================================
// STUDENTS COMPONENT
// =====================================================

export default function Students() {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const [search, setSearch] = useState("");
  const [status, setStatus] = useState("all");

  const [selected, setSelected] = useState(null);
  const [updating, setUpdating] = useState(false);

  // Toast state
  const [toast, setToast] = useState(null);

  // ===================================================
  // TOAST MESSAGE
  // ===================================================

  const showStudentToast = useCallback((message, type = "success") => {
    setToast({
      message,
      type,
      id: Date.now(),
    });
  }, []);

  useEffect(() => {
    if (!toast) return;

    const timer = setTimeout(() => {
      setToast(null);
    }, 3500);

    return () => clearTimeout(timer);
  }, [toast]);

  // ===================================================
  // LOAD STUDENTS
  // ===================================================

  const loadStudents = useCallback(async () => {
    setLoading(true);
    setError("");

    try {
      const data = await apiRequest(USERS_API);
      const allUsers = getUsers(data);

      const studentUsers = allUsers.filter(
        (user) =>
          getRole(user).trim().toLowerCase() === "student"
      );

      setStudents(studentUsers);

      return studentUsers;
    } catch (err) {
      console.error("Students API error:", err);

      setError(
        err.message ||
          "Unable to connect to the Django students API."
      );

      return null;
    } finally {
      setLoading(false);
    }
  }, []);

  // ===================================================
  // INITIAL LOAD
  // ===================================================

  useEffect(() => {
    loadStudents();
  }, [loadStudents]);

  // ===================================================
  // STUDENT STATISTICS
  // ===================================================

  const stats = useMemo(() => {
    const active = students.filter(
      (student) => student.is_active !== false
    ).length;

    return {
      total: students.length,
      active,
      inactive: students.length - active,
    };
  }, [students]);

  // ===================================================
  // SEARCH AND STATUS FILTER
  // ===================================================

  const filteredStudents = useMemo(() => {
    const query = search.trim().toLowerCase();

    return students.filter((student) => {
      const matchesSearch =
        !query ||
        [
          getName(student),
          student.email,
          student.username,
          String(student.id ?? ""),
        ]
          .filter(Boolean)
          .some((value) =>
            String(value).toLowerCase().includes(query)
          );

      const active = student.is_active !== false;

      const matchesStatus =
        status === "all" ||
        (status === "active" && active) ||
        (status === "inactive" && !active);

      return matchesSearch && matchesStatus;
    });
  }, [students, search, status]);

  // ===================================================
  // ACTIVATE / DEACTIVATE STUDENT
  // ===================================================

  async function toggleStudentStatus(student) {
    const isCurrentlyActive = student.is_active !== false;

    const nextStatus = isCurrentlyActive ? "Inactive" : "Active";

    const confirmed = window.confirm(
      `${nextStatus === "Active" ? "Activate" : "Deactivate"} ${getName(student)}'s account?`
    );

    if (!confirmed) return;

    setUpdating(true);

    try {
      await apiRequest(`${USERS_API}${student.id}/`, {
        method: "PATCH",
        body: JSON.stringify({
          status: nextStatus,
        }),
      });

      showStudentToast(
        nextStatus === "Active"
          ? "Student account activated successfully!"
          : "Student account deactivated successfully!",
        "success"
      );

      setSelected(null);
      await loadStudents();
    } catch (err) {
      console.error("Student status update error:", err);

      showStudentToast(
        err.message || "Unable to update account status.",
        "error"
      );
    } finally {
      setUpdating(false);
    }
  }

  // ===================================================
  // PROMOTE STUDENT TO MENTOR
  // ===================================================

  async function promoteToMentor(student) {
    const confirmed = window.confirm(
      `Change ${getName(student)}'s role from Student to Mentor?`
    );

    if (!confirmed) return;

    setUpdating(true);

    try {
      await apiRequest(`${USERS_API}${student.id}/role/`, {
        method: "POST",
        body: JSON.stringify({
          role: "Mentor",
        }),
      });

      showStudentToast(
        "Student role changed to Mentor.",
        "success"
      );

      setSelected(null);
      await loadStudents();
    } catch (err) {
      console.error("Promote student error:", err);

      showStudentToast(
        err.message || "Unable to update the student's role.",
        "error"
      );
    } finally {
      setUpdating(false);
    }
  }

  // ===================================================
  // RENDER
  // ===================================================

  return (
    <section className="students-module">

      {/* TOAST NOTIFICATION */}

      {toast && (
        <div
          key={toast.id}
          className={`students-toast students-toast-${toast.type}`}
          role={toast.type === "error" ? "alert" : "status"}
        >
          <span className="students-toast-icon">
            {toast.type === "success" ? "✓" : "!"}
          </span>

          <span className="students-toast-message">
            {toast.message}
          </span>

          <button
            type="button"
            className="students-toast-close"
            onClick={() => setToast(null)}
            aria-label="Close notification"
          >
            ×
          </button>

          <div className="students-toast-progress" />
        </div>
      )}

      {/* INTRODUCTION */}

      <div className="students-intro">
        <div>
          <span className="students-kicker">
            USER DIRECTORY
          </span>

          <h2>Students Overview</h2>

          <p>
            View student accounts, search records, and review
            account status.
          </p>
        </div>

        <button
          type="button"
          className="students-refresh"
          onClick={loadStudents}
          disabled={loading}
        >
          ↻ {loading ? "Loading..." : "Refresh students"}
        </button>
      </div>

      {/* STATISTICS */}

      <div className="students-stats">

        <article>
          <span className="student-stat-icon blue">♧</span>
          <div>
            <small>Total students</small>
            <strong>{loading ? "…" : stats.total}</strong>
          </div>
        </article>

        <article>
          <span className="student-stat-icon green">✓</span>
          <div>
            <small>Active accounts</small>
            <strong>{loading ? "…" : stats.active}</strong>
          </div>
        </article>

        <article>
          <span className="student-stat-icon orange">Ⅱ</span>
          <div>
            <small>Inactive accounts</small>
            <strong>{loading ? "…" : stats.inactive}</strong>
          </div>
        </article>

      </div>

      {/* STUDENT DIRECTORY */}

      <div className="students-panel">

        <div className="students-panel-heading">
          <div>
            <h3>Student Directory</h3>

            <p>
              {loading
                ? "Loading student accounts..."
                : `${filteredStudents.length} student${
                    filteredStudents.length === 1 ? "" : "s"
                  } shown`}
            </p>
          </div>

          {/* SEARCH AND FILTER */}

          <div className="students-controls">

            <label className="students-search">
              <span aria-hidden="true">⌕</span>

              <input
                type="search"
                value={search}
                onChange={(event) => setSearch(event.target.value)}
                placeholder="Search name, email, or ID"
                aria-label="Search students"
              />
            </label>

            <select
              value={status}
              onChange={(event) => setStatus(event.target.value)}
              aria-label="Filter students by status"
            >
              <option value="all">All statuses</option>
              <option value="active">Active</option>
              <option value="inactive">Inactive</option>
            </select>

          </div>
        </div>

        {/* ERROR */}

        {error ? (
          <div className="students-feedback error">
            <strong>Students could not be loaded</strong>

            <p>{error}</p>

            <p>
              Expected API: <code>/api/auth/users/</code>.
              Verify this route in your Django URLs.
            </p>

            <button type="button" onClick={loadStudents}>
              Try again
            </button>
          </div>
        ) : loading ? (
          <div className="students-feedback">
            Loading student accounts...
          </div>
        ) : filteredStudents.length === 0 ? (
          <div className="students-feedback">
            <strong>
              {students.length
                ? "No matching students"
                : "No student accounts found"}
            </strong>

            <p>
              {students.length
                ? "Try a different search or status filter."
                : "Accounts assigned the Student role will appear here."}
            </p>
          </div>
        ) : (
          <div className="students-table-wrap">
            <table className="students-table">

              <thead>
                <tr>
                  <th>Student</th>
                  <th>ID</th>
                  <th>Registered</th>
                  <th>Status</th>
                  <th>Action</th>
                </tr>
              </thead>

              <tbody>
                {filteredStudents.map((student) => {
                  const active = student.is_active !== false;

                  return (
                    <tr key={student.id ?? student.email}>
                      <td>
                        <div className="students-person">
                          <span className="students-avatar">
                            {getName(student)
                              .slice(0, 1)
                              .toUpperCase()}
                          </span>

                          <span>
                            <strong>{getName(student)}</strong>
                            <small>
                              {student.email || "No email"}
                            </small>
                          </span>
                        </div>
                      </td>

                      <td>#{student.id ?? "—"}</td>

                      <td>
                        {formatDate(
                          student.date_joined ||
                            student.created_at ||
                            student.createdAt
                        )}
                      </td>

                      <td>
                        <span
                          className={`students-status ${
                            active ? "active" : "inactive"
                          }`}
                        >
                          <i />
                          {active ? "Active" : "Inactive"}
                        </span>
                      </td>

                      <td>
                        <button
                          type="button"
                          className="students-view"
                          onClick={() => setSelected(student)}
                        >
                          View details
                        </button>
                      </td>
                    </tr>
                  );
                })}
              </tbody>

            </table>
          </div>
        )}

      </div>

      {/* STUDENT DETAILS MODAL */}

      {selected && (
        <div
          className="students-modal-shade"
          onMouseDown={(event) => {
            if (
              event.target === event.currentTarget &&
              !updating
            ) {
              setSelected(null);
            }
          }}
        >
          <section
            className="students-modal"
            role="dialog"
            aria-modal="true"
            aria-labelledby="student-detail-title"
          >

            <button
              className="students-modal-x"
              type="button"
              aria-label="Close student details"
              onClick={() => setSelected(null)}
              disabled={updating}
            >
              ×
            </button>

            <span className="students-kicker">
              STUDENT ACCOUNT
            </span>

            <h3 id="student-detail-title">
              {getName(selected)}
            </h3>

            <dl>
              <div>
                <dt>Student ID</dt>
                <dd>{selected.id ?? "—"}</dd>
              </div>

              <div>
                <dt>Email</dt>
                <dd>{selected.email || "—"}</dd>
              </div>

              <div>
                <dt>Username</dt>
                <dd>{selected.username || "—"}</dd>
              </div>

              <div>
                <dt>Registration date</dt>
                <dd>
                  {formatDate(
                    selected.date_joined ||
                      selected.created_at ||
                      selected.createdAt
                  )}
                </dd>
              </div>

              <div>
                <dt>Account status</dt>
                <dd>
                  {selected.is_active === false
                    ? "Inactive"
                    : "Active"}
                </dd>
              </div>
            </dl>

            <p className="students-modal-note">
              Manage the student's account status or promote
              the student to a Mentor role.
            </p>

            <div className="students-modal-actions">

              <button
                type="button"
                className="students-cancel"
                onClick={() => setSelected(null)}
                disabled={updating}
              >
                Close
              </button>

              <button
                type="button"
                className="students-promote"
                disabled={updating}
                onClick={() => toggleStudentStatus(selected)}
              >
                {updating
                  ? "Updating..."
                  : selected.is_active === false
                    ? "Activate Account"
                    : "Deactivate Account"}
              </button>

              <button
                type="button"
                className="students-promote"
                disabled={updating}
                onClick={() => promoteToMentor(selected)}
              >
                {updating ? "Updating..." : "Promote to Mentor"}
              </button>

            </div>
          </section>
        </div>
      )}

    </section>
  );
}
