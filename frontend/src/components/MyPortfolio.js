
import React, { useEffect, useState } from "react";
import "./MyPortfolio.css";
import Toast from "./Toast";

const STORAGE_KEY = "skillsphere_student_portfolio";
const API_URL = "https://skillsphere-17hl.onrender.com/api/portfolio/";

const DEFAULT_PORTFOLIO = {
  name: "",
  headline: "Aspiring Software Developer",
  email: "",
  location: "",
  objective: "",
  phone: "",
  skills: "Python, Java, JavaScript, React, Django, SQL",
  education: [
    { qualification: "", institution: "", year: "", result: "" },
  ],
  projects: [
    {
      title: "SkillSphere",
      description: "An AI-powered career and skill evolution platform.",
      technologies: "React, Django REST Framework",
      github: "",
      demo: "",
    },
  ],
  certifications: "",
  resume_url: "",
  portfolio_url: "",
  github_url: "",
  linkedin_url: "",
};

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

function normalizePortfolio(data = {}) {
  return {
    ...DEFAULT_PORTFOLIO,
    ...data,
    education: Array.isArray(data.education)
      ? data.education
      : [...DEFAULT_PORTFOLIO.education],
    projects: Array.isArray(data.projects)
      ? data.projects
      : [...DEFAULT_PORTFOLIO.projects],
  };
}

function loadCachedPortfolio() {
  try {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) return normalizePortfolio(JSON.parse(saved));
  } catch {
    // Continue with default values if the cache is invalid.
  }

  return normalizePortfolio();
}

function getErrorMessage(data, fallback) {
  if (data?.detail) return data.detail;
  if (data?.message) return data.message;

  if (data && typeof data === "object") {
    const firstError = Object.values(data).flat(Infinity).find(
      (item) => typeof item === "string"
    );
    if (firstError) return firstError;
  }

  return fallback;
}

