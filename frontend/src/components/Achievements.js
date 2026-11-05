
import React, { useCallback, useEffect, useMemo, useState } from "react";
import "./Achievements.css";
import { showToast } from "../components/ToastProvider";

const ACHIEVEMENTS_API = "http://127.0.0.1:8000/api/achievements/";

const ACHIEVEMENTS = [
  { id: "career-starter", icon: "🎯", title: "Career Starter", description: "Set your first career goal.", category: "Career", requirement: "career", target: 1, points: 20, tier: "bronze" },
  { id: "first-assessment", icon: "🧠", title: "First Assessment", description: "Complete your first skill assessment.", category: "Assessment", requirement: "assessment", target: 1, points: 25, tier: "bronze" },
  { id: "assessment-pro", icon: "🌟", title: "Assessment Pro", description: "Complete five skill assessments.", category: "Assessment", requirement: "assessment", target: 5, points: 100, tier: "gold" },
  { id: "high-scorer", icon: "🏅", title: "High Scorer", description: "Score 80% or higher in an assessment.", category: "Assessment", requirement: "highScore", target: 1, points: 50, tier: "silver" },
  { id: "first-project", icon: "💻", title: "Project Builder", description: "Complete your first project.", category: "Projects", requirement: "project", target: 1, points: 30, tier: "bronze" },
  { id: "project-creator", icon: "🚀", title: "Project Creator", description: "Complete three projects.", category: "Projects", requirement: "project", target: 3, points: 75, tier: "silver" },
  { id: "challenge-solver", icon: "⚡", title: "Challenge Solver", description: "Complete five coding challenges.", category: "Challenges", requirement: "challenge", target: 5, points: 60, tier: "silver" },
  { id: "learning-star", icon: "📚", title: "Learning Star", description: "Complete five learning activities.", category: "Learning", requirement: "lesson", target: 5, points: 60, tier: "silver" },
  { id: "interview-ready", icon: "🎤", title: "Interview Ready", description: "Practise five interview questions.", category: "Interview", requirement: "interview", target: 5, points: 60, tier: "silver" },
  { id: "skill-gap-master", icon: "🧩", title: "Skill Gap Master", description: "Complete five skill-gap checklist items.", category: "Skills", requirement: "skillGap", target: 5, points: 75, tier: "gold" },
  { id: "roadmap-explorer", icon: "🗺️", title: "Roadmap Explorer", description: "Complete five roadmap items.", category: "Roadmap", requirement: "roadmap", target: 5, points: 75, tier: "gold" },
  { id: "dedicated-learner", icon: "👑", title: "Dedicated Learner", description: "Earn five different achievements.", category: "Special", requirement: "badges", target: 5, points: 100, tier: "gold" },
];

function getAccessToken() {
  const directToken =
    localStorage.getItem("access") ||
    localStorage.getItem("access_token") ||
    localStorage.getItem("accessToken");

  if (directToken) return directToken;

  try {
    const tokens = JSON.parse(localStorage.getItem("tokens") || "{}");
    return tokens.access || "";
  } catch {
    return "";
  }
}

function getAuthHeaders() {
  const token = getAccessToken();

  return {
    "Content-Type": "application/json",
    ...(token ? { Authorization: `Bearer ${token}` } : {}),
  };
}

async function readResponse(response) {
  const data = await response.json().catch(() => ({}));

  if (!response.ok) {
    if (response.status === 401) {
      throw new Error("Your session has expired. Please log in again.");
    }

    throw new Error(
      data.detail || data.error || data.message ||
      `Request failed with status ${response.status}.`
    );
  }

  return data;
}

