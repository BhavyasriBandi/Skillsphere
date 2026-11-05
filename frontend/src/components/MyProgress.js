
import React, { useEffect, useMemo, useState } from "react";
import "./MyProgress.css";
import { showToast } from "../components/ToastProvider";

const API_URL = "http://127.0.0.1:8000/api/careers/roadmap-progress/";

const STORAGE_KEYS = {
  assessments: "skillsphere_assessment_history",
  skillGap: "skillsphere_student_skill_gap",
  roadmap: "skillsphere_student_roadmap_progress",
  challenges: "skillsphere_challenges_progress",
  learning: "skillsphere_learning_hub_progress",
  projects: "skillsphere_student_projects",
  interview: "skillsphere_interview_prep_progress",
  careerGoal: "skillsphere_student_career_goal",
};

const ACCESS_TOKEN_KEYS = [
  "skillsphere_access",
  "access",
  "access_token",
  "accessToken",
];

function readStorage(key, fallback = null) {
  try {
    const value = localStorage.getItem(key);
    return value ? JSON.parse(value) : fallback;
  } catch {
    return fallback;
  }
}

// Read the access token using the same key as SkillSphere AuthContext.
function getAccessToken() {
  for (const key of ACCESS_TOKEN_KEYS) {
    const value = localStorage.getItem(key);

    if (value && value.trim()) {
      return value.trim().replace(/^Bearer\s+/i, "");
    }
  }

  try {
    const tokens = JSON.parse(localStorage.getItem("tokens") || "{}");

    if (tokens.access) {
      return String(tokens.access)
        .trim()
        .replace(/^Bearer\s+/i, "");
    }
  } catch (error) {
    console.error("Unable to read stored tokens:", error);
  }

  return "";
}

function countCompleted(value) {
  if (value === true) return 1;

  if (Array.isArray(value)) {
    return value.reduce(
      (total, item) => total + countCompleted(item),
      0
    );
  }

  if (value && typeof value === "object") {
    let total = 0;

    Object.entries(value).forEach(([key, item]) => {
      const normalizedKey = key.toLowerCase();

      if (
        [
          "completed",
          "iscompleted",
          "practiced",
          "ispracticed",
          "done",
        ].includes(normalizedKey)
      ) {
        if (item === true) total += 1;
      } else if (item && typeof item === "object") {
        total += countCompleted(item);
      }
    });

    return total;
  }

  return 0;
}

function getPercentage(value) {
  const number = Number(value);

  return Number.isFinite(number)
    ? Math.max(0, Math.min(100, Math.round(number)))
    : 0;
}

function getInitialData(roadmapCompletedOverride = null) {
  const history = readStorage(STORAGE_KEYS.assessments, []);
  const validHistory = Array.isArray(history) ? history : [];

  const averageScore = validHistory.length
    ? Math.round(
        validHistory.reduce(
          (total, item) => total + getPercentage(item.percentage),
          0
        ) / validHistory.length
      )
    : 0;

  const projects = readStorage(STORAGE_KEYS.projects, []);
  const projectCount = Array.isArray(projects) ? projects.length : 0;

  const roadmapData = readStorage(STORAGE_KEYS.roadmap, {});
  const challengeData = readStorage(STORAGE_KEYS.challenges, {});
  const learningData = readStorage(STORAGE_KEYS.learning, {});
  const interviewData = readStorage(STORAGE_KEYS.interview, {});
  const skillGapData = readStorage(STORAGE_KEYS.skillGap, {});
  const careerGoal = readStorage(STORAGE_KEYS.careerGoal, null);

  const roadmapCompleted =
    roadmapCompletedOverride === null
      ? countCompleted(roadmapData)
      : roadmapCompletedOverride;

  const challengesCompleted = countCompleted(challengeData);
  const lessonsCompleted = countCompleted(learningData);
  const interviewPractised = countCompleted(interviewData);
  const skillGapCompleted = countCompleted(skillGapData);

  const activityTotal =
    validHistory.length +
    challengesCompleted +
    lessonsCompleted +
    interviewPractised +
    projectCount;

  const activityScore = Math.min(
    100,
    Math.round(
      (validHistory.length * 10 +
        challengesCompleted * 5 +
        lessonsCompleted * 5 +
        interviewPractised * 5 +
        projectCount * 10) /
        2
    )
  );

  return {
    assessmentCount: validHistory.length,
    averageScore,
    latestAssessment: validHistory[0] || null,
    projectCount,
    roadmapCompleted,
    challengesCompleted,
    lessonsCompleted,
    interviewPractised,
    skillGapCompleted,
    hasCareerGoal: Boolean(careerGoal),
    activityTotal,
    activityScore,
  };
}

