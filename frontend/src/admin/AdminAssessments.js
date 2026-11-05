
import React, { useEffect, useState, useCallback } from "react";
import "./AdminAssessments.css";
import AssessmentQuestionManagement from "./AssessmentQuestionManagement";

const API_BASE_URL = "http://127.0.0.1:8000";

function getAccessToken() {
  return (
    localStorage.getItem("skillsphere_access") ||
    localStorage.getItem("access") ||
    ""
  );
}

async function readResponse(response) {
  const text = await response.text();

  let data = {};

  try {
    data = text ? JSON.parse(text) : {};
  } catch {
    data = {
      detail: text || "Unexpected server response.",
    };
  }

  if (!response.ok) {
    throw new Error(
      data.detail ||
        data.message ||
        `Request failed with status ${response.status}.`
    );
  }

  return data;
}

function normalizeQuestions(data) {
  if (Array.isArray(data)) return data;
  if (Array.isArray(data.questions)) return data.questions;
  if (Array.isArray(data.results)) return data.results;
  if (Array.isArray(data.data)) return data.data;
  if (Array.isArray(data.data?.results)) return data.data.results;

  return [];
}

function normalizeSkills(data) {
  if (Array.isArray(data)) return data;
  if (Array.isArray(data.skills)) return data.skills;
  if (Array.isArray(data.results)) return data.results;
  if (Array.isArray(data.data)) return data.data;
  if (Array.isArray(data.data?.results)) return data.data.results;

  return [];
}

function getQuestionText(question) {
  return (
    question.question ||
    question.question_text ||
    question.text ||
    "Question text unavailable"
  );
}

function getQuestionOptions(question) {
  if (Array.isArray(question.options)) {
    return question.options;
  }

  if (question.options && typeof question.options === "object") {
    return Object.values(question.options);
  }

  return [];
}

function getSkillName(skill) {
  if (typeof skill === "string") return skill;

  return skill?.name || skill?.skill_name || "Unknown";
}

function isQuestionActive(question) {
  return (
    question.is_active === true ||
    question.is_active === 1 ||
    question.is_active === "true" ||
    question.is_active === "1"
  );
}

function isQuestionInactive(question) {
  return (
    question.is_active === false ||
    question.is_active === 0 ||
    question.is_active === "false" ||
    question.is_active === "0"
  );
}

// Connect Admin Skills names with existing question-bank names.
const SKILL_QUESTION_NAME_MAP = {
  "c programming": "C",
  "java": "Java",
  "python": "Python",
  "sql & databases": "Sql",
};