function Achievements() {
  const [achievements, setAchievements] = useState([]);
  const [filter, setFilter] = useState("All");
  const [loading, setLoading] = useState(true);
  const [savingId, setSavingId] = useState(null);
  const [error, setError] = useState("");

  const loadAchievements = useCallback(async (showMessage = false) => {
    const token = getAccessToken();

    if (!token) {
      setError("Please log in to view your achievements.");
      setLoading(false);
      return;
    }

    setLoading(true);
    setError("");

    try {
      const response = await fetch(ACHIEVEMENTS_API, {
        method: "GET",
        headers: getAuthHeaders(),
        cache: "no-store",
      });

      const data = await readResponse(response);
      const serverResults = Array.isArray(data.results) ? data.results : [];

      const serverByKey = new Map(
        serverResults.map((item) => [item.badge_key, item])
      );

      const mergedAchievements = ACHIEVEMENTS.map((badge) => {
        const serverBadge = serverByKey.get(badge.id);

        return {
          ...badge,
          databaseId: serverBadge?.id ?? null,
          isEarned: serverBadge?.is_earned === true,
          isSaved: serverBadge?.is_saved === true,
          earnedAt: serverBadge?.earned_at ?? null,
          savedAt: serverBadge?.saved_at ?? null,
        };
      });

      setAchievements(mergedAchievements);

      if (showMessage) {
        showToast("Achievement data refreshed.", "success");
      }
    } catch (requestError) {
      setError(
        requestError.message || "Unable to connect to the SkillSphere backend."
      );

      if (showMessage) {
        showToast(requestError.message || "Unable to refresh achievements.", "error");
      }
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadAchievements();

    const refreshOnFocus = () => loadAchievements();
    window.addEventListener("focus", refreshOnFocus);

    return () => window.removeEventListener("focus", refreshOnFocus);
  }, [loadAchievements]);

  const earned = useMemo(
    () => achievements.filter((badge) => badge.isEarned),
    [achievements]
  );

  const earnedIds = useMemo(
    () => new Set(earned.map((badge) => badge.id)),
    [earned]
  );

  const totalPoints = earned.reduce(
    (total, badge) => total + Number(badge.points || 0),
    0
  );

  const visibleAchievements = achievements.filter((badge) => {
    if (filter === "Earned") return earnedIds.has(badge.id);
    if (filter === "Locked") return !earnedIds.has(badge.id);
    return true;
  });

  async function saveAchievement(badge) {
    if (!badge.isEarned) {
      showToast("Complete the required activity to unlock this badge.", "warning");
      return;
    }

    if (badge.isSaved) {
      showToast("This achievement is already saved.", "info");
      return;
    }

    if (!badge.databaseId) {
      showToast("The achievement is missing its database ID. Refresh and try again.", "error");
      return;
    }

    if (!getAccessToken()) {
      showToast("Please log in again to save this achievement.", "error");
      return;
    }

    setSavingId(badge.id);

    try {
      const response = await fetch(
        `${ACHIEVEMENTS_API}${badge.databaseId}/save/`,
        {
          method: "POST",
          headers: getAuthHeaders(),
          body: JSON.stringify({}),
        }
      );

      const result = await readResponse(response);

      setAchievements((current) =>
        current.map((item) =>
          item.id === badge.id
            ? {
                ...item,
                isSaved: result.is_saved === true,
                savedAt: result.saved_at ?? item.savedAt,
              }
            : item
        )
      );

      showToast(`${badge.title} saved successfully!`, "success");
    } catch (requestError) {
      showToast(requestError.message || "Unable to save this achievement.", "error");
    } finally {
      setSavingId(null);
    }
  }

  return (
    <main className="ach-page">
      <header className="ach-header">
        <div>
          <span className="ach-eyebrow">RECOGNISE YOUR GROWTH</span>
          <h1>Achievements</h1>
          <p>Every assessment, project and learning milestone brings you one step closer to your goals.</p>
        </div>

        <button
          className="ach-refresh"
          onClick={() => loadAchievements(true)}
          type="button"
          disabled={loading}
        >
          ↻ {loading ? "Refreshing..." : "Refresh progress"}
        </button>
      </header>

      <section className="ach-hero">
        <div className="ach-hero-copy">
          <span className="ach-hero-label">YOUR JOURNEY, YOUR REWARDS</span>
          <h2>Small wins. Bigger dreams.</h2>
          <p>Keep learning, keep practising, and unlock new milestones as you grow your skills.</p>
        </div>
        <div className="ach-hero-trophy" aria-hidden="true">🏆</div>
      </section>

      {error && (
        <div className="ach-empty" role="alert">
          <h3>Unable to load achievements</h3>
          <p>{error}</p>
          <button className="ach-refresh" type="button" onClick={() => loadAchievements(true)}>
            Try again
          </button>
        </div>
      )}

      <section className="ach-stats">
        <article className="ach-stat">
          <span className="ach-stat-icon">🏆</span>
          <div><p>Badges Earned</p><strong>{earned.length}/{achievements.length || ACHIEVEMENTS.length}</strong></div>
        </article>
        <article className="ach-stat">
          <span className="ach-stat-icon">⭐</span>
          <div><p>Points Earned</p><strong>{totalPoints}</strong></div>
        </article>
        <article className="ach-stat">
          <span className="ach-stat-icon">🔒</span>
          <div><p>Still to Unlock</p><strong>{Math.max(0, (achievements.length || ACHIEVEMENTS.length) - earned.length)}</strong></div>
        </article>
      </section>

      <section className="ach-progress-panel">
        <div className="ach-progress-heading">
          <div><h2>Your achievement progress</h2><p>Complete activities to unlock more badges.</p></div>
          <strong>{Math.round((earned.length / (achievements.length || ACHIEVEMENTS.length)) * 100)}%</strong>
        </div>
        <div
          className="ach-progress-track"
          role="progressbar"
          aria-valuenow={earned.length}
          aria-valuemin={0}
          aria-valuemax={achievements.length || ACHIEVEMENTS.length}
        >
          <div
            className="ach-progress-fill"
            style={{ width: `${(earned.length / (achievements.length || ACHIEVEMENTS.length)) * 100}%` }}
          />
        </div>
      </section>

      <section className="ach-badges-section">
        <div className="ach-section-heading">
          <div><span className="ach-eyebrow">YOUR COLLECTION</span><h2>Achievement Badges</h2></div>
          <div className="ach-filters">
            {["All", "Earned", "Locked"].map((item) => (
              <button
                key={item}
                type="button"
                className={filter === item ? "ach-filter active" : "ach-filter"}
                onClick={() => setFilter(item)}
              >
                {item}
              </button>
            ))}
          </div>
        </div>

        {loading && achievements.length === 0 ? (
          <div className="ach-empty">
            <span>🏅</span><h3>Loading achievements...</h3>
            <p>Your achievement collection is being loaded.</p>
          </div>
        ) : (
          <div className="ach-grid">
            {visibleAchievements.map((badge) => (
              <article
                key={badge.id}
                className={`ach-card ${badge.isEarned ? "ach-earned" : "ach-locked"}`}
              >
                <div className={`ach-badge-art ach-tier-${badge.tier}`}>
                  <span>{badge.isEarned ? badge.icon : "🔒"}</span>
                </div>

                <span className={`ach-tier-label ach-label-${badge.tier}`}>
                  {badge.tier.toUpperCase()}
                </span>

                <h3>{badge.title}</h3>
                <p>{badge.description}</p>

                <div className="ach-card-footer">
                  <span>⭐ {badge.points} points</span>
                  <span className={badge.isEarned ? "ach-status-earned" : "ach-status-locked"}>
                    {badge.isEarned ? "✓ Earned" : "Locked"}
                  </span>
                </div>

                {badge.isEarned ? (
                  <button
                    type="button"
                    className={`ach-claim-button ${badge.isSaved ? "ach-saved" : ""}`}
                    onClick={() => saveAchievement(badge)}
                    disabled={badge.isSaved || savingId === badge.id}
                  >
                    {badge.isSaved ? "✓ Saved" : savingId === badge.id ? "Saving..." : "Save achievement"}
                  </button>
                ) : (
                  <div className="ach-unlock-hint">
                    Complete the required activity to unlock this badge.
                  </div>
                )}
              </article>
            ))}
          </div>
        )}

        {!loading && visibleAchievements.length === 0 && !error && (
          <div className="ach-empty">
            <span>🏅</span><h3>No badges in this filter yet</h3>
            <p>Try another filter or complete more learning activities.</p>
          </div>
        )}
      </section>
    </main>
  );
}

export default Achievements;
