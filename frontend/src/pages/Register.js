
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

import RegisterNavigation from "../components/RegisterNavigation";
import Toast, { showToast } from "../components/Toast";

import "./Register.css";

const API_BASE_URL = "https://skillsphere-u93o.onrender.com/api/auth";

const initialFormData = {
  first_name: "",
  last_name: "",
  email: "",
  password: "",
  confirm_password: "",
  role: "",
};

const roles = [
  {
    value: "Student",
    title: "Student",
    description: "Build skills and explore career opportunities.",
    icon: "🎓",
    available: true,
  },
  {
    value: "Mentor",
    title: "Mentor",
    description: "Guide learners and share your expertise.",
    icon: "🧭",
    available: true,
  },
  {
    value: "Admin",
    title: "Admin",
    description: "Manage users and platform operations.",
    icon: "🛡️",
    available: false,
  },
];

function EyeIcon({ visible }) {
  return visible ? (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="20"
      height="20"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="1.8"
      strokeLinecap="round"
      strokeLinejoin="round"
      aria-hidden="true"
    >
      <path d="M3 3l18 18" />
      <path d="M10.6 10.6a2 2 0 002.8 2.8" />
      <path d="M9.9 5.2A11 11 0 0112 5c5 0 9 4 10 7a11 11 0 01-3 4.2" />
      <path d="M6.2 6.2C4.1 7.4 2.6 9.2 2 12c1 3 5 7 10 7a10 10 0 003-.5" />
    </svg>
  ) : (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="20"
      height="20"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="1.8"
      strokeLinecap="round"
      strokeLinejoin="round"
      aria-hidden="true"
    >
      <path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z" />
      <circle cx="12" cy="12" r="3" />
    </svg>
  );
}

