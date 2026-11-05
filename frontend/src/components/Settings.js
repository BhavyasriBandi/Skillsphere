
import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Settings.css";
import { showToast } from "../components/ToastProvider";
import { API_BASE_URL, useAuth } from "../auth/AuthContext";

const SETTINGS_KEY = "skillsphere_student_settings";

const DEFAULT_SETTINGS = {
  firstName: "",
  lastName: "",
  displayName: "",
  email: "",
  language: "English",
  emailNotifications: true,
  learningReminders: true,
  achievementAlerts: true,
  weeklySummary: false,
  theme: "light",
};

function loadSettings() {
  try {
    const saved = localStorage.getItem(SETTINGS_KEY);

    if (saved) {
      const parsed = JSON.parse(saved);

      if (
        parsed &&
        typeof parsed === "object" &&
        !Array.isArray(parsed)
      ) {
        const nameParts = String(parsed.displayName || "")
          .trim()
          .split(/\s+/)
          .filter(Boolean);

        const firstName = parsed.firstName || nameParts.shift() || "";
        const lastName = parsed.lastName || nameParts.join(" ");

        return {
          ...DEFAULT_SETTINGS,
          ...parsed,
          firstName,
          lastName,
          displayName: [firstName, lastName]
            .filter(Boolean)
            .join(" "),
        };
      }
    }
  } catch {
    // Use default preferences if browser storage cannot be read.
  }

  return { ...DEFAULT_SETTINGS };
}

/* Apply theme globally across SkillSphere */
function applyGlobalTheme(theme) {
  const selectedTheme = theme === "dark" ? "dark" : "light";

  document.documentElement.setAttribute(
    "data-theme",
    selectedTheme
  );

  document.body.setAttribute(
    "data-theme",
    selectedTheme
  );

  window.dispatchEvent(
    new CustomEvent("skillsphere-theme-change", {
      detail: { theme: selectedTheme },
    })
  );
}

async function readResponse(response) {
  const data = await response.json().catch(() => ({}));

  if (!response.ok) {
    const detail = data.detail || data.message;

    const errors = detail
      ? [detail]
      : Object.entries(data).map(([key, value]) => {
          const messages = Array.isArray(value)
            ? value.join(" ")
            : typeof value === "object"
              ? JSON.stringify(value)
              : String(value);

          return `${key}: ${messages}`;
        });

    throw new Error(
      errors.length
        ? errors.join(" ")
        : `Request failed (${response.status}).`
    );
  }

  return data;
}

function getErrorMessage(error) {
  return error?.message || "Something went wrong. Please try again.";
}

