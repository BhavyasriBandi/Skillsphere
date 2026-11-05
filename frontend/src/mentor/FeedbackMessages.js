import React, { useCallback, useEffect, useState } from "react";
import "./FeedbackMessages.css";

const API_BASE_URL = "http://127.0.0.1:8000";

function FeedbackMessages({ students = [] }) {
  const [activeTab, setActiveTab] = useState("messages");
  const [selectedStudent, setSelectedStudent] = useState("");

  const [messages, setMessages] = useState([]);
  const [feedbacks, setFeedbacks] = useState([]);

  const [messageText, setMessageText] = useState("");
  const [subject, setSubject] = useState("");
  const [feedbackText, setFeedbackText] = useState("");

  const [loading, setLoading] = useState(false);
  const [sending, setSending] = useState(false);
  const [toast, setToast] = useState(null);
  const [unreadCount, setUnreadCount] = useState(0);

  const getToken = () =>
    localStorage.getItem("skillsphere_access");

  const getStudentId = (student) =>
    student?.id || student?.student_id || student?.student;

  const selectedStudentData = students.find(
    (student) =>
      String(getStudentId(student)) === String(selectedStudent)
  );

  // Automatically hide toast after 3.5 seconds.
  useEffect(() => {
    if (!toast) return undefined;

    const timer = window.setTimeout(() => {
      setToast(null);
    }, 3500);

    return () => window.clearTimeout(timer);
  }, [toast]);

  // Toast notification function.
  const showToast = (type, message) => {
    setToast({
      id: Date.now(),
      type,
      message,
    });
  };

  // API REQUEST
  const apiRequest = async (endpoint, options = {}) => {
    const token = getToken();

    if (!token) {
      throw new Error(
        "Access token not found. Please login again."
      );
    }

    const response = await fetch(
      `${API_BASE_URL}${endpoint}`,
      {
        ...options,
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
          ...options.headers,
        },
      }
    );

    const data = await response.json().catch(() => ({}));

    if (!response.ok) {
      const errorMessage =
        typeof data === "object"
          ? Object.entries(data)
              .map(([field, messages]) => {
                const details = Array.isArray(messages)
                  ? messages.join(", ")
                  : String(messages);

                return `${field}: ${details}`;
              })
              .join(" | ")
          : "Unable to complete your request.";

      throw new Error(
        data.detail ||
        data.message ||
        errorMessage ||
        "Unable to complete your request."
      );
    }

    return data;
  };

  // FETCH FEEDBACK
  const fetchFeedback = useCallback(async () => {
    try {
      const data = await apiRequest(
        "/api/mentors/student-feedback/"
      );

      setFeedbacks(
        data.feedbacks || data.feedback || []
      );
    } catch (err) {
      showToast("error", err.message);
    }
  }, []);

  // FETCH MESSAGES
  const fetchMessages = useCallback(async () => {
    if (!selectedStudent) {
      setMessages([]);
      return;
    }

    try {
      setLoading(true);

      const data = await apiRequest(
        `/api/mentors/messages/?student_id=${selectedStudent}`
      );

      setMessages(data.messages || []);
      setUnreadCount(data.unread_count || 0);

    } catch (err) {
      showToast("error", err.message);

    } finally {
      setLoading(false);
    }
  }, [selectedStudent]);

  useEffect(() => {
    fetchFeedback();
  }, [fetchFeedback]);

  useEffect(() => {
    fetchMessages();
  }, [fetchMessages]);

  // SEND MESSAGE
  const handleSendMessage = async (event) => {
    event.preventDefault();

    if (!selectedStudent || !messageText.trim()) {
      showToast(
        "error",
        "Select a student and enter a message."
      );
      return;
    }

    try {
      setSending(true);
      setToast(null);

      await apiRequest(
        "/api/mentors/messages/",
        {
          method: "POST",
          body: JSON.stringify({
            student_id: Number(selectedStudent),
            message: messageText.trim(),
          }),
        }
      );

      setMessageText("");

      showToast(
        "success",
        "Message sent successfully."
      );

      await fetchMessages();

    } catch (err) {
      showToast("error", err.message);

    } finally {
      setSending(false);
    }
  };

  // SUBMIT FEEDBACK
  const handleSubmitFeedback = async (event) => {
    event.preventDefault();

    if (
      !selectedStudent ||
      !subject.trim() ||
      !feedbackText.trim()
    ) {
      showToast(
        "error",
        "Please complete all feedback fields."
      );
      return;
    }

    try {
      setSending(true);
      setToast(null);

      await apiRequest(
        "/api/mentors/student-feedback/",
        {
          method: "POST",
          body: JSON.stringify({
            student: Number(selectedStudent),
            subject: subject.trim(),
            feedback: feedbackText.trim(),
          }),
        }
      );

      setSubject("");
      setFeedbackText("");

      showToast(
        "success",
        "Feedback submitted successfully."
      );

      await fetchFeedback();

    } catch (err) {
      showToast("error", err.message);

    } finally {
      setSending(false);
    }
  };

  // MARK MESSAGE AS READ
  const handleMarkRead = async (messageId) => {
    try {
      await apiRequest(
        `/api/mentors/messages/${messageId}/read/`,
        {
          method: "PATCH",
        }
      );

      showToast(
        "success",
        "Message marked as read."
      );

      await fetchMessages();

    } catch (err) {
      showToast("error", err.message);
    }
  };

  // FORMAT DATE
  const formatDate = (date) => {
    if (!date) return "";

    return new Date(date).toLocaleString();
  };

  return (
    <section className="fm-container">

      {/* HEADING */}
      <div className="fm-heading">
        <div>
          <h2>Feedback & Messages</h2>

          <p>
            Communicate with your students and guide their progress.
          </p>
        </div>

        <div className="fm-unread">
          <span>Unread Messages</span>
          <strong>{unreadCount}</strong>
        </div>
      </div>

      {/* TABS */}
      <div className="fm-tabs">

        <button
          type="button"
          className={
            activeTab === "messages" ? "active" : ""
          }
          onClick={() => {
            setActiveTab("messages");
            setToast(null);
          }}
        >
          Messages
        </button>

        <button
          type="button"
          className={
            activeTab === "feedback" ? "active" : ""
          }
          onClick={() => {
            setActiveTab("feedback");
            setToast(null);
          }}
        >
          Feedback
        </button>

      </div>

      {/* FLOATING TOAST */}
      {toast && (
        <div
          key={toast.id}
          className={`fm-toast fm-toast-${toast.type}`}
          role={
            toast.type === "error"
              ? "alert"
              : "status"
          }
          aria-live="polite"
        >

          <span
            className="fm-toast-icon"
            aria-hidden="true"
          >
            {toast.type === "success" ? "✓" : "!"}
          </span>

          <span className="fm-toast-message">
            {toast.message}
          </span>

          <button
            type="button"
            className="fm-toast-close"
            aria-label="Close notification"
            onClick={() => setToast(null)}
          >
            ×
          </button>

        </div>
      )}

      {/* STUDENT SELECTOR */}
      <div className="fm-student-selector">

        <label htmlFor="fm-student">
          Select Student
        </label>

        <select
          id="fm-student"
          value={selectedStudent}
          onChange={(event) => {
            setSelectedStudent(event.target.value);
            setToast(null);
          }}
        >

          <option value="">
            Choose an assigned student
          </option>

          {students.map((student) => {
            const id = getStudentId(student);

            return (
              <option key={id} value={id}>
                {student.name ||
                  student.student_name ||
                  student.full_name ||
                  student.email ||
                  `Student ${id}`}
              </option>
            );
          })}

        </select>

        {students.length === 0 && (
          <p className="fm-muted">
            No assigned students are available.
          </p>
        )}

        {selectedStudentData && (
          <p className="fm-student-email">
            {selectedStudentData.email || ""}
          </p>
        )}

      </div>

      {/* NO STUDENT SELECTED */}
      {!selectedStudent ? (

        <div className="fm-empty">
          <span>👨‍🎓</span>

          <h3>Select a Student</h3>

          <p>
            Choose an actively assigned student to view messages
            or submit feedback.
          </p>
        </div>

      ) : activeTab === "messages" ? (

        /* MESSAGES SECTION */
        <div className="fm-panel">

          <div className="fm-panel-heading">

            <div>
              <h3>Conversation</h3>

              <p>
                {selectedStudentData?.name ||
                  selectedStudentData?.student_name ||
                  "Selected student"}
              </p>
            </div>

            <button
              type="button"
              onClick={fetchMessages}
              className="fm-refresh"
            >
              ↻ Refresh
            </button>

          </div>

          {/* MESSAGE LIST */}
          <div className="fm-message-list">

            {loading ? (

              <p className="fm-muted">
                Loading messages...
              </p>

            ) : messages.length > 0 ? (

              messages.map((message) => {

                const isSent =
                  String(message.sender) !==
                  String(selectedStudent);

                return (
                  <div
                    key={message.id}
                    className={`fm-message ${
                      isSent ? "sent" : "received"
                    }`}
                  >

                    <div className="fm-message-bubble">

                      <strong>
                        {isSent
                          ? "You"
                          : message.sender_name || "Student"}
                      </strong>

                      <p>{message.message}</p>

                      <small>
                        {formatDate(message.created_at)}
                      </small>

                      {!isSent && !message.is_read && (
                        <button
                          type="button"
                          className="fm-read-button"
                          onClick={() =>
                            handleMarkRead(message.id)
                          }
                        >
                          Mark as read
                        </button>
                      )}

                    </div>

                  </div>
                );
              })

            ) : (

              <div className="fm-empty">
                <span>💬</span>

                <h3>No Messages Yet</h3>

                <p>
                  Start a conversation with your student.
                </p>
              </div>

            )}

          </div>

          {/* SEND MESSAGE FORM */}
          <form
            className="fm-compose"
            onSubmit={handleSendMessage}
          >

            <textarea
              placeholder="Write your message..."
              value={messageText}
              onChange={(event) =>
                setMessageText(event.target.value)
              }
              rows={3}
            />

            <button
              type="submit"
              disabled={
                sending || !messageText.trim()
              }
            >
              {sending
                ? "Sending..."
                : "Send Message"}
            </button>

          </form>

        </div>

      ) : (

        /* FEEDBACK SECTION */
        <div className="fm-panel">

          <div className="fm-panel-heading">
            <div>
              <h3>Student Feedback</h3>

              <p>
                Share guidance and improvement suggestions.
              </p>
            </div>
          </div>

          {/* FEEDBACK FORM */}
          <form
            className="fm-feedback-form"
            onSubmit={handleSubmitFeedback}
          >

            <label htmlFor="fm-subject">
              Feedback Subject
            </label>

            <input
              id="fm-subject"
              type="text"
              placeholder="Example: Python Programming"
              value={subject}
              onChange={(event) =>
                setSubject(event.target.value)
              }
            />

            <label htmlFor="fm-feedback">
              Feedback Description
            </label>

            <textarea
              id="fm-feedback"
              rows={5}
              placeholder="Write your feedback here..."
              value={feedbackText}
              onChange={(event) =>
                setFeedbackText(event.target.value)
              }
            />

            <button
              type="submit"
              disabled={sending}
            >
              {sending
                ? "Submitting..."
                : "Submit Feedback"}
            </button>

          </form>

          {/* PREVIOUS FEEDBACK */}
          <div className="fm-history">

            <h3>Previous Feedback</h3>

            {feedbacks.filter(
              (item) =>
                String(item.student) ===
                String(selectedStudent)
            ).length > 0 ? (

              feedbacks
                .filter(
                  (item) =>
                    String(item.student) ===
                    String(selectedStudent)
                )
                .map((item) => (

                  <div
                    className="fm-feedback-card"
                    key={item.id}
                  >

                    <h4>{item.subject}</h4>

                    <p>{item.feedback}</p>

                    <small>
                      {formatDate(item.created_at)}
                    </small>

                  </div>

                ))

            ) : (

              <p className="fm-muted">
                No feedback has been submitted for this student yet.
              </p>

            )}

          </div>

        </div>

      )}

    </section>
  );
}

export default FeedbackMessages;