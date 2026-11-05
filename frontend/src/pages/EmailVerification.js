
import React, { useEffect, useRef, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { showToast } from "../components/ToastProvider";
import "./EmailVerification.css";

const API_URL = "http://127.0.0.1:8000/api/auth";

function EmailVerification() {
  const navigate = useNavigate();
  const location = useLocation();
  const inputRefs = useRef([]);

  const [email, setEmail] = useState(
    location.state?.email ||
      sessionStorage.getItem("skillsphere_email") ||
      ""
  );
  const [code, setCode] = useState(["", "", "", "", "", ""]);
  const [loading, setLoading] = useState(false);
  const [resending, setResending] = useState(false);

  useEffect(() => {
    if (location.state?.email) {
      const registeredEmail = location.state.email.trim();

      sessionStorage.setItem("skillsphere_email", registeredEmail);
      setEmail(registeredEmail);
    }
  }, [location.state]);

  const getErrorMessage = (data, fallback) => {
    if (typeof data?.detail === "string") {
      return data.detail;
    }

    if (typeof data?.message === "string") {
      return data.message;
    }

    if (data && typeof data === "object") {
      const messages = Object.values(data)
        .flat()
        .filter((value) => typeof value === "string");

      if (messages.length) {
        return messages.join(" ");
      }
    }

    return fallback;
  };

  const handleCodeChange = (index, value) => {
    const digits = value.replace(/\D/g, "");

    if (digits.length > 1) {
      const pastedDigits = digits.slice(0, 6).split("");
      const updated = [...code];

      pastedDigits.forEach((digit, offset) => {
        if (index + offset < 6) {
          updated[index + offset] = digit;
        }
      });

      setCode(updated);

      const nextIndex = Math.min(index + pastedDigits.length, 5);
      inputRefs.current[nextIndex]?.focus();
      return;
    }

    const digit = digits.slice(-1);

    setCode((previous) => {
      const updated = [...previous];
      updated[index] = digit;
      return updated;
    });

    if (digit && index < 5) {
      inputRefs.current[index + 1]?.focus();
    }
  };

  const handleKeyDown = (index, event) => {
    if (
      event.key === "Backspace" &&
      !code[index] &&
      index > 0
    ) {
      inputRefs.current[index - 1]?.focus();
    }

    if (event.key === "ArrowLeft" && index > 0) {
      inputRefs.current[index - 1]?.focus();
    }

    if (event.key === "ArrowRight" && index < 5) {
      inputRefs.current[index + 1]?.focus();
    }
  };

  const handlePaste = (event) => {
    event.preventDefault();

    const pastedCode = event.clipboardData
      .getData("text")
      .replace(/\D/g, "")
      .slice(0, 6);

    if (!pastedCode) return;

    setCode(
      Array.from(
        { length: 6 },
        (_, index) => pastedCode[index] || ""
      )
    );

    inputRefs.current[Math.min(pastedCode.length, 5)]?.focus();
  };

  const handleVerify = async (event) => {
    event.preventDefault();

    const cleanEmail = email.trim().toLowerCase();
    const verificationCode = code.join("");

    if (!cleanEmail) {
      showToast(
        "Please return to registration and enter your email address.",
        "error"
      );
      return;
    }

    if (!/^\d{6}$/.test(verificationCode)) {
      showToast(
        "Please enter all six digits of the verification code.",
        "warning"
      );
      return;
    }

    setLoading(true);

    try {
      const response = await fetch(`${API_URL}/verify-email/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email: cleanEmail,
          code: verificationCode,
        }),
      });

      const data = await response.json().catch(() => ({}));

      if (!response.ok) {
        showToast(
          getErrorMessage(
            data,
            "Verification failed. Please check your code and try again."
          ),
          "error"
        );
        return;
      }

      sessionStorage.removeItem("skillsphere_email");
      setCode(["", "", "", "", "", ""]);

      showToast(
        data.message || "Email verified successfully!",
        "success"
      );

      navigate("/login", { replace: true });
    } catch (error) {
      showToast(
        "Unable to connect to the server. Please check that Django is running.",
        "error"
      );
    } finally {
      setLoading(false);
    }
  };

  const handleResendCode = async () => {
    const cleanEmail = email.trim().toLowerCase();

    if (!cleanEmail) {
      showToast(
        "Please return to registration and enter your email address.",
        "error"
      );
      return;
    }

    setResending(true);

    try {
      const response = await fetch(
        `${API_URL}/resend-verification/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ email: cleanEmail }),
        }
      );

      const data = await response.json().catch(() => ({}));

      if (!response.ok) {
        showToast(
          getErrorMessage(
            data,
            "Unable to resend the verification code."
          ),
          "error"
        );
        return;
      }

      setCode(["", "", "", "", "", ""]);

      showToast(
        data.message ||
          "Please check your Gmail inbox for the verification code.",
        "success"
      );

      inputRefs.current[0]?.focus();
    } catch (error) {
      showToast(
        "Unable to connect to the server. Please check that Django is running.",
        "error"
      );
    } finally {
      setResending(false);
    }
  };

  return (
    <main className="verification-page">
      <section className="verification-card">
        <button
          type="button"
          className="verification-back"
          onClick={() => navigate("/register")}
        >
          <span aria-hidden="true">←</span>
          Back to registration
        </button>

        <div className="verification-brand">
          <div className="verification-brand-mark">S</div>
          <span>SkillSphere</span>
        </div>

        <div className="verification-icon">
          <svg
            viewBox="0 0 64 64"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
            aria-hidden="true"
          >
            <rect
              x="8"
              y="15"
              width="48"
              height="34"
              rx="8"
              stroke="currentColor"
              strokeWidth="3"
            />
            <path
              d="M11 20L32 36L53 20"
              stroke="currentColor"
              strokeWidth="3"
              strokeLinecap="round"
              strokeLinejoin="round"
            />
            <circle
              cx="48"
              cy="47"
              r="11"
              fill="#EAF2FF"
              stroke="currentColor"
              strokeWidth="2.5"
            />
            <path
              d="M43.5 47L47 50.5L53 43.5"
              stroke="currentColor"
              strokeWidth="2.5"
              strokeLinecap="round"
              strokeLinejoin="round"
            />
          </svg>
        </div>

        <p className="verification-eyebrow">ONE LAST STEP</p>

        <h1>Verify your email</h1>

        <p className="verification-description">
          Your future starts here. Enter the six-digit verification
          code associated with your email address to continue.
        </p>

        <div className="verification-email-box">
          <span className="verification-email-icon">✉</span>

          <div className="verification-email-details">
            <span className="verification-email-label">
              Email address
            </span>

            <strong>
              {email || "No email address provided"}
            </strong>
          </div>

          <button
            type="button"
            className="verification-edit-email"
            onClick={() => navigate("/register")}
            aria-label="Edit email address"
          >
            Edit
          </button>
        </div>

        <form
          className="verification-form"
          onSubmit={handleVerify}
        >
          <label className="verification-code-label">
            Enter verification code
          </label>

          <div
            className="verification-code-inputs"
            onPaste={handlePaste}
          >
            {code.map((digit, index) => (
              <input
                key={index}
                ref={(element) => {
                  inputRefs.current[index] = element;
                }}
                type="text"
                inputMode="numeric"
                autoComplete={
                  index === 0 ? "one-time-code" : "off"
                }
                aria-label={`Verification digit ${index + 1}`}
                maxLength={1}
                value={digit}
                onChange={(event) =>
                  handleCodeChange(index, event.target.value)
                }
                onKeyDown={(event) =>
                  handleKeyDown(index, event)
                }
                className="verification-code-input"
                disabled={loading}
                required
              />
            ))}
          </div>

          <button
            type="submit"
            className="verification-submit"
            disabled={loading || resending}
          >
            {loading ? "Verifying..." : "Verify email"}
            {!loading && <span aria-hidden="true">→</span>}
          </button>
        </form>

        <div className="verification-resend">
          <span>Didn't receive a code?</span>

          <button
            type="button"
            onClick={handleResendCode}
            disabled={resending || loading}
          >
            {resending ? "Sending..." : "Resend code"}
          </button>
        </div>

        <div className="verification-security-note">
          <span aria-hidden="true">🔒</span>
          <span>
            Your information is protected. Never share your
            verification code with anyone.
          </span>
        </div>

        <footer className="verification-footer">
          <span>SkillSphere</span>
          <span>Know Your Skills. Shape Your Future.</span>
        </footer>
      </section>
    </main>
  );
}

export default EmailVerification;
