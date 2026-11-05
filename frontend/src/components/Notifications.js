
import React, {
  useCallback,
  useEffect,
  useMemo,
  useState,
} from "react";
import "./Notifications.css";
import { showToast } from "./ToastProvider";
import { API_BASE_URL, useAuth } from "../auth/AuthContext";

const ACCESS_KEY = "skillsphere_access";

function formatDate(value) {
  const date = new Date(value);

  if (Number.isNaN(date.getTime())) {
    return "Date unavailable";
  }

  const now = new Date();

  if (date.toDateString() === now.toDateString()) {
    return `Today, ${date.toLocaleTimeString([], {
      hour: "2-digit",
      minute: "2-digit",
    })}`;
  }

  return date.toLocaleDateString([], {
    day: "numeric",
    month: "short",
    year: "numeric",
  });
}

function getCategory(type) {
  const categories = {
    career: "Career",
    skill: "Learning",
    assessment: "Assessment",
    system: "General",
  };

  return categories[type] || "General";
}

function getIcon(type) {
  const icons = {
    career: "🎯",
    skill: "📚",
    assessment: "🧠",
    system: "🔔",
  };

  return icons[type] || "🔔";
}

function getAccessToken(contextToken) {
  // Prefer the token already provided by the authentication context.
  // Fall back to the existing saved token during session restoration.
  if (contextToken) {
    return contextToken;
  }

  try {
    return localStorage.getItem(ACCESS_KEY) || "";
  } catch {
    return "";
  }
}

