
import React, { useCallback, useEffect, useState } from "react";
import "./MyStudents.css";

const API_BASE_URL = "https://skillsphere-u93o.onrender.com";

function MyStudents() {
  const [assignments, setAssignments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [actionLoading, setActionLoading] = useState(null);
  const [search, setSearch] = useState("");
  const [filter, setFilter] = useState("All");
  const [toast, setToast] = useState(null);
  const [toastKey, setToastKey] = useState(0);
  const [error, setError] = useState("");

  // Same three-second timer toast used by Mentor Profile.
  useEffect(() => {
    if (!toast) return;

    const timer = setTimeout(() => {
      setToast(null);
    }, 3000);

    return () => clearTimeout(timer);
  }, [toast, toastKey]);

  const showToast = (type, message) => {
    setToast({ type, message });
    setToastKey((previous) => previous + 1);
  };

  const getToken = () => {
    const token = localStorage.getItem("skillsphere_access");

    if (!token) {
      throw new Error("Access token not found. Please login again.");
    }

    return token;
  };

  const fetchStudents = useCallback(async () => {
    try {
      setLoading(true);
      setError("");

      const token = getToken();

      const response = await fetch(
        `${API_BASE_URL}/api/mentors/my-students/`,
        {
          method: "GET",
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || data.message || "Unable to load students."
        );
      }

      setAssignments(
        Array.isArray(data.assignments) ? data.assignments : []
      );
    } catch (err) {
      setError(err.message || "Something went wrong.");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchStudents();
  }, [fetchStudents]);

  const getStudentName = (item) => {
    return (
      item.student_name ||
      item.student_full_name ||
      item.student_details?.full_name ||
      item.student_details?.name ||
      item.student?.full_name ||
      item.student?.name ||
      item.student_username ||
      item.student ||
      "Student"
    );
  };

  const getStudentEmail = (item) => {
    return (
      item.student_email ||
      item.student_details?.email ||
      item.student?.email ||
      ""
    );
  };

  const getStatus = (item) => {
    return item.status || item.assignment_status || "Pending";
  };

  const getAssignmentId = (item) => {
    return item.id || item.assignment_id;
  };

  const handleDecision = async (assignmentId, newStatus) => {
    try {
      setActionLoading(assignmentId);
      const token = getToken();

      const response = await fetch(
        `${API_BASE_URL}/api/mentors/my-students/${assignmentId}/`,
        {
          method: "PATCH",
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ status: newStatus }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || data.message || "Unable to update request."
        );
      }

      showToast(
        "success",
        data.message ||
          `Mentorship request ${newStatus.toLowerCase()} successfully.`
      );

      await fetchStudents();
    } catch (err) {
      showToast(
        "error",
        err.message || "Unable to update mentorship request."
      );
    } finally {
      setActionLoading(null);
    }
  };

  const filteredAssignments = assignments.filter((item) => {
    const name = getStudentName(item).toLowerCase();
    const email = getStudentEmail(item).toLowerCase();
    const query = search.toLowerCase();
    const status = getStatus(item);

    const matchesSearch =
      name.includes(query) || email.includes(query);

    const matchesFilter =
      filter === "All" || status.toLowerCase() === filter.toLowerCase();

    return matchesSearch && matchesFilter;
  });

  const totalCount = assignments.length;
  const activeCount = assignments.filter(
    (item) => getStatus(item) === "Active"
  ).length;
  const pendingCount = assignments.filter(
    (item) => getStatus(item) === "Pending"
  ).length;
  const rejectedCount = assignments.filter(
    (item) => getStatus(item) === "Rejected"
  ).length;

  if (loading) {
    return (
      <section className="mentor-students-content">
        <div className="mentor-students-message">
          Loading your students...
        </div>
      </section>
    );
  }

  return (
    <section className="mentor-students-content">
      {/* TIMER TOAST */}
      {toast && (
        <div
          key={toastKey}
          className={`mentor-students-toast ${toast.type}`}
          role={toast.type === "error" ? "alert" : "status"}
        >
          <span className="mentor-students-toast-icon">
            {toast.type === "success" ? "✓" : "!"}
          </span>

          <div className="mentor-students-toast-text">
            <strong>
              {toast.type === "success" ? "SUCCESS" : "ERROR"}
            </strong>
            <p>{toast.message}</p>
          </div>

          <button
            type="button"
            onClick={() => setToast(null)}
            aria-label="Close notification"
          >
            ×
          </button>

          <div className="mentor-students-toast-progress" />
        </div>
      )}

      <div className="mentor-students-heading">
        <div>
          <h1>My Students</h1>
          <p>Manage your students and mentorship requests.</p>
        </div>

        <button
          type="button"
          className="mentor-students-refresh"
          onClick={fetchStudents}
        >
          ↻ Refresh
        </button>
      </div>

      {error && (
        <div className="mentor-students-error">
          <span>{error}</span>
          <button type="button" onClick={fetchStudents}>
            Try Again
          </button>
        </div>
      )}

      {/* SUMMARY CARDS */}
      <div className="mentor-students-stats">
        <div className="mentor-students-stat-card">
          <span>👨‍🎓</span>
          <div>
            <p>Total Assignments</p>
            <h2>{totalCount}</h2>
          </div>
        </div>

        <div className="mentor-students-stat-card">
          <span>🟢</span>
          <div>
            <p>Active Students</p>
            <h2>{activeCount}</h2>
          </div>
        </div>

        <div className="mentor-students-stat-card">
          <span>⏳</span>
          <div>
            <p>Pending Requests</p>
            <h2>{pendingCount}</h2>
          </div>
        </div>

        <div className="mentor-students-stat-card">
          <span>↩️</span>
          <div>
            <p>Rejected Requests</p>
            <h2>{rejectedCount}</h2>
          </div>
        </div>
      </div>

      {/* STUDENT LIST */}
      <div className="mentor-students-panel">
        <div className="mentor-students-panel-heading">
          <div>
            <h3>Student Directory</h3>
            <p>View and manage your mentorship assignments.</p>
          </div>

          <input
            type="search"
            placeholder="Search by name or email..."
            value={search}
            onChange={(event) => setSearch(event.target.value)}
          />
        </div>

        <div className="mentor-students-filters">
          {["All", "Active", "Pending", "Rejected"].map((item) => (
            <button
              key={item}
              type="button"
              className={filter === item ? "selected" : ""}
              onClick={() => setFilter(item)}
            >
              {item}
            </button>
          ))}
        </div>

        {filteredAssignments.length > 0 ? (
          <div className="mentor-students-table-wrapper">
            <table className="mentor-students-table">
              <thead>
                <tr>
                  <th>Student</th>
                  <th>Email</th>
                  <th>Status</th>
                  <th>Assigned Date</th>
                  <th>Actions</th>
                </tr>
              </thead>

              <tbody>
                {filteredAssignments.map((item) => {
                  const id = getAssignmentId(item);
                  const name = getStudentName(item);
                  const email = getStudentEmail(item);
                  const status = getStatus(item);
                  const isBusy = actionLoading === id;

                  return (
                    <tr key={id}>
                      <td>
                        <div className="mentor-students-person">
                          <div className="mentor-students-avatar">
                            {String(name).charAt(0).toUpperCase()}
                          </div>
                          <strong>{name}</strong>
                        </div>
                      </td>

                      <td>{email || "Not available"}</td>

                      <td>
                        <span
                          className={`mentor-students-status ${status.toLowerCase()}`}
                        >
                          {status}
                        </span>
                      </td>

                      <td>
                        {item.assigned_at
                          ? new Date(item.assigned_at).toLocaleDateString()
                          : "—"}
                      </td>

                      <td>
                        {status === "Pending" ? (
                          <div className="mentor-students-actions">
                            <button
                              type="button"
                              className="mentor-students-accept"
                              disabled={isBusy}
                              onClick={() => handleDecision(id, "Active")}
                            >
                              {isBusy ? "Please wait..." : "Accept"}
                            </button>

                            <button
                              type="button"
                              className="mentor-students-reject"
                              disabled={isBusy}
                              onClick={() => handleDecision(id, "Rejected")}
                            >
                              Reject
                            </button>
                          </div>
                        ) : (
                          <span className="mentor-students-no-action">
                            —
                          </span>
                        )}
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        ) : (
          <div className="mentor-students-empty">
            <span>👨‍🎓</span>
            <h3>No students found</h3>
            <p>
              {search
                ? "Try another search term."
                : "Student assignments and mentorship requests will appear here."}
            </p>
          </div>
        )}
      </div>
    </section>
  );
}

export default MyStudents;
