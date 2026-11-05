
import React, { useEffect, useRef, useState } from "react";
import "./Login.css";

const API_BASE_URL = "http://127.0.0.1:8000";

const ACCESS_KEY = "skillsphere_access";
const REFRESH_KEY = "skillsphere_refresh";
const USER_KEY = "skillsphere_user";
const SAVED_EMAIL_KEY = "skillsphere_saved_email";
const EMAIL_HISTORY_KEY = "skillsphere_email_history";

const TOAST_DURATION = 3000;
const REDIRECT_DELAY = 3200;

const roles = [
  {
    value: "student",
    title: "Student",
    icon: "🎓",
    description: "Build skills and explore career opportunities.",
  },
  {
    value: "mentor",
    title: "Mentor",
    icon: "⏱️",
    description: "Guide learners and share your expertise.",
  },
  {
    value: "admin",
    title: "Admin",
    icon: "🛡️",
    description: "Manage users and platform operations.",
  },
];

function normalizeRole(value) {
  const role = String(value || "").trim().toLowerCase();

  if (role === "admin" || role === "platform admin") return "admin";
  if (role === "mentor") return "mentor";
  if (role === "student") return "student";

  return "";
}

export default function Login() {
  const [email, setEmail] = useState(
    () => localStorage.getItem(SAVED_EMAIL_KEY) || ""
  );

  const [emailHistory, setEmailHistory] = useState(() => {
    try {
      const saved = JSON.parse(
        localStorage.getItem(EMAIL_HISTORY_KEY) || "[]"
      );

      if (Array.isArray(saved)) {
        return saved.filter((item) => typeof item === "string");
      }

      return [];
    } catch {
      return [];
    }
  });

  const [showEmailSuggestions, setShowEmailSuggestions] = useState(false);
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("");
  const [showPassword, setShowPassword] = useState(false);

  const [rememberEmail, setRememberEmail] = useState(
    () => Boolean(localStorage.getItem(SAVED_EMAIL_KEY))
  );

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [toast, setToast] = useState(null);

  const redirectTimer = useRef(null);
  const toastTimer = useRef(null);

  // Add the older saved email to history if history is empty.
  useEffect(() => {
    const oldSavedEmail = localStorage.getItem(SAVED_EMAIL_KEY);

    if (oldSavedEmail && emailHistory.length === 0) {
      const history = [oldSavedEmail];

      setEmailHistory(history);
      localStorage.setItem(
        EMAIL_HISTORY_KEY,
        JSON.stringify(history)
      );
    }
  }, []);

  useEffect(() => {
    return () => {
      if (redirectTimer.current) {
        window.clearTimeout(redirectTimer.current);
      }

      if (toastTimer.current) {
        window.clearTimeout(toastTimer.current);
      }
    };
  }, []);

  // Toast notification.
  function showToast(type, message, duration = TOAST_DURATION) {
    if (toastTimer.current) {
      window.clearTimeout(toastTimer.current);
    }

    setToast({
      type,
      message,
      duration,
      id: Date.now(),
    });

    toastTimer.current = window.setTimeout(() => {
      setToast(null);
      toastTimer.current = null;
    }, duration);
  }

  // Save email history.
  function saveEmailHistory(nextHistory) {
    setEmailHistory(nextHistory);

    try {
      localStorage.setItem(
        EMAIL_HISTORY_KEY,
        JSON.stringify(nextHistory)
      );
    } catch (storageError) {
      console.error("Email history error:", storageError);
    }
  }

  // Email input handler.
  function handleEmailChange(event) {
    const value = event.target.value;

    setEmail(value);
    setShowEmailSuggestions(true);
  }

  // Select suggested email.
  function handleEmailSuggestionSelect(suggestedEmail) {
    setEmail(suggestedEmail);
    setShowEmailSuggestions(false);
  }

  // Remember email checkbox.
  function handleRememberEmailChange(event) {
    const checked = event.target.checked;

    setRememberEmail(checked);

    const currentEmail = email.trim().toLowerCase();

    if (checked) {
      if (currentEmail) {
        const nextHistory = [
          currentEmail,
          ...emailHistory.filter(
            (item) => item.toLowerCase() !== currentEmail
          ),
        ].slice(0, 10);

        saveEmailHistory(nextHistory);
        localStorage.setItem(SAVED_EMAIL_KEY, currentEmail);
      }
    } else {
      const nextHistory = emailHistory.filter(
        (item) => item.toLowerCase() !== currentEmail
      );

      saveEmailHistory(nextHistory);
      localStorage.removeItem(SAVED_EMAIL_KEY);
    }
  }

  // Show all saved emails when the field is empty.
  // Filter saved emails when the user starts typing.
  const filteredEmailSuggestions =
    email.trim().length === 0
      ? emailHistory
      : emailHistory.filter((item) =>
          item.toLowerCase().startsWith(email.trim().toLowerCase())
        );

  // Login handler.
  async function handleLogin(event) {
    event.preventDefault();

    if (loading) return;

    if (redirectTimer.current) {
      window.clearTimeout(redirectTimer.current);
      redirectTimer.current = null;
    }

    if (toastTimer.current) {
      window.clearTimeout(toastTimer.current);
      toastTimer.current = null;
    }

    setError("");
    setToast(null);

    const normalizedEmail = email.trim().toLowerCase();
    const selectedRole = normalizeRole(role);

    if (!normalizedEmail || !password || !selectedRole) {
      const message =
        "Please enter your email, password, and role.";

      setError(message);
      showToast("error", message);
      return;
    }

    setLoading(true);

    try {
      const response = await fetch(
        `${API_BASE_URL}/api/auth/login/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json",
          },
          body: JSON.stringify({
            email: normalizedEmail,
            password,
            role: selectedRole,
          }),
        }
      );

      const data = await response.json().catch(() => ({}));

      if (!response.ok) {
        const message =
          data.detail ||
          data.message ||
          data.error ||
          (typeof data === "object"
            ? Object.values(data)
                .flat()
                .filter((item) => typeof item === "string")
                .join(" ")
            : "") ||
          "Login failed. Please check your credentials.";

        throw new Error(message);
      }

      const accessToken = data.access || data.access_token;
      const refreshToken = data.refresh || data.refresh_token;

      if (!accessToken) {
        throw new Error(
          "Login response did not contain an access token."
        );
      }

      const userData =
        data.user ||
        data.profile ||
        (data.id || data.email
          ? {
              id: data.id,
              email: data.email || normalizedEmail,
              role: data.role || selectedRole,
            }
          : {
              email: normalizedEmail,
              role: selectedRole,
            });

      const actualRole = normalizeRole(
        userData.role || data.role || selectedRole
      );

      const dashboardRoutes = {
        student: "/student/dashboard",
        mentor: "/mentor/dashboard",
        admin: "/admin/dashboard",
      };

      const destination = dashboardRoutes[actualRole];

      if (!destination) {
        throw new Error(
          "Unable to identify your account role. Please contact the administrator."
        );
      }

      // Save authentication tokens.
      localStorage.setItem(ACCESS_KEY, accessToken);

      if (refreshToken) {
        localStorage.setItem(REFRESH_KEY, refreshToken);
      } else {
        localStorage.removeItem(REFRESH_KEY);
      }

      localStorage.setItem(
        USER_KEY,
        JSON.stringify(userData)
      );

      // Save email only when Remember Email is enabled.
      if (rememberEmail) {
        const nextHistory = [
          normalizedEmail,
          ...emailHistory.filter(
            (item) => item.toLowerCase() !== normalizedEmail
          ),
        ].slice(0, 10);

        saveEmailHistory(nextHistory);
        localStorage.setItem(
          SAVED_EMAIL_KEY,
          normalizedEmail
        );
      }

      setPassword("");
      setShowPassword(false);

      // Success toast.
      showToast(
        "success",
        "Login successful! Welcome to SkillSphere.",
        TOAST_DURATION
      );

      // Redirect after toast.
      redirectTimer.current = window.setTimeout(() => {
        window.location.assign(destination);
      }, REDIRECT_DELAY);

    } catch (err) {
      console.error("[SkillSphere] Login error:", err);

      const message =
        err instanceof TypeError && /fetch/i.test(err.message)
          ? "Cannot connect to the backend. Make sure Django is running at http://127.0.0.1:8000."
          : err.message || "Something went wrong. Please try again.";

      setError(message);
      showToast("error", message, 3500);

    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="login-page">

      {/* Toast notification */}
      {toast && (
        <div
          key={toast.id}
          className={`login-toast login-toast-${toast.type}`}
          role={toast.type === "error" ? "alert" : "status"}
          aria-live="polite"
          style={{
            position: "fixed",
            top: "24px",
            right: "24px",
            left: "auto",
            zIndex: 10000,
          }}
        >
          <span className="login-toast-icon" aria-hidden="true">
            {toast.type === "success" ? "✓" : "!"}
          </span>

          <span className="login-toast-message">
            {toast.message}
          </span>

          <button
            type="button"
            className="login-toast-close"
            aria-label="Dismiss notification"
            onClick={() => {
              if (toastTimer.current) {
                window.clearTimeout(toastTimer.current);
                toastTimer.current = null;
              }

              setToast(null);
            }}
          >
            ×
          </button>

          <div
            className="login-toast-progress"
            style={{
              animationDuration: `${toast.duration}ms`,
            }}
          />
        </div>
      )}

      <div className="login-layout">

        {/* LEFT PROMOTIONAL PANEL */}
        <section className="login-promo">
          <div className="login-promo-content">

            <span className="login-promo-eyebrow">
              YOUR SKILLS. YOUR FUTURE.
            </span>

            <h1>
              Your next chapter
              <br />
              <span>starts here.</span>
            </h1>

            <p className="login-promo-description">
              Turn your potential into progress. Discover your
              strengths, develop valuable skills, and take
              confident steps toward your dream career.
            </p>

            <div className="login-benefits">

              <div className="login-benefit">
                <div className="login-benefit-icon">◎</div>
                <div>
                  <h3>Discover your strengths</h3>
                  <p>
                    Understand your skills and growth opportunities.
                  </p>
                </div>
              </div>

              <div className="login-benefit">
                <div className="login-benefit-icon">↗</div>
                <div>
                  <h3>Build your career roadmap</h3>
                  <p>
                    Turn your learning goals into meaningful progress.
                  </p>
                </div>
              </div>

              <div className="login-benefit">
                <div className="login-benefit-icon">✧</div>
                <div>
                  <h3>Grow with expert guidance</h3>
                  <p>
                    Learn, practice, and prepare for what comes next.
                  </p>
                </div>
              </div>

            </div>
          </div>

          <div className="login-promo-footer">
            KNOW YOUR SKILLS. SHAPE YOUR FUTURE.
          </div>

          <div className="login-decoration" aria-hidden="true" />
        </section>

        {/* RIGHT LOGIN PANEL */}
        <section className="login-form-panel">
          <div className="login-form-container">

            {/* BACK TO HOME */}
            <a className="login-back-home" href="/">
              <span aria-hidden="true">←</span>
              <span>Back to Home</span>
            </a>

            <div className="login-mobile-brand">
              SkillSphere
            </div>

            <span className="login-form-eyebrow">
              WELCOME BACK
            </span>

            <h2>Login to your account</h2>

            <p className="login-form-description">
              Continue your journey toward your future.
            </p>

            <form onSubmit={handleLogin} noValidate autoComplete="on">

              {/* EMAIL */}
              <div className="login-form-group">
                <label htmlFor="login-email">
                  Email Address
                </label>

                <div className="login-email-autocomplete">
                  <input
                    id="login-email"
                    type="email"
                    name="email"
                    placeholder="you@example.com"
                    autoComplete="email"
                    value={email}
                    onChange={handleEmailChange}
                    onFocus={() => {
                      setShowEmailSuggestions(emailHistory.length > 0);
                    }}
                    onBlur={() => {
                      window.setTimeout(() => {
                        setShowEmailSuggestions(false);
                      }, 150);
                    }}
                    required
                  />

                  {showEmailSuggestions &&
                    filteredEmailSuggestions.length > 0 && (
                      <div className="login-email-suggestions">
                        {filteredEmailSuggestions.map((suggestion) => (
                          <button
                            type="button"
                            key={suggestion}
                            className="login-email-suggestion"
                            onMouseDown={(event) =>
                              event.preventDefault()
                            }
                            onClick={() =>
                              handleEmailSuggestionSelect(suggestion)
                            }
                          >
                            <span aria-hidden="true">✉</span>
                            <span>{suggestion}</span>
                          </button>
                        ))}
                      </div>
                    )}
                </div>
              </div>

              {/* PASSWORD */}
              <div className="login-form-group">
                <label htmlFor="login-password">
                  Password
                </label>

                <div className="login-password-wrapper">
                  <input
                    id="login-password"
                    type={showPassword ? "text" : "password"}
                    name="password"
                    placeholder="Enter your password"
                    autoComplete="current-password"
                    value={password}
                    onChange={(event) =>
                      setPassword(event.target.value)
                    }
                    required
                  />

                  <button
                    type="button"
                    className="login-password-toggle"
                    onClick={() =>
                      setShowPassword((previous) => !previous)
                    }
                    aria-label={
                      showPassword ? "Hide password" : "Show password"
                    }
                  >
                    {showPassword ? "🙈" : "👁"}
                  </button>
                </div>
              </div>

              {/* ROLE SELECTION */}
              <div className="login-role-section">
                <div className="login-role-heading">
                  <label>Choose your account type</label>
                  <p>
                    Select the role that best describes you.
                  </p>
                </div>

                <div className="login-role-grid">
                  {roles.map((item) => (
                    <button
                      type="button"
                      key={item.value}
                      className={`login-role-card ${
                        role === item.value
                          ? "login-role-card-selected"
                          : ""
                      }`}
                      onClick={() => setRole(item.value)}
                      aria-pressed={role === item.value}
                    >
                      <span className="login-role-icon">
                        {item.icon}
                      </span>

                      <span className="login-role-title">
                        {item.title}
                      </span>

                      <span className="login-role-description">
                        {item.description}
                      </span>

                      {role === item.value && (
                        <span className="login-role-check">
                          ✓
                        </span>
                      )}
                    </button>
                  ))}
                </div>
              </div>

              {/* REMEMBER EMAIL */}
              <label className="login-remember-email">
                <input
                  type="checkbox"
                  checked={rememberEmail}
                  onChange={handleRememberEmailChange}
                />
                <span>Remember email</span>
              </label>

              {/* ERROR MESSAGE */}
              {error && (
                <div className="login-error" role="alert">
                  {error}
                </div>
              )}

              {/* LOGIN BUTTON */}
              <button
                type="submit"
                className="login-submit-button"
                disabled={loading}
              >
                <span>
                  {loading ? "Logging in..." : "Login"}
                </span>

                {!loading && (
                  <span aria-hidden="true">→</span>
                )}
              </button>

            </form>

            <div className="login-bottom-note">
              Your future starts with one step.
              <span> Keep moving forward.</span>
            </div>

          </div>
        </section>
      </div>
    </div>
  );
}