function Notifications() {
  const { accessToken: contextToken } = useAuth();

  const [token, setToken] = useState(() =>
    getAccessToken(contextToken)
  );

  const [notifications, setNotifications] = useState([]);
  const [filter, setFilter] = useState("All");
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);
  const [busyIds, setBusyIds] = useState([]);
  const [markingAll, setMarkingAll] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    const currentToken = getAccessToken(contextToken);
    setToken(currentToken);
  }, [contextToken]);

  const unreadCount = notifications.filter(
    (item) => !item.is_read
  ).length;

  const readCount = notifications.length - unreadCount;

  const request = useCallback(
    async (path, options = {}) => {
      const currentToken = getAccessToken(contextToken);

      if (!currentToken) {
        throw new Error(
          "No access token was found. Please log in again."
        );
      }

      const response = await fetch(`${API_BASE_URL}${path}`, {
        ...options,
        headers: {
          Authorization: `Bearer ${currentToken}`,
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
    const currentToken = getAccessToken(contextToken);

    if (!currentToken) {
      setNotifications([]);
      setLoading(false);
      setError(
        "No login token was found. Please log in again and reopen Notifications."
      );
      return;
    }

    setLoading(true);
    setError("");

    try {
      const data = await request("/api/notifications/");

      if (!Array.isArray(data.notifications)) {
        throw new Error(
          "The notifications API returned an unexpected response."
        );
      }

      setNotifications(data.notifications);
    } catch (err) {
      setError(err.message || "Unable to load notifications.");

      showToast(
        err.message || "Unable to load notifications.",
        "error"
      );
    } finally {
      setLoading(false);
    }
  }, [contextToken, request]);

  useEffect(() => {
    loadNotifications();
  }, [loadNotifications]);

  const filteredNotifications = useMemo(() => {
    const query = search.trim().toLowerCase();

    return notifications
      .filter((item) => {
        if (filter === "Unread" && item.is_read) {
          return false;
        }

        if (filter === "Read" && !item.is_read) {
          return false;
        }

        const category = getCategory(item.notification_type);
        const text =
          `${item.title} ${item.message} ${category}`.toLowerCase();

        return text.includes(query);
      })
      .sort(
        (a, b) =>
          new Date(b.created_at).getTime() -
          new Date(a.created_at).getTime()
      );
  }, [notifications, filter, search]);

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
    <main className="sn-page">
      <header className="sn-header">
        <div>
          <span className="sn-eyebrow">STAY INFORMED</span>
          <h1>Notifications</h1>
          <p>
            Keep track of your learning reminders and important updates in
            SkillSphere.
          </p>
        </div>

        <button
          type="button"
          className="sn-primary-button"
          onClick={markAllAsRead}
          disabled={markingAll || loading || unreadCount === 0}
        >
          {markingAll ? "Marking..." : "✓ Mark all as read"}
        </button>
      </header>

      <section className="sn-summary-grid">
        <article className="sn-summary-card">
          <span className="sn-summary-icon sn-icon-blue">🔔</span>
          <div>
            <p>Total Notifications</p>
            <strong>{notifications.length}</strong>
          </div>
        </article>

        <article className="sn-summary-card">
          <span className="sn-summary-icon sn-icon-orange">📩</span>
          <div>
            <p>Unread</p>
            <strong>{unreadCount}</strong>
          </div>
        </article>

        <article className="sn-summary-card">
          <span className="sn-summary-icon sn-icon-green">✓</span>
          <div>
            <p>Read</p>
            <strong>{readCount}</strong>
          </div>
        </article>
      </section>

      <section className="sn-panel">
        <div className="sn-toolbar">
          <div>
            <h2>Your inbox</h2>
            <p>
              {loading
                ? "Loading your notifications..."
                : error
                  ? "Notifications could not be loaded."
                  : unreadCount
                    ? `You have ${unreadCount} unread notification${
                        unreadCount === 1 ? "" : "s"
                      }.`
                    : "You're all caught up!"}
            </p>
          </div>

          <label className="sn-search">
            <span aria-hidden="true">⌕</span>
            <input
              type="search"
              value={search}
              onChange={(event) => setSearch(event.target.value)}
              placeholder="Search notifications..."
              aria-label="Search notifications"
            />
          </label>
        </div>

        <div className="sn-filter-row">
          <div className="sn-filters">
            {["All", "Unread", "Read"].map((item) => (
              <button
                key={item}
                type="button"
                className={`sn-filter ${
                  filter === item ? "sn-filter-active" : ""
                }`}
                onClick={() => setFilter(item)}
              >
                {item}

                {item === "Unread" && (
                  <span className="sn-filter-count">
                    {unreadCount}
                  </span>
                )}
              </button>
            ))}
          </div>

          <button
            type="button"
            className="sn-text-button"
            onClick={loadNotifications}
            disabled={loading}
          >
            {loading ? "Refreshing..." : "Refresh"}
          </button>
        </div>

        <div className="sn-notification-list">
          {loading && (
            <div className="sn-empty">
              <span>⏳</span>
              <h3>Loading notifications</h3>
              <p>Please wait while we retrieve your inbox.</p>
            </div>
          )}

          {!loading &&
            !error &&
            filteredNotifications.map((item) => (
              <article
                key={item.id}
                className={`sn-notification ${
                  item.is_read
                    ? "sn-notification-read"
                    : "sn-notification-unread"
                }`}
              >
                <div className="sn-notification-icon">
                  {getIcon(item.notification_type)}
                </div>

                <div className="sn-notification-content">
                  <div className="sn-notification-title-row">
                    <h3>{item.title}</h3>

                    {!item.is_read && (
                      <span className="sn-unread-dot" title="Unread" />
                    )}
                  </div>

                  <p>{item.message}</p>

                  <div className="sn-notification-meta">
                    <span className="sn-category">
                      {getCategory(item.notification_type)}
                    </span>
                    <span>{formatDate(item.created_at)}</span>
                  </div>

                  <div className="sn-notification-actions">
                    {!item.is_read && (
                      <button
                        type="button"
                        onClick={() => markAsRead(item.id)}
                        disabled={busyIds.includes(item.id)}
                      >
                        {busyIds.includes(item.id)
                          ? "Marking..."
                          : "✓ Mark as read"}
                      </button>
                    )}
                  </div>
                </div>
              </article>
            ))}

          {!loading && error && (
            <div className="sn-empty">
              <span>⚠️</span>
              <h3>Unable to load notifications</h3>
              <p>{error}</p>

              <button
                type="button"
                className="sn-text-button"
                onClick={loadNotifications}
              >
                Try again
              </button>
            </div>
          )}

          {!loading &&
            !error &&
            filteredNotifications.length === 0 && (
              <div className="sn-empty">
                <span>🔔</span>
                <h3>No notifications found</h3>
                <p>
                  {search
                    ? "Try another search term."
                    : filter === "Unread"
                      ? "You're all caught up. There are no unread notifications."
                      : filter === "Read"
                        ? "Read notifications will appear here."
                        : "Your inbox is empty. New notifications will appear here when available."}
                </p>

                {search && (
                  <button
                    type="button"
                    className="sn-text-button"
                    onClick={() => setSearch("")}
                  >
                    Clear search
                  </button>
                )}
              </div>
            )}
        </div>

        <footer className="sn-inbox-footer">
          <span>
            Showing {loading ? 0 : filteredNotifications.length} of{" "}
            {notifications.length} notifications
          </span>

          <button
            type="button"
            className="sn-demo-button"
            onClick={loadNotifications}
            disabled={loading}
          >
            ↻ Refresh inbox
          </button>
        </footer>
      </section>

      <aside className="sn-info-banner">
        <span>💡</span>
        <div>
          <h3>Stay on track</h3>
          <p>
            Your notifications are loaded from your SkillSphere account.
            Read status is saved in the database.
          </p>
        </div>
      </aside>
    </main>
  );
}

export default Notifications;
