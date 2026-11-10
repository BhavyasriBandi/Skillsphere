
import React, { useCallback, useEffect, useState } from "react";
import "./CareerGoal.css";
import Toast, { showToast } from "./Toast";

const API_URL =
  "https://skillsphere-u93o.onrender.com/api/learning-goals/career-goal/";

const initialGoal = {
  careerRole: "",
  domain: "",
  experienceLevel: "Beginner",
  targetDate: "",
  objective: "",
};

const careerOptions = [
  "Full Stack Developer",
  "Frontend Developer",
  "Backend Developer",
  "Python Developer",
  "Java Developer",
  "Data Analyst",
  "Data Scientist",
  "AI / Machine Learning Engineer",
  "Software Engineer",
  "Cybersecurity Analyst",
  "Cloud Engineer",
  "DevOps Engineer",
  "UI/UX Designer",
  "Other",
];

const domainOptions = [
  "Web Development",
  "Software Development",
  "Data Science",
  "Artificial Intelligence",
  "Cloud Computing",
  "Cybersecurity",
  "UI/UX Design",
  "Mobile Development",
  "Other",
];

function getAccessToken() {
  return (
    localStorage.getItem("skillsphere_access") ||
    localStorage.getItem("access")
  );
}

function mapApiToForm(data) {
  return {
    careerRole: data?.career_role || "",
    domain: data?.domain || "",
    experienceLevel: data?.experience_level || "Beginner",
    targetDate: data?.target_date || "",
    objective: data?.objective || "",
  };
}

function mapFormToApi(goal) {
  return {
    career_role: goal.careerRole.trim(),
    domain: goal.domain.trim(),
    experience_level: goal.experienceLevel,
    target_date: goal.targetDate || null,
    objective: goal.objective.trim(),
  };
}

function getErrorMessage(data) {
  if (data?.detail) {
    return data.detail;
  }

  const fields = [
    "career_role",
    "domain",
    "experience_level",
    "target_date",
    "objective",
  ];

  for (const field of fields) {
    if (Array.isArray(data?.[field]) && data[field].length > 0) {
      return data[field][0];
    }
  }

  return "Something went wrong. Please try again.";
}

