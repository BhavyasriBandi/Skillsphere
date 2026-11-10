
import React, { useCallback, useEffect, useMemo, useState } from "react";
import "./Assessments.css";

const API_BASE_URL = "https://skillsphere-17hl.onrender.com";

function Assessments() {
  const [assessments, setAssessments] = useState([]);
  const [summary, setSummary] = useState({
    total_assessments: 0,
    overall_assessments: 0,
    skill_assessments: 0,
  });
  const [studentCount, setStudentCount] = useState(0);
  const [search, setSearch] = useState("");
  const [typeFilter, setTypeFilter] = useState("All");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const fetchAssessments = useCallback(async () => {
    setLoading(true);
    setError("");

    try {
      const token = localStorage.getItem("skillsphere_access");

      if (!token) {
        throw new Error("Access token not found. Please login again.");
      }

      const response = await fetch(
        `${API_BASE_URL}/api/mentors/assessments/`,
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
        }
      );

      const data = await response.json();

      if (!response.ok) {
        if (response.status === 401) {
          throw new Error("Session expired. Please login again.");
        }

        throw new Error(
          data.detail || data.message || "Unable to load assessments."
        );
      }

      setAssessments(
        Array.isArray(data.assessments) ? data.assessments : []
      );

      setSummary(
        data.summary || {
          total_assessments: 0,
          overall_assessments: 0,
          skill_assessments: 0,
        }
      );

      setStudentCount(data.student_count || 0);
    } catch (err) {
      setError(err.message || "Something went wrong.");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchAssessments();
  }, [fetchAssessments]);

  const filteredAssessments = useMemo(() => {
    const query = search.trim().toLowerCase();

    return assessments.filter((item) => {
      const matchesSearch =
        !query ||
        (item.student_name || "").toLowerCase().includes(query) ||
        (item.student_email || "").toLowerCase().includes(query) ||
        (item.skill || "").toLowerCase().includes(query);

      const matchesType =
        typeFilter === "All" || item.assessment_type === typeFilter;

      return matchesSearch && matchesType;
    });
  }, [assessments, search, typeFilter]);

  const getLevelClass = (level) => {
    if (!level) return "assessment-level unknown";

    const normalized = level.toLowerCase();

    if (normalized === "advanced") {
      return "assessment-level advanced";
    }

    if (normalized === "intermediate") {
      return "assessment-level intermediate";
    }

    return "assessment-level beginner";
  };

  const formatDate = (value) => {
    if (!value) return "—";

    const date = new Date(value);

    if (Number.isNaN(date.getTime())) return "—";

    return date.toLocaleDateString("en-IN", {
      day: "2-digit",
      month: "short",
      year: "numeric",
    });
  };

  if (loading) {
    return (
      <section className="assessments-page">
        <div className="assessment-state">
          <div className="assessment-spinner" />
          <h3>Loading Assessments</h3>
          <p>Please wait while we retrieve student assessment results.</p>
        </div>
      </section>
    );
  }

  if (error) {
    return (
      <section className="assessments-page">
        <div className="assessment-state">
          <div className="assessment-state-icon">⚠️</div>
          <h3>Unable to Load Assessments</h3>
          <p>{error}</p>
          <button
            type="button"
            className="assessment-primary-button"
            onClick={fetchAssessments}
          >
            Try Again
          </button>
        </div>
      </section>
    );
  }

  return (
    <section className="assessments-page">
      <div className="assessments-heading">
        <div>
          <h1>Student Assessments</h1>
          <p>
            Review student assessment performance and track skill development.
          </p>
        </div>

        <button
          type="button"
          className="assessment-refresh-button"
          onClick={fetchAssessments}
        >
          ↻ Refresh
        </button>
      </div>

      <div className="assessment-stats-grid">
        <div className="assessment-stat-card">
          <div className="assessment-stat-icon">📝</div>
          <div>
            <p>Total Assessments</p>
            <h2>{summary.total_assessments || 0}</h2>
          </div>
        </div>

        <div className="assessment-stat-card">
          <div className="assessment-stat-icon">📊</div>
          <div>
            <p>Overall Assessments</p>
            <h2>{summary.overall_assessments || 0}</h2>
          </div>
        </div>

        <div className="assessment-stat-card">
          <div className="assessment-stat-icon">🎯</div>
          <div>
            <p>Skill Assessments</p>
            <h2>{summary.skill_assessments || 0}</h2>
          </div>
        </div>

        <div className="assessment-stat-card">
          <div className="assessment-stat-icon">👨‍🎓</div>
          <div>
            <p>Active Students</p>
            <h2>{studentCount}</h2>
          </div>
        </div>
      </div>

      <div className="assessment-toolbar">
        <div className="assessment-search">
          <span>⌕</span>
          <input
            type="text"
            placeholder="Search student or skill..."
            value={search}
            onChange={(event) => setSearch(event.target.value)}
          />
        </div>

        <select
          className="assessment-filter"
          value={typeFilter}
          onChange={(event) => setTypeFilter(event.target.value)}
          aria-label="Filter assessment type"
        >
          <option value="All">All Assessment Types</option>
          <option value="Overall Assessment">Overall Assessment</option>
          <option value="Skill Assessment">Skill Assessment</option>
        </select>
      </div>

      <div className="assessment-table-card">
        <div className="assessment-table-heading">
          <div>
            <h3>Assessment Records</h3>
            <p>
              Showing {filteredAssessments.length} of {assessments.length}{" "}
              assessment records
            </p>
          </div>
        </div>

        {filteredAssessments.length > 0 ? (
          <div className="assessment-table-scroll">
            <table className="assessment-table">
              <thead>
                <tr>
                  <th>Student</th>
                  <th>Assessment</th>
                  <th>Skill</th>
                  <th>Score</th>
                  <th>Percentage</th>
                  <th>Level</th>
                  <th>Completed Date</th>
                </tr>
              </thead>

              <tbody>
                {filteredAssessments.map((item) => (
                  <tr key={`${item.assessment_type}-${item.id}`}>
                    <td>
                      <div className="assessment-student-cell">
                        <div className="assessment-student-avatar">
                          {(item.student_name || "S")
                            .charAt(0)
                            .toUpperCase()}
                        </div>
                        <div>
                          <strong>{item.student_name || "Student"}</strong>
                          <span>{item.student_email || "—"}</span>
                        </div>
                      </div>
                    </td>

                    <td>
                      <span className="assessment-type-label">
                        {item.assessment_type}
                      </span>
                    </td>

                    <td>{item.skill || "—"}</td>

                    <td>
                      {item.score ?? 0} / {item.total_questions ?? 0}
                    </td>

                    <td>
                      <strong className="assessment-percentage">
                        {item.percentage ?? 0}%
                      </strong>
                    </td>

                    <td>
                      <span className={getLevelClass(item.estimated_level)}>
                        {item.estimated_level || "Not specified"}
                      </span>
                    </td>

                    <td>{formatDate(item.completed_at)}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : (
          <div className="assessment-empty-state">
            <div>📋</div>
            <h3>
              {assessments.length === 0
                ? "No Assessment Records Yet"
                : "No Matching Assessments"}
            </h3>
            <p>
              {assessments.length === 0
                ? "Assessment results will appear here when your active students complete assessments."
                : "Try changing your search or assessment type filter."}
            </p>

            {assessments.length > 0 && (
              <button
                type="button"
                className="assessment-clear-button"
                onClick={() => {
                  setSearch("");
                  setTypeFilter("All");
                }}
              >
                Clear Filters
              </button>
            )}
          </div>
        )}
      </div>
    </section>
  );
}

export default Assessments;
