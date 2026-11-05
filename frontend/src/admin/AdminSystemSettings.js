
import React, { useCallback, useEffect, useState } from "react";
import { API_BASE_URL, useAuth } from "../auth/AuthContext";
import "./AdminSystemSettings.css";

const INITIAL_SETTINGS = {
  platform_name: "SkillSphere",
  platform_tagline: "Know Your Skills, Shape Your Future",
  support_email: "",
  allow_registration: true,
  require_email_verification: true,
  maintenance_mode: false,
  email_notifications: true,
  learning_reminders: true,
  weekly_summary: true,
  minimum_password_length: 8,
  session_timeout_minutes: 60,
};

export default function AdminSystemSettings() {
  const auth = useAuth();

  const [settings, setSettings] = useState(INITIAL_SETTINGS);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [toast, setToast] = useState(null);
  const [dirty, setDirty] = useState(false);

  const token =
    auth?.accessToken ||
    auth?.access ||
    auth?.tokens?.access ||
    localStorage.getItem("skillsphere_access") ||
    localStorage.getItem("access");

  const showToast = useCallback((message, type = "success") => {
    setToast({ message, type });
    window.clearTimeout(window.__systemSettingsToastTimer);

    window.__systemSettingsToastTimer = window.setTimeout(() => {
      setToast(null);
    }, 3500);
  }, []);

  const apiRequest = useCallback(
    async (method = "GET", body = null) => {
      const response = await fetch(
        `${API_BASE_URL}/api/user-preferences/system/`,
        {
          method,
          headers: {
            Authorization: `Bearer ${token}`,
            ...(body ? { "Content-Type": "application/json" } : {}),
          },
          ...(body ? { body: JSON.stringify(body) } : {}),
        }
      );

      const data = await response.json().catch(() => ({}));

      if (!response.ok) {
        const firstError = Object.values(data).flat()[0];

        throw new Error(
          data.detail ||
            (typeof firstError === "string" ? firstError : null) ||
            `Request failed (${response.status}).`
        );
      }

      return data;
    },
    [token]
  );

  const loadSettings = useCallback(async () => {
    setLoading(true);

    try {
      const data = await apiRequest("GET");

      setSettings({
        ...INITIAL_SETTINGS,
        ...data,
      });

      setDirty(false);
    } catch (error) {
      showToast(error.message || "Unable to load system settings.", "error");
    } finally {
      setLoading(false);
    }
  }, [apiRequest, showToast]);

  useEffect(() => {
    loadSettings();
  }, [loadSettings]);

  function updateSetting(name, value) {
    setSettings((current) => ({
      ...current,
      [name]: value,
    }));
    setDirty(true);
  }

  async function handleSave(event) {
    event.preventDefault();

    if (!settings.platform_name.trim()) {
      showToast("Platform name is required.", "error");
      return;
    }

    const passwordLength = Number(settings.minimum_password_length);
    const sessionTimeout = Number(settings.session_timeout_minutes);

    if (passwordLength < 8 || passwordLength > 128) {
      showToast("Password length must be between 8 and 128.", "error");
      return;
    }

    if (sessionTimeout < 5 || sessionTimeout > 1440) {
      showToast("Session timeout must be between 5 and 1440 minutes.", "error");
      return;
    }

    setSaving(true);

    try {
      const payload = {
        ...settings,
        platform_name: settings.platform_name.trim(),
        platform_tagline: settings.platform_tagline.trim(),
        support_email: settings.support_email.trim(),
        minimum_password_length: passwordLength,
        session_timeout_minutes: sessionTimeout,
      };

      const saved = await apiRequest("PATCH", payload);

      setSettings({
        ...INITIAL_SETTINGS,
        ...saved,
      });

      setDirty(false);
      showToast("System settings saved successfully!", "success");
    } catch (error) {
      showToast(error.message || "Unable to save settings.", "error");
    } finally {
      setSaving(false);
    }
  }

  function handleReset() {
    if (!window.confirm("Discard your unsaved changes?")) return;

    loadSettings();
    showToast("Reloading saved settings.", "success");
  }

  function Toggle({ name, label, description }) {
    return (
      <div className="ass-setting-row">
        <div className="ass-setting-copy">
          <strong>{label}</strong>
          <p>{description}</p>
        </div>

        <button
          type="button"
          className={`ass-switch ${settings[name] ? "is-on" : ""}`}
          role="switch"
          aria-checked={Boolean(settings[name])}
          aria-label={label}
          onClick={() => updateSetting(name, !settings[name])}
          disabled={loading || saving}
        >
          <span />
        </button>
      </div>
    );
  }

  if (loading) {
    return (
      <div className="admin-system-settings">
        <div className="ass-loading">
          <span className="ass-spinner" />
          <p>Loading system settings...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="admin-system-settings">
      {toast && (
        <div
          className={`ass-toast ass-toast-${toast.type}`}
          role="status"
          aria-live="polite"
        >
          <span className="ass-toast-icon">
            {toast.type === "success" ? "✓" : "!"}
          </span>

          <span>{toast.message}</span>

          <button
            type="button"
            aria-label="Close notification"
            onClick={() => {
              window.clearTimeout(window.__systemSettingsToastTimer);
              setToast(null);
            }}
          >
            ×
          </button>
        </div>
      )}

      <header className="ass-header">
        <div>
          <h2>System Settings</h2>
          <p>Configure platform-wide preferences and administration.</p>
        </div>

        <span className="ass-status">
          <span />
          Administration
        </span>
      </header>

      <form onSubmit={handleSave}>
        <section className="ass-card">
          <div className="ass-section-heading">
            <span className="ass-section-icon">⚙</span>
            <div>
              <h3>General Settings</h3>
              <p>Manage your platform identity and support information.</p>
            </div>
          </div>

          <div className="ass-form-grid">
            <div className="ass-field">
              <label htmlFor="ass-platform-name">Platform Name</label>
              <input
                id="ass-platform-name"
                value={settings.platform_name}
                onChange={(e) => updateSetting("platform_name", e.target.value)}
                maxLength={100}
                required
              />
            </div>

            <div className="ass-field">
              <label htmlFor="ass-support-email">Support Email</label>
              <input
                id="ass-support-email"
                type="email"
                value={settings.support_email}
                onChange={(e) => updateSetting("support_email", e.target.value)}
                placeholder="support@example.com"
              />
            </div>

            <div className="ass-field ass-field-full">
              <label htmlFor="ass-tagline">Platform Tagline</label>
              <input
                id="ass-tagline"
                value={settings.platform_tagline}
                onChange={(e) => updateSetting("platform_tagline", e.target.value)}
                maxLength={255}
              />
            </div>
          </div>
        </section>

        <section className="ass-card">
          <div className="ass-section-heading">
            <span className="ass-section-icon">♙</span>
            <div>
              <h3>User Management</h3>
              <p>Configure registration and account verification preferences.</p>
            </div>
          </div>

          <div className="ass-settings-list">
            <Toggle
              name="allow_registration"
              label="Allow New Registrations"
              description="Allow new users to register for SkillSphere."
            />
            <Toggle
              name="require_email_verification"
              label="Require Email Verification"
              description="Require users to verify their email during registration."
            />
          </div>
        </section>

        <section className="ass-card">
          <div className="ass-section-heading">
            <span className="ass-section-icon">♧</span>
            <div>
              <h3>Notification Settings</h3>
              <p>Set the platform-wide notification preferences.</p>
            </div>
          </div>

          <div className="ass-settings-list">
            <Toggle
              name="email_notifications"
              label="Email Notifications"
              description="Enable platform email notification preferences."
            />
            <Toggle
              name="learning_reminders"
              label="Learning Reminders"
              description="Enable learning reminder preferences."
            />
            <Toggle
              name="weekly_summary"
              label="Weekly Summary"
              description="Enable weekly summary preferences."
            />
          </div>
        </section>

        <section className="ass-card">
          <div className="ass-section-heading">
            <span className="ass-section-icon">♙</span>
            <div>
              <h3>Security Settings</h3>
              <p>Configure the password policy and session preferences.</p>
            </div>
          </div>

          <div className="ass-form-grid">
            <div className="ass-field">
              <label htmlFor="ass-password-length">
                Minimum Password Length
              </label>
              <input
                id="ass-password-length"
                type="number"
                min="8"
                max="128"
                value={settings.minimum_password_length}
                onChange={(e) =>
                  updateSetting("minimum_password_length", e.target.value)
                }
                required
              />
              <small>Allowed range: 8–128 characters.</small>
            </div>

            <div className="ass-field">
              <label htmlFor="ass-session-timeout">
                Session Timeout (minutes)
              </label>
              <input
                id="ass-session-timeout"
                type="number"
                min="5"
                max="1440"
                value={settings.session_timeout_minutes}
                onChange={(e) =>
                  updateSetting("session_timeout_minutes", e.target.value)
                }
                required
              />
              <small>Allowed range: 5–1440 minutes.</small>
            </div>
          </div>
        </section>

        <section className="ass-card ass-maintenance-card">
          <div className="ass-section-heading">
            <span className="ass-section-icon">⚠</span>
            <div>
              <h3>Maintenance</h3>
              <p>Configure the platform maintenance flag.</p>
            </div>
          </div>

          <Toggle
            name="maintenance_mode"
            label="Maintenance Mode"
            description="Save the maintenance-mode setting for future backend enforcement."
          />

          {settings.maintenance_mode && (
            <p className="ass-maintenance-warning">
              Maintenance mode is enabled in settings. This flag does not
              automatically block access until connected to backend
              enforcement.
            </p>
          )}
        </section>

        <footer className="ass-save-footer">
          <p>
            {dirty
              ? "You have unsaved changes."
              : "Your settings are synchronized with the server."}
          </p>

          <div>
            <button
              type="button"
              className="ass-reset-button"
              onClick={handleReset}
              disabled={saving || !dirty}
            >
              Discard Changes
            </button>

            <button
              type="submit"
              className="ass-save-button"
              disabled={saving || !dirty}
            >
              {saving ? "Saving..." : "Save Changes"}
            </button>
          </div>
        </footer>
      </form>
    </div>
  );
}
