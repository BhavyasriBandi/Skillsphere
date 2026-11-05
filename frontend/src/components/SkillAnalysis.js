
import React, { useEffect, useMemo, useState } from "react";
import Toast from "./Toast";
import "./SkillAnalysis.css";

const API_BASE_URL = "http://127.0.0.1:8000";

const EXCLUDED_SKILLS = [
  "object-oriented programming",
  "testing & debugging",
];

function getLevel(score) {
  if (score >= 80) return "Advanced";
  if (score >= 60) return "Intermediate";
  return "Beginner";
}

function getLevelClass(level) {
  return `analysis-level-${String(level).toLowerCase()}`;
}

function formatDate(value) {
  if (!value) return "Date not available";

  const date = new Date(value);

  if (Number.isNaN(date.getTime())) {
    return "Date not available";
  }

  return date.toLocaleDateString("en-IN", {
    year: "numeric",
    month: "short",
    day: "numeric",
  });
}

function getSkillShortName(name) {
  const value = String(name || "").toLowerCase();

  if (value.includes("python")) return "Py";
  if (value.includes("java")) return "Ja";
  if (value.includes("javascript")) return "JS";
  if (value.includes("c programming")) return "C";
  if (value.includes("sql")) return "SQL";
  if (value.includes("django")) return "Dj";
  if (value.includes("git")) return "Git";
  if (value.includes("data structures")) return "DS";
  if (value.includes("web")) return "Web";

  return String(name || "").slice(0, 3).toUpperCase();
}

function getSkillColor(name) {
  const value = String(name || "").toLowerCase();

  if (value.includes("python")) return "python";
  if (value.includes("java")) return "java";
  if (value.includes("javascript")) return "javascript";
  if (value.includes("c programming")) return "c";
  if (value.includes("sql")) return "sql";
  if (value.includes("django")) return "django";
  if (value.includes("git")) return "git";
  if (value.includes("data structures")) return "data";
  if (value.includes("web")) return "web";

  return "blue";
}

function normalizeSkillName(item) {
  if (typeof item.skill_name === "string") {
    return item.skill_name.trim();
  }

  if (typeof item.skill === "string") {
    return item.skill.trim();
  }

  if (item.skill && typeof item.skill === "object") {
    return item.skill.name || "";
  }

  return "";
}