function MyPortfolio() {
  const [portfolio, setPortfolio] = useState(loadCachedPortfolio);
  const [savedPortfolio, setSavedPortfolio] = useState(loadCachedPortfolio);
  const [activeTab, setActiveTab] = useState("edit");
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [toast, setToast] = useState({ message: "", type: "success" });

  function showMessage(message, type = "success") {
    setToast({ message, type });
  }

  function closeToast() {
    setToast({ message: "", type: "success" });
  }

  useEffect(() => {
    if (!toast.message) return undefined;

    const timer = window.setTimeout(closeToast, 3500);
    return () => window.clearTimeout(timer);
  }, [toast]);

  useEffect(() => {
    let cancelled = false;

    async function fetchPortfolio() {
      const token = getAccessToken();

      if (!token) {
        setLoading(false);
        showMessage(
          "Please log in again to load your saved portfolio.",
          "warning"
        );
        return;
      }

      try {
        const response = await fetch(API_URL, {
          method: "GET",
          headers: getAuthHeaders(),
        });

        const data = await response.json().catch(() => ({}));

        if (cancelled) return;

        if (response.status === 404) {
          // No server portfolio yet; keep the current draft as a starting point.
          const draft = loadCachedPortfolio();

          try {
            const savedProfile = JSON.parse(
              localStorage.getItem("skillsphere_student_profile") || "{}"
            );

            draft.name =
              draft.name ||
              savedProfile.fullName ||
              savedProfile.name ||
              [savedProfile.firstName, savedProfile.lastName]
                .filter(Boolean)
                .join(" ");

            draft.email = draft.email || savedProfile.email || "";
          } catch {
            // Profile cache is optional.
          }

          setPortfolio(draft);
          setSavedPortfolio(draft);
          setLoading(false);
          return;
        }

        if (!response.ok) {
          throw new Error(
            getErrorMessage(data, "Could not load your portfolio.")
          );
        }

        const loaded = normalizePortfolio(data);
        setPortfolio(loaded);
        setSavedPortfolio(loaded);

        try {
          localStorage.setItem(STORAGE_KEY, JSON.stringify(loaded));
        } catch {
          // The server remains the source of truth if caching fails.
        }
      } catch (error) {
        if (!cancelled) {
          showMessage(
            error.message ||
              "Unable to connect to the server. Check that Django is running.",
            "error"
          );
        }
      } finally {
        if (!cancelled) setLoading(false);
      }
    }

    fetchPortfolio();

    return () => {
      cancelled = true;
    };
  }, []);

  function updateField(field, value) {
    setPortfolio((current) => ({ ...current, [field]: value }));
  }

  function updateItem(section, index, field, value) {
    setPortfolio((current) => ({
      ...current,
      [section]: current[section].map((item, itemIndex) =>
        itemIndex === index ? { ...item, [field]: value } : item
      ),
    }));
  }

  function addEducation() {
    setPortfolio((current) => ({
      ...current,
      education: [
        ...current.education,
        { qualification: "", institution: "", year: "", result: "" },
      ],
    }));
  }

  function removeEducation(index) {
    setPortfolio((current) => ({
      ...current,
      education: current.education.filter((_, i) => i !== index),
    }));
  }

  function addProject() {
    setPortfolio((current) => ({
      ...current,
      projects: [
        ...current.projects,
        { title: "", description: "", technologies: "", github: "", demo: "" },
      ],
    }));
  }

  function removeProject(index) {
    setPortfolio((current) => ({
      ...current,
      projects: current.projects.filter((_, i) => i !== index),
    }));
  }

  async function savePortfolio(event) {
    if (event) event.preventDefault();

    if (!portfolio.name.trim()) {
      showMessage("Please enter your full name before saving.", "warning");
      return;
    }

    if (
      portfolio.email.trim() &&
      !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(portfolio.email.trim())
    ) {
      showMessage("Please enter a valid email address.", "warning");
      return;
    }

    if (!getAccessToken()) {
      showMessage("Your login token is missing. Please log in again.", "error");
      return;
    }

    setSaving(true);

    try {
      const response = await fetch(API_URL, {
        method: "PUT",
        headers: getAuthHeaders(),
        body: JSON.stringify(portfolio),
      });

      const data = await response.json().catch(() => ({}));

      if (!response.ok) {
        if (response.status === 401) {
          throw new Error("Your session has expired. Please log in again.");
        }

        throw new Error(
          getErrorMessage(data, "Unable to save your portfolio.")
        );
      }

      const saved = normalizePortfolio(data.portfolio || data);
      setPortfolio(saved);
      setSavedPortfolio(saved);

      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(saved));
      } catch {
        // Database save succeeded even if browser caching fails.
      }

      showMessage(
        data.message || "Portfolio saved to the database successfully!",
        "success"
      );
    } catch (error) {
      showMessage(
        error.message || "Unable to save your portfolio.",
        "error"
      );
    } finally {
      setSaving(false);
    }
  }

  function resetPortfolio() {
    const restored = normalizePortfolio(savedPortfolio);
    setPortfolio(restored);
    showMessage("Your last server-loaded or saved portfolio was restored.", "info");
  }

  function printPortfolio() {
    window.print();
  }

  const skills = (portfolio.skills || "")
    .split(",")
    .map((skill) => skill.trim())
    .filter(Boolean);

  const savedAchievements = (() => {
    try {
      const saved = JSON.parse(
        localStorage.getItem("skillsphere_student_achievements") || "{}"
      );
      return saved && typeof saved === "object" ? saved : {};
    } catch {
      return {};
    }
  })();

  const earnedBadges = [
    ["career-starter", "Career Starter"],
    ["first-assessment", "First Assessment"],
    ["assessment-pro", "Assessment Pro"],
    ["high-scorer", "High Scorer"],
    ["first-project", "Project Builder"],
    ["project-creator", "Project Creator"],
    ["challenge-solver", "Challenge Solver"],
    ["learning-star", "Learning Star"],
    ["interview-ready", "Interview Ready"],
    ["skill-gap-master", "Skill Gap Master"],
    ["roadmap-explorer", "Roadmap Explorer"],
    ["dedicated-learner", "Dedicated Learner"],
  ].filter(([id]) => savedAchievements[id]);

  return (
    <main className="mpf-page">
      <Toast message={toast.message} type={toast.type} onClose={closeToast} />

      <header className="mpf-header">
        <div>
          <span className="mpf-eyebrow">YOUR PROFESSIONAL IDENTITY</span>
          <h1>My Portfolio</h1>
          <p>
            Showcase your skills, education, projects and achievements in one
            professional space.
          </p>
        </div>
        <button type="button" className="mpf-print-button" onClick={printPortfolio}>
          ⎙ Print Portfolio
        </button>
      </header>

      <div className="mpf-tabs">
        <button
          type="button"
          className={activeTab === "edit" ? "mpf-tab active" : "mpf-tab"}
          onClick={() => setActiveTab("edit")}
        >
          ✎ Edit Portfolio
        </button>
        <button
          type="button"
          className={activeTab === "preview" ? "mpf-tab active" : "mpf-tab"}
          onClick={() => setActiveTab("preview")}
        >
          ◉ Portfolio Preview
        </button>
      </div>

      {loading && <p>Loading your portfolio...</p>}

      {activeTab === "edit" ? (
        <form className="mpf-editor" onSubmit={savePortfolio}>
          <section className="mpf-card">
            <div className="mpf-card-heading">
              <span className="mpf-heading-icon">👤</span>
              <div>
                <h2>Personal Information</h2>
                <p>Introduce yourself professionally.</p>
              </div>
            </div>

            <div className="mpf-form-grid">
              <label>
                Full Name *
                <input
                  value={portfolio.name}
                  onChange={(e) => updateField("name", e.target.value)}
                  placeholder="Enter your full name"
                />
              </label>
              <label>
                Professional Headline
                <input
                  value={portfolio.headline}
                  onChange={(e) => updateField("headline", e.target.value)}
                  placeholder="e.g. Aspiring Full Stack Developer"
                />
              </label>
              <label>
                Email
                <input
                  type="email"
                  value={portfolio.email}
                  onChange={(e) => updateField("email", e.target.value)}
                  placeholder="you@example.com"
                />
              </label>
              <label>
                Location
                <input
                  value={portfolio.location}
                  onChange={(e) => updateField("location", e.target.value)}
                  placeholder="City, State"
                />
              </label>
              <label>
                Contact Number
                <input
                  value={portfolio.phone}
                  onChange={(e) => updateField("phone", e.target.value)}
                  placeholder="Optional"
                />
              </label>
            </div>

            <label className="mpf-full-field">
              Career Objective / About Me
              <textarea
                rows="4"
                value={portfolio.objective}
                onChange={(e) => updateField("objective", e.target.value)}
                placeholder="Write a short introduction about your interests, skills and career goals."
              />
            </label>
          </section>

          <section className="mpf-card">
            <div className="mpf-card-heading">
              <span className="mpf-heading-icon">⚡</span>
              <div>
                <h2>Technical Skills</h2>
                <p>Separate each skill with a comma.</p>
              </div>
            </div>
            <label className="mpf-full-field">
              Skills
              <textarea
                rows="3"
                value={portfolio.skills}
                onChange={(e) => updateField("skills", e.target.value)}
                placeholder="Python, Java, React, Django, SQL"
              />
            </label>
            <div className="mpf-skill-preview">
              {skills.map((skill, index) => (
                <span key={`${skill}-${index}`}>{skill}</span>
              ))}
            </div>
          </section>

          <section className="mpf-card">
            <div className="mpf-card-heading mpf-heading-with-action">
              <div className="mpf-heading-left">
                <span className="mpf-heading-icon">🎓</span>
                <div>
                  <h2>Education</h2>
                  <p>Add your academic qualifications.</p>
                </div>
              </div>
              <button type="button" className="mpf-add-button" onClick={addEducation}>
                + Add Education
              </button>
            </div>

            {portfolio.education.map((item, index) => (
              <div className="mpf-repeat-item" key={index}>
                <div className="mpf-repeat-title">
                  <strong>Education {index + 1}</strong>
                  {portfolio.education.length > 1 && (
                    <button
                      type="button"
                      className="mpf-remove-button"
                      onClick={() => removeEducation(index)}
                    >
                      Remove
                    </button>
                  )}
                </div>
                <div className="mpf-form-grid">
                  <label>
                    Qualification
                    <input
                      value={item.qualification || ""}
                      onChange={(e) =>
                        updateItem("education", index, "qualification", e.target.value)
                      }
                      placeholder="e.g. B.Tech / B.Sc / Diploma"
                    />
                  </label>
                  <label>
                    Institution
                    <input
                      value={item.institution || ""}
                      onChange={(e) =>
                        updateItem("education", index, "institution", e.target.value)
                      }
                      placeholder="College or university"
                    />
                  </label>
                  <label>
                    Year
                    <input
                      value={item.year || ""}
                      onChange={(e) =>
                        updateItem("education", index, "year", e.target.value)
                      }
                      placeholder="e.g. 2027"
                    />
                  </label>
                  <label>
                    Result
                    <input
                      value={item.result || ""}
                      onChange={(e) =>
                        updateItem("education", index, "result", e.target.value)
                      }
                      placeholder="CGPA or percentage"
                    />
                  </label>
                </div>
              </div>
            ))}
          </section>

          <section className="mpf-card">
            <div className="mpf-card-heading mpf-heading-with-action">
              <div className="mpf-heading-left">
                <span className="mpf-heading-icon">💻</span>
                <div>
                  <h2>Projects</h2>
                  <p>Showcase projects you have worked on.</p>
                </div>
              </div>
              <button type="button" className="mpf-add-button" onClick={addProject}>
                + Add Project
              </button>
            </div>

            {portfolio.projects.length === 0 && (
              <p className="mpf-empty-text">
                No projects added yet. Click Add Project to begin.
              </p>
            )}

            {portfolio.projects.map((item, index) => (
              <div className="mpf-repeat-item" key={index}>
                <div className="mpf-repeat-title">
                  <strong>Project {index + 1}</strong>
                  <button
                    type="button"
                    className="mpf-remove-button"
                    onClick={() => removeProject(index)}
                  >
                    Remove
                  </button>
                </div>
                <div className="mpf-form-grid">
                  <label>
                    Project Title
                    <input
                      value={item.title || ""}
                      onChange={(e) =>
                        updateItem("projects", index, "title", e.target.value)
                      }
                      placeholder="Project name"
                    />
                  </label>
                  <label>
                    Technologies
                    <input
                      value={item.technologies || ""}
                      onChange={(e) =>
                        updateItem("projects", index, "technologies", e.target.value)
                      }
                      placeholder="React, Django, PostgreSQL"
                    />
                  </label>
                  <label>
                    GitHub URL
                    <input
                      type="url"
                      value={item.github || ""}
                      onChange={(e) =>
                        updateItem("projects", index, "github", e.target.value)
                      }
                      placeholder="https://github.com/..."
                    />
                  </label>
                  <label>
                    Live Demo URL
                    <input
                      type="url"
                      value={item.demo || ""}
                      onChange={(e) =>
                        updateItem("projects", index, "demo", e.target.value)
                      }
                      placeholder="https://..."
                    />
                  </label>
                </div>
                <label className="mpf-full-field">
                  Project Description
                  <textarea
                    rows="3"
                    value={item.description || ""}
                    onChange={(e) =>
                      updateItem("projects", index, "description", e.target.value)
                    }
                    placeholder="Explain what the project does and what you contributed."
                  />
                </label>
              </div>
            ))}
          </section>

          <section className="mpf-card">
            <div className="mpf-card-heading">
              <span className="mpf-heading-icon">🏆</span>
              <div>
                <h2>Certifications & Additional Achievements</h2>
                <p>Add certificates, awards, workshops or other accomplishments.</p>
              </div>
            </div>
            <label className="mpf-full-field">
              Certifications and Achievements
              <textarea
                rows="4"
                value={portfolio.certifications}
                onChange={(e) => updateField("certifications", e.target.value)}
                placeholder="Enter your certifications and achievements."
              />
            </label>
            <div className="mpf-earned-badges">
              <h3>Saved SkillSphere Achievements</h3>
              {earnedBadges.length ? (
                <div className="mpf-skill-preview">
                  {earnedBadges.map(([, title]) => (
                    <span key={title}>🏅 {title}</span>
                  ))}
                </div>
              ) : (
                <p>Saved achievement badges will appear here when available.</p>
              )}
            </div>
          </section>

          <div className="mpf-save-row">
            <p>Your portfolio is saved to your SkillSphere account.</p>
            <button
              type="button"
              className="mpf-print-button"
              onClick={resetPortfolio}
            >
              ↺ Reset Changes
            </button>
            <button
              className="mpf-save-button"
              type="submit"
              disabled={saving || loading}
            >
              {saving ? "Saving..." : "✓ Save Portfolio"}
            </button>
          </div>
        </form>
      ) : (
        <section className="mpf-preview">
          <div className="mpf-preview-hero">
            <div className="mpf-avatar">
              {(portfolio.name || "S").trim().charAt(0).toUpperCase()}
            </div>
            <span className="mpf-preview-label">STUDENT PORTFOLIO</span>
            <h2>{portfolio.name || "Your Name"}</h2>
            <p>{portfolio.headline || "Aspiring Professional"}</p>
            <div className="mpf-contact-row">
              {portfolio.email && <span>✉ {portfolio.email}</span>}
              {portfolio.location && <span>⌖ {portfolio.location}</span>}
              {portfolio.phone && <span>☎ {portfolio.phone}</span>}
            </div>
          </div>

          <div className="mpf-preview-body">
            <section className="mpf-preview-section">
              <h3>About Me</h3>
              <p>
                {portfolio.objective ||
                  "Add your career objective in Edit Portfolio to introduce yourself."}
              </p>
            </section>

            <section className="mpf-preview-section">
              <h3>Technical Skills</h3>
              <div className="mpf-skill-preview">
                {skills.length ? (
                  skills.map((skill, index) => (
                    <span key={`${skill}-${index}`}>{skill}</span>
                  ))
                ) : (
                  <p>Add your skills in Edit Portfolio.</p>
                )}
              </div>
            </section>

            <section className="mpf-preview-section">
              <h3>Education</h3>
              {portfolio.education.filter(
                (item) => item.qualification || item.institution
              ).length ? (
                portfolio.education
                  .filter((item) => item.qualification || item.institution)
                  .map((item, index) => (
                    <div className="mpf-preview-entry" key={index}>
                      <h4>{item.qualification || "Qualification"}</h4>
                      <p>{item.institution}</p>
                      <span>
                        {[item.year, item.result].filter(Boolean).join(" • ")}
                      </span>
                    </div>
                  ))
              ) : (
                <p>Add your education details in Edit Portfolio.</p>
              )}
            </section>

            <section className="mpf-preview-section">
              <h3>Projects</h3>
              {portfolio.projects.filter(
                (item) => item.title || item.description
              ).length ? (
                portfolio.projects
                  .filter((item) => item.title || item.description)
                  .map((item, index) => (
                    <article className="mpf-preview-project" key={index}>
                      <h4>{item.title || "Project"}</h4>
                      <p>{item.description}</p>
                      {item.technologies && (
                        <div className="mpf-skill-preview">
                          {item.technologies
                            .split(",")
                            .map((tech) => tech.trim())
                            .filter(Boolean)
                            .map((tech, techIndex) => (
                              <span key={`${tech}-${techIndex}`}>{tech}</span>
                            ))}
                        </div>
                      )}
                      <div className="mpf-project-links">
                        {item.github && (
                          <a href={item.github} target="_blank" rel="noreferrer">
                            GitHub ↗
                          </a>
                        )}
                        {item.demo && (
                          <a href={item.demo} target="_blank" rel="noreferrer">
                            Live Demo ↗
                          </a>
                        )}
                      </div>
                    </article>
                  ))
              ) : (
                <p>Add your projects in Edit Portfolio.</p>
              )}
            </section>

            <section className="mpf-preview-section">
              <h3>Certifications & Achievements</h3>
              <p>
                {portfolio.certifications ||
                  "Add certifications and achievements in Edit Portfolio."}
              </p>
              {earnedBadges.length > 0 && (
                <div className="mpf-skill-preview">
                  {earnedBadges.map(([, title]) => (
                    <span key={title}>🏅 {title}</span>
                  ))}
                </div>
              )}
            </section>
          </div>

          <div className="mpf-preview-actions">
            <button
              type="button"
              className="mpf-save-button"
              onClick={() => setActiveTab("edit")}
            >
              ✎ Edit Details
            </button>
            <button
              type="button"
              className="mpf-print-button"
              onClick={printPortfolio}
            >
              ⎙ Print Portfolio
            </button>
          </div>
        </section>
      )}
    </main>
  );
}

export default MyPortfolio;