function ProgressBar({ value, color = "blue" }) {
  return (
    <div className="mp-progress-track">
      <div
        className={`mp-progress-fill mp-fill-${color}`}
        style={{ width: `${getPercentage(value)}%` }}
      />
    </div>
  );
}

function StatCard({ icon, label, value, caption, color }) {
  return (
    <article className="mp-stat-card">
      <div className={`mp-stat-icon mp-icon-${color}`}>{icon}</div>

      <div className="mp-stat-content">
        <p>{label}</p>
        <h3>{value}</h3>
        <span>{caption}</span>
      </div>
    </article>
  );
}

function MyProgress() {
  const [progress, setProgress] = useState(getInitialData);
  const [lastUpdated, setLastUpdated] = useState(new Date());
  const [roadmapSynced, setRoadmapSynced] = useState(false);

  useEffect(() => {
    let isMounted = true;
    let requestInProgress = false;

    const refreshProgress = async (showMessage = false) => {
      if (requestInProgress) return;

      requestInProgress = true;

      setProgress(getInitialData());

      const token = getAccessToken();

      if (!token) {
        if (isMounted) {
          setRoadmapSynced(false);
          setLastUpdated(new Date());
        }

        requestInProgress = false;
        return;
      }

      try {
        const response = await fetch(API_URL, {
          method: "GET",
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        });

        if (response.status === 401) {
          console.error(
            "Roadmap API returned 401. The stored access token was rejected."
          );

          if (isMounted) {
            setRoadmapSynced(false);
            setLastUpdated(new Date());
          }

          return;
        }

        if (!response.ok) {
          throw new Error(
            `Roadmap API request failed with status ${response.status}`
          );
        }

        const responseData = await response.json();

        const roadmapRecords = Array.isArray(responseData)
          ? responseData
          : Array.isArray(responseData.results)
            ? responseData.results
            : [];

        const completedCount = roadmapRecords.filter(
          (item) =>
            item.is_completed === true ||
            item.is_completed === 1 ||
            item.is_completed === "true"
        ).length;

        if (!isMounted) return;

        setProgress(getInitialData(completedCount));
        setRoadmapSynced(true);
        setLastUpdated(new Date());

        if (showMessage) {
          showToast(
            "Your learning progress has been refreshed.",
            "success"
          );
        }
      } catch (error) {
        console.error("Unable to load roadmap progress:", error);

        if (isMounted) {
          setProgress(getInitialData());
          setRoadmapSynced(false);
          setLastUpdated(new Date());
        }
      } finally {
        requestInProgress = false;
      }
    };

    const handleStorageChange = (event) => {
      if (
        event.key === null ||
        Object.values(STORAGE_KEYS).includes(event.key) ||
        ACCESS_TOKEN_KEYS.includes(event.key) ||
        event.key === "tokens"
      ) {
        refreshProgress(true);
      }
    };

    const handleFocus = () => {
      refreshProgress();
    };

    refreshProgress();

    window.addEventListener("storage", handleStorageChange);
    window.addEventListener("focus", handleFocus);

    return () => {
      isMounted = false;
      window.removeEventListener("storage", handleStorageChange);
      window.removeEventListener("focus", handleFocus);
    };
  }, []);

  const milestones = useMemo(
    () => [
      {
        icon: "🎯",
        title: "Set your career goal",
        description: "Choose the career you want to work towards.",
        done: progress.hasCareerGoal,
      },
      {
        icon: "🧠",
        title: "Complete a skill assessment",
        description: "Understand your current technical skill level.",
        done: progress.assessmentCount > 0,
      },
      {
        icon: "📚",
        title: "Start learning",
        description: "Complete lessons in your Learning Hub.",
        done: progress.lessonsCompleted > 0,
      },
      {
        icon: "💻",
        title: "Build a project",
        description: "Add a project to your portfolio.",
        done: progress.projectCount > 0,
      },
      {
        icon: "🎤",
        title: "Practise interviews",
        description: "Practise questions before your next interview.",
        done: progress.interviewPractised > 0,
      },
    ],
    [progress]
  );

  const milestoneCount = milestones.filter(
    (item) => item.done
  ).length;

  const milestonePercentage = Math.round(
    (milestoneCount / milestones.length) * 100
  );

  const learningItems = [
    {
      icon: "🧠",
      title: "Skill Assessments",
      detail: `${progress.assessmentCount} assessment(s) completed`,
      value: progress.assessmentCount > 0 ? progress.averageScore : 0,
      caption:
        progress.assessmentCount > 0
          ? `${progress.averageScore}% average score`
          : "Take your first assessment",
      color: "blue",
    },
    {
      icon: "🗺️",
      title: "My Roadmap",
      detail: `${progress.roadmapCompleted} completed task(s)`,
      value: Math.min(100, progress.roadmapCompleted * 10),
      caption: roadmapSynced
        ? "Progress synced with the backend"
        : "Keep moving towards your career goal",
      color: "purple",
    },
    {
      icon: "📖",
      title: "Learning Hub",
      detail: `${progress.lessonsCompleted} completed lesson(s) detected`,
      value: Math.min(100, progress.lessonsCompleted * 10),
      caption: "Small lessons lead to big progress",
      color: "green",
    },
    {
      icon: "⚡",
      title: "Challenges",
      detail: `${progress.challengesCompleted} completed challenge(s) detected`,
      value: Math.min(100, progress.challengesCompleted * 10),
      caption: "Practise problem-solving regularly",
      color: "orange",
    },
    {
      icon: "🎤",
      title: "Interview Prep",
      detail: `${progress.interviewPractised} practised item(s) detected`,
      value: Math.min(100, progress.interviewPractised * 10),
      caption: "Build confidence one question at a time",
      color: "pink",
    },
    {
      icon: "🧩",
      title: "Skill Gap",
      detail: `${progress.skillGapCompleted} completed item(s) detected`,
      value: Math.min(100, progress.skillGapCompleted * 10),
      caption: "Work on the skills you still need",
      color: "teal",
    },
  ];

  return (
    <main className="my-progress-page">
      <section className="mp-page-heading">
        <div>
          <span className="mp-eyebrow">YOUR LEARNING JOURNEY</span>
          <h1>My Progress</h1>
          <p>
            Track your learning, celebrate your milestones, and keep moving
            towards your career goals.
          </p>
        </div>

        <div className="mp-heading-badge">
          <span>📈</span>
          <div>
            <strong>
              {milestoneCount} of {milestones.length}
            </strong>
            <small>Milestones reached</small>
          </div>
        </div>
      </section>

      <section className="mp-overview-banner">
        <div className="mp-overview-copy">
          <span className="mp-banner-label">YOUR PROGRESS OVERVIEW</span>
          <h2>Every skill you build moves you forward.</h2>
          <p>
            Stay consistent, practise regularly, and keep building your future.
          </p>
        </div>

        <div className="mp-overview-ring">
          <div className="mp-ring-inner">
            <strong>{milestonePercentage}%</strong>
            <span>milestones</span>
          </div>
        </div>
      </section>

      <section className="mp-stats-grid">
        <StatCard
          icon="🧠"
          label="Assessments"
          value={progress.assessmentCount}
          caption="Attempts completed"
          color="blue"
        />

        <StatCard
          icon="⭐"
          label="Average Score"
          value={`${progress.averageScore}%`}
          caption="Across your assessments"
          color="orange"
        />

        <StatCard
          icon="💻"
          label="My Projects"
          value={progress.projectCount}
          caption="Projects in your portfolio"
          color="purple"
        />

        <StatCard
          icon="🏆"
          label="Activity Points"
          value={progress.activityTotal}
          caption="Learning activities recorded"
          color="green"
        />
      </section>

      <section className="mp-main-grid">
        <div className="mp-panel mp-milestones-panel">
          <div className="mp-section-heading">
            <div>
              <span className="mp-section-kicker">KEEP GOING</span>
              <h2>Your Milestones</h2>
            </div>

            <span className="mp-count-pill">
              {milestoneCount}/{milestones.length}
            </span>
          </div>

          <ProgressBar value={milestonePercentage} />

          <div className="mp-milestone-list">
            {milestones.map((item) => (
              <div
                className={`mp-milestone ${
                  item.done ? "mp-milestone-done" : ""
                }`}
                key={item.title}
              >
                <div className="mp-milestone-icon">{item.icon}</div>

                <div className="mp-milestone-copy">
                  <h3>{item.title}</h3>
                  <p>{item.description}</p>
                </div>

                <span
                  className="mp-milestone-status"
                  aria-label={item.done ? "Completed" : "Not completed"}
                >
                  {item.done ? "✓" : "○"}
                </span>
              </div>
            ))}
          </div>
        </div>

        <div className="mp-panel mp-score-panel">
          <div className="mp-section-heading">
            <div>
              <span className="mp-section-kicker">ASSESSMENT INSIGHTS</span>
              <h2>Latest Assessment</h2>
            </div>

            <span className="mp-score-icon">🎯</span>
          </div>

          {progress.latestAssessment ? (
            <>
              <div className="mp-latest-score">
                <strong>
                  {getPercentage(progress.latestAssessment.percentage)}%
                </strong>
                <span>
                  {progress.latestAssessment.skill || "Skill Assessment"}
                </span>
              </div>

              <ProgressBar
                value={progress.latestAssessment.percentage}
                color="green"
              />

              <div className="mp-score-details">
                <div>
                  <span>Correct answers</span>
                  <strong>
                    {progress.latestAssessment.correctAnswers ?? "—"}
                  </strong>
                </div>

                <div>
                  <span>Total questions</span>
                  <strong>
                    {progress.latestAssessment.totalQuestions ?? "—"}
                  </strong>
                </div>
              </div>

              <p className="mp-score-note">
                Keep practising to improve your next score.
              </p>
            </>
          ) : (
            <div className="mp-empty-state">
              <span>📝</span>
              <h3>Your journey starts here</h3>
              <p>
                Complete a skill assessment to see your score and track your
                performance.
              </p>
            </div>
          )}
        </div>
      </section>

      <section className="mp-panel mp-learning-panel">
        <div className="mp-section-heading">
          <div>
            <span className="mp-section-kicker">FEATURE BREAKDOWN</span>
            <h2>Learning Activity</h2>
          </div>

          <span className="mp-live-label">
            <span className="mp-live-dot" />
            {roadmapSynced ? "Backend synced" : "Local progress"}
          </span>
        </div>

        <div className="mp-activity-list">
          {learningItems.map((item) => (
            <article className="mp-activity-item" key={item.title}>
              <div className={`mp-activity-icon mp-activity-${item.color}`}>
                {item.icon}
              </div>

              <div className="mp-activity-main">
                <div className="mp-activity-title-row">
                  <h3>{item.title}</h3>
                  <span>{item.value}%</span>
                </div>

                <ProgressBar value={item.value} color={item.color} />

                <p>{item.detail}</p>
                <small>{item.caption}</small>
              </div>
            </article>
          ))}
        </div>
      </section>

      <section className="mp-bottom-note">
        <span>💡</span>
        <div>
          <h3>Consistency beats perfection.</h3>
          <p>
            Roadmap completion is loaded from your authenticated SkillSphere
            backend. Other activity counts still use the progress data currently
            saved in this browser and can be connected to their APIs separately.
          </p>
        </div>
      </section>

      <p className="mp-updated-text">
        Last refreshed: {lastUpdated.toLocaleTimeString()}
      </p>
    </main>
  );
}

export default MyProgress;
