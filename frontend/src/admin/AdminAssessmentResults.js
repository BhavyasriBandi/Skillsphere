
import React, { useCallback, useEffect, useState } from "react";
import "./AdminAssessmentResults.css";

const API_URL =
  "https://skillsphere-17hl.onrender.com/api/skills/assessments/admin/results/";

function getToken() {
  return (
    localStorage.getItem("skillsphere_access") ||
    localStorage.getItem("access") ||
    ""
  );
}

function formatDate(value) {
  if (!value) return "—";

  const date = new Date(value);

  if (Number.isNaN(date.getTime())) return "—";

  return date.toLocaleString();
}

export default function AdminAssessmentResults() {
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [search, setSearch] = useState("");
  const [skill, setSkill] = useState("All Skills");

  const loadResults = useCallback(async () => {
    const token = getToken();

    if (!token) {
      setError("Admin session expired. Please login again.");
      setLoading(false);
      return;
    }

    setLoading(true);
    setError("");

    try {
      const params = new URLSearchParams();

      if (search.trim()) {
        params.set("search", search.trim());
      }

      if (skill !== "All Skills") {
        params.set("skill", skill);
      }

      const query = params.toString();
      const url = query ? `${API_URL}?${query}` : API_URL;

      const response = await fetch(url, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${token}`,
          Accept: "application/json",
        },
      });

      const data = await response.json().catch(() => ({}));

      if (!response.ok) {
        throw new Error(
          data.detail ||
            data.message ||
            `Unable to load results (${response.status}).`
        );
      }

      setResults(
        Array.isArray(data.results) ? data.results : []
      );
    } catch (err) {
      setError(err.message || "Unable to load assessment results.");
      setResults([]);
    } finally {
      setLoading(false);
    }
  }, [search, skill]);

  useEffect(() => {
    loadResults();
  }, [loadResults]);

  const totalStudents = new Set(
    results.map((item) => item.student_id)
  ).size;

  const averageScore = results.length
    ? (
        results.reduce(
          (sum, item) => sum + Number(item.percentage || 0),
          0
        ) / results.length
      ).toFixed(1)
    : "0.0";

  const averageCorrect = results.length
    ? (
        results.reduce(
          (sum, item) => sum + Number(item.correct_answers || 0),
          0
        ) / results.length
      ).toFixed(1)
    : "0";

  const skills = [
    ...new Set(results.map((item) => item.skill).filter(Boolean)),
  ];

  return (
    <div className="admin-assessment-results">
      <div className="aar-heading">
        <div>
          <span className="aar-eyebrow">STUDENT PERFORMANCE</span>
          <h2>Assessment Results</h2>
          <p>
            View completed student assessments, scores and performance.
          </p>
        </div>

        <button
          type="button"
          className="aar-refresh-button"
          onClick={loadResults}
          disabled={loading}
        >
          ↻ {loading ? "Refreshing..." : "Refresh"}
        </button>
      </div>

      {error && (
        <div className="aar-error" role="alert">
          {error}
        </div>
      )}

      <div className="aar-stat-grid">
        <article className="aar-stat-card">
          <span>Total Assessments</span>
          <strong>{results.length}</strong>
          <small>Completed assessments</small>
        </article>

        <article className="aar-stat-card">
          <span>Students Assessed</span>
          <strong>{totalStudents}</strong>
          <small>Unique students</small>
        </article>

        <article className="aar-stat-card">
          <span>Average Score</span>
          <strong>{averageScore}%</strong>
          <small>Across displayed results</small>
        </article>

        <article className="aar-stat-card">
          <span>Average Correct</span>
          <strong>{averageCorrect}</strong>
          <small>Correct answers per assessment</small>
        </article>
      </div>

      <section className="aar-panel">
        <div className="aar-panel-heading">
          <div>
            <h3>Student Assessment History</h3>
            <p>Search students and filter their completed assessments.</p>
          </div>
        </div>

        <div className="aar-filters">
          <input
            type="search"
            placeholder="Search student name, email or skill..."
            value={search}
            onChange={(event) => setSearch(event.target.value)}
          />

          <select
            value={skill}
            onChange={(event) => setSkill(event.target.value)}
          >
            <option value="All Skills">All Skills</option>
            {skills.map((item) => (
              <option key={item} value={item}>
                {item}
              </option>
            ))}
          </select>
        </div>

        {loading ? (
          <div className="aar-empty">Loading assessment results...</div>
        ) : results.length === 0 ? (
          <div className="aar-empty">
            {error
              ? "Unable to display results."
              : "No completed assessment results found."}
          </div>
        ) : (
          <div className="aar-table-wrapper">
            <table className="aar-table">
              <thead>
                <tr>
                  <th>Student</th>
                  <th>Skill</th>
                  <th>Score</th>
                  <th>Correct</th>
                  <th>Wrong</th>
                  <th>Percentage</th>
                  <th>Completed Date</th>
                </tr>
              </thead>

              <tbody>
                {results.map((item) => (
                  <tr key={item.id}>
                    <td>
                      <strong>{item.student_name}</strong>
                      <small>{item.student_email}</small>
                    </td>

                    <td>
                      <span className="aar-skill">
                        {item.skill}
                      </span>
                    </td>

                    <td>
                      <strong>
                        {item.score}/{item.total_questions}
                      </strong>
                    </td>

                    <td>{item.correct_answers}</td>
                    <td>{item.wrong_answers}</td>

                    <td>
                      <div className="aar-percentage">
                        <strong>{item.percentage}%</strong>
                        <div className="aar-progress">
                          <span
                            style={{
                              width: `${Math.min(
                                Math.max(Number(item.percentage), 0),
                                100
                              )}%`,
                            }}
                          />
                        </div>
                      </div>
                    </td>

                    <td>{formatDate(item.completed_at)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}

        <div className="aar-table-footer">
          Showing {results.length} completed assessment result(s)
        </div>
      </section>
    </div>
  );
}
