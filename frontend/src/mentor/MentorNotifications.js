
import React, { useCallback, useEffect, useState } from "react";
import "./MentorNotifications.css";

const API_BASE_URL = "https://skillsphere-17hl.onrender.com";

function MentorNotifications() {
  const [notifications, setNotifications] = useState([]);
  const [filter, setFilter] = useState("all");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const [updating, setUpdating] = useState(false);

  const fetchNotifications = useCallback(async () => {
    try {
      setLoading(true);
      setError("");

      const token = localStorage.getItem("skillsphere_access");

      if (!token) {
        throw new Error("Access token not found. Please login again.");
      }

      const response = await fetch(
        `${API_BASE_URL}/api/notifications/`,
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
        throw new Error(
          data.detail || data.message || "Unable to load notifications."
        );
      }

      setNotifications(data.notifications || []);
    } catch (err) {
      setError(err.message || "Something went wrong.");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchNotifications();
  }, [fetchNotifications]);

  const unreadCount = notifications.filter(
    (item) => !item.is_read
  ).length;

  const readCount = notifications.length - unreadCount;

  const filteredNotifications = notifications.filter((item) => {
    if (filter === "unread") return !item.is_read;
    if (filter === "read") return item.is_read;
    return true;
  });

  const getToken = () =>
    localStorage.getItem("skillsphere_access");

  const markAsRead = async (notificationId) => {
    try {
      setUpdating(true);
      setError("");
      setSuccess("");

      const response = await fetch(
        `${API_BASE_URL}/api/notifications/${notificationId}/read/`,
        {
          method: "PATCH",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${getToken()}`,
          },
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || "Unable to mark notification as read."
        );
      }

      setNotifications((previous) =>
        previous.map((item) =>
          item.id === notificationId
            ? { ...item, is_read: true }
            : item
        )
      );

      setSuccess("Notification marked as read.");
    } catch (err) {
      setError(err.message);
    } finally {
      setUpdating(false);
    }
  };

  const markAllAsRead = async () => {
    if (unreadCount === 0) {
      setSuccess("There are no unread notifications.");
      return;
    }

    try {
      setUpdating(true);
      setError("");
      setSuccess("");

      const response = await fetch(
        `${API_BASE_URL}/api/notifications/read-all/`,
        {
          method: "PATCH",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${getToken()}`,
          },
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || "Unable to mark all notifications as read."
        );
      }

      setNotifications((previous) =>
        previous.map((item) => ({
          ...item,
          is_read: true,
        }))
      );

      setSuccess("All notifications marked as read.");
    } catch (err) {
      setError(err.message);
    } finally {
      setUpdating(false);
    }
  };

  const getTypeIcon = (type) => {
    const icons = {
      career: "💼",
      skill: "📚",
      assessment: "📝",
      system: "⚙️",
    };

    return icons[type] || "🔔";
  };

  const getTypeLabel = (type) => {
    const labels = {
      career: "Career",
      skill: "Skill",
      assessment: "Assessment",
      system: "System",
    };

    return labels[type] || "Notification";
  };

  const formatDate = (date) => {
    if (!date) return "";

    return new Date(date).toLocaleString("en-IN", {
      day: "2-digit",
      month: "short",
      year: "numeric",
      hour: "2-digit",
      minute: "2-digit",
    });
  };

  return (
    <section className="mn-container">

      {/* PAGE HEADING */}

      <div className="mn-heading">
        <div>
          <h2>Notifications</h2>
          <p>
            Stay updated with your students and mentoring activities.
          </p>
        </div>

        <button
          type="button"
          className="mn-refresh-button"
          onClick={fetchNotifications}
          disabled={loading}
        >
          ↻ Refresh
        </button>
      </div>

      {/* ALERTS */}

      {error && (
        <div className="mn-alert mn-error">
          {error}
        </div>
      )}

      {success && (
        <div className="mn-alert mn-success">
          {success}
        </div>
      )}

      {/* STATISTICS */}

      <div className="mn-stats">

        <div className="mn-stat-card">
          <div className="mn-stat-icon">🔔</div>
          <div>
            <p>Total Notifications</p>
            <h2>{notifications.length}</h2>
          </div>
        </div>

        <div className="mn-stat-card">
          <div className="mn-stat-icon">📩</div>
          <div>
            <p>Unread Notifications</p>
            <h2>{unreadCount}</h2>
          </div>
        </div>

        <div className="mn-stat-card">
          <div className="mn-stat-icon">✓</div>
          <div>
            <p>Read Notifications</p>
            <h2>{readCount}</h2>
          </div>
        </div>

      </div>

      {/* FILTER AND ACTIONS */}

      <div className="mn-toolbar">

        <div className="mn-filters">

          <button
            type="button"
            className={filter === "all" ? "active" : ""}
            onClick={() => setFilter("all")}
          >
            All
          </button>

          <button
            type="button"
            className={filter === "unread" ? "active" : ""}
            onClick={() => setFilter("unread")}
          >
            Unread
          </button>

          <button
            type="button"
            className={filter === "read" ? "active" : ""}
            onClick={() => setFilter("read")}
          >
            Read
          </button>

        </div>

        <button
          type="button"
          className="mn-mark-all-button"
          onClick={markAllAsRead}
          disabled={updating || unreadCount === 0}
        >
          Mark All as Read
        </button>

      </div>

      {/* NOTIFICATION LIST */}

      <div className="mn-list">

        {loading ? (
          <div className="mn-empty">
            <span>⏳</span>
            <h3>Loading Notifications...</h3>
            <p>Please wait while we retrieve your notifications.</p>
          </div>
        ) : filteredNotifications.length > 0 ? (

          filteredNotifications.map((notification) => (

            <div
              className={`mn-card ${
                notification.is_read ? "read" : "unread"
              }`}
              key={notification.id}
            >

              <div className="mn-card-icon">
                {getTypeIcon(notification.notification_type)}
              </div>

              <div className="mn-card-content">

                <div className="mn-card-heading">

                  <h3>{notification.title}</h3>

                  {!notification.is_read && (
                    <span className="mn-unread-dot"></span>
                  )}

                </div>

                <p>{notification.message}</p>

                <div className="mn-card-meta">

                  <span className="mn-type">
                    {getTypeLabel(notification.notification_type)}
                  </span>

                  <span>
                    {formatDate(notification.created_at)}
                  </span>

                </div>

              </div>

              <div className="mn-card-action">

                {notification.is_read ? (
                  <span className="mn-read-label">
                    ✓ Read
                  </span>
                ) : (
                  <button
                    type="button"
                    onClick={() => markAsRead(notification.id)}
                    disabled={updating}
                  >
                    Mark as Read
                  </button>
                )}

              </div>

            </div>

          ))

        ) : (

          <div className="mn-empty">
            <span>🔔</span>

            <h3>
              {filter === "unread"
                ? "No Unread Notifications"
                : filter === "read"
                ? "No Read Notifications"
                : "No Notifications Yet"}
            </h3>

            <p>
              {filter === "unread"
                ? "You're all caught up!"
                : "Your notifications will appear here."}
            </p>
          </div>

        )}

      </div>

    </section>
  );
}

export default MentorNotifications;