export default function AdminAssessments() {
  const [selectedSkill, setSelectedSkill] = useState("All Skills");

  const [skills, setSkills] = useState([]);
  const [questions, setQuestions] = useState([]);

  const [loading, setLoading] = useState(false);
  const [skillsLoading, setSkillsLoading] = useState(true);

  const [error, setError] = useState("");
  const [skillsError, setSkillsError] = useState("");

  const [lastUpdated, setLastUpdated] = useState("");

  const [showQuestionManagement, setShowQuestionManagement] =
    useState(false);

  // ==========================================
  // LOAD ACTIVE SKILLS
  // ==========================================

  const loadSkills = useCallback(async () => {
    setSkillsLoading(true);
    setSkillsError("");

    try {
      const response = await fetch(
        `${API_BASE_URL}/api/skills/`,
        {
          method: "GET",
          headers: {
            Accept: "application/json",
          },
        }
      );

      const data = await readResponse(response);

      const activeSkills = normalizeSkills(data).filter(
        (skill) =>
          skill.is_active !== false &&
          skill.is_active !== 0
      );

      setSkills(activeSkills);

      setSelectedSkill((previous) => {
        if (previous === "All Skills") return previous;

        const stillAvailable = activeSkills.some(
          (skill) =>
            getSkillName(skill).toLowerCase() ===
            previous.toLowerCase()
        );

        return stillAvailable ? previous : "All Skills";
      });
    } catch (err) {
      setSkills([]);
      setSkillsError(
        err.message || "Unable to load active skills."
      );
    } finally {
      setSkillsLoading(false);
    }
  }, []);

  // ==========================================
  // LOAD QUESTIONS
  // ==========================================

  const loadQuestions = useCallback(async (skill) => {
    setLoading(true);
    setError("");

    try {
      const token = getAccessToken();

      if (!token) {
        throw new Error(
          "Authentication token not found. Please log in again."
        );
      }

      let query = "";

      if (skill !== "All Skills") {
        const normalizedSkill = skill.trim().toLowerCase();

        const databaseSkill =
          SKILL_QUESTION_NAME_MAP[normalizedSkill] || skill;

        query = `?skill=${encodeURIComponent(databaseSkill)}`;
      }

      const response = await fetch(
        `${API_BASE_URL}/api/assessments/admin/questions/${query}`,
        {
          method: "GET",
          headers: {
            Authorization: `Bearer ${token}`,
            Accept: "application/json",
          },
        }
      );

      const data = await readResponse(response);

      setQuestions(normalizeQuestions(data));
      setLastUpdated(new Date().toLocaleTimeString());
    } catch (err) {
      setQuestions([]);
      setError(
        err.message || "Unable to load assessment questions."
      );
    } finally {
      setLoading(false);
    }
  }, []);

  // ==========================================
  // INITIAL LOAD
  // ==========================================

  useEffect(() => {
    loadSkills();
  }, [loadSkills]);

  useEffect(() => {
    loadQuestions(selectedSkill);
  }, [selectedSkill, loadQuestions]);

  // ==========================================
  // QUESTION COUNTS
  // ==========================================

  const activeCount = questions.filter(
    isQuestionActive
  ).length;

  const inactiveCount = questions.filter(
    isQuestionInactive
  ).length;

  // ==========================================
  // HANDLERS
  // ==========================================

  function handleSkillChange(event) {
    setSelectedSkill(event.target.value);
  }

  function openQuestionManagement() {
    setShowQuestionManagement(true);
  }

  async function closeQuestionManagement() {
    setShowQuestionManagement(false);

    await loadSkills();
    await loadQuestions(selectedSkill);
  }

  async function handleRefresh() {
    await loadSkills();
    await loadQuestions(selectedSkill);
  }

  // ==========================================
  // QUESTION MANAGEMENT
  // ==========================================

  if (showQuestionManagement) {
    return (
      <div>
        <div style={{ marginBottom: "18px" }}>
          <button
            type="button"
            className="aa-refresh-button"
            onClick={closeQuestionManagement}
          >
            ← Back to Assessments
          </button>
        </div>

        <AssessmentQuestionManagement />
      </div>
    );
  }

  // ==========================================
  // ADMIN ASSESSMENTS PAGE
  // ==========================================

  return (
    <section className="admin-assessments">

      {/* HEADER */}

      <div className="aa-header">
        <div>
          <p className="aa-eyebrow">
            SKILLSPHERE ADMINISTRATION
          </p>

          <h1>Assessments</h1>

          <p className="aa-subtitle">
            View and manage all questions available in skill assessments.
          </p>
        </div>

        <div
          style={{
            display: "flex",
            flexWrap: "wrap",
            gap: "10px",
            alignItems: "center",
          }}
        >
          <button
            type="button"
            className="aa-refresh-button"
            onClick={openQuestionManagement}
          >
            + Manage Questions
          </button>

          <button
            type="button"
            className="aa-refresh-button"
            onClick={handleRefresh}
            disabled={loading || skillsLoading}
          >
            <span aria-hidden="true">↻</span>{" "}
            {loading || skillsLoading ? "Loading..." : "Refresh"}
          </button>
        </div>
      </div>

      {/* SUMMARY CARDS */}

      <div className="aa-summary-grid">

        <article className="aa-summary-card">
          <div className="aa-summary-icon">▤</div>

          <div>
            <p className="aa-summary-label">
              Total Questions
            </p>

            <h2>
              {loading ? "—" : questions.length}
            </h2>
          </div>
        </article>

        <article className="aa-summary-card">
          <div className="aa-summary-icon aa-summary-icon-blue">
            ✓
          </div>

          <div>
            <p className="aa-summary-label">
              Active Questions
            </p>

            <h2>
              {loading ? "—" : activeCount}
            </h2>
          </div>
        </article>

        <article className="aa-summary-card">
          <div className="aa-summary-icon">◷</div>

          <div>
            <p className="aa-summary-label">
              Inactive Questions
            </p>

            <h2>
              {loading ? "—" : inactiveCount}
            </h2>
          </div>
        </article>

      </div>

      {/* COMPLETE QUESTION BANK */}

      <div className="aa-content-card">

        <div className="aa-content-header">
          <div>
            <h2>Complete Question Bank</h2>

            <p>
              Choose a skill to view its stored assessment questions.
            </p>
          </div>

          <label className="aa-skill-control">
            <span>Filter by Skill</span>

            <select
              value={selectedSkill}
              onChange={handleSkillChange}
              disabled={loading || skillsLoading}
            >
              <option value="All Skills">
                All Skills
              </option>

              {skills.map((skill) => (
                <option
                  key={skill.id || getSkillName(skill)}
                  value={getSkillName(skill)}
                >
                  {getSkillName(skill)}
                </option>
              ))}
            </select>
          </label>
        </div>

        {/* SKILLS ERROR */}

        {skillsError && (
          <div className="aa-error" role="alert">
            <strong>Unable to load active skills</strong>

            <p>{skillsError}</p>

            <button type="button" onClick={loadSkills}>
              Try again
            </button>
          </div>
        )}

        {/* QUESTIONS ERROR */}

        {error && (
          <div className="aa-error" role="alert">
            <strong>Unable to load questions</strong>

            <p>{error}</p>

            <button
              type="button"
              onClick={() => loadQuestions(selectedSkill)}
            >
              Try again
            </button>
          </div>
        )}

        {/* LOADING */}

        {(loading || skillsLoading) && (
          <div className="aa-state-message">
            <span className="aa-spinner" />

            <p>Loading complete question bank...</p>
          </div>
        )}

        {/* EMPTY STATE */}

        {!loading &&
          !skillsLoading &&
          !error &&
          !skillsError &&
          questions.length === 0 && (
            <div className="aa-state-message">
              <div className="aa-empty-icon">▤</div>

              <h3>No questions found</h3>

              <p>
                No questions are available for {selectedSkill}.
                Use Manage Questions to add questions.
              </p>
            </div>
          )}

        {/* QUESTION TABLE */}

        {!loading &&
          !skillsLoading &&
          !error &&
          questions.length > 0 && (
            <>
              <div className="aa-table-info">
                <span>
                  Showing <strong>{questions.length}</strong> questions
                </span>

                {lastUpdated && (
                  <span className="aa-updated">
                    Updated at {lastUpdated}
                  </span>
                )}
              </div>

              <div className="aa-table-wrapper">
                <table className="aa-table">

                  <thead>
                    <tr>
                      <th className="aa-number-column">#</th>
                      <th>Question</th>
                      <th>Options</th>
                      <th>Skill</th>
                      <th>Status</th>
                    </tr>
                  </thead>

                  <tbody>
                    {questions.map((question, index) => {
                      const options = getQuestionOptions(question);
                      const active = isQuestionActive(question);

                      return (
                        <tr key={question.id || index}>

                          <td>
                            <span className="aa-number">
                              {index + 1}
                            </span>
                          </td>

                          <td className="aa-question-cell">
                            {getQuestionText(question)}
                          </td>

                          <td>
                            {options.length > 0 ? (
                              <div className="aa-options">
                                {options.map((option, optionIndex) => {
                                  const optionText =
                                    typeof option === "object" &&
                                    option !== null
                                      ? option.text ||
                                        option.label ||
                                        option.value ||
                                        JSON.stringify(option)
                                      : String(option);

                                  return (
                                    <span
                                      className="aa-option-chip"
                                      key={`${question.id}-${optionIndex}`}
                                    >
                                      {optionText}
                                    </span>
                                  );
                                })}
                              </div>
                            ) : (
                              <span className="aa-muted">
                                Not provided
                              </span>
                            )}
                          </td>

                          <td>
                            <span className="aa-skill-badge">
                              {getSkillName(question.skill)}
                            </span>
                          </td>

                          <td>
                            <span
                              className={
                                active
                                  ? "aa-status-active"
                                  : "aa-status-inactive"
                              }
                            >
                              {active ? "Active" : "Inactive"}
                            </span>
                          </td>

                        </tr>
                      );
                    })}
                  </tbody>

                </table>
              </div>
            </>
          )}

      </div>

      {/* FOOTER */}

      <p className="aa-footer-note">
        All questions are retrieved from the admin question bank.
        Use Manage Questions to create, edit, activate, deactivate,
        and delete assessment questions.
      </p>

    </section>
  );
}
