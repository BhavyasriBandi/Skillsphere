
import React, { useEffect, useState } from "react";
import Toast from "./Toast";
import "./SkillAssessment.css";

const API_BASE_URL = "https://skillsphere-u93o.onrender.com";
const QUESTION_COUNT = 10;

const DIFFICULTIES = [
  { value: "beginner", label: "Beginner" },
  { value: "intermediate", label: "Intermediate" },
  { value: "advanced", label: "Advanced" },
];

function getAuthToken() {
  return localStorage.getItem("skillsphere_access");
}

async function assessmentRequest(endpoint, method = "GET", body = null) {
  const token = getAuthToken();

  if (!token) {
    throw new Error("Your login session was not found. Please log in again.");
  }

  const options = {
    method,
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json",
    },
  };

  if (body !== null) {
    options.body = JSON.stringify(body);
  }

  const response = await fetch(`${API_BASE_URL}${endpoint}`, options);

  let data = {};

  try {
    data = await response.json();
  } catch {
    data = {};
  }

  if (!response.ok) {
    throw new Error(
      data.detail ||
      data.message ||
      "Something went wrong. Please try again."
    );
  }

  return data;
}

function getSkillLevel(percentage) {
  if (percentage >= 80) return "Advanced";
  if (percentage >= 60) return "Intermediate";
  return "Beginner";
}

function getOptionLetter(index) {
  return String.fromCharCode(65 + index);
}

function renderSkillIcon(skill) {
  const normalizedSkill = String(skill || "").trim().toLowerCase();

  if (normalizedSkill === "python") return "🐍";
  if (normalizedSkill === "java") return "☕";
  if (normalizedSkill.includes("javascript")) return "JS";
  if (normalizedSkill.startsWith("c ")) return "C";
  if (normalizedSkill.includes("sql")) return "▤";
  if (normalizedSkill.includes("django")) return "D";
  if (normalizedSkill.includes("git")) return "⌘";
  if (normalizedSkill.includes("data structures")) return "▦";
  if (normalizedSkill.includes("web")) return "🌐";

  return "✦";
}

function formatDate(dateValue) {
  if (!dateValue) return "Date unavailable";

  const date = new Date(dateValue);

  if (Number.isNaN(date.getTime())) {
    return "Date unavailable";
  }

  return date.toLocaleDateString("en-IN", {
    day: "2-digit",
    month: "short",
    year: "numeric",
  });
}

function mapHistoryItem(item) {
  const percentage = Number(item.percentage) || 0;

  return {
    id: item.id,
    skill: item.skill_name || item.skill || "Skill",
    percentage,
    correctAnswers: Number(item.score) || 0,
    totalQuestions: Number(item.total_questions) || QUESTION_COUNT,
    wrongAnswers:
      (Number(item.total_questions) || QUESTION_COUNT) -
      (Number(item.score) || 0),
    level: getSkillLevel(percentage),
    date: formatDate(item.completed_at),
  };
}

