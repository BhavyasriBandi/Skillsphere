
import React, { useEffect, useMemo, useState } from "react";
import { apiFetch } from "../auth/AuthContext";
import "./Mentors.css";

const API_URL = "/api/auth/users/";

// Share an in-progress request to avoid duplicate API calls.
let usersRequestPromise = null;

function fetchUsers() {
  if (!usersRequestPromise) {
    usersRequestPromise = (async () => {
      const response = await apiFetch(API_URL, {
        method: "GET",
        headers: {
          Accept: "application/json",
        },
      });

      let payload = {};

      try {
        payload = await response.json();
      } catch {
        payload = {};
      }

      if (!response.ok) {
        throw new Error(
          payload.detail ||
            payload.message ||
            `Unable to load users. Status: ${response.status}`
        );
      }

      return getUserList(payload);
    })().finally(() => {
      usersRequestPromise = null;
    });
  }

  return usersRequestPromise;
}

function getUserName(user) {
  const firstName = user.first_name || user.firstname || "";
  const lastName = user.last_name || user.lastname || "";
  const fullName = `${firstName} ${lastName}`.trim();

  return (
    user.name ||
    user.full_name ||
    fullName ||
    user.username ||
    user.email ||
    "Unnamed mentor"
  );
}

function getUserRole(user) {
  const role =
    user.role ??
    user.user_role ??
    user.user_type ??
    user.account_type ??
    user.profile?.role ??
    user.profile?.user_role ??
    "";

  return String(role).trim().toLowerCase();
}

function isMentor(user) {
  return ["mentor", "mentors"].includes(getUserRole(user));
}

function getMentorStatus(user) {
  return user.is_active === false || user.is_active === 0
    ? "Inactive"
    : "Active";
}

function getUserList(payload) {
  if (Array.isArray(payload)) return payload;

  const possibleLists = [
    payload?.results,
    payload?.users,
    payload?.data,
    payload?.data?.results,
    payload?.data?.users,
    payload?.data?.data,
  ];

  return possibleLists.find(Array.isArray) || [];
}

function formatDate(value) {
  if (!value) return "—";

  const date = new Date(value);

  if (Number.isNaN(date.getTime())) return "—";

  return date.toLocaleDateString(undefined, {
    day: "2-digit",
    month: "short",
    year: "numeric",
  });
}