function Settings() {
  const navigate = useNavigate();
  const { user, accessToken, logout } = useAuth();

  const [settings, setSettings] = useState(loadSettings);
  const [activeSection, setActiveSection] = useState("Account");
  const [showResetConfirm, setShowResetConfirm] = useState(false);
  const [showLogoutConfirm, setShowLogoutConfirm] = useState(false);
  const [loadingProfile, setLoadingProfile] = useState(true);
  const [saving, setSaving] = useState(false);
  const [passwordSaving, setPasswordSaving] = useState(false);

  const [passwordForm, setPasswordForm] = useState({
    current_password: "",
    new_password: "",
    confirm_new_password: "",
  });

  // Apply the theme already saved in browser storage.
  useEffect(() => {
    applyGlobalTheme(loadSettings().theme);
  }, []);

  // Load the student's existing account details from Django.
  useEffect(() => {
    let cancelled = false;

    async function loadProfile() {
      const token =
        accessToken || localStorage.getItem("skillsphere_access");

      if (!token) {
        if (!cancelled) setLoadingProfile(false);
        return;
      }

      try {
        const response = await fetch(
          `${API_BASE_URL}/api/auth/profile/`,
          {
            method: "GET",
            headers: {
              Authorization: `Bearer ${token}`,
              Accept: "application/json",
            },
          }
        );

        const profile = await readResponse(response);

        if (cancelled) return;

        const firstName = profile.first_name || "";
        const lastName = profile.last_name || "";

        setSettings((current) => ({
          ...current,
          firstName: firstName || current.firstName || "",
          lastName: lastName || current.lastName || "",
          displayName: [
            firstName || current.firstName,
            lastName || current.lastName,
          ]
            .filter(Boolean)
            .join(" "),
          email: profile.email || current.email || user?.email || "",
        }));
      } catch (error) {
        if (!cancelled) {
          showToast(
            `Unable to load account details: ${getErrorMessage(error)}`,
            "error"
          );
        }
      } finally {
        if (!cancelled) setLoadingProfile(false);
      }
    }

    loadProfile();

    return () => {
      cancelled = true;
    };
  }, [accessToken, user?.email]);

  // Load saved notification and appearance preferences from Django.
  useEffect(() => {
    let cancelled = false;

    async function loadPreferences() {
      const token =
        accessToken || localStorage.getItem("skillsphere_access");

      if (!token) return;

      try {
        const response = await fetch(
          `${API_BASE_URL}/api/user-preferences/`,
          {
            method: "GET",
            headers: {
              Authorization: `Bearer ${token}`,
              Accept: "application/json",
            },
          }
        );

        const data = await readResponse(response);

        if (cancelled) return;

        const preferences = data.preferences || data;
        const savedSettings = loadSettings();

        const updated = {
          ...savedSettings,
          emailNotifications:
            preferences.email_notifications ??
            savedSettings.emailNotifications,
          learningReminders:
            preferences.learning_reminders ??
            savedSettings.learningReminders,
          weeklySummary:
            preferences.weekly_summary ??
            savedSettings.weeklySummary,
          language: preferences.language || savedSettings.language,
          theme: preferences.theme || savedSettings.theme,
        };

        const finalSettings = {
          ...updated,
          firstName: savedSettings.firstName,
          lastName: savedSettings.lastName,
          displayName: savedSettings.displayName,
          email: savedSettings.email,
        };

        setSettings((current) => ({
          ...current,
          ...finalSettings,
          firstName: current.firstName || finalSettings.firstName,
          lastName: current.lastName || finalSettings.lastName,
          displayName: current.displayName || finalSettings.displayName,
          email: current.email || finalSettings.email,
        }));

        localStorage.setItem(
          SETTINGS_KEY,
          JSON.stringify(finalSettings)
        );

        applyGlobalTheme(updated.theme);
      } catch (error) {
        if (!cancelled) {
          showToast(
            `Unable to load saved preferences: ${getErrorMessage(error)}`,
            "error"
          );
        }
      }
    }

    loadPreferences();

    return () => {
      cancelled = true;
    };
  }, [accessToken]);

  // Update a setting and immediately apply theme changes.
  function updateSetting(field, value) {
    setSettings((current) => ({
      ...current,
      [field]: value,
    }));

    if (field === "theme") {
      applyGlobalTheme(value);
    }
  }

  function updatePassword(field, value) {
    setPasswordForm((current) => ({
      ...current,
      [field]: value,
    }));
  }

  // Save account details or notification and appearance preferences.
  async function saveSettings(event) {
    event.preventDefault();

    if (saving) return;

    const firstName = String(settings.firstName || "").trim();
    const lastName = String(settings.lastName || "").trim();

    const settingsToSave = {
      ...settings,
      firstName,
      lastName,
      displayName: [firstName, lastName].filter(Boolean).join(" "),
      email: String(settings.email || "").trim(),
    };

    const token =
      accessToken || localStorage.getItem("skillsphere_access");

    if (!token) {
      showToast(
        "Your session has expired. Please log in again.",
        "error"
      );
      return;
    }

    if (activeSection === "Account") {
      if (!firstName || !lastName) {
        showToast(
          "Please enter both your first name and last name.",
          "error"
        );
        return;
      }

      setSaving(true);

      try {
        const response = await fetch(
          `${API_BASE_URL}/api/auth/profile/`,
          {
            method: "PATCH",
            headers: {
              Authorization: `Bearer ${token}`,
              "Content-Type": "application/json",
              Accept: "application/json",
            },
            body: JSON.stringify({
              first_name: firstName,
              last_name: lastName,
            }),
          }
        );

        const data = await readResponse(response);
        const profile = data.profile || data;

        const updatedFirstName = profile.first_name || firstName;
        const updatedLastName = profile.last_name || lastName;

        const updatedSettings = {
          ...settingsToSave,
          firstName: updatedFirstName,
          lastName: updatedLastName,
          displayName: [
            updatedFirstName,
            updatedLastName,
          ]
            .filter(Boolean)
            .join(" "),
          email: profile.email || settingsToSave.email,
        };

        localStorage.setItem(
          SETTINGS_KEY,
          JSON.stringify(updatedSettings)
        );

        setSettings(updatedSettings);

        try {
          const savedUser = JSON.parse(
            localStorage.getItem("skillsphere_user") || "{}"
          );

          localStorage.setItem(
            "skillsphere_user",
            JSON.stringify({
              ...savedUser,
              first_name: updatedFirstName,
              last_name: updatedLastName,
              email: updatedSettings.email,
            })
          );
        } catch {
          // The Django profile update has already succeeded.
        }

        showToast(
          data.message || "Account details updated successfully.",
          "success"
        );
      } catch (error) {
        showToast(getErrorMessage(error), "error");
      } finally {
        setSaving(false);
      }

      return;
    }

    setSaving(true);

    try {
      const response = await fetch(
        `${API_BASE_URL}/api/user-preferences/`,
        {
          method: "PATCH",
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
            Accept: "application/json",
          },
          body: JSON.stringify({
            email_notifications: Boolean(
              settingsToSave.emailNotifications
            ),
            learning_reminders: Boolean(
              settingsToSave.learningReminders
            ),
            weekly_summary: Boolean(settingsToSave.weeklySummary),
            language: settingsToSave.language,
            theme: settingsToSave.theme,
          }),
        }
      );

      const data = await readResponse(response);
      const savedPreferences = data.preferences || {};

      const updatedSettings = {
        ...settingsToSave,
        emailNotifications:
          savedPreferences.email_notifications ??
          settingsToSave.emailNotifications,
        learningReminders:
          savedPreferences.learning_reminders ??
          settingsToSave.learningReminders,
        weeklySummary:
          savedPreferences.weekly_summary ??
          settingsToSave.weeklySummary,
        language: savedPreferences.language || settingsToSave.language,
        theme: savedPreferences.theme || settingsToSave.theme,
      };

      localStorage.setItem(
        SETTINGS_KEY,
        JSON.stringify(updatedSettings)
      );

      setSettings(updatedSettings);
      applyGlobalTheme(updatedSettings.theme);

      showToast(
        data.message || "Your preferences have been saved to your account.",
        "success"
      );
    } catch (error) {
      showToast(
        `Unable to save preferences: ${getErrorMessage(error)}`,
        "error"
      );
    } finally {
      setSaving(false);
    }
  }

  async function resetSettings() {
    const token =
      accessToken || localStorage.getItem("skillsphere_access");

    if (!token) {
      showToast(
        "Your session has expired. Please log in again.",
        "error"
      );
      return;
    }

    setSaving(true);

    try {
      const response = await fetch(
        `${API_BASE_URL}/api/user-preferences/`,
        {
          method: "PATCH",
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
            Accept: "application/json",
          },
          body: JSON.stringify({
            email_notifications: DEFAULT_SETTINGS.emailNotifications,
            learning_reminders: DEFAULT_SETTINGS.learningReminders,
            weekly_summary: DEFAULT_SETTINGS.weeklySummary,
            language: DEFAULT_SETTINGS.language,
            theme: DEFAULT_SETTINGS.theme,
          }),
        }
      );

      await readResponse(response);

      const reset = {
        ...DEFAULT_SETTINGS,
        firstName: settings.firstName,
        lastName: settings.lastName,
        displayName: [
          settings.firstName,
          settings.lastName,
        ]
          .filter(Boolean)
          .join(" "),
        email: settings.email,
      };

      localStorage.setItem(SETTINGS_KEY, JSON.stringify(reset));
      setSettings(reset);
      applyGlobalTheme(reset.theme);
      setShowResetConfirm(false);

      showToast(
        "Preferences restored to their defaults.",
        "success"
      );
    } catch (error) {
      showToast(
        `Unable to reset preferences: ${getErrorMessage(error)}`,
        "error"
      );
    } finally {
      setSaving(false);
    }
  }

  async function changePassword(event) {
    event.preventDefault();

    if (passwordSaving) return;

    if (
      !passwordForm.current_password ||
      !passwordForm.new_password ||
      !passwordForm.confirm_new_password
    ) {
      showToast("Please fill in all password fields.", "error");
      return;
    }

    if (
      passwordForm.new_password !==
      passwordForm.confirm_new_password
    ) {
      showToast("The new passwords do not match.", "error");
      return;
    }

    if (passwordForm.new_password.length < 8) {
      showToast(
        "Your new password must contain at least 8 characters.",
        "error"
      );
      return;
    }

    const token =
      accessToken || localStorage.getItem("skillsphere_access");

    if (!token) {
      showToast(
        "Your session has expired. Please log in again.",
        "error"
      );
      return;
    }

    setPasswordSaving(true);

    try {
      const response = await fetch(
        `${API_BASE_URL}/api/auth/change-password/`,
        {
          method: "POST",
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
            Accept: "application/json",
          },
          body: JSON.stringify(passwordForm),
        }
      );

      const data = await readResponse(response);

      setPasswordForm({
        current_password: "",
        new_password: "",
        confirm_new_password: "",
      });

      showToast(
        data.message ||
          "Password changed successfully. Please log in again.",
        "success"
      );

      await Promise.resolve(logout());
      navigate("/login", { replace: true });
    } catch (error) {
      showToast(getErrorMessage(error), "error");
    } finally {
      setPasswordSaving(false);
    }
  }

  async function confirmLogout() {
    setShowLogoutConfirm(false);

    try {
      await Promise.resolve(logout());
      navigate("/login", { replace: true });
    } catch (error) {
      showToast(
        `Unable to complete logout: ${getErrorMessage(error)}`,
        "error"
      );
    }
  }

  const sections = [
    { name: "Account", icon: "👤" },
    { name: "Notifications", icon: "🔔" },
    { name: "Appearance", icon: "🎨" },
    { name: "Security", icon: "🔒" },
  ];

  return (
    <main className="ss-page">
      <header className="ss-header">
        <div>
          <span className="ss-eyebrow">
            PERSONALISE YOUR EXPERIENCE
          </span>
          <h1>Settings</h1>
          <p>
            Manage your preferences and make SkillSphere work for you.
          </p>
        </div>

        <div className="ss-header-icon" aria-hidden="true">
          ⚙️
        </div>
      </header>

      <div className="ss-layout">
        <aside className="ss-nav">
          <h2>Preferences</h2>

          {sections.map((section) => (
            <button
              key={section.name}
              type="button"
              className={
                activeSection === section.name
                  ? "ss-nav-item ss-nav-active"
                  : "ss-nav-item"
              }
              onClick={() => setActiveSection(section.name)}
            >
              <span>{section.icon}</span>
              {section.name}
              <span className="ss-nav-arrow">›</span>
            </button>
          ))}

          <div className="ss-nav-note">
            <span>💡</span>
            <p>
              Remember to save your changes before leaving this page.
            </p>
          </div>
        </aside>

        <section className="ss-content">
          {activeSection === "Account" && (
            <form onSubmit={saveSettings} noValidate>
              <div className="ss-section-heading">
                <div>
                  <h2>Account Preferences</h2>
                  <p>
                    Manage the personal information shown in your account.
                  </p>
                </div>
                <span className="ss-section-icon">👤</span>
              </div>

              <div className="ss-field-grid">
                <label>
                  First Name
                  <input
                    type="text"
                    value={settings.firstName}
                    onChange={(event) =>
                      updateSetting("firstName", event.target.value)
                    }
                    placeholder="Enter your first name"
                    autoComplete="given-name"
                    disabled={loadingProfile || saving}
                    required
                  />
                </label>

                <label>
                  Last Name
                  <input
                    type="text"
                    value={settings.lastName}
                    onChange={(event) =>
                      updateSetting("lastName", event.target.value)
                    }
                    placeholder="Enter your last name"
                    autoComplete="family-name"
                    disabled={loadingProfile || saving}
                    required
                  />
                </label>

                <label>
                  Email Address
                  <input
                    type="email"
                    value={settings.email}
                    readOnly
                    aria-readonly="true"
                    placeholder="Your registered email"
                  />
                  <small>
                    Your login email is managed by your account. Email
                    editing is not enabled by the current Django
                    profile API.
                  </small>
                </label>

                <label>
                  Preferred Language
                  <select
                    value={settings.language}
                    onChange={(event) =>
                      updateSetting("language", event.target.value)
                    }
                  >
                    <option value="English">English</option>
                    <option value="Telugu">Telugu</option>
                    <option value="Hindi">Hindi</option>
                  </select>
                </label>
              </div>

              <div className="ss-form-footer">
                <span>
                  {loadingProfile
                    ? "Loading your account..."
                    : "Your name is saved to your Django account."}
                </span>

                <button
                  className="ss-primary-button"
                  type="submit"
                  disabled={loadingProfile || saving}
                >
                  {saving ? "Saving..." : "✓ Save Preferences"}
                </button>
              </div>
            </form>
          )}

          {activeSection === "Notifications" && (
            <form onSubmit={saveSettings} noValidate>
              <div className="ss-section-heading">
                <div>
                  <h2>Notification Preferences</h2>
                  <p>Choose the reminders you want to enable.</p>
                </div>
                <span className="ss-section-icon">🔔</span>
              </div>

              <div className="ss-toggle-list">
                {[
                  {
                    field: "emailNotifications",
                    title: "Email Notifications",
                    description:
                      "Allow email updates when email delivery is connected.",
                  },
                  {
                    field: "learningReminders",
                    title: "Learning Reminders",
                    description:
                      "Keep learning goals and practice sessions in mind.",
                  },
                  {
                    field: "achievementAlerts",
                    title: "Achievement Alerts",
                    description:
                      "Show your achievement-related preference.",
                  },
                  {
                    field: "weeklySummary",
                    title: "Weekly Summary",
                    description:
                      "Choose whether you want a weekly progress summary.",
                  },
                ].map((item) => (
                  <div className="ss-toggle-row" key={item.field}>
                    <div>
                      <h3>{item.title}</h3>
                      <p>{item.description}</p>
                    </div>

                    <label className="ss-switch">
                      <input
                        type="checkbox"
                        checked={settings[item.field]}
                        onChange={(event) =>
                          updateSetting(
                            item.field,
                            event.target.checked
                          )
                        }
                      />
                      <span className="ss-switch-track" />
                    </label>
                  </div>
                ))}
              </div>

              <div className="ss-form-footer">
                <span>
                  These are saved preferences, not active email delivery.
                </span>
                <button
                  className="ss-primary-button"
                  type="submit"
                  disabled={saving}
                >
                  {saving ? "Saving..." : "✓ Save Preferences"}
                </button>
              </div>
            </form>
          )}

          {activeSection === "Appearance" && (
            <form onSubmit={saveSettings} noValidate>
              <div className="ss-section-heading">
                <div>
                  <h2>Appearance</h2>
                  <p>Choose your preferred appearance setting.</p>
                </div>
                <span className="ss-section-icon">🎨</span>
              </div>

              <div className="ss-theme-options">
                <button
                  type="button"
                  className={
                    settings.theme === "light"
                      ? "ss-theme-card ss-theme-selected"
                      : "ss-theme-card"
                  }
                  onClick={() => updateSetting("theme", "light")}
                >
                  <span className="ss-theme-art ss-theme-light-art">
                    <span />
                    <span />
                    <span />
                  </span>
                  <strong>Light Theme</strong>
                  <small>Clean and bright</small>
                  {settings.theme === "light" && (
                    <span className="ss-theme-check">✓ Selected</span>
                  )}
                </button>

                <button
                  type="button"
                  className={
                    settings.theme === "dark"
                      ? "ss-theme-card ss-theme-selected"
                      : "ss-theme-card"
                  }
                  onClick={() => updateSetting("theme", "dark")}
                >
                  <span className="ss-theme-art ss-theme-dark-art">
                    <span />
                    <span />
                    <span />
                  </span>
                  <strong>Dark Theme</strong>
                  <small>Low-light appearance preference</small>
                  {settings.theme === "dark" && (
                    <span className="ss-theme-check">✓ Selected</span>
                  )}
                </button>
              </div>

              <p className="ss-helper-text">
                Your selected theme is applied immediately across the app.
                Save Appearance to store your preference.
              </p>

              <div className="ss-form-footer">
                <span>
                  Choose a theme and save your selection.
                </span>
                <button
                  className="ss-primary-button"
                  type="submit"
                  disabled={saving}
                >
                  {saving ? "Saving..." : "✓ Save Appearance"}
                </button>
              </div>
            </form>
          )}

          {activeSection === "Security" && (
            <div>
              <div className="ss-section-heading">
                <div>
                  <h2>Security &amp; Account</h2>
                  <p>
                    Change your password or sign out of SkillSphere.
                  </p>
                </div>
                <span className="ss-section-icon">🔒</span>
              </div>

              <div className="ss-security-card">
                <div className="ss-security-icon">🔑</div>
                <div className="ss-security-copy">
                  <h3>Password Management</h3>
                  <p>
                    Change your password securely using your current
                    password. You will need to log in again after a
                    successful change.
                  </p>
                </div>
              </div>

              <form onSubmit={changePassword} noValidate>
                <div className="ss-field-grid">
                  <label>
                    Current Password
                    <input
                      type="password"
                      value={passwordForm.current_password}
                      onChange={(event) =>
                        updatePassword(
                          "current_password",
                          event.target.value
                        )
                      }
                      autoComplete="current-password"
                      required
                    />
                  </label>

                  <label>
                    New Password
                    <input
                      type="password"
                      value={passwordForm.new_password}
                      onChange={(event) =>
                        updatePassword(
                          "new_password",
                          event.target.value
                        )
                      }
                      autoComplete="new-password"
                      minLength={8}
                      required
                    />
                  </label>

                  <label>
                    Confirm New Password
                    <input
                      type="password"
                      value={passwordForm.confirm_new_password}
                      onChange={(event) =>
                        updatePassword(
                          "confirm_new_password",
                          event.target.value
                        )
                      }
                      autoComplete="new-password"
                      minLength={8}
                      required
                    />
                  </label>
                </div>

                <div className="ss-form-footer">
                  <span>
                    Use at least 8 characters and follow your account's
                    password rules.
                  </span>
                  <button
                    className="ss-primary-button"
                    type="submit"
                    disabled={passwordSaving}
                  >
                    {passwordSaving
                      ? "Updating..."
                      : "Update Password"}
                  </button>
                </div>
              </form>

              <div className="ss-security-card">
                <div className="ss-security-icon">🚪</div>
                <div className="ss-security-copy">
                  <h3>Sign Out</h3>
                  <p>
                    Sign out of your current SkillSphere session.
                  </p>
                </div>
                <button
                  type="button"
                  className="ss-danger-button"
                  onClick={() => setShowLogoutConfirm(true)}
                >
                  Logout
                </button>
              </div>
            </div>
          )}

          <div className="ss-bottom-actions">
            <button
              type="button"
              className="ss-reset-button"
              onClick={() => setShowResetConfirm(true)}
            >
              Reset Preferences
            </button>
          </div>
        </section>
      </div>

      {showResetConfirm && (
        <div className="ss-modal-backdrop">
          <section
            className="ss-confirm-modal"
            role="dialog"
            aria-modal="true"
            aria-labelledby="ss-reset-title"
          >
            <div className="ss-modal-icon">↻</div>
            <h2 id="ss-reset-title">Reset your preferences?</h2>
            <p>
              Your saved notification, language, and theme preferences
              will return to their defaults. Your account name and email
              will not be changed.
            </p>

            <div className="ss-modal-actions">
              <button
                type="button"
                className="ss-cancel-button"
                onClick={() => setShowResetConfirm(false)}
              >
                Cancel
              </button>
              <button
                type="button"
                className="ss-primary-button"
                onClick={resetSettings}
                disabled={saving}
              >
                {saving ? "Resetting..." : "Reset Preferences"}
              </button>
            </div>
          </section>
        </div>
      )}

      {showLogoutConfirm && (
        <div className="ss-modal-backdrop">
          <section
            className="ss-confirm-modal"
            role="dialog"
            aria-modal="true"
            aria-labelledby="ss-logout-title"
          >
            <div className="ss-modal-icon">🚪</div>
            <h2 id="ss-logout-title">Ready to log out?</h2>
            <p>You'll be returned to the login page.</p>

            <div className="ss-modal-actions">
              <button
                type="button"
                className="ss-cancel-button"
                onClick={() => setShowLogoutConfirm(false)}
              >
                Cancel
              </button>
              <button
                type="button"
                className="ss-danger-button"
                onClick={confirmLogout}
              >
                Yes, Logout
              </button>
            </div>
          </section>
        </div>
      )}
    </main>
  );
}

export default Settings;