function SkillAssessment() {
  const [skills, setSkills] = useState([]);
  const [skillsLoading, setSkillsLoading] = useState(true);

  // No default skill or difficulty selection.
  const [selectedSkill, setSelectedSkill] = useState("");
  const [selectedDifficulty, setSelectedDifficulty] = useState("");

  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState([]);

  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [totalQuestions, setTotalQuestions] = useState(QUESTION_COUNT);

  const [attemptId, setAttemptId] = useState(null);

  const [started, setStarted] = useState(false);
  const [result, setResult] = useState(null);
  const [reviewMode, setReviewMode] = useState(false);

  const [history, setHistory] = useState([]);

  const [loading, setLoading] = useState(false);
  const [submitting, setSubmitting] = useState(false);

  const [toast, setToast] = useState({
    message: "",
    type: "success",
  });

  const closeToast = () => {
    setToast({
      message: "",
      type: "success",
    });
  };

  const showToast = (message, type = "success") => {
    setToast({
      message,
      type,
    });
  };

  // =======================================================
  // LOAD ACTIVE SKILLS FROM DJANGO
  // =======================================================

  const loadSkills = async () => {
    setSkillsLoading(true);

    try {
      const response = await fetch(`${API_BASE_URL}/api/skills/`);
      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || "Unable to load skills from the server."
        );
      }

      const excludedSkills = [
        "object-oriented programming",
        "testing & debugging",
      ];

      const activeSkills = Array.isArray(data.skills)
        ? data.skills.filter(
            (skill) =>
              skill.is_active &&
              !excludedSkills.includes(
                String(skill.name || "").trim().toLowerCase()
              )
          )
        : [];

      setSkills(activeSkills);
    } catch (error) {
      console.error("Load skills error:", error);
      showToast(error.message, "error");
      setSkills([]);
    } finally {
      setSkillsLoading(false);
    }
  };

  // =======================================================
  // LOAD ASSESSMENT HISTORY
  // =======================================================

  const loadHistory = async () => {
    try {
      const data = await assessmentRequest(
        "/api/skills/assessments/"
      );

      const historyItems = Array.isArray(data.assessments)
        ? data.assessments.map(mapHistoryItem)
        : [];

      setHistory(historyItems);
    } catch (error) {
      console.error("Assessment history error:", error);
    }
  };

  useEffect(() => {
    loadSkills();
    loadHistory();
  }, []);

  // =======================================================
  // CHANGE SELECTED SKILL
  // =======================================================

  const changeSkill = (skill) => {
    if (loading || submitting) return;

    setSelectedSkill(skill);

    setStarted(false);
    setResult(null);
    setReviewMode(false);

    setQuestions([]);
    setAnswers([]);

    setAttemptId(null);
    setCurrentQuestion(0);
  };

  // =======================================================
  // CHANGE DIFFICULTY
  // =======================================================

  const changeDifficulty = (difficulty) => {
    if (loading || submitting) return;

    setSelectedDifficulty(difficulty);

    setStarted(false);
    setResult(null);
    setReviewMode(false);

    setQuestions([]);
    setAnswers([]);

    setAttemptId(null);
    setCurrentQuestion(0);
  };

  // =======================================================
  // START ASSESSMENT
  // =======================================================

  const startAssessment = async () => {
    if (loading || submitting) return;

    if (!selectedSkill) {
      showToast("Please select a skill first.", "error");
      return;
    }

    if (!selectedDifficulty) {
      showToast("Please select assessment difficulty.", "error");
      return;
    }

    setLoading(true);

    try {
      const data = await assessmentRequest(
        "/api/skills/assessments/start/",
        "POST",
        {
          skill_name: selectedSkill,
          difficulty: selectedDifficulty,
        }
      );

      if (
        !Array.isArray(data.questions) ||
        data.questions.length !== QUESTION_COUNT
      ) {
        throw new Error(
          "The server did not return exactly 10 questions."
        );
      }

      const formattedQuestions = data.questions.map((item) => ({
        id: item.id,
        question: item.question_text,
        options: item.options,
      }));

      setQuestions(formattedQuestions);
      setAnswers(Array(QUESTION_COUNT).fill(null));

      setAttemptId(data.attempt_id);
      setTotalQuestions(data.total_questions || QUESTION_COUNT);

      setCurrentQuestion(0);
      setResult(null);
      setReviewMode(false);
      setStarted(true);

      showToast(
        `${selectedDifficulty.charAt(0).toUpperCase() + selectedDifficulty.slice(1)} assessment is ready!`,
        "success"
      );
    } catch (error) {
      console.error("Start assessment error:", error);
      showToast(error.message, "error");
    } finally {
      setLoading(false);
    }
  };

  // =======================================================
  // SELECT ANSWER
  // =======================================================

  const selectAnswer = (selectedIndex) => {
    setAnswers((previous) => {
      const updated = [...previous];
      updated[currentQuestion] = selectedIndex;
      return updated;
    });
  };

  // =======================================================
  // SUBMIT ASSESSMENT
  // =======================================================

  const submitAssessment = async () => {
    if (submitting) return;

    if (!attemptId) {
      showToast(
        "Assessment attempt was not found. Please start again.",
        "error"
      );
      return;
    }

    const answeredCount = answers.filter(
      (answer) => answer !== null
    ).length;

    if (answeredCount !== totalQuestions) {
      showToast(
        "Please answer all 10 questions before submitting.",
        "error"
      );
      return;
    }

    setSubmitting(true);

    try {
      const data = await assessmentRequest(
        "/api/skills/assessments/submit/",
        "POST",
        {
          attempt_id: attemptId,
          answers,
        }
      );

      const resultData = data.result || {};

      const percentage = Number(
        data.percentage ?? resultData.percentage ?? 0
      );

      const correctAnswers = Number(
        data.correct_answers ?? resultData.score ?? 0
      );

      const questionTotal = Number(
        data.total_questions ??
        resultData.total_questions ??
        QUESTION_COUNT
      );

      const formattedResult = {
        id: resultData.id,
        skill: selectedSkill,
        percentage,
        correctAnswers,
        wrongAnswers: questionTotal - correctAnswers,
        totalQuestions: questionTotal,
        level: data.level || getSkillLevel(percentage),
      };

      const reviewQuestions = Array.isArray(data.review)
        ? data.review.map((item) => ({
            id: item.question_id,
            question: item.question_text,
            options: item.options,
            answer: item.correct_answer,
            explanation: item.explanation,
            selectedAnswer: item.selected_answer,
          }))
        : [];

      setQuestions(reviewQuestions);
      setResult(formattedResult);

      setStarted(false);
      setReviewMode(true);

      await loadHistory();

      showToast(
        "Assessment submitted successfully!",
        "success"
      );
    } catch (error) {
      console.error("Submit assessment error:", error);
      showToast(error.message, "error");
    } finally {
      setSubmitting(false);
    }
  };

  // =======================================================
  // RESET ASSESSMENT
  // =======================================================

  const resetAssessment = () => {
    setStarted(false);
    setResult(null);
    setReviewMode(false);

    setQuestions([]);
    setAnswers([]);

    setAttemptId(null);
    setCurrentQuestion(0);
    setTotalQuestions(QUESTION_COUNT);

    setSelectedSkill("");
    setSelectedDifficulty("");
  };

  // =======================================================
  // DERIVED VALUES
  // =======================================================

  const question = questions[currentQuestion];

  const answeredCount = answers.filter(
    (answer) => answer !== null
  ).length;

  const progress =
    totalQuestions > 0
      ? (answeredCount / totalQuestions) * 100
      : 0;

  // =======================================================
  // UI
  // =======================================================

  return (
    <div className="sa-page">
      <Toast
        message={toast.message}
        type={toast.type}
        onClose={closeToast}
      />

      <div className="sa-heading">
        <div>
          <span className="sa-eyebrow">
            LEARN · ASSESS · IMPROVE
          </span>

          <h1>Skill Assessment</h1>

          <p>
            Discover your current knowledge and identify where to grow next.
          </p>
        </div>

        <div className="sa-heading-icon" aria-hidden="true">
          <span>✓</span>
        </div>
      </div>

      {/* START ASSESSMENT */}

      {!started && !result && !reviewMode && (
        <section className="sa-card sa-start-card">
          <div className="sa-section-heading">
            <div>
              <h2>Choose your skill</h2>
              <p>Select a subject to begin your assessment.</p>
            </div>

            <span className="sa-question-count">
              {QUESTION_COUNT} fresh questions
            </span>
          </div>

          <div className="sa-skill-grid">
            {skillsLoading ? (
              <p>Loading skills...</p>
            ) : skills.length === 0 ? (
              <p>No active skills are available right now.</p>
            ) : (
              skills.map((skillItem) => {
                const skill = skillItem.name;

                return (
                  <button
                    key={skillItem.id}
                    type="button"
                    className={`sa-skill-option ${
                      selectedSkill === skill ? "selected" : ""
                    }`}
                    onClick={() => changeSkill(skill)}
                    aria-pressed={selectedSkill === skill}
                    disabled={loading}
                  >
                    <span
                      className={`sa-skill-icon sa-icon-${skill
                        .toLowerCase()
                        .replace(/[^a-z0-9]+/g, "-")}`}
                    >
                      {renderSkillIcon(skill)}
                    </span>

                    <span className="sa-skill-text">
                      <strong>{skill}</strong>
                      <small>Assessment questions</small>
                    </span>

                    <span className="sa-radio-mark">
                      {selectedSkill === skill ? "✓" : ""}
                    </span>
                  </button>
                );
              })
            )}
          </div>

          {/* DIFFICULTY SELECTION */}

          <div className="sa-difficulty-selection">
            <h3>Choose Difficulty</h3>

            <p>Select your preferred assessment level.</p>

            <select
              value={selectedDifficulty}
              onChange={(event) =>
                changeDifficulty(event.target.value)
              }
              disabled={skillsLoading || loading || submitting}
              className="sa-difficulty-select"
            >
              <option value="">Select Difficulty</option>

              {DIFFICULTIES.map((difficulty) => (
                <option
                  key={difficulty.value}
                  value={difficulty.value}
                >
                  {difficulty.label}
                </option>
              ))}
            </select>
          </div>

          <div className="sa-test-info">
            <div>
              <span className="sa-info-icon">Q</span>
              <span>
                <strong>10 fresh questions</strong>
                <small>Generated for your selected skill</small>
              </span>
            </div>

            <div>
              <span className="sa-info-icon">%</span>
              <span>
                <strong>Instant results</strong>
                <small>Score and skill level</small>
              </span>
            </div>

            <div>
              <span className="sa-info-icon">↻</span>
              <span>
                <strong>New attempt</strong>
                <small>Previous questions are considered</small>
              </span>
            </div>
          </div>

          <button
            type="button"
            className="sa-primary-button sa-start-button"
            onClick={startAssessment}
            disabled={
              loading ||
              skillsLoading ||
              skills.length === 0 ||
              !selectedSkill ||
              !selectedDifficulty
            }
          >
            {skillsLoading
              ? "Loading Skills..."
              : loading
                ? "Generating Questions..."
                : "Start Assessment"}
            {!loading && !skillsLoading && <span> →</span>}
          </button>
        </section>
      )}

      {/* QUIZ QUESTIONS */}

      {started && question && (
        <section className="sa-card sa-quiz-card">
          <div className="sa-quiz-top">
            <div>
              <span className="sa-eyebrow">YOUR ASSESSMENT</span>
              <h2>{selectedSkill}</h2>
              <p>
                Difficulty: {selectedDifficulty}
              </p>
            </div>

            <span className="sa-question-count">
              Question {currentQuestion + 1} of {totalQuestions}
            </span>
          </div>

          <div
            className="sa-progress-track"
            role="progressbar"
            aria-valuenow={Math.round(progress)}
            aria-valuemin={0}
            aria-valuemax={100}
            aria-label="Question progress"
          >
            <div
              className="sa-progress-fill"
              style={{ width: `${progress}%` }}
            />
          </div>

          <div className="sa-progress-label">
            <span>Assessment progress</span>
            <strong>{Math.round(progress)}%</strong>
          </div>

          <div className="sa-question-area">
            <span className="sa-question-label">
              QUESTION {String(currentQuestion + 1).padStart(2, "0")}
            </span>

            <h3>{question.question}</h3>

            <p className="sa-select-hint">
              Select one correct answer from the options below.
            </p>

            <div className="sa-options">
              {question.options.map((option, index) => {
                const isSelected =
                  answers[currentQuestion] === index;

                return (
                  <button
                    key={`${question.id}-${index}`}
                    type="button"
                    className={`sa-option ${
                      isSelected ? "selected" : ""
                    }`}
                    onClick={() => selectAnswer(index)}
                    aria-pressed={isSelected}
                  >
                    <span className="sa-option-letter">
                      {getOptionLetter(index)}
                    </span>

                    <span className="sa-option-text">
                      {option}
                    </span>

                    <span className="sa-option-check">
                      {isSelected ? "✓" : ""}
                    </span>
                  </button>
                );
              })}
            </div>
          </div>

          <div className="sa-quiz-footer">
            <button
              type="button"
              className="sa-secondary-button"
              onClick={() =>
                setCurrentQuestion((previous) =>
                  Math.max(0, previous - 1)
                )
              }
              disabled={currentQuestion === 0 || submitting}
            >
              ← Previous
            </button>

            <span className="sa-answered-count">
              {answeredCount} of {totalQuestions} answered
            </span>

            {currentQuestion < totalQuestions - 1 ? (
              <button
                type="button"
                className="sa-primary-button"
                onClick={() =>
                  setCurrentQuestion((previous) =>
                    Math.min(totalQuestions - 1, previous + 1)
                  )
                }
                disabled={submitting}
              >
                Next Question →
              </button>
            ) : (
              <button
                type="button"
                className="sa-primary-button"
                onClick={submitAssessment}
                disabled={submitting}
              >
                {submitting ? "Submitting..." : "Submit Assessment ✓"}
              </button>
            )}
          </div>
        </section>
      )}

      {/* RESULTS */}

      {result && reviewMode && (
        <section className="sa-card sa-result-card">
          <div className="sa-result-icon">✓</div>

          <span className="sa-eyebrow">
            ASSESSMENT COMPLETED
          </span>

          <h2>Your Results</h2>

          <p className="sa-result-subtitle">
            Here is your {result.skill} assessment performance.
          </p>

          <div className="sa-score-circle">
            <strong>{result.percentage}%</strong>
            <span>Overall score</span>
          </div>

          <div className="sa-result-stats">
            <div>
              <span>Correct answers</span>
              <strong className="sa-correct-number">
                {result.correctAnswers}/{result.totalQuestions}
              </strong>
            </div>

            <div>
              <span>Wrong answers</span>
              <strong className="sa-wrong-number">
                {result.wrongAnswers}/{result.totalQuestions}
              </strong>
            </div>

            <div>
              <span>Skill level</span>
              <strong className="sa-level-value">
                {result.level}
              </strong>
            </div>
          </div>

          <div className="sa-feedback">
            <h3>Your next step</h3>

            <p>
              {result.percentage >= 80
                ? "Excellent work! Practise advanced problems and real-world projects."
                : result.percentage >= 60
                  ? "Good progress! Review incorrect answers and practise those concepts."
                  : "Keep learning! Revise the fundamentals and try another assessment."}
            </p>
          </div>

          <div className="sa-result-actions">
            <button
              type="button"
              className="sa-secondary-button"
              onClick={resetAssessment}
            >
              Choose Another Skill
            </button>

            <button
              type="button"
              className="sa-primary-button"
              onClick={startAssessment}
              disabled={loading}
            >
              {loading ? "Generating..." : "Retake Assessment ↻"}
            </button>
          </div>
        </section>
      )}

      {/* ANSWER REVIEW */}

      {result && reviewMode && (
        <section className="sa-card sa-review-card">
          <div className="sa-section-heading">
            <div>
              <span className="sa-eyebrow">
                LEARN FROM YOUR ANSWERS
              </span>

              <h2>Answer Review</h2>

              <p>
                See your selected answer, the correct answer, and its explanation.
              </p>
            </div>

            <span className="sa-question-count">
              {questions.length} reviewed
            </span>
          </div>

          <div className="sa-review-list">
            {questions.map((item, index) => {
              const selectedAnswer = item.selectedAnswer;
              const isCorrect = selectedAnswer === item.answer;

              return (
                <article
                  className={`sa-review-item ${
                    isCorrect ? "review-correct" : "review-wrong"
                  }`}
                  key={item.id}
                >
                  <div className="sa-review-question-heading">
                    <span className="sa-review-number">
                      Question {index + 1}
                    </span>

                    <span
                      className={`sa-review-status ${
                        isCorrect ? "status-correct" : "status-wrong"
                      }`}
                    >
                      {isCorrect ? "✓ Correct" : "✕ Incorrect"}
                    </span>
                  </div>

                  <h3>{item.question}</h3>

                  <div className="sa-review-options">
                    {item.options.map((option, optionIndex) => {
                      const isRightAnswer =
                        optionIndex === item.answer;

                      const isStudentAnswer =
                        optionIndex === selectedAnswer;

                      let optionClass = "sa-review-option";

                      if (isRightAnswer) {
                        optionClass += " correct-answer";
                      } else if (isStudentAnswer) {
                        optionClass += " wrong-answer";
                      }

                      return (
                        <div
                          className={optionClass}
                          key={`${item.id}-${optionIndex}`}
                        >
                          <span className="sa-review-letter">
                            {getOptionLetter(optionIndex)}
                          </span>

                          <span className="sa-review-option-text">
                            {option}
                          </span>

                          <span className="sa-review-option-label">
                            {isRightAnswer
                              ? "Correct answer"
                              : isStudentAnswer
                                ? "Your answer"
                                : ""}
                          </span>
                        </div>
                      );
                    })}
                  </div>

                  <div className="sa-explanation">
                    <span className="sa-explanation-icon">i</span>

                    <div>
                      <strong>Explanation</strong>
                      <p>{item.explanation}</p>
                    </div>
                  </div>
                </article>
              );
            })}
          </div>

          <div className="sa-review-bottom">
            <div>
              <strong>Keep improving!</strong>

              <p>
                Review the explanations and try another fresh assessment.
              </p>
            </div>

            <button
              type="button"
              className="sa-primary-button"
              onClick={startAssessment}
              disabled={loading}
            >
              {loading ? "Generating..." : "Try Again ↻"}
            </button>
          </div>
        </section>
      )}

      {/* ASSESSMENT HISTORY */}

      <section className="sa-card sa-history-card">
        <div className="sa-section-heading">
          <div>
            <h2>Assessment History</h2>
            <p>Your completed assessments saved in your account.</p>
          </div>
        </div>

        {history.length === 0 ? (
          <div className="sa-empty-state">
            <span className="sa-empty-icon">▤</span>

            <strong>No assessments yet</strong>

            <p>
              Complete your first assessment to see your results here.
            </p>
          </div>
        ) : (
          <div className="sa-history-list">
            {history.map((item, index) => {
              const level =
                typeof item.level === "string"
                  ? item.level
                  : getSkillLevel(Number(item.percentage) || 0);

              return (
                <div
                  className="sa-history-row"
                  key={item.id || index}
                >
                  <div className="sa-history-skill-icon">
                    {renderSkillIcon(item.skill)}
                  </div>

                  <div className="sa-history-details">
                    <strong>{item.skill} Assessment</strong>
                    <span>{item.date || "Date unavailable"}</span>
                  </div>

                  <div className="sa-history-score">
                    <strong>{Number(item.percentage) || 0}%</strong>

                    <span>
                      {item.correctAnswers ?? 0}/
                      {item.totalQuestions ?? 0} correct
                    </span>
                  </div>

                  <span
                    className={`sa-level-badge sa-level-${level.toLowerCase()}`}
                  >
                    {level}
                  </span>
                </div>
              );
            })}
          </div>
        )}
      </section>
    </div>
  );
}

export default SkillAssessment;
