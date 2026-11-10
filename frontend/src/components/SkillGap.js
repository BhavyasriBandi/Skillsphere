import React, { useEffect, useMemo, useState } from "react";
import Toast from "./Toast";
import "./SkillGap.css";

const API_BASE = "https://skillsphere-u93o.onrender.com/api/skills/";
const SKILLS_API = API_BASE;
const ASSESSMENT_API = `${API_BASE}assessments/`;
const PROGRESS_API = `${API_BASE}progress/`;

const TOKEN_KEY = "skillsphere_access";
const CAREER_GOAL_KEY = "skillsphere_student_career_goal";
const ASSESSMENT_KEY = "skillsphere_assessment_history";
const SKILL_GAP_KEY = "skillsphere_student_skill_gap";

const EXCLUDED_SKILLS = [
  "object-oriented programming",
  "testing & debugging",
];

const CAREERS = {
  "Full Stack Developer":
    "Build complete web applications using frontend and backend technologies.",
  "Python Developer":
    "Develop applications, automation tools, and backend services.",
  "Java Developer":
    "Create reliable applications using Java and backend technologies.",
  "Data Analyst":
    "Turn data into useful insights using queries and analysis.",
  "AI / Machine Learning Engineer":
    "Build intelligent systems using data and machine learning.",
  "Frontend Developer":
    "Create responsive and interactive user interfaces.",
  "Backend Developer":
    "Design APIs, application logic, and server-side systems.",
};

const DEFAULT_CAREER = "Full Stack Developer";

function getToken() {
  return localStorage.getItem(TOKEN_KEY);
}

function readJSON(key, fallback) {
  try {
    const value = localStorage.getItem(key);
    return value ? JSON.parse(value) : fallback;
  } catch {
    return fallback;
  }
}

function readSavedProgress() {
  const saved = readJSON(SKILL_GAP_KEY, {});
  return saved && typeof saved === "object" && !Array.isArray(saved)
    ? saved
    : {};
}

function normalizeCareer(value) {
  if (typeof value !== "string") return "";

  const name = value.trim().toLowerCase();

  const aliases = {
    "full stack": "Full Stack Developer",
    "full-stack developer": "Full Stack Developer",
    fullstack: "Full Stack Developer",
    python: "Python Developer",
    java: "Java Developer",
    "data analytics": "Data Analyst",
    "data analysis": "Data Analyst",
    frontend: "Frontend Developer",
    "front-end developer": "Frontend Developer",
    backend: "Backend Developer",
    "back-end developer": "Backend Developer",
    "machine learning engineer": "AI / Machine Learning Engineer",
    "ai engineer": "AI / Machine Learning Engineer",
  };

  if (aliases[name]) return aliases[name];

  return (
    Object.keys(CAREERS).find(
      (career) => career.toLowerCase() === name
    ) || ""
  );
}

function getCareerFromGoal(goal) {
  if (!goal || typeof goal !== "object") return "";

  const values = [
    goal.role,
    goal.career,
    goal.careerGoal,
    goal.targetRole,
    goal.targetCareer,
    goal.goal,
    goal.title,
  ];

  for (const value of values) {
    const career = normalizeCareer(value);
    if (career) return career;
  }

  return "";
}

function normalizeSkillName(name) {
  return String(name || "")
    .toLowerCase()
    .trim()
    .replace(/[._/&+-]/g, " ")
    .replace(/\s+/g, " ");
}

function getAssessmentSkill(name) {
  const normalized = normalizeSkillName(name);

  const aliases = {
    python: "python",
    java: "java",
    "c programming": "c programming",
    c: "c programming",
    "sql databases": "sql databases",
    sql: "sql databases",
    "django rest apis": "django rest apis",
    django: "django rest apis",
    "git github": "git github",
    "data structures": "data structures",
    "web technologies": "web technologies",
  };

  return aliases[normalized] || normalized;
}

function getAssessmentName(item) {
  if (!item || typeof item !== "object") return "";

  if (typeof item.skill_name === "string") {
    return item.skill_name;
  }

  if (typeof item.skill === "string") {
    return item.skill;
  }

  if (item.skill && typeof item.skill === "object") {
    return item.skill.name || item.skill.skill_name || "";
  }

  return "";
}

