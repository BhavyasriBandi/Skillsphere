
import React, { useCallback, useEffect, useState } from "react";
import "./MentorSettings.css";

const API_BASE_URL = "https://skillsphere-17hl.onrender.com";
const SETTINGS_KEY = "skillsphere_student_settings";

const initialSettings = {
  learning_format: "",
  career_interests: "",
  email_notifications: true,
  learning_reminders: true,
  weekly_summary: false,
  language: "English",
  theme: "light",
};

// Apply theme throughout the application
const applyTheme = (theme) => {
  const selectedTheme = theme === "dark" ? "dark" : "light";

  document.documentElement.setAttribute("data-theme", selectedTheme);
  document.body.setAttribute("data-theme", selectedTheme);

  // Preserve existing settings in LocalStorage
  try {
    const existingSettings = JSON.parse(
      localStorage.getItem(SETTINGS_KEY) || "{}"
    );

    localStorage.setItem(
      SETTINGS_KEY,
      JSON.stringify({
        ...existingSettings,
        theme: selectedTheme,
      })
    );
  } catch (error) {
    console.error("Unable to save theme locally:", error);
  }

  // Notify App.js about the theme change
  window.dispatchEvent(
    new CustomEvent("skillsphere-theme-change", {
      detail: { theme: selectedTheme },
    })
  );
};