export default function Mentors() {
  const [users, setUsers] = useState([]);
  const [search, setSearch] = useState("");
  const [statusFilter, setStatusFilter] = useState("All");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [refreshKey, setRefreshKey] = useState(0);

  const [selectedMentor, setSelectedMentor] = useState(null);
  const [updating, setUpdating] = useState(false);
  const [toast, setToast] = useState(null);

  // Load users
  useEffect(() => {
    let active = true;

    async function loadUsers() {
      setLoading(true);
      setError("");

      try {
        const mentorUsers = await fetchUsers();

        if (active) {
          setUsers(mentorUsers);
        }
      } catch (err) {
        if (active) {
          setError(
            err.message ||
              "Unable to connect to Django. Check your backend."
          );
        }
      } finally {
        if (active) {
          setLoading(false);
        }
      }
    }

    loadUsers();

    return () => {
      active = false;
    };
  }, [refreshKey]);

  // Toast auto-dismiss
  useEffect(() => {
    if (!toast) return;

    const timer = setTimeout(() => {
      setToast(null);
    }, 3500);

    return () => clearTimeout(timer);
  }, [toast]);

  // Filter mentor users
  const mentors = useMemo(() => {
    return users
      .filter(isMentor)
      .map((user) => ({
        id: user.id ?? user.pk ?? null,
        name: getUserName(user),
        email: user.email || "No email provided",
        status: getMentorStatus(user),
        isActive: user.is_active === true || user.is_active === 1,
        joined:
          user.date_joined ||
          user.created_at ||
          user.created ||
          user.joined_at ||
          "",
      }));
  }, [users]);

  // Search and status filter
  const filteredMentors = useMemo(() => {
    const query = search.trim().toLowerCase();

    return mentors.filter((mentor) => {
      const matchesSearch =
        mentor.name.toLowerCase().includes(query) ||
        mentor.email.toLowerCase().includes(query);

      const matchesStatus =
        statusFilter === "All" ||
        mentor.status === statusFilter;

      return matchesSearch && matchesStatus;
    });
  }, [mentors, search, statusFilter]);

  const activeCount = mentors.filter(
    (mentor) => mentor.isActive
  ).length;

  const inactiveCount = mentors.length - activeCount;

  // Open confirmation modal
  function openStatusConfirmation(mentor) {
    setSelectedMentor(mentor);
  }

  // Update mentor account status
  async function confirmStatusChange() {
    if (!selectedMentor || !selectedMentor.id || updating) return;

    const newStatus = !selectedMentor.isActive;

    setUpdating(true);

    try {
      const response = await apiFetch(
        `${API_URL}${selectedMentor.id}/status/`,
        {
          method: "PATCH",
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json",
          },
          body: JSON.stringify({
            is_active: newStatus,
          }),
        }
      );

      let data = {};

      try {
        data = await response.json();
      } catch {
        data = {};
      }

      if (!response.ok) {
        throw new Error(
          data.detail ||
            data.message ||
            `Unable to update account. Status: ${response.status}`
        );
      }

      const mentorName = selectedMentor.name;

      setSelectedMentor(null);

      setToast({
        type: "success",
        message:
          data.message ||
          `${mentorName}'s account ${
            newStatus ? "activated" : "deactivated"
          } successfully.`,
      });

      // Refresh mentor list after updating status.
      setRefreshKey((value) => value + 1);
    } catch (err) {
      setSelectedMentor(null);

      setToast({
        type: "error",
        message: err.message || "Unable to update mentor account.",
      });
    } finally {
      setUpdating(false);
    }
  }

  return (
    <section className="mentors-page">
      {/* Toast */}
      {toast && (
        <div
          className={`mentors-toast mentors-toast-${toast.type}`}
          role={toast.type === "error" ? "alert" : "status"}
        >
          <span className="mentors-toast-icon">
            {toast.type === "success" ? "✓" : "!"}
          </span>

          <span className="mentors-toast-message">
            {toast.message}
          </span>

          <button
            type="button"
            className="mentors-toast-close"
            onClick={() => setToast(null)}
            aria-label="Close notification"
          >
            ×
          </button>

          <span className="mentors-toast-progress" />
        </div>
      )}

      {/* Page heading */}
      <div className="mentors-intro">
        <div>
          <span className="mentors-eyebrow">
            PEOPLE &amp; ACCESS
          </span>

          <h2>Mentor Management</h2>

          <p>
            View mentor accounts registered on the SkillSphere platform.
          </p>
        </div>

        <button
          type="button"
          className="mentors-refresh-button"
          onClick={() => setRefreshKey((value) => value + 1)}
          disabled={loading}
        >
          <span aria-hidden="true">↻</span>
          {loading ? "Loading..." : "Refresh"}
        </button>
      </div>

      {/* Statistics */}
      <div className="mentors-stat-grid">
        <article className="mentors-stat-card">
          <span className="mentors-stat-icon" aria-hidden="true">
            ♙
          </span>

          <div>
            <p>Total Mentors</p>
            <strong>{loading ? "—" : mentors.length}</strong>
          </div>
        </article>

        <article className="mentors-stat-card">
          <span
            className="mentors-stat-icon mentors-stat-active"
            aria-hidden="true"
          >
            ✓
          </span>

          <div>
            <p>Active Mentors</p>
            <strong>{loading ? "—" : activeCount}</strong>
          </div>
        </article>

        <article className="mentors-stat-card">
          <span
            className="mentors-stat-icon mentors-stat-inactive"
            aria-hidden="true"
          >
            ◷
          </span>

          <div>
            <p>Inactive Mentors</p>
            <strong>{loading ? "—" : inactiveCount}</strong>
          </div>
        </article>
      </div>

      {/* Mentor table */}
      <div className="mentors-table-card">
        <div className="mentors-table-heading">
          <div>
            <h3>Registered Mentors</h3>

            <p>
              {loading
                ? "Retrieving mentor accounts..."
                : `${filteredMentors.length} mentor${
                    filteredMentors.length === 1 ? "" : "s"
                  } found`}
            </p>
          </div>
        </div>

        <div className="mentors-toolbar">
          <label className="mentors-search">
            <span aria-hidden="true">⌕</span>

            <input
              type="search"
              value={search}
              onChange={(event) => setSearch(event.target.value)}
              placeholder="Search by name or email..."
              aria-label="Search mentors"
            />
          </label>

          <select
            value={statusFilter}
            onChange={(event) => setStatusFilter(event.target.value)}
            aria-label="Filter mentors by status"
            className="mentors-status-filter"
          >
            <option value="All">All statuses</option>
            <option value="Active">Active</option>
            <option value="Inactive">Inactive</option>
          </select>
        </div>

        {error && (
          <div className="mentors-error" role="alert">
            <strong>Unable to load mentors</strong>

            <p>{error}</p>

            <button
              type="button"
              onClick={() => setRefreshKey((value) => value + 1)}
            >
              Try again
            </button>
          </div>
        )}

        {!error && loading && (
          <div className="mentors-empty-state">
            <span className="mentors-loader" aria-label="Loading" />
            <p>Loading mentor accounts...</p>
          </div>
        )}

        {!error && !loading && filteredMentors.length === 0 && (
          <div className="mentors-empty-state">
            <span className="mentors-empty-icon" aria-hidden="true">
              ♙
            </span>

            <h4>
              {mentors.length === 0
                ? "No mentor accounts found"
                : "No matching mentors"}
            </h4>

            <p>
              {mentors.length === 0
                ? "No mentor-role users were returned by the API. Check the user role field and the Django response."
                : "Try changing your search or status filter."}
            </p>
          </div>
        )}

        {!error && !loading && filteredMentors.length > 0 && (
          <div className="mentors-table-wrapper">
            <table className="mentors-table">
              <thead>
                <tr>
                  <th>Mentor</th>
                  <th>Email Address</th>
                  <th>Status</th>
                  <th>Date Joined</th>
                  <th>Account Action</th>
                </tr>
              </thead>

              <tbody>
                {filteredMentors.map((mentor, index) => (
                  <tr key={mentor.id ?? `${mentor.email}-${index}`}>
                    <td>
                      <div className="mentors-person">
                        <span className="mentors-avatar">
                          {mentor.name
                            .split(/\s+/)
                            .map((part) => part[0] || "")
                            .join("")
                            .slice(0, 2)
                            .toUpperCase()}
                        </span>

                        <strong>{mentor.name}</strong>
                      </div>
                    </td>

                    <td>{mentor.email}</td>

                    <td>
                      <span
                        className={`mentors-status ${
                          mentor.isActive
                            ? "mentors-status-active"
                            : "mentors-status-inactive"
                        }`}
                      >
                        <span className="mentors-status-dot" />
                        {mentor.status}
                      </span>
                    </td>

                    <td>{formatDate(mentor.joined)}</td>

                    <td>
                      <button
                        type="button"
                        className={`mentors-action-button ${
                          mentor.isActive
                            ? "mentors-deactivate-button"
                            : "mentors-activate-button"
                        }`}
                        disabled={!mentor.id}
                        onClick={() => openStatusConfirmation(mentor)}
                      >
                        {mentor.isActive ? "Deactivate" : "Activate"}
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>

      {/* Centered confirmation modal */}
      {selectedMentor && (
        <div
          className="mentors-modal-overlay"
          onMouseDown={(event) => {
            if (
              event.target === event.currentTarget &&
              !updating
            ) {
              setSelectedMentor(null);
            }
          }}
        >
          <div
            className="mentors-confirm-modal"
            role="dialog"
            aria-modal="true"
            aria-labelledby="mentor-confirm-title"
          >
            <div
              className={`mentors-confirm-icon ${
                selectedMentor.isActive
                  ? "mentors-confirm-warning"
                  : "mentors-confirm-success"
              }`}
            >
              {selectedMentor.isActive ? "!" : "✓"}
            </div>

            <h3 id="mentor-confirm-title">
              {selectedMentor.isActive
                ? "Deactivate Mentor?"
                : "Activate Mentor?"}
            </h3>

            <p>
              Are you sure you want to{" "}
              {selectedMentor.isActive ? "deactivate" : "activate"}{" "}
              <strong>{selectedMentor.name}</strong>'s account?
            </p>

            <div className="mentors-confirm-actions">
              <button
                type="button"
                className="mentors-confirm-cancel"
                disabled={updating}
                onClick={() => setSelectedMentor(null)}
              >
                Cancel
              </button>

              <button
                type="button"
                className={`mentors-confirm-submit ${
                  selectedMentor.isActive
                    ? "mentors-confirm-danger"
                    : "mentors-confirm-primary"
                }`}
                disabled={updating}
                onClick={confirmStatusChange}
              >
                {updating
                  ? "Please wait..."
                  : selectedMentor.isActive
                  ? "Yes, Deactivate"
                  : "Yes, Activate"}
              </button>
            </div>
          </div>
        </div>
      )}
    </section>
  );
}