function getAssessmentPercentage(item) {
  if (!item || typeof item !== "object") return null;

  let percentage = Number(item.percentage);

  if (
    item.percentage === null ||
    item.percentage === undefined ||
    item.percentage === ""
  ) {
    const score = Number(item.score);
    const total = Number(item.total_questions);

    if (Number.isFinite(score) && total > 0) {
      percentage = (score / total) * 100;
    }
  }

  if (
    !Number.isFinite(percentage) ||
    percentage < 0 ||
    percentage > 100
  ) {
    return null;
  }

  return percentage;
}

function getLevel(score) {
  if (score >= 80) return "Strong";
  if (score >= 60) return "Developing";
  return "Needs practice";
}

function getPriority(category) {
  const value = String(category || "").toLowerCase();

  if (
    value.includes("programming") ||
    value.includes("backend") ||
    value.includes("database")
  ) {
    return "High";
  }

  return "Medium";
}

function getCategoryName(skill) {
  return skill.category_name || "Other";
}

function getSkillShortName(name) {
  const value = String(name || "").toLowerCase();

  if (value === "python") return "Py";
  if (value === "java") return "Ja";
  if (value.includes("c programming")) return "C";
  if (value.includes("data structures")) return "DS";
  if (value.includes("django")) return "Dj";
  if (value.includes("git")) return "Git";
  if (value.includes("sql")) return "SQL";
  if (value.includes("web")) return "Web";

  return String(name || "").slice(0, 3).toUpperCase();
}

function getAttemptTimestamp(item) {
  if (!item?.completed_at) return 0;

  const value = new Date(item.completed_at).getTime();
  return Number.isFinite(value) ? value : 0;
}

