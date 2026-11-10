
import React, { useEffect, useState } from "react";
import Toast from "./Toast";
import "./SkillAssessment.css";

const API_BASE_URL = "https://skillsphere-u93o.onrender.com/api/assessments";

function getAccessToken() {
  return (
    localStorage.getItem("skillsphere_access") ||
    localStorage.getItem("access") ||
    ""
  );
}

async function assessmentRequest(path, options = {}) {
  const token = getAccessToken();

  const response = await fetch(`${API_BASE_URL}/${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...options.headers,
    },
  });

  const data = await response.json().catch(() => ({}));

  if (!response.ok) {
    const detail =
      data.detail ||
      data.message ||
      Object.values(data)
        .flat()
        .filter((value) => typeof value === "string")
        .join(" ") ||
      `Request failed (${response.status})`;

    throw new Error(String(detail));
  }

  return data;
}

function normalizeHistoryItem(item) {
  return {
    id: item.id,
    skill: item.skill || "Unknown",
    totalQuestions: Number(
      item.total_questions ?? item.totalQuestions ?? 0
    ),
    correctAnswers: Number(
      item.correct_answers ?? item.correctAnswers ?? 0
    ),
    percentage: Number(
      item.score_percentage ?? item.percentage ?? item.score ?? 0
    ),
    level: item.estimated_level ?? item.level ?? "Beginner",
    date: item.created_at
      ? new Date(item.created_at).toLocaleString()
      : item.date || "Date unavailable",
  };
}

export default function SkillAssessment() {
  const [selectedSkill, setSelectedSkill] = useState("Python");
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState({});
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [started, setStarted] = useState(false);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [history, setHistory] = useState([]);
  const [error, setError] = useState("");
  const [toast, setToast] = useState(null);

  const totalQuestions = questions.length;
  const answeredCount = Object.keys(answers).length;
  const currentItem = questions[currentQuestion];

  const progress =
    totalQuestions > 0
      ? ((currentQuestion + 1) / totalQuestions) * 100
      : 0;

  function showToast(message, type = "success") {
    setToast({ message, type });
  }

  function closeToast() {
    setToast(null);
  }

  function changeSkill(skill) {
    if (loading) return;

    setSelectedSkill(skill);
    setQuestions([]);
    setAnswers({});
    setCurrentQuestion(0);
    setStarted(false);
    setResult(null);
    setError("");
    closeToast();
  }

  function selectAnswer(index) {
    setAnswers((previous) => ({
      ...previous,
      [currentQuestion]: index,
    }));
  }

  async function loadHistory() {
    if (!getAccessToken()) {
      setHistory([]);
      return;
    }

    try {
      const data = await assessmentRequest("history/");
      const items = Array.isArray(data)
        ? data
        : data.results || data.history || [];

      setHistory(items.map(normalizeHistoryItem));
    } catch (err) {
      setError(err.message || "Unable to load assessment history.");
    }
  }

  useEffect(() => {
    loadHistory();
  }, []);

  async function startAssessment() {
    if (!getAccessToken()) {
      showToast("Please log in before starting an assessment.", "error");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const data = await assessmentRequest(
        `questions/?skill=${encodeURIComponent(selectedSkill.toLowerCase())}`
      );

      const items = Array.isArray(data)
        ? data
        : data.results || data.questions || [];

      if (!Array.isArray(items) || items.length === 0) {
        throw new Error("No questions were returned by the server.");
      }

      const formattedQuestions = items.map((item) => ({
        id: String(item.id),
        skill: item.skill || selectedSkill,
        question: item.question,
        options: item.options,
      }));

      const invalidQuestion = formattedQuestions.some(
        (item) =>
          !item.id ||
          !item.question ||
          !Array.isArray(item.options) ||
          item.options.length === 0
      );

      if (invalidQuestion) {
        throw new Error(
          "The server returned questions in an unexpected format."
        );
      }

      setQuestions(formattedQuestions);
      setAnswers({});
      setCurrentQuestion(0);
      setStarted(true);
      showToast("Assessment questions loaded successfully.");
    } catch (err) {
      setQuestions([]);
      setStarted(false);
      setError(err.message || "Unable to load questions.");
      showToast(err.message || "Unable to load questions.", "error");
    } finally {
      setLoading(false);
    }
  }

  async function submitAssessment() {
    if (answeredCount !== totalQuestions) {
      showToast(
        "Please answer every question before submitting.",
        "error"
      );
      return;
    }

    setLoading(true);
    setError("");

    try {
      const submittedAnswers = {};

      questions.forEach((question, index) => {
        submittedAnswers[question.id] = answers[index];
      });

      const data = await assessmentRequest("submit/", {
        method: "POST",
        body: JSON.stringify({
          skill: selectedSkill,
          answers: submittedAnswers,
        }),
      });

      setResult({
        skill: data.skill || selectedSkill,
        totalQuestions: Number(
          data.total_questions ?? totalQuestions
        ),
        correctAnswers: Number(data.correct_answers ?? 0),
        percentage: Number(data.score_percentage ?? 0),
        level: data.estimated_level || "Beginner",
        date: data.created_at
          ? new Date(data.created_at).toLocaleString()
          : new Date().toLocaleString(),
      });

      setStarted(false);
      showToast("Assessment submitted successfully.");

      await loadHistory();
    } catch (err) {
      setError(err.message || "Unable to submit assessment.");
      showToast(err.message || "Unable to submit assessment.", "error");
    } finally {
      setLoading(false);
    }
  }

  function resetAssessment() {
    setQuestions([]);
    setAnswers({});
    setCurrentQuestion(0);
    setStarted(false);
    setResult(null);
    setError("");
    closeToast();
  }

  return (
    <div className="sa-page">
      <div className="sa-heading">
        <h1>Skill Assessment</h1>
        <p>
          Discover your current skills and track your learning progress.
        </p>
      </div>

      {toast && (
        <Toast
          message={toast.message}
          type={toast.type}
          onClose={closeToast}
        />
      )}

      {error && (
        <div className="sa-error-message" role="alert">
          {error}
        </div>
      )}

      {!started && !result && (
        <section className="sa-card sa-start-card">
          <h2>Choose Your Skill</h2>
          <p>Select a skill to begin your assessment.</p>

          <div className="sa-skill-grid">
            {["Python", "Java", "C", "SQL"].map((skill) => (
              <button
                type="button"
                key={skill}
                className={`sa-skill-card ${
                  selectedSkill === skill ? "active" : ""
                }`}
                onClick={() => changeSkill(skill)}
                disabled={loading}
              >
                <span className="sa-skill-icon">
                  {skill === "Python"
                    ? "🐍"
                    : skill === "Java"
                    ? "☕"
                    : skill === "C"
                    ? "💻"
                    : "🗄️"}
                </span>
                <span>{skill}</span>
              </button>
            ))}
          </div>

          <button
            type="button"
            className="sa-primary-button sa-start-button"
            onClick={startAssessment}
            disabled={loading}
          >
            {loading ? "Loading Questions..." : "Start Assessment"}
          </button>
        </section>
      )}

      {started && currentItem && (
        <section className="sa-card sa-quiz-card">
          <div className="sa-quiz-header">
            <span>{selectedSkill} Assessment</span>
            <span>
              Question {currentQuestion + 1} of {totalQuestions}
            </span>
          </div>

          <div className="sa-progress-track">
            <div
              className="sa-progress-fill"
              style={{ width: `${progress}%` }}
            />
          </div>

          <h2 className="sa-question">{currentItem.question}</h2>

          <div className="sa-options">
            {currentItem.options.map((option, index) => (
              <button
                type="button"
                key={`${currentItem.id}-${index}`}
                className={`sa-option ${
                  answers[currentQuestion] === index ? "selected" : ""
                }`}
                onClick={() => selectAnswer(index)}
                disabled={loading}
              >
                <span className="sa-option-letter">
                  {String.fromCharCode(65 + index)}
                </span>
                <span>{option}</span>
              </button>
            ))}
          </div>

          <div className="sa-quiz-navigation">
            <button
              type="button"
              className="sa-secondary-button"
              onClick={() =>
                setCurrentQuestion((previous) =>
                  Math.max(0, previous - 1)
                )
              }
              disabled={currentQuestion === 0 || loading}
            >
              Previous
            </button>

            {currentQuestion < totalQuestions - 1 ? (
              <button
                type="button"
                className="sa-primary-button"
                onClick={() =>
                  setCurrentQuestion((previous) =>
                    Math.min(totalQuestions - 1, previous + 1)
                  )
                }
                disabled={loading}
              >
                Next
              </button>
            ) : (
              <button
                type="button"
                className="sa-primary-button"
                onClick={submitAssessment}
                disabled={loading}
              >
                {loading ? "Submitting..." : "Submit Assessment"}
              </button>
            )}
          </div>

          <p className="sa-answered-count">
            Answered {answeredCount} of {totalQuestions} questions
          </p>
        </section>
      )}

      {result && (
        <section className="sa-card sa-result-card">
          <div className="sa-result-icon">🎉</div>
          <h2>Assessment Completed!</h2>
          <p>Your {result.skill} assessment has been submitted.</p>

          <div className="sa-result-summary">
            <div className="sa-result-stat">
              <span>Score</span>
              <strong>{result.percentage}%</strong>
            </div>

            <div className="sa-result-stat">
              <span>Correct Answers</span>
              <strong>
                {result.correctAnswers}/{result.totalQuestions}
              </strong>
            </div>

            <div className="sa-result-stat">
              <span>Skill Level</span>
              <strong>{result.level}</strong>
            </div>
          </div>

          <p className="sa-result-date">
            Completed: {result.date}
          </p>

          <div className="sa-result-actions">
            <button
              type="button"
              className="sa-primary-button"
              onClick={resetAssessment}
              disabled={loading}
            >
              Take Another Assessment
            </button>
          </div>
        </section>
      )}

      <section className="sa-card sa-history-card">
        <div className="sa-history-header">
          <div>
            <h2>Assessment History</h2>
            <p>Review your previously saved assessment results.</p>
          </div>

          <button
            type="button"
            className="sa-secondary-button"
            onClick={loadHistory}
            disabled={loading}
          >
            Refresh History
          </button>
        </div>

        {history.length === 0 ? (
          <p className="sa-empty-history">
            No assessment history available yet.
          </p>
        ) : (
          <div className="sa-history-list">
            {history.map((item, index) => (
              <div
                className="sa-history-item"
                key={item.id ?? `${item.skill}-${index}`}
              >
                <div className="sa-history-info">
                  <h3>{item.skill}</h3>
                  <p>{item.date}</p>
                </div>

                <div className="sa-history-score">
                  <strong>{item.percentage}%</strong>
                  <span>{item.level}</span>
                  <small>
                    {item.correctAnswers}/{item.totalQuestions} correct
                  </small>
                </div>
              </div>
            ))}
          </div>
        )}
      </section>
    </div>
  );
}