function MentorSettings() {
  const [settings, setSettings] = useState(initialSettings);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);

  const [success, setSuccess] = useState("");
  const [error, setError] = useState("");
  const [toastKey, setToastKey] = useState(0);

  const showSuccessToast = (message) => {
    setError("");
    setSuccess(message);
    setToastKey((previous) => previous + 1);
  };

  const showErrorToast = (message) => {
    setSuccess("");
    setError(message);
    setToastKey((previous) => previous + 1);
  };

  const fetchSettings = useCallback(async () => {
    try {
      setLoading(true);
      setError("");

      const token = localStorage.getItem("skillsphere_access");

      if (!token) {
        throw new Error("Access token not found. Please login again.");
      }

      const response = await fetch(
        `${API_BASE_URL}/api/user-preferences/`,
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
          data.detail || data.message || "Unable to load settings."
        );
      }

      const loadedSettings = {
        ...initialSettings,
        ...data,
        theme: data.theme === "dark" ? "dark" : "light",
      };

      setSettings(loadedSettings);

      // Apply saved theme when settings load
      applyTheme(loadedSettings.theme);
    } catch (err) {
      showErrorToast(err.message || "Unable to load settings.");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchSettings();
  }, [fetchSettings]);

  useEffect(() => {
    if (!success && !error) return;

    const timer = setTimeout(() => {
      setSuccess("");
      setError("");
    }, 3500);

    return () => clearTimeout(timer);
  }, [success, error, toastKey]);

  const handleChange = (event) => {
    const { name, value, type, checked } = event.target;

    const newValue = type === "checkbox" ? checked : value;

    setSettings((previous) => ({
      ...previous,
      [name]: newValue,
    }));

    // Apply theme immediately when Light/Dark is selected
    if (name === "theme") {
      applyTheme(newValue);
    }

    setSuccess("");
    setError("");
  };

  const handleSave = async (event) => {
    event.preventDefault();

    try {
      setSaving(true);
      setSuccess("");
      setError("");

      const token = localStorage.getItem("skillsphere_access");

      if (!token) {
        throw new Error("Access token not found. Please login again.");
      }

      const response = await fetch(
        `${API_BASE_URL}/api/user-preferences/`,
        {
          method: "PATCH",
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
          body: JSON.stringify(settings),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        const validationMessage =
          typeof data === "object"
            ? Object.entries(data)
                .map(([field, messages]) => {
                  const detail = Array.isArray(messages)
                    ? messages.join(", ")
                    : String(messages);

                  return `${field}: ${detail}`;
                })
                .join(" | ")
            : "Unable to save settings.";

        throw new Error(
          data.detail || data.message || validationMessage
        );
      }

      const savedPreferences = data.preferences || data;

      const updatedSettings = {
        ...settings,
        ...(savedPreferences &&
        typeof savedPreferences === "object"
          ? savedPreferences
          : {}),
        theme: settings.theme === "dark" ? "dark" : "light",
      };

      setSettings(updatedSettings);

      // Ensure selected theme remains applied after saving
      applyTheme(updatedSettings.theme);

      showSuccessToast(
        data.message || "Settings saved successfully!"
      );
    } catch (err) {
      showErrorToast(
        err.message || "Unable to save settings."
      );
    } finally {
      setSaving(false);
    }
  };

  if (loading) {
    return (
      <section className="mentor-settings-content">
        <div className="mentor-settings-message">
          Loading your settings...
        </div>
      </section>
    );
  }

  return (
    <section className="mentor-settings-content">

      {success && (
        <div
          key={`success-${toastKey}`}
          className="mentor-settings-toast success"
          role="status"
        >
          <span className="mentor-settings-toast-icon">✓</span>
          <div className="mentor-settings-toast-text">
            <strong>SUCCESS</strong>
            <p>{success}</p>
          </div>
          <button
            type="button"
            onClick={() => setSuccess("")}
            aria-label="Close success message"
          >
            ×
          </button>
          <div className="mentor-settings-toast-progress success-progress" />
        </div>
      )}

      {error && (
        <div
          key={`error-${toastKey}`}
          className="mentor-settings-toast error"
          role="alert"
        >
          <span className="mentor-settings-toast-icon">!</span>
          <div className="mentor-settings-toast-text">
            <strong>ERROR</strong>
            <p>{error}</p>
          </div>
          <button
            type="button"
            onClick={() => setError("")}
            aria-label="Close error message"
          >
            ×
          </button>
          <div className="mentor-settings-toast-progress error-progress" />
        </div>
      )}

      <div className="mentor-settings-heading">
        <div>
          <h1>Settings</h1>
          <p>
            Manage your learning, notifications and appearance preferences.
          </p>
        </div>
      </div>

      <form onSubmit={handleSave}>

        <div className="mentor-settings-card">
          <div className="mentor-settings-card-heading">
            <span className="mentor-settings-icon">🎓</span>
            <div>
              <h2>Learning Preferences</h2>
              <p>Customize your preferred learning experience.</p>
            </div>
          </div>

          <div className="mentor-settings-grid">
            <div className="mentor-settings-field">
              <label htmlFor="learning_format">Learning Format</label>
              <select
                id="learning_format"
                name="learning_format"
                value={settings.learning_format}
                onChange={handleChange}
              >
                <option value="">Select learning format</option>
                <option value="Online">Online</option>
                <option value="Offline">Offline</option>
                <option value="Hybrid">Hybrid</option>
                <option value="Self-paced">Self-paced</option>
              </select>
            </div>

            <div className="mentor-settings-field">
              <label htmlFor="career_interests">Career Interests</label>
              <input
                id="career_interests"
                name="career_interests"
                type="text"
                value={settings.career_interests}
                onChange={handleChange}
                placeholder="e.g. Python, Web Development, AI"
              />
            </div>
          </div>
        </div>

        <div className="mentor-settings-card">
          <div className="mentor-settings-card-heading">
            <span className="mentor-settings-icon">🔔</span>
            <div>
              <h2>Notification Preferences</h2>
              <p>Choose which notifications you want to receive.</p>
            </div>
          </div>

          <div className="mentor-settings-options">

            <label className="mentor-settings-option">
              <div>
                <strong>Email Notifications</strong>
                <p>Receive important updates through email.</p>
              </div>
              <input
                type="checkbox"
                name="email_notifications"
                checked={Boolean(settings.email_notifications)}
                onChange={handleChange}
              />
              <span className="mentor-settings-switch" />
            </label>

            <label className="mentor-settings-option">
              <div>
                <strong>Learning Reminders</strong>
                <p>Receive reminders about learning activities.</p>
              </div>
              <input
                type="checkbox"
                name="learning_reminders"
                checked={Boolean(settings.learning_reminders)}
                onChange={handleChange}
              />
              <span className="mentor-settings-switch" />
            </label>

            <label className="mentor-settings-option">
              <div>
                <strong>Weekly Summary</strong>
                <p>Receive a weekly summary of your activities.</p>
              </div>
              <input
                type="checkbox"
                name="weekly_summary"
                checked={Boolean(settings.weekly_summary)}
                onChange={handleChange}
              />
              <span className="mentor-settings-switch" />
            </label>

          </div>
        </div>

        <div className="mentor-settings-card">
          <div className="mentor-settings-card-heading">
            <span className="mentor-settings-icon">🎨</span>
            <div>
              <h2>Appearance</h2>
              <p>Customize your application preferences.</p>
            </div>
          </div>

          <div className="mentor-settings-grid">
            <div className="mentor-settings-field">
              <label htmlFor="language">Language</label>
              <select
                id="language"
                name="language"
                value={settings.language}
                onChange={handleChange}
              >
                <option value="English">English</option>
                <option value="Telugu">Telugu</option>
                <option value="Hindi">Hindi</option>
              </select>
            </div>

            <div className="mentor-settings-field">
              <label htmlFor="theme">Theme</label>
              <select
                id="theme"
                name="theme"
                value={settings.theme}
                onChange={handleChange}
              >
                <option value="light">Light Mode</option>
                <option value="dark">Dark Mode</option>
              </select>
            </div>
          </div>
        </div>

        <div className="mentor-settings-actions">
          <button
            type="button"
            className="mentor-settings-reset"
            onClick={fetchSettings}
            disabled={saving}
          >
            Reset Changes
          </button>

          <button
            type="submit"
            className="mentor-settings-save"
            disabled={saving}
          >
            {saving ? "Saving..." : "Save Changes"}
          </button>
        </div>

      </form>
    </section>
  );
}

export default MentorSettings;