function SkillAnalysis() {
  const [skills, setSkills] = useState([]);
  const [history, setHistory] = useState([]);

  const [loading, setLoading] = useState(true);
  const [loadError, setLoadError] = useState("");

  const [selectedSkill, setSelectedSkill] = useState("All");

  const [toast, setToast] = useState({
    message: "",
    type: "success",
  });

  function showToast(message, type = "success") {
    setToast({ message, type });
  }

  function closeToast() {
    setToast({ message: "", type: "success" });
  }

  // =====================================================
  // LOAD SKILLS AND ASSESSMENT HISTORY
  // =====================================================

  async function loadAnalysisData() {
    setLoading(true);
    setLoadError("");

    try {
      const token = localStorage.getItem("skillsphere_access");

      if (!token) {
        throw new Error(
          "Your login session was not found. Please log in again."
        );
      }

      const [skillsResponse, historyResponse] = await Promise.all([
        fetch(`${API_BASE_URL}/api/skills/`),

        fetch(`${API_BASE_URL}/api/skills/assessments/`, {
          method: "GET",
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        }),
      ]);

      if (!skillsResponse.ok) {
        throw new Error(
          `Unable to load skills. Server returned ${skillsResponse.status}.`
        );
      }

      if (historyResponse.status === 401 || historyResponse.status === 403) {
        throw new Error(
          "Your session may have expired. Please log in again."
        );
      }

      if (!historyResponse.ok) {
        throw new Error(
          `Unable to load assessment results. Server returned ${historyResponse.status}.`
        );
      }

      const skillsData = await skillsResponse.json();
      const historyData = await historyResponse.json();

      // Dynamic active skills from Django.
      const activeSkills = Array.isArray(skillsData.skills)
        ? skillsData.skills.filter((skill) => {
            const name = String(skill.name || "").trim().toLowerCase();

            return (
              skill.is_active &&
              name &&
              !EXCLUDED_SKILLS.includes(name)
            );
          })
        : [];

      // Backend assessment history response.
      const resultItems = Array.isArray(historyData)
        ? historyData
        : Array.isArray(historyData.assessments)
          ? historyData.assessments
          : Array.isArray(historyData.results)
            ? historyData.results
            : [];

      const normalizedHistory = resultItems
        .map((item) => {
          const skillName = normalizeSkillName(item);
          const score = Number(item.score ?? 0);
          const totalQuestions = Number(item.total_questions ?? 0);

          const percentage =
            item.percentage !== null &&
            item.percentage !== undefined &&
            item.percentage !== ""
              ? Number(item.percentage)
              : totalQuestions > 0
                ? Math.round((score / totalQuestions) * 100)
                : NaN;

          return {
            id: item.id,
            skill: skillName,
            percentage,
            correctAnswers: score,
            totalQuestions,
            completedAt: item.completed_at || "",
            date: formatDate(item.completed_at),
          };
        })
        .filter(
          (item) =>
            item.skill &&
            Number.isFinite(item.percentage) &&
            item.percentage >= 0 &&
            item.percentage <= 100
        )
        .sort((a, b) => {
          const dateA = new Date(a.completedAt).getTime() || 0;
          const dateB = new Date(b.completedAt).getTime() || 0;
          return dateB - dateA;
        });

      setSkills(activeSkills);
      setHistory(normalizedHistory);
    } catch (error) {
      console.error("Skill Analysis loading error:", error);
      setLoadError(error.message || "Unable to load skill analysis.");
      setSkills([]);
      setHistory([]);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadAnalysisData();

    function handleWindowFocus() {
      loadAnalysisData();
    }

    window.addEventListener("focus", handleWindowFocus);

    return () => {
      window.removeEventListener("focus", handleWindowFocus);
    };
  }, []);

  // =====================================================
  // VALID HISTORY
  // =====================================================

  const validHistory = useMemo(() => {
    return history.filter(
      (item) =>
        item &&
        Number.isFinite(Number(item.percentage)) &&
        Number(item.percentage) >= 0 &&
        Number(item.percentage) <= 100
    );
  }, [history]);

  // =====================================================
  // SKILL SUMMARIES
  // =====================================================

  const skillSummaries = useMemo(() => {
    return skills.map((skill) => {
      const attempts = validHistory.filter(
        (item) =>
          item.skill.toLowerCase() === skill.name.toLowerCase()
      );

      const latest = attempts[0] || null;
      const previous = attempts[1] || null;

      const average = attempts.length
        ? Math.round(
            attempts.reduce(
              (sum, item) => sum + item.percentage,
              0
            ) / attempts.length
          )
        : null;

      const change =
        latest && previous
          ? latest.percentage - previous.percentage
          : null;

      return {
        ...skill,
        short: getSkillShortName(skill.name),
        color: getSkillColor(skill.name),
        description:
          skill.description || "Skill assessment and development",
        attempts,
        latest,
        previous,
        average,
        change,
        level: latest
          ? getLevel(latest.percentage)
          : "Not assessed",
      };
    });
  }, [skills, validHistory]);

  const assessedSkills = skillSummaries.filter(
    (skill) => skill.latest
  );

  const overallAverage = assessedSkills.length
    ? Math.round(
        assessedSkills.reduce(
          (sum, skill) => sum + skill.latest.percentage,
          0
        ) / assessedSkills.length
      )
    : null;

  const totalAttempts = validHistory.length;

  const filteredHistory =
    selectedSkill === "All"
      ? validHistory
      : validHistory.filter(
          (item) => item.skill === selectedSkill
        );

  const strongestSkill = [...assessedSkills].sort(
    (a, b) => b.latest.percentage - a.latest.percentage
  )[0];

  const improvementSkill = [...assessedSkills]
    .filter((skill) => skill.change !== null)
    .sort((a, b) => b.change - a.change)[0];

  const needsPractice = [...assessedSkills].sort(
    (a, b) => a.latest.percentage - b.latest.percentage
  )[0];

  function handleSkillFilterChange(value) {
    setSelectedSkill(value);

    showToast(
      value === "All"
        ? "Showing assessment history for all skills."
        : `Showing assessment history for ${value}.`,
      "info"
    );
  }

  function getRecommendation(skill) {
    if (!skill.latest) {
      return "Take your first assessment to discover your current level.";
    }

    if (skill.latest.percentage >= 80) {
      return "Practise advanced questions and build a real-world project.";
    }

    if (skill.latest.percentage >= 60) {
      return "Revise incorrect answers and practise intermediate problems.";
    }

    return "Review fundamentals and practise basic problems before retaking.";
  }

  // =====================================================
  // UI
  // =====================================================

  return (
    <div className="skill-analysis-page">
      <Toast
        message={toast.message}
        type={toast.type}
        onClose={closeToast}
      />

      <header className="analysis-header">
        <div>
          <span className="analysis-eyebrow">
            MEASURE · UNDERSTAND · IMPROVE
          </span>

          <h1>Skill Analysis</h1>

          <p>
            Understand your assessment performance and decide what to learn
            next.
          </p>
        </div>

        <div className="analysis-header-icon" aria-hidden="true">
          <span>↗</span>
        </div>
      </header>

      <section className="analysis-summary-grid">
        <article className="analysis-summary-card">
          <div className="analysis-summary-icon blue">%</div>
          <span className="analysis-summary-label">Overall score</span>

          <strong className="analysis-summary-value">
            {overallAverage === null ? "—" : `${overallAverage}%`}
          </strong>

          <small>Average of latest assessed skills</small>
        </article>

        <article className="analysis-summary-card">
          <div className="analysis-summary-icon purple">✓</div>
          <span className="analysis-summary-label">Skills assessed</span>

          <strong className="analysis-summary-value">
            {assessedSkills.length}/{skills.length}
          </strong>

          <small>Subjects with assessment results</small>
        </article>

        <article className="analysis-summary-card">
          <div className="analysis-summary-icon green">↻</div>
          <span className="analysis-summary-label">Total attempts</span>

          <strong className="analysis-summary-value">
            {totalAttempts}
          </strong>

          <small>Saved assessment results</small>
        </article>
      </section>

      {loading ? (
        <section className="analysis-empty-card">
          <div className="analysis-empty-icon">↻</div>
          <h2>Loading your skill analysis</h2>
          <p>Fetching your saved assessment results from the server.</p>
        </section>
      ) : loadError ? (
        <section className="analysis-empty-card">
          <div className="analysis-empty-icon">!</div>
          <h2>Unable to load assessment results</h2>
          <p>{loadError}</p>

          <button
            type="button"
            onClick={loadAnalysisData}
          >
            Try again
          </button>
        </section>
      ) : validHistory.length === 0 ? (
        <section className="analysis-empty-card">
          <div className="analysis-empty-icon">▤</div>
          <h2>Your skill analysis starts here</h2>

          <p>
            You haven't completed an assessment yet. Finish a Skill
            Assessment to see your actual scores, skill levels, and
            learning recommendations.
          </p>

          <div className="analysis-empty-note">
            Your analysis will update using saved assessment results.
          </div>
        </section>
      ) : (
        <>
          <section className="analysis-panel">
            <div className="analysis-panel-heading">
              <div>
                <h2>Skill performance</h2>
                <p>Your latest result for each subject.</p>
              </div>

              <span className="analysis-neutral-badge">
                {assessedSkills.length} assessed
              </span>
            </div>

            <div className="analysis-skill-list">
              {skillSummaries.map((skill) => (
                <article
                  className="analysis-skill-row"
                  key={skill.id}
                >
                  <div
                    className={`analysis-skill-icon ${skill.color}`}
                    aria-hidden="true"
                  >
                    {skill.short}
                  </div>

                  <div className="analysis-skill-main">
                    <div className="analysis-skill-title-row">
                      <div>
                        <h3>{skill.name}</h3>
                        <p>{skill.description}</p>
                      </div>

                      {skill.latest ? (
                        <span
                          className={`analysis-level-badge ${getLevelClass(
                            skill.level
                          )}`}
                        >
                          {skill.level}
                        </span>
                      ) : (
                        <span className="analysis-not-assessed">
                          Not assessed
                        </span>
                      )}
                    </div>

                    <div className="analysis-bar-track">
                      <div
                        className={`analysis-bar-fill ${skill.color}`}
                        style={{
                          width: `${skill.latest?.percentage ?? 0}%`,
                        }}
                      />
                    </div>

                    <div className="analysis-skill-meta">
                      <span>
                        {skill.latest
                          ? `${skill.latest.percentage}% latest score`
                          : "Complete an assessment to get a score"}
                      </span>

                      <span>
                        {skill.attempts.length}{" "}
                        {skill.attempts.length === 1
                          ? "attempt"
                          : "attempts"}
                      </span>
                    </div>
                  </div>
                </article>
              ))}
            </div>
          </section>

          <section className="analysis-insights-grid">
            <article className="analysis-insight-card">
              <span className="analysis-insight-label">
                STRONGEST SKILL
              </span>

              {strongestSkill ? (
                <>
                  <div className="analysis-insight-heading">
                    <h3>{strongestSkill.name}</h3>
                    <span className="analysis-insight-score">
                      {strongestSkill.latest.percentage}%
                    </span>
                  </div>

                  <p>
                    Your highest latest assessment score is in{" "}
                    {strongestSkill.name}.
                  </p>
                </>
              ) : (
                <p>
                  Complete an assessment to discover your strongest skill.
                </p>
              )}
            </article>

            <article className="analysis-insight-card">
              <span className="analysis-insight-label">
                BIGGEST SCORE IMPROVEMENT
              </span>

              {improvementSkill ? (
                <>
                  <div className="analysis-insight-heading">
                    <h3>{improvementSkill.name}</h3>

                    <span
                      className={`analysis-change ${
                        improvementSkill.change > 0
                          ? "positive"
                          : improvementSkill.change < 0
                            ? "negative"
                            : ""
                      }`}
                    >
                      {improvementSkill.change > 0 ? "+" : ""}
                      {improvementSkill.change}%
                    </span>
                  </div>

                  <p>
                    Compared with the previous saved attempt in this subject.
                  </p>
                </>
              ) : (
                <p>
                  Take another assessment in the same subject to compare
                  scores.
                </p>
              )}
            </article>
          </section>

          <section className="analysis-panel">
            <div className="analysis-panel-heading">
              <div>
                <h2>Learning recommendations</h2>
                <p>Suggested next steps based on your latest scores.</p>
              </div>
            </div>

            <div className="analysis-recommendation-list">
              {skillSummaries.map((skill) => (
                <article
                  className="analysis-recommendation"
                  key={skill.id}
                >
                  <div
                    className={`analysis-recommendation-icon ${skill.color}`}
                  >
                    {skill.short}
                  </div>

                  <div className="analysis-recommendation-content">
                    <h3>{skill.name}</h3>
                    <p>{getRecommendation(skill)}</p>
                  </div>

                  {skill.latest && (
                    <span className="analysis-recommendation-score">
                      {skill.latest.percentage}%
                    </span>
                  )}
                </article>
              ))}
            </div>

            {needsPractice && (
              <div className="analysis-priority-note">
                <span className="analysis-priority-icon">!</span>

                <div>
                  <strong>Suggested practice priority</strong>

                  <p>
                    Focus on {needsPractice.name} next because it currently
                    has your lowest latest score among assessed subjects.
                  </p>
                </div>
              </div>
            )}
          </section>

          <section className="analysis-panel">
            <div className="analysis-panel-heading analysis-history-heading">
              <div>
                <h2>Assessment history</h2>
                <p>Review scores from your previous attempts.</p>
              </div>

              <select
                className="analysis-filter"
                value={selectedSkill}
                onChange={(event) =>
                  handleSkillFilterChange(event.target.value)
                }
                aria-label="Filter assessment history by skill"
              >
                <option value="All">All skills</option>

                {skills.map((skill) => (
                  <option key={skill.id} value={skill.name}>
                    {skill.name}
                  </option>
                ))}
              </select>
            </div>

            {filteredHistory.length === 0 ? (
              <div className="analysis-filter-empty">
                No assessment history is available for this skill.
              </div>
            ) : (
              <div className="analysis-history-list">
                {filteredHistory.map((item, index) => {
                  const level = getLevel(item.percentage);
                  const color = getSkillColor(item.skill);

                  return (
                    <article
                      className="analysis-history-row"
                      key={
                        item.id ||
                        `${item.skill}-${item.date}-${index}`
                      }
                    >
                      <div
                        className={`analysis-history-icon ${color}`}
                      >
                        {getSkillShortName(item.skill)}
                      </div>

                      <div className="analysis-history-details">
                        <strong>{item.skill} Assessment</strong>
                        <span>{item.date}</span>
                      </div>

                      <div className="analysis-history-score">
                        <strong>{item.percentage}%</strong>

                        <span>
                          {item.correctAnswers}/{item.totalQuestions} correct
                        </span>
                      </div>

                      <span
                        className={`analysis-level-badge ${getLevelClass(
                          level
                        )}`}
                      >
                        {level}
                      </span>
                    </article>
                  );
                })}
              </div>
            )}
          </section>
        </>
      )}

      <div className="analysis-footer-note">
        <span>i</span>
        Analysis is based on assessment results saved to your account. It
        refreshes from the server when this page opens or regains focus.
      </div>
    </div>
  );
}

export default SkillAnalysis;