function SkillGap() {
  const [career, setCareer] = useState(DEFAULT_CAREER);

  const [skills, setSkills] = useState([]);
  const [skillsLoading, setSkillsLoading] = useState(true);
  const [skillsError, setSkillsError] = useState("");

  const [completedSkills, setCompletedSkills] = useState(readSavedProgress);
  const [databaseProgress, setDatabaseProgress] = useState({});

  const [categoryFilter, setCategoryFilter] = useState("All");
  const [showCompleted, setShowCompleted] = useState(true);

  const [assessments, setAssessments] = useState([]);
  const [assessmentLoading, setAssessmentLoading] = useState(true);
  const [assessmentError, setAssessmentError] = useState("");

  const [progressLoading, setProgressLoading] = useState(true);
  const [progressError, setProgressError] = useState("");

  const [savingSkills, setSavingSkills] = useState({});

  const [toast, setToast] = useState({
    message: "",
    type: "success",
  });

  function showMessage(message, type = "success") {
    setToast({ message, type });
  }

  function closeToast() {
    setToast({ message: "", type: "success" });
  }

  useEffect(() => {
    if (!toast.message) return undefined;

    const timer = window.setTimeout(closeToast, 3000);
    return () => window.clearTimeout(timer);
  }, [toast.message]);

  // Load saved career goal.
  useEffect(() => {
    const goal = readJSON(CAREER_GOAL_KEY, {});
    const savedCareer = getCareerFromGoal(goal);

    if (savedCareer) setCareer(savedCareer);
  }, []);

  // Load all active skills from Django.
  useEffect(() => {
    let active = true;

    async function loadSkills() {
      setSkillsLoading(true);
      setSkillsError("");

      try {
        const response = await fetch(SKILLS_API);
        const data = await response.json();

        if (!response.ok) {
          throw new Error(
            data.detail || `Unable to load skills (${response.status}).`
          );
        }

        const excluded = EXCLUDED_SKILLS.map(normalizeSkillName);

        const activeSkills = Array.isArray(data.skills)
          ? data.skills.filter((skill) => {
              const name = normalizeSkillName(skill.name);
              return skill.is_active && !excluded.includes(name);
            })
          : [];

        if (active) {
          setSkills(activeSkills);
        }
      } catch (error) {
        console.error("Skill list loading error:", error);

        if (active) {
          setSkills([]);
          setSkillsError(error.message);
        }
      } finally {
        if (active) setSkillsLoading(false);
      }
    }

    loadSkills();

    return () => {
      active = false;
    };
  }, []);

  // Load assessment history from Django.
  // No AbortController here: React StrictMode can run effect cleanup
  // during its development-only setup/cleanup/setup check.
  useEffect(() => {
    let active = true;

    async function loadAssessments() {
      setAssessmentLoading(true);
      setAssessmentError("");

      const token = getToken();

      if (!token) {
        const localHistory = readJSON(ASSESSMENT_KEY, []);

        if (active) {
          setAssessments(
            Array.isArray(localHistory) ? localHistory : []
          );
          setAssessmentError("Please log in to load assessment history.");
          setAssessmentLoading(false);
        }

        return;
      }

      try {
        const response = await fetch(ASSESSMENT_API, {
          headers: {
            Authorization: `Bearer ${token}`,
            Accept: "application/json",
          },
        });

        if (response.status === 401 || response.status === 403) {
          throw new Error(
            "Your login session has expired. Please log in again."
          );
        }

        if (!response.ok) {
          throw new Error(
            `Unable to load assessment history (${response.status}).`
          );
        }

        const data = await response.json();

        const results = Array.isArray(data)
          ? data
          : Array.isArray(data.assessments)
            ? data.assessments
            : Array.isArray(data.results)
              ? data.results
              : [];

        results.sort(
          (a, b) => getAttemptTimestamp(b) - getAttemptTimestamp(a)
        );

        if (!active) return;

        setAssessments(results);

        try {
          localStorage.setItem(
            ASSESSMENT_KEY,
            JSON.stringify(results)
          );
        } catch (storageError) {
          console.warn(
            "Could not cache assessment history:",
            storageError
          );
        }
      } catch (error) {
        if (!active) return;

        console.error("Assessment history error:", error);

        const localHistory = readJSON(ASSESSMENT_KEY, []);
        setAssessments(
          Array.isArray(localHistory) ? localHistory : []
        );
        setAssessmentError(error.message);
      } finally {
        if (active) setAssessmentLoading(false);
      }
    }

    loadAssessments();

    return () => {
      active = false;
    };
  }, []);

  // Load completed skill progress from Django.
  // No AbortController here for the same React StrictMode reason.
  useEffect(() => {
    let active = true;

    async function loadProgress() {
      setProgressLoading(true);
      setProgressError("");

      const token = getToken();

      if (!token) {
        if (active) {
          setProgressError(
            "Please log in to synchronize your progress."
          );
          setProgressLoading(false);
        }
        return;
      }

      try {
        const response = await fetch(PROGRESS_API, {
          headers: {
            Authorization: `Bearer ${token}`,
            Accept: "application/json",
          },
        });

        if (response.status === 401 || response.status === 403) {
          throw new Error("Your login session has expired.");
        }

        if (!response.ok) {
          throw new Error(
            `Unable to load saved progress (${response.status}).`
          );
        }

        const data = await response.json();

        const records = Array.isArray(data)
          ? data
          : Array.isArray(data.results)
            ? data.results
            : Array.isArray(data.progress)
              ? data.progress
              : [];

        const progressMap = {};

        records.forEach((record) => {
          if (record && record.skill_name) {
            progressMap[record.skill_name] = Boolean(
              record.is_completed
            );
          }
        });

        if (active) setDatabaseProgress(progressMap);
      } catch (error) {
        if (!active) return;

        console.error("Progress loading error:", error);
        setProgressError(error.message);
      } finally {
        if (active) setProgressLoading(false);
      }
    }

    loadProgress();

    return () => {
      active = false;
    };
  }, []);

  // Get the latest assessment score for each skill.
  const assessmentScores = useMemo(() => {
    const scores = {};

    assessments.forEach((item) => {
      const name = getAssessmentName(item);
      const percentage = getAssessmentPercentage(item);

      if (!name || percentage === null) return;

      const normalized = getAssessmentSkill(name);

      if (!scores[normalized]) {
        scores[normalized] = {
          score: percentage,
          completedAt: item.completed_at || null,
        };
      }
    });

    return scores;
  }, [assessments]);

  // Use exactly the same skills returned by the Skill Assessment API.
  const careerProgress = completedSkills[career] || {};

  const skillItems = skills.map((skill) => {
    const name = skill.name;
    const assessmentKey = getAssessmentSkill(name);
    const assessment = assessmentScores[assessmentKey];

    const localCompleted = Boolean(careerProgress[name]);
    const remoteCompleted = Boolean(databaseProgress[name]);

    const completed =
      localCompleted ||
      remoteCompleted ||
      Boolean(assessment && assessment.score >= 80);

    let source = "Not yet confirmed";

    if (assessment && assessment.score >= 80) {
      source = "Assessment score ≥ 80%";
    } else if (remoteCompleted) {
      source = "Saved to Django";
    } else if (localCompleted) {
      source = "Marked as learned in this browser";
    } else if (assessment) {
      source = "Assessment indicates more practice is needed";
    }

    return {
      ...skill,
      category: getCategoryName(skill),
      priority: getPriority(getCategoryName(skill)),
      short: getSkillShortName(name),
      completed,
      assessmentScore: assessment ? assessment.score : null,
      level: assessment ? getLevel(assessment.score) : "Not assessed",
      source,
    };
  });

  const categories = [
    "All",
    ...new Set(skillItems.map((skill) => skill.category)),
  ];

  const visibleSkills = skillItems.filter((skill) => {
    const categoryMatches =
      categoryFilter === "All" || skill.category === categoryFilter;

    return categoryMatches && (showCompleted || !skill.completed);
  });

  const completedCount = skillItems.filter(
    (skill) => skill.completed
  ).length;

  const remainingCount = skillItems.length - completedCount;

  const progress = skillItems.length
    ? Math.round((completedCount / skillItems.length) * 100)
    : 0;

  const highPriorityGaps = skillItems.filter(
    (skill) => !skill.completed && skill.priority === "High"
  );

  function changeCareer(event) {
    const nextCareer = event.target.value;

    setCareer(nextCareer);
    setCategoryFilter("All");

    showMessage(`Career changed to ${nextCareer}.`, "info");
  }

  // Save checklist progress in browser and Django.
  async function toggleSkill(skillName) {
    if (savingSkills[skillName]) return;

    const currentProgress = readSavedProgress();
    const currentCareerProgress = currentProgress[career] || {};

    const nextValue = !Boolean(
      currentCareerProgress[skillName] ||
      databaseProgress[skillName] ||
      assessmentScores[getAssessmentSkill(skillName)]?.score >= 80
    );

    const updatedProgress = {
      ...currentProgress,
      [career]: {
        ...currentCareerProgress,
        [skillName]: nextValue,
      },
    };

    try {
      localStorage.setItem(
        SKILL_GAP_KEY,
        JSON.stringify(updatedProgress)
      );

      setCompletedSkills(updatedProgress);
    } catch (error) {
      console.error("Local progress save error:", error);
      showMessage(
        "Unable to save progress in this browser.",
        "error"
      );
      return;
    }

    const token = getToken();

    if (!token) {
      showMessage("Progress saved in this browser.", "info");
      return;
    }

    setSavingSkills((previous) => ({
      ...previous,
      [skillName]: true,
    }));

    try {
      const response = await fetch(PROGRESS_API, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
          Accept: "application/json",
        },
        body: JSON.stringify({
          skill_name: skillName,
          is_completed: nextValue,
        }),
      });

      if (!response.ok) {
        let errorMessage = "";

        try {
          const errorData = await response.json();
          errorMessage =
            errorData.detail ||
            errorData.skill_name?.[0] ||
            errorData.is_completed?.[0] ||
            "";
        } catch {
          // Ignore non-JSON response.
        }

        throw new Error(
          errorMessage ||
            `Progress save failed (${response.status}).`
        );
      }

      const savedRecord = await response.json();

      setDatabaseProgress((previous) => ({
        ...previous,
        [skillName]:
          typeof savedRecord.is_completed === "boolean"
            ? savedRecord.is_completed
            : nextValue,
      }));

      showMessage(
        nextValue
          ? `${skillName} marked as covered.`
          : `${skillName} marked as not covered.`,
        "success"
      );
    } catch (error) {
      console.error("Django progress save error:", error);

      showMessage(
        `Saved locally, but Django sync failed: ${error.message}`,
        "error"
      );
    } finally {
      setSavingSkills((previous) => ({
        ...previous,
        [skillName]: false,
      }));
    }
  }

  return (
    <div className="skill-gap-page">
      <Toast
        message={toast.message}
        type={toast.type}
        onClose={closeToast}
      />

      <header className="skill-gap-header">
        <div>
          <span className="skill-gap-eyebrow">
            IDENTIFY · PRIORITIZE · GROW
          </span>

          <h1>Skill Gap Analysis</h1>

          <p>
            Compare your current skills with your target career and build a
            focused learning plan.
          </p>
        </div>

        <div className="skill-gap-header-art" aria-hidden="true">
          <span className="gap-art-line" />
          <span className="gap-art-circle">↗</span>
        </div>
      </header>

      {(assessmentError || progressError || skillsError) && (
        <div className="skill-gap-toast" role="status">
          <span>i</span>
          {skillsError || assessmentError || progressError}
        </div>
      )}

      <section className="skill-gap-career-card">
        <div className="skill-gap-career-top">
          <div>
            <span className="skill-gap-section-label">
              YOUR TARGET CAREER
            </span>

            <h2>{career}</h2>

            <p>{CAREERS[career] || CAREERS[DEFAULT_CAREER]}</p>
          </div>

          <div className="skill-gap-career-symbol" aria-hidden="true">
            ✦
          </div>
        </div>

        <label
          className="skill-gap-career-label"
          htmlFor="gap-career-select"
        >
          Explore another career
        </label>

        <select
          id="gap-career-select"
          className="skill-gap-career-select"
          value={career}
          onChange={changeCareer}
        >
          {Object.keys(CAREERS).map((name) => (
            <option key={name} value={name}>
              {name}
            </option>
          ))}
        </select>

        <p className="skill-gap-career-help">
          The same active skills are displayed for every career. Your checklist
          progress is maintained separately for each career.
        </p>
      </section>

      <section className="skill-gap-metrics">
        <article className="skill-gap-metric">
          <span className="skill-gap-metric-icon blue">✓</span>

          <div>
            <span>Skills covered</span>
            <strong>
              {completedCount}
              <small> / {skillItems.length}</small>
            </strong>
          </div>
        </article>

        <article className="skill-gap-metric">
          <span className="skill-gap-metric-icon orange">◎</span>

          <div>
            <span>Skills to develop</span>
            <strong>{remainingCount}</strong>
          </div>
        </article>

        <article className="skill-gap-metric">
          <span className="skill-gap-metric-icon purple">↗</span>

          <div>
            <span>Coverage</span>
            <strong>{progress}%</strong>
          </div>
        </article>
      </section>

      <section className="skill-gap-panel skill-gap-progress-panel">
        <div className="skill-gap-panel-heading">
          <div>
            <h2>Your career readiness checklist</h2>

            <p>
              Mark a skill as learned when you feel confident using it in
              practice.
            </p>
          </div>

          <span className="skill-gap-progress-number">{progress}%</span>
        </div>

        <div
          className="skill-gap-progress-track"
          role="progressbar"
          aria-label="Career skill coverage"
          aria-valuemin={0}
          aria-valuemax={100}
          aria-valuenow={progress}
        >
          <div
            className="skill-gap-progress-fill"
            style={{ width: `${progress}%` }}
          />
        </div>

        <div className="skill-gap-progress-legend">
          <span>
            <i className="gap-dot gap-dot-covered" />
            Covered: {completedCount}
          </span>

          <span>
            <i className="gap-dot gap-dot-missing" />
            To learn: {remainingCount}
          </span>
        </div>
      </section>

      <section className="skill-gap-panel">
        <div className="skill-gap-panel-heading">
          <div>
            <h2>Required skills</h2>

            <p>
              These are the same active courses available in Skill Assessment.
              {skillsLoading ? " Loading skills..." : ""}
              {assessmentLoading ? " Loading assessment results..." : ""}
              {progressLoading ? " Loading saved progress..." : ""}
            </p>
          </div>
        </div>

        <div className="skill-gap-filters">
          <div className="skill-gap-category-filters">
            {categories.map((category) => (
              <button
                type="button"
                key={category}
                className={`skill-gap-filter ${
                  categoryFilter === category ? "active" : ""
                }`}
                onClick={() => setCategoryFilter(category)}
              >
                {category}
              </button>
            ))}
          </div>

          <label className="skill-gap-show-toggle">
            <input
              type="checkbox"
              checked={showCompleted}
              onChange={(event) => setShowCompleted(event.target.checked)}
            />

            Show covered skills
          </label>
        </div>

        <div className="skill-gap-skill-list">
          {skillsLoading ? (
            <p>Loading skills from SkillSphere...</p>
          ) : visibleSkills.length === 0 ? (
            <div className="skill-gap-filter-empty">
              No skills match these filters.
            </div>
          ) : (
            visibleSkills.map((skill, index) => (
              <article
                key={skill.id}
                className={`skill-gap-skill-item ${
                  skill.completed ? "is-covered" : ""
                }`}
              >
                <div className="skill-gap-skill-number">
                  {String(index + 1).padStart(2, "0")}
                </div>

                <div className="skill-gap-skill-info">
                  <div className="skill-gap-skill-title">
                    <h3>{skill.name}</h3>

                    <span
                      className={`skill-gap-priority ${
                        skill.priority === "High"
                          ? "priority-high"
                          : "priority-medium"
                      }`}
                    >
                      {skill.priority} priority
                    </span>
                  </div>

                  <div className="skill-gap-skill-meta">
                    <span>{skill.category}</span>

                    <span className="skill-gap-meta-divider">•</span>

                    <span>
                      {skill.assessmentScore !== null
                        ? `Assessment: ${skill.assessmentScore}% · ${skill.level}`
                        : assessmentLoading
                          ? "Loading assessment..."
                          : "No matching assessment score"}
                    </span>
                  </div>

                  <span className="skill-gap-source">
                    {savingSkills[skill.name]
                      ? "Saving to Django..."
                      : skill.source}
                  </span>
                </div>

                <label className="skill-gap-complete-control">
                  <input
                    type="checkbox"
                    checked={skill.completed}
                    disabled={Boolean(savingSkills[skill.name])}
                    onChange={() => toggleSkill(skill.name)}
                    aria-label={`Mark ${skill.name} as learned`}
                  />

                  <span>
                    {savingSkills[skill.name]
                      ? "Saving..."
                      : skill.completed
                        ? "Covered"
                        : "Mark learned"}
                  </span>
                </label>
              </article>
            ))
          )}
        </div>

        <p className="skill-gap-disclaimer">
          Checklist progress is self-reported. Assessment scores of 80% or
          above also count as covered.
        </p>
      </section>

      <section className="skill-gap-panel">
        <div className="skill-gap-panel-heading">
          <div>
            <h2>Your next learning priorities</h2>
            <p>Start with uncovered high-priority requirements.</p>
          </div>

          <span className="skill-gap-priority-count">
            {highPriorityGaps.length} remaining
          </span>
        </div>

        {highPriorityGaps.length > 0 ? (
          <div className="skill-gap-priority-list">
            {highPriorityGaps.slice(0, 3).map((skill, index) => (
              <div className="skill-gap-priority-item" key={skill.id}>
                <span className="skill-gap-priority-step">
                  {index + 1}
                </span>

                <div>
                  <strong>{skill.name}</strong>

                  <p>
                    Review the fundamentals, practise exercises, and build a
                    small project to apply this skill.
                  </p>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="skill-gap-all-covered">
            <span>✓</span>

            <div>
              <strong>
                All high-priority checklist skills are covered!
              </strong>

              <p>
                Continue practising and demonstrate your knowledge through
                projects.
              </p>
            </div>
          </div>
        )}
      </section>

      <footer className="skill-gap-footer">
        <span>i</span>

        Skill list and assessment results are loaded from Django.
        Browser storage is used as a local checklist fallback.
      </footer>
    </div>
  );
}

export default SkillGap;