function CareerGoal() {
  const [goal, setGoal] = useState({ ...initialGoal });
  const [savedGoal, setSavedGoal] = useState({ ...initialGoal });
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);

  const loadCareerGoal = useCallback(async () => {
    const token = getAccessToken();

    if (!token) {
      setLoading(false);
      showToast(
        "Please log in again to load your career goal.",
        "error"
      );
      return;
    }

    try {
      const response = await fetch(API_URL, {
        method: "GET",
        headers: {
          Accept: "application/json",
          Authorization: `Bearer ${token}`,
        },
      });

      if (response.status === 401) {
        throw new Error(
          "Your session has expired. Please log in again."
        );
      }

      const data = await response.json().catch(() => ({}));

      if (!response.ok) {
        throw new Error(getErrorMessage(data));
      }

      const formData = mapApiToForm(data);

      setGoal(formData);
      setSavedGoal(formData);
    } catch (error) {
      showToast(
        error.message || "Unable to load your career goal.",
        "error"
      );
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadCareerGoal();
  }, [loadCareerGoal]);

  function handleChange(event) {
    const { name, value } = event.target;

    setGoal((previousGoal) => ({
      ...previousGoal,
      [name]: value,
    }));
  }

  async function handleSave(event) {
    event.preventDefault();

    if (saving) {
      return;
    }

    if (
      !goal.careerRole.trim() ||
      !goal.domain.trim() ||
      !goal.experienceLevel.trim()
    ) {
      showToast(
        "Please complete all required fields.",
        "warning"
      );
      return;
    }

    if (goal.targetDate) {
      const today = new Date();
      today.setHours(0, 0, 0, 0);

      const selectedDate = new Date(
        `${goal.targetDate}T00:00:00`
      );

      if (
        Number.isNaN(selectedDate.getTime()) ||
        selectedDate < today
      ) {
        showToast(
          "Please select today or a future target date.",
          "error"
        );
        return;
      }
    }

    const token = getAccessToken();

    if (!token) {
      showToast(
        "Please log in before saving your career goal.",
        "error"
      );
      return;
    }

    setSaving(true);

    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(mapFormToApi(goal)),
      });

      const data = await response.json().catch(() => ({}));

      if (response.status === 401) {
        throw new Error(
          "Your session has expired. Please log in again."
        );
      }

      if (!response.ok) {
        throw new Error(getErrorMessage(data));
      }

      const updatedGoal = mapApiToForm(data);

      setGoal(updatedGoal);
      setSavedGoal(updatedGoal);

      showToast(
        "Your career goal has been saved successfully!",
        "success"
      );
    } catch (error) {
      showToast(
        error.message || "Unable to save your career goal.",
        "error"
      );
    } finally {
      setSaving(false);
    }
  }

  function handleReset() {
    setGoal({ ...savedGoal });

    showToast(
      "Your saved career goal has been restored.",
      "info"
    );
  }

  const hasSavedGoal = Boolean(
    savedGoal.careerRole &&
      savedGoal.domain &&
      savedGoal.experienceLevel
  );

  const goalProgress = hasSavedGoal ? 100 : 0;

  const hasChanges =
    JSON.stringify(goal) !== JSON.stringify(savedGoal);

  const now = new Date();

  const todayString = [
    now.getFullYear(),
    String(now.getMonth() + 1).padStart(2, "0"),
    String(now.getDate()).padStart(2, "0"),
  ].join("-");

  return (
    <>
      <Toast />

      <section className="career-goal-page">
        <div className="career-goal-heading">
          <div>
            <h1>Career Goal</h1>
            <p>
              Define your career destination and create a clear
              direction for your skills, learning, and professional
              growth.
            </p>
          </div>

          <div
            className="career-goal-heading-icon"
            aria-hidden="true"
          >
            🎯
          </div>
        </div>

        <div className="career-goal-banner">
          <div
            className="career-goal-banner-symbol"
            aria-hidden="true"
          >
            🚀
          </div>

          <div className="career-goal-banner-copy">
            <span>YOUR FUTURE STARTS HERE</span>

            <h2>
              {hasSavedGoal
                ? savedGoal.careerRole
                : "Dream it. Plan it. Achieve it."}
            </h2>

            <p>
              {hasSavedGoal
                ? `Your career goal is saved in ${savedGoal.domain}. Keep learning and moving forward!`
                : "Choose your destination today. Every skill you build brings you one step closer to your dream career."}
            </p>
          </div>

          <div
            className="career-goal-progress"
            aria-label={`Career goal setup ${goalProgress}% complete`}
          >
            <strong>{goalProgress}%</strong>
            <span>SETUP</span>
          </div>
        </div>

        <div className="career-goal-card">
          <div className="career-goal-card-heading">
            <div
              className="career-goal-card-icon"
              aria-hidden="true"
            >
              ✨
            </div>

            <div>
              <h2>Define Your Career Path</h2>
              <p>
                Tell us where you want to go. Fields marked with *
                are required.
              </p>
            </div>
          </div>

          {loading ? (
            <p role="status">Loading your career goal...</p>
          ) : (
            <form onSubmit={handleSave} noValidate>
              <div className="career-goal-fields">
                <div className="career-goal-field">
                  <label htmlFor="careerRole">
                    Target Career Role *
                  </label>

                  <select
                    id="careerRole"
                    name="careerRole"
                    value={goal.careerRole}
                    onChange={handleChange}
                    required
                  >
                    <option value="">
                      Select your dream career
                    </option>

                    {careerOptions.map((career) => (
                      <option key={career} value={career}>
                        {career}
                      </option>
                    ))}
                  </select>

                  <small>
                    Choose the role you want to work toward.
                  </small>
                </div>

                <div className="career-goal-field">
                  <label htmlFor="domain">
                    Preferred Domain *
                  </label>

                  <select
                    id="domain"
                    name="domain"
                    value={goal.domain}
                    onChange={handleChange}
                    required
                  >
                    <option value="">Select a domain</option>

                    {domainOptions.map((domain) => (
                      <option key={domain} value={domain}>
                        {domain}
                      </option>
                    ))}
                  </select>

                  <small>
                    Select the field that interests you most.
                  </small>
                </div>

                <div className="career-goal-field">
                  <label htmlFor="experienceLevel">
                    Current Experience Level *
                  </label>

                  <select
                    id="experienceLevel"
                    name="experienceLevel"
                    value={goal.experienceLevel}
                    onChange={handleChange}
                    required
                  >
                    <option value="Beginner">
                      Beginner — just getting started
                    </option>

                    <option value="Intermediate">
                      Intermediate — know the basics
                    </option>

                    <option value="Advanced">
                      Advanced — building real projects
                    </option>
                  </select>

                  <small>
                    Be honest about your current skill level.
                  </small>
                </div>

                <div className="career-goal-field">
                  <label htmlFor="targetDate">
                    Target Achievement Date
                  </label>

                  <input
                    id="targetDate"
                    type="date"
                    name="targetDate"
                    value={goal.targetDate}
                    min={todayString}
                    onChange={handleChange}
                  />

                  <small>
                    Set a realistic target date for your career goal.
                  </small>
                </div>

                <div className="career-goal-field career-goal-field-full">
                  <label htmlFor="objective">
                    Your Career Objective
                  </label>

                  <textarea
                    id="objective"
                    name="objective"
                    value={goal.objective}
                    onChange={handleChange}
                    placeholder="Describe your career dream, what motivates you, and what you want to achieve..."
                    maxLength={500}
                    rows={5}
                  />

                  <small className="career-goal-character-count">
                    {goal.objective.length}/500 characters
                  </small>
                </div>
              </div>

              <div className="career-goal-actions">
                <button
                  type="button"
                  className="career-goal-reset"
                  onClick={handleReset}
                  disabled={!hasChanges || saving}
                >
                  ↺ Reset Changes
                </button>

                <button
                  type="submit"
                  className="career-goal-save"
                  disabled={saving}
                >
                  {saving
                    ? "Saving..."
                    : "✓ Save Career Goal"}
                </button>
              </div>
            </form>
          )}
        </div>

        <div className="career-goal-tip">
          <span aria-hidden="true">💡</span>

          <div>
            <strong>A small tip for your future</strong>

            <p>
              Your career goal is your starting point, not your
              finish line. Review it regularly, practice
              consistently, and celebrate every improvement along
              the way.
            </p>
          </div>
        </div>
      </section>
    </>
  );
}

export default CareerGoal;
