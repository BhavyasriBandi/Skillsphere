
import React, { useCallback, useState } from "react";

import { API_BASE_URL, useAuth } from "../auth/AuthContext";
import { showToast } from "../components/ToastProvider";
import "./AdminEmailManagement.css";

const ACCESS_KEY = "skillsphere_access";

function getToken(contextToken) {
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

export default function AdminEmailManagement() {
  const { accessToken: contextToken } = useAuth();

  const [recipient, setRecipient] = useState("");
  const [subject, setSubject] = useState("");
  const [message, setMessage] = useState("");
  const [sending, setSending] = useState(false);
  const [result, setResult] = useState("");

  const sendEmail = useCallback(async (event) => {
    event.preventDefault();

    if (sending) return;

    const email = recipient.trim();
    const emailSubject = subject.trim();
    const emailMessage = message.trim();

    if (!email || !emailSubject || !emailMessage) {
      showToast("Please complete all email fields.", "error");
      return;
    }

    const token = getToken(contextToken);

    if (!token) {
      showToast("Please log in again.", "error");
      return;
    }

    setSending(true);
    setResult("");

    try {
      const response = await fetch(
        `${API_BASE_URL}/api/auth/admin/email/`,
        {
          method: "POST",
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
            Accept: "application/json",
          },
          body: JSON.stringify({
            recipient_email: email,
            subject: emailSubject,
            message: emailMessage,
          }),
        }
      );

      const data = await response.json().catch(() => ({}));

      if (!response.ok) {
        throw new Error(
          data.detail ||
          data.message ||
          `Unable to send email (${response.status}).`
        );
      }

      const successMessage =
        data.message || "Email sent successfully.";

      setResult(successMessage);
      showToast(successMessage, "success");

      setRecipient("");
      setSubject("");
      setMessage("");
    } catch (error) {
      const errorMessage =
        error.message || "Unable to send the email.";

      setResult(errorMessage);
      showToast(errorMessage, "error");
    } finally {
      setSending(false);
    }
  }, [contextToken, recipient, subject, message, sending]);

  return (
    <div className="admin-email-management">
      <div className="aem-heading">
        <div>
          <span className="aem-eyebrow">SYSTEM MANAGEMENT</span>
          <h2>Email Management</h2>
          <p>Send email communications from SkillSphere.</p>
        </div>

        <span className="aem-heading-icon" aria-hidden="true">
          ✉
        </span>
      </div>

      <section className="aem-panel">
        <div className="aem-panel-heading">
          <div>
            <h3>Compose Email</h3>
            <p>Enter the recipient and write your message below.</p>
          </div>
        </div>

        <form className="aem-form" onSubmit={sendEmail}>
          <div className="aem-field">
            <label htmlFor="aem-recipient">
              Recipient Email
            </label>
            <input
              id="aem-recipient"
              type="email"
              value={recipient}
              onChange={(event) => setRecipient(event.target.value)}
              placeholder="recipient@example.com"
              autoComplete="email"
              required
              disabled={sending}
            />
          </div>

          <div className="aem-field">
            <label htmlFor="aem-subject">Subject</label>
            <input
              id="aem-subject"
              type="text"
              value={subject}
              onChange={(event) => setSubject(event.target.value)}
              placeholder="Enter email subject"
              maxLength={200}
              required
              disabled={sending}
            />
          </div>

          <div className="aem-field">
            <label htmlFor="aem-message">Message</label>
            <textarea
              id="aem-message"
              value={message}
              onChange={(event) => setMessage(event.target.value)}
              placeholder="Write your email message..."
              rows={8}
              maxLength={10000}
              required
              disabled={sending}
            />
            <span className="aem-character-count">
              {message.length}/10000 characters
            </span>
          </div>

          {result && (
            <div className="aem-result" role="status">
              {result}
            </div>
          )}

          <div className="aem-actions">
            <button
              type="button"
              className="aem-secondary-button"
              onClick={() => {
                setRecipient("");
                setSubject("");
                setMessage("");
                setResult("");
              }}
              disabled={sending}
            >
              Clear
            </button>

            <button
              type="submit"
              className="aem-primary-button"
              disabled={sending}
            >
              {sending ? "Sending..." : "✉ Send Email"}
            </button>
          </div>
        </form>
      </section>

      <div className="aem-info">
        <span aria-hidden="true">ⓘ</span>
        <p>
          Emails can only be sent after the admin-only Django
          endpoint is implemented and tested.
        </p>
      </div>
    </div>
  );
}