function Register() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState(initialFormData);
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);
  const [loading, setLoading] = useState(false);

  function handleChange(event) {
    const { name, value } = event.target;

    setFormData((previous) => ({
      ...previous,
      [name]: value,
    }));
  }

  function handleRoleChange(role) {
    if (!["Student", "Mentor"].includes(role)) {
      showToast(
        "Admin accounts are restricted. Please contact the platform administrator.",
        "warning"
      );
      return;
    }

    setFormData((previous) => ({
      ...previous,
      role,
    }));
  }

  function validateForm() {
    const firstName = formData.first_name.trim();
    const lastName = formData.last_name.trim();
    const email = formData.email.trim().toLowerCase();
    const password = formData.password;
    const confirmPassword = formData.confirm_password;

    // Role validation
    if (!["Student", "Mentor"].includes(formData.role)) {
      showToast("Please select Student or Mentor.", "warning");
      return false;
    }

    // Required fields validation
    if (
      !firstName ||
      !lastName ||
      !email ||
      !password ||
      !confirmPassword
    ) {
      showToast("Please fill in all required fields.", "warning");
      return false;
    }

    // Name validation
    const namePattern = /^\p{L}+(?:[ '-]\p{L}+)*$/u;

    if (!namePattern.test(firstName)) {
      showToast("Please enter a valid first name.", "warning");
      return false;
    }

    if (!namePattern.test(lastName)) {
      showToast("Please enter a valid last name.", "warning");
      return false;
    }

    // Email validation
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!emailPattern.test(email)) {
      showToast("Please enter a valid email address.", "warning");
      return false;
    }

    // Password validation
    if (password.length < 8) {
      showToast(
        "Your password must contain at least 8 characters.",
        "warning"
      );
      return false;
    }

    if (/^\d+$/.test(password)) {
      showToast(
        "Your password cannot contain only numbers.",
        "warning"
      );
      return false;
    }

    // Confirm password validation
    if (password !== confirmPassword) {
      showToast("Passwords do not match.", "warning");
      return false;
    }

    return true;
  }

  async function handleSubmit(event) {
    event.preventDefault();

    if (loading) return;

    if (!validateForm()) {
      return;
    }

    const firstName = formData.first_name.trim();
    const lastName = formData.last_name.trim();
    const email = formData.email.trim().toLowerCase();

    setLoading(true);

    try {
      const response = await fetch(`${API_BASE_URL}/register/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          first_name: firstName,
          last_name: lastName,
          email,
          password: formData.password,
          confirm_password: formData.confirm_password,
          role: formData.role,
        }),
      });

      const data = await response.json().catch(() => ({}));

      if (!response.ok) {
        let message = data.detail || data.message || "";

        if (!message && Object.keys(data).length > 0) {
          message = Object.entries(data)
            .map(([field, messages]) => {
              const description = Array.isArray(messages)
                ? messages.join(" ")
                : typeof messages === "string"
                  ? messages
                  : JSON.stringify(messages);

              return `${field.replaceAll("_", " ")}: ${description}`;
            })
            .join(" ");
        }

        throw new Error(
          message || "Registration failed. Please check your details."
        );
      }

      sessionStorage.setItem("skillsphere_email", email);

      showToast(
        data.message ||
          "Registration successful! Proceeding to email verification.",
        "success"
      );

      window.setTimeout(() => {
        navigate("/verify-email");
      }, 1400);
    } catch (error) {
      showToast(
        error.message ||
          "Unable to connect to the server. Please try again.",
        "error"
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="register-page">
      <Toast />

      <aside className="register-intro">
        <a href="/" className="intro-brand">
          <span className="intro-brand-icon">✦</span>
          SkillSphere
        </a>

        <div className="intro-content">
          <span className="intro-eyebrow">
            YOUR SKILLS. YOUR FUTURE.
          </span>

          <h1>
            Your next chapter <span>starts here.</span>
          </h1>

          <p className="intro-description">
            Turn your potential into progress. Discover your strengths,
            develop valuable skills, and take confident steps toward
            your dream career.
          </p>

          <div className="intro-features">
            <div className="intro-feature">
              <span className="intro-feature-icon">◎</span>
              <div>
                <h3>Discover your strengths</h3>
                <p>
                  Understand your skills and growth opportunities.
                </p>
              </div>
            </div>

            <div className="intro-feature">
              <span className="intro-feature-icon">↗</span>
              <div>
                <h3>Build your career roadmap</h3>
                <p>
                  Turn your learning goals into meaningful progress.
                </p>
              </div>
            </div>

            <div className="intro-feature">
              <span className="intro-feature-icon">✧</span>
              <div>
                <h3>Grow with expert guidance</h3>
                <p>
                  Learn, practice, and prepare for what comes next.
                </p>
              </div>
            </div>
          </div>
        </div>

        <div className="intro-footer">
          <span>LEARN WITH PURPOSE.</span>
          <span>GROW WITH CONFIDENCE.</span>
        </div>
      </aside>

      <section className="register-card">
        <RegisterNavigation />

        <div className="register-heading">
          <span className="register-eyebrow">START YOUR JOURNEY</span>
          <h2>Create your account</h2>
          <p>
            Join SkillSphere and take the next step toward your future.
          </p>
        </div>

        <form
          className="register-form"
          onSubmit={handleSubmit}
          autoComplete="off"
          noValidate
        >
          <div className="register-name-grid">
            <div className="register-field">
              <label htmlFor="first_name">First Name</label>
              <input
                id="first_name"
                name="first_name"
                type="text"
                placeholder="Enter first name"
                value={formData.first_name}
                onChange={handleChange}
                autoComplete="off"
                required
              />
            </div>

            <div className="register-field">
              <label htmlFor="last_name">Last Name</label>
              <input
                id="last_name"
                name="last_name"
                type="text"
                placeholder="Enter last name"
                value={formData.last_name}
                onChange={handleChange}
                autoComplete="off"
                required
              />
            </div>
          </div>

          <div className="register-field">
            <label htmlFor="email">Email Address</label>
            <input
              id="email"
              name="email"
              type="email"
              placeholder="you@example.com"
              value={formData.email}
              onChange={handleChange}
              autoComplete="off"
              required
            />
          </div>

          <div className="register-field">
            <label htmlFor="password">Password</label>

            <div className="register-password-wrap">
              <input
                id="password"
                name="password"
                type={showPassword ? "text" : "password"}
                placeholder="At least 8 characters"
                value={formData.password}
                onChange={handleChange}
                autoComplete="new-password"
                required
              />

              <button
                className="register-password-toggle"
                type="button"
                onClick={() =>
                  setShowPassword((previous) => !previous)
                }
                aria-label={
                  showPassword ? "Hide password" : "Show password"
                }
                title={showPassword ? "Hide password" : "Show password"}
              >
                <EyeIcon visible={showPassword} />
              </button>
            </div>
          </div>

          <div className="register-field">
            <label htmlFor="confirm_password">Confirm Password</label>

            <div className="register-password-wrap">
              <input
                id="confirm_password"
                name="confirm_password"
                type={showConfirmPassword ? "text" : "password"}
                placeholder="Enter password again"
                value={formData.confirm_password}
                onChange={handleChange}
                autoComplete="new-password"
                required
              />

              <button
                className="register-password-toggle"
                type="button"
                onClick={() =>
                  setShowConfirmPassword((previous) => !previous)
                }
                aria-label={
                  showConfirmPassword
                    ? "Hide confirm password"
                    : "Show confirm password"
                }
                title={
                  showConfirmPassword
                    ? "Hide confirm password"
                    : "Show confirm password"
                }
              >
                <EyeIcon visible={showConfirmPassword} />
              </button>
            </div>
          </div>

          <section
            className="register-role-section"
            aria-labelledby="register-role-title"
          >
            <div className="register-role-heading">
              <h3 id="register-role-title">
                Choose your account type
              </h3>
              <p>Select the role that best describes you.</p>
            </div>

            <div className="register-role-options">
              {roles.map((role) => (
                <button
                  key={role.value}
                  type="button"
                  className={`register-role-card ${
                    formData.role === role.value ? "selected" : ""
                  } ${!role.available ? "role-restricted" : ""}`}
                  onClick={() => handleRoleChange(role.value)}
                  aria-pressed={
                    role.available && formData.role === role.value
                  }
                  aria-disabled={!role.available}
                >
                  <span
                    className="register-role-icon"
                    aria-hidden="true"
                  >
                    {role.icon}
                  </span>

                  <span className="register-role-copy">
                    <strong>{role.title}</strong>
                    <small>{role.description}</small>

                    {!role.available && (
                      <small className="role-restricted-label">
                        Restricted account
                      </small>
                    )}
                  </span>

                  <span
                    className="register-role-check"
                    aria-hidden="true"
                  >
                    {formData.role === role.value ? "✓" : ""}
                  </span>
                </button>
              ))}
            </div>
          </section>

          <button
            className="register-submit"
            type="submit"
            disabled={loading}
          >
            {loading ? "Creating your account..." : "Create Account"}
            {!loading && <span aria-hidden="true"> →</span>}
          </button>

          <p className="register-login-text">
            Already have an account? <a href="/login">Sign in</a>
          </p>
        </form>
      </section>
    </main>
  );
}

export default Register;
