
import React, {
  useCallback,
  useEffect,
  useMemo,
  useState,
} from "react";

import { API_BASE_URL, useAuth } from "../auth/AuthContext";
import { showToast } from "../components/ToastProvider";
import "./AdminNotifications.css";

const ACCESS_KEY = "skillsphere_access";

function getAccessToken(contextToken) {
  if (contextToken) return contextToken;

  try {
    return (
      localStorage.getItem(ACCESS_KEY) ||
      localStorage.getItem("access") ||
      ""
    );
  } catch {
    return "";
  }
}

function formatDate(value) {
  if (!value) return "Date unavailable";

  const date = new Date(value);

  if (Number.isNaN(date.getTime())) {
    return "Date unavailable";
  }

  return date.toLocaleString([], {
    day: "numeric",
    month: "short",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
}

function getCategory(type) {
  const categories = {
    career: "Career",
    skill: "Learning",
    assessment: "Assessment",
    system: "System",
  };

  return categories[String(type || "").toLowerCase()] || "General";
}

function getIcon(type) {
  const icons = {
    career: "🎯",
    skill: "📚",
    assessment: "🧠",
    system: "🔔",
  };

  return icons[String(type || "").toLowerCase()] || "🔔";
}

export default function AdminNotifications() {
  const { accessToken: contextToken } = useAuth();

  const [notifications, setNotifications] = useState([]);
  const [search, setSearch] = useState("");
  const [filter, setFilter] = useState("all");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [busyIds, setBusyIds] = useState([]);
  const [markingAll, setMarkingAll] = useState(false);

  const request = useCallback(
    async (path, options = {}) => {
      const token = getAccessToken(contextToken);

      if (!token) {
        throw new Error("No login token found. Please log in again.");
      }

      const response = await fetch(`${API_BASE_URL}${path}`, {
        ...options,
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
          ...options.headers,
        },
      });

      const data = await response.json().catch(() => ({}));

      if (!response.ok) {
        if (response.status === 401) {
          throw new Error(
            "Your login session may have expired. Please log in again."
          );
        }

        if (response.status === 403) {
          throw new Error(
            "Your account does not have permission to access these notifications."
          );
        }

        throw new Error(
          data.detail ||
            data.message ||
            "Unable to complete the notification request."
        );
      }

      return data;
    },
    [contextToken]
  );

  const loadNotifications = useCallback(async () => {
    setLoading(true);
    setError("");

    try {
      const data = await request("/api/notifications/");

      if (!Array.isArray(data.notifications)) {
        throw new Error(
          "Unexpected API response: notifications list was not found."
        );
      }

      setNotifications(data.notifications);
    } catch (err) {
      const message =
        err.message || "Unable to load notifications.";

      setError(message);
      showToast(message, "error");
    } finally {
      setLoading(false);
    }
  }, [request]);

  useEffect(() => {
    loadNotifications();
  }, [loadNotifications]);

  const unreadCount = notifications.filter(
    (item) => !item.is_read
  ).length;

  const readCount = notifications.length - unreadCount;

  const filteredNotifications = useMemo(() => {
    const query = search.trim().toLowerCase();

    return notifications
      .filter((item) => {
        if (filter === "unread" && item.is_read) return false;
        if (filter === "read" && !item.is_read) return false;

        const category = getCategory(item.notification_type);
        const searchableText =
          `${item.title || ""} ${item.message || ""} ${category}`
            .toLowerCase();

        return searchableText.includes(query);
      })
      .sort(
        (a, b) =>
          new Date(b.created_at || 0).getTime() -
          new Date(a.created_at || 0).getTime()
      );
  }, [notifications, search, filter]);

  async function markAsRead(id) {
    const item = notifications.find(
      (notification) => notification.id === id
    );

    if (!item || item.is_read || busyIds.includes(id)) {
      return;
    }

    setBusyIds((current) => [...current, id]);

    try {
      await request(`/api/notifications/${id}/read/`, {
        method: "PATCH",
      });

      setNotifications((current) =>
        current.map((notification) =>
          notification.id === id
            ? { ...notification, is_read: true }
            : notification
        )
      );

      showToast("Notification marked as read.", "success");
    } catch (err) {
      showToast(
        err.message || "Unable to mark notification as read.",
        "error"
      );
    } finally {
      setBusyIds((current) =>
        current.filter((busyId) => busyId !== id)
      );
    }
  }

  async function markAllAsRead() {
    if (unreadCount === 0 || markingAll) {
      if (unreadCount === 0) {
        showToast("You have no unread notifications.", "info");
      }
      return;
    }

    setMarkingAll(true);

    try {
      await request("/api/notifications/read-all/", {
        method: "PATCH",
      });

      setNotifications((current) =>
        current.map((item) => ({
          ...item,
          is_read: true,
        }))
      );

      showToast("All notifications marked as read.", "success");
    } catch (err) {
      showToast(
        err.message || "Unable to mark all notifications as read.",
        "error"
      );
    } finally {
      setMarkingAll(false);
    }
  }

  return (
    <div className="admin-notifications">
      <div className="an-heading">
        <div>
          <span className="an-eyebrow">SYSTEM MANAGEMENT</span>
          <h2>Notifications</h2>
          <p>Manage platform announcements and notifications.</p>
        </div>

        <button
          type="button"
          className="an-button an-secondary"
          onClick={loadNotifications}
          disabled={loading}
        >
          {loading ? "Refreshing..." : "↻ Refresh"}
        </button>
      </div>

      <div className="an-stats">
        <div className="an-stat-card">
          <span>Total Notifications</span>
          <strong>{notifications.length}</strong>
        </div>

        <div className="an-stat-card">
          <span>Unread Notifications</span>
          <strong>{unreadCount}</strong>
        </div>

        <div className="an-stat-card">
          <span>Read Notifications</span>
          <strong>{readCount}</strong>
        </div>
      </div>

      <section className="an-panel">
        <div className="an-toolbar">
          <input
            type="search"
            value={search}
            onChange={(event) => setSearch(event.target.value)}
            placeholder="Search notifications..."
            aria-label="Search notifications"
          />

          <select
            value={filter}
            onChange={(event) => setFilter(event.target.value)}
            aria-label="Filter notifications"
          >
            <option value="all">All notifications</option>
            <option value="unread">Unread</option>
            <option value="read">Read</option>
          </select>

          <button
            type="button"
            className="an-button an-primary"
            onClick={markAllAsRead}
            disabled={loading || markingAll || unreadCount === 0}
          >
            {markingAll ? "Marking..." : "Mark All as Read"}
          </button>
        </div>

        {loading && (
          <div className="an-empty">
            <h3>Loading notifications...</h3>
            <p>Please wait while we load your inbox.</p>
          </div>
        )}

        {!loading && error && (
          <div className="an-empty">
            <h3>Unable to load notifications</h3>
            <p>{error}</p>
            <button
              type="button"
              className="an-button an-primary"
              onClick={loadNotifications}
            >
              Try Again
            </button>
          </div>
        )}

        {!loading && !error && (
          <div className="an-list">
            {filteredNotifications.length === 0 ? (
              <div className="an-empty">
                <span>♧</span>
                <h3>No notifications found</h3>
                <p>Try another search or filter.</p>
              </div>
            ) : (
              filteredNotifications.map((item) => (
                <article
                  key={item.id}
                  className={`an-item ${
                    item.is_read ? "an-read" : "an-unread"
                  }`}
                >
                  <div className="an-icon">
                    {getIcon(item.notification_type)}
                  </div>

                  <div className="an-content">
                    <div className="an-title-row">
                      <h3>{item.title || "Notification"}</h3>

                      <span
                        className={`an-status ${
                          item.is_read
                            ? "status-read"
                            : "status-unread"
                        }`}
                      >
                        {item.is_read ? "Read" : "Unread"}
                      </span>
                    </div>

                    <p>{item.message || ""}</p>

                    <div className="an-meta">
                      <span>
                        {getCategory(item.notification_type)}
                      </span>
                      <span>{formatDate(item.created_at)}</span>
                    </div>
                  </div>

                  {!item.is_read && (
                    <button
                      type="button"
                      className="an-read-button"
                      onClick={() => markAsRead(item.id)}
                      disabled={busyIds.includes(item.id)}
                    >
                      {busyIds.includes(item.id)
                        ? "Marking..."
                        : "Mark as Read"}
                    </button>
                  )}
                </article>
              ))
            )}
          </div>
        )}
      </section>
    </div>
  );
}
