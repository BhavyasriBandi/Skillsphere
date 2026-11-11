
import React, { useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";

const API_BASE_URL = "https://skillsphere-u93o.onrender.com";

export default function SetPassword() {
  const { uid, token } = useParams();
  const navigate = useNavigate();

  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError("");
    setSuccess("");

    if (password !== confirmPassword) {
      setError("Passwords do not match.");
      return;
    }

    setLoading(true);

    try {
      const response = await fetch(`${API_BASE_URL}/api/auth/set-password/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          uid,
          token,
          password,
          confirm_password: confirmPassword,
        }),
      });

      const data = await response.json().catch(() => ({}));

      if (!response.ok) {
        throw new Error(
          data.detail || data.message || "Password setup failed. Check your email link."
        );
      }

      setSuccess(data.message || "Password set successfully! Redirecting to login...");
      setPassword("");
      setConfirmPassword("");

      setTimeout(() => navigate("/login", { replace: true }), 2500);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main style={styles.page}>
      <section style={styles.card}>
        <h1 style={styles.logo}>SkillSphere</h1>
        <div style={styles.icon}>🔐</div>
        <h2 style={styles.heading}>Set Your Password</h2>
        <p style={styles.description}>
          Create a secure password to activate your SkillSphere account.
        </p>

        <form onSubmit={handleSubmit}>
          <label style={styles.label}>New Password</label>
          <input
            style={styles.input}
            type={showPassword ? "text" : "password"}
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Enter new password"
            autoComplete="new-password"
            required
          />

          <label style={styles.label}>Confirm Password</label>
          <input
            style={styles.input}
            type={showPassword ? "text" : "password"}
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            placeholder="Confirm new password"
            autoComplete="new-password"
            required
          />

          <label style={styles.showPassword}>
            <input
              type="checkbox"
              checked={showPassword}
              onChange={(e) => setShowPassword(e.target.checked)}
            />
            Show password
          </label>

          {error && <p style={styles.error}>{error}</p>}
          {success && <p style={styles.success}>{success}</p>}

          <button type="submit" disabled={loading} style={styles.button}>
            {loading ? "Setting Password..." : "Set Password"}
          </button>
        </form>

        <p style={styles.footer}>
          Already have an account? <Link to="/login">Login</Link>
        </p>
      </section>
    </main>
  );
}

const styles = {
  page: {
    minHeight: "100vh",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    padding: 24,
    background: "linear-gradient(135deg, #edf3ff, #f7f8fc)",
    fontFamily: "Arial, sans-serif",
  },
  card: {
    width: "100%",
    maxWidth: 440,
    padding: 38,
    background: "#fff",
    borderRadius: 18,
    boxShadow: "0 15px 45px rgba(36,59,100,0.12)",
  },
  logo: { textAlign: "center", color: "#243b64" },
  icon: { textAlign: "center", fontSize: 38, marginTop: 20 },
  heading: { textAlign: "center", color: "#243b64" },
  description: {
    textAlign: "center",
    color: "#68758a",
    fontSize: 14,
    lineHeight: 1.6,
    marginBottom: 25,
  },
  label: {
    display: "block",
    margin: "17px 0 8px",
    color: "#263750",
    fontWeight: 600,
    fontSize: 14,
  },
  input: {
    boxSizing: "border-box",
    width: "100%",
    padding: 13,
    border: "1px solid #d7deea",
    borderRadius: 9,
    fontSize: 14,
  },
  showPassword: {
    display: "flex",
    gap: 8,
    alignItems: "center",
    marginTop: 13,
    fontSize: 13,
    color: "#52627a",
  },
  error: {
    padding: 11,
    background: "#fff0f0",
    color: "#bd3030",
    borderRadius: 8,
    fontSize: 13,
  },
  success: {
    padding: 11,
    background: "#eaf8ef",
    color: "#18743b",
    borderRadius: 8,
    fontSize: 13,
  },
  button: {
    width: "100%",
    marginTop: 22,
    padding: 14,
    border: 0,
    borderRadius: 9,
    background: "#243b64",
    color: "#fff",
    fontSize: 15,
    fontWeight: 700,
    cursor: "pointer",
  },
  footer: { textAlign: "center", marginTop: 24, fontSize: 13 },
};
