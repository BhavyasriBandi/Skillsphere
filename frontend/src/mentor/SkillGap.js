
import React, { useCallback, useEffect, useState } from "react";
import "./SkillGap.css";

const API_BASE_URL = "https://skillsphere-17hl.onrender.com";

function SkillGaps() {
  const [gapData, setGapData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [search, setSearch] = useState("");

  const fetchSkillGaps = useCallback(async () => {
    try {
      setLoading(true);
      setError("");

      const token = localStorage.getItem("skillsphere_access");

      if (!token) {
        throw new Error("Access token not found. Please login again.");
      }

      const response = await fetch(
        `${API_BASE_URL}/api/mentors/skill-gaps/`,
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

        if (response.status === 403) {
          throw new Error("Only mentors can access Skill Gaps.");
        }

        throw new Error(
          data.detail || data.message || "Unable to load Skill Gaps."
        );
      }

      setGapData(data);
    } catch (err) {
      setError(err.message || "Something went wrong.");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchSkillGaps();
  }, [fetchSkillGaps]);

  if (loading) {
    return (
      <section className="mentor-skill-gaps">
        <div className="gap-message">
          <h2>Loading Skill Gaps...</h2>
          <p>Please wait while we retrieve student information.</p>
        </div>
      </section>
    );
  }

  if (error) {
    return (
      <section className="mentor-skill-gaps">
        <div className="gap-message">
          <h2>Unable to Load Skill Gaps</h2>
          <p>{error}</p>
          <button onClick={fetchSkillGaps}>Try Again</button>
        </div>
      </section>
    );
  }

  const summary = gapData?.summary || {};
  const proficiency = summary.proficiency || {};
  const students = gapData?.students || [];
  const breakdown = gapData?.skill_breakdown || [];

  const filteredStudents = students.filter((item) => {
    const name = item.student?.name || "";
    const email = item.student?.email || "";
    const query = search.toLowerCase();

    return (
      name.toLowerCase().includes(query) ||
      email.toLowerCase().includes(query)
    );
  });

  const cards = [
    {
      title: "Total Students",
      value: gapData?.student_count ?? 0,
      icon: "👨‍🎓",
    },
    {
      title: "Total Skills",
      value: summary.total_skills ?? 0,
      icon: "💡",
    },
    {
      title: "Completed Skills",
      value: summary.completed_skills ?? 0,
      icon: "✅",
    },
    {
      title: "Incomplete Skills",
      value: summary.incomplete_skills ?? 0,
      icon: "⚠️",
    },
  ];

  return (
    <section className="mentor-skill-gaps">
      <div className="gap-heading">
        <div>
          <h1>Student Skill Gaps</h1>
          <p>
            Identify skill gaps and monitor student skill development.
          </p>
        </div>

        <button onClick={fetchSkillGaps} className="gap-refresh">
          ↻ Refresh
        </button>
      </div>

      {/* Summary */}
      <div className="gap-summary-grid">
        {cards.map((card) => (
          <div className="gap-summary-card" key={card.title}>
            <div className="gap-card-icon">{card.icon}</div>
            <div>
              <p>{card.title}</p>
              <h2>{card.value}</h2>
            </div>
          </div>
        ))}
      </div>

      {/* Overall gap */}
      <div className="gap-overview-panel">
        <div>
          <h2>Overall Skill Gap</h2>
          <p>Percentage of incomplete recorded student skills</p>
        </div>

        <div className="gap-percentage">
          {summary.overall_gap_percentage ?? 0}%
        </div>

        <div className="gap-progress-track">
          <div
            className="gap-progress-fill"
            style={{
              width: `${Math.min(
                100,
                Math.max(0, Number(summary.overall_gap_percentage) || 0)
              )}%`,
            }}
          />
        </div>
      </div>

      {/* Proficiency */}
      <div className="gap-panel">
        <h2>Proficiency Distribution</h2>

        <div className="gap-proficiency-grid">
          <div className="gap-proficiency beginner">
            <span>Beginner</span>
            <strong>{proficiency.beginner ?? 0}</strong>
          </div>

          <div className="gap-proficiency intermediate">
            <span>Intermediate</span>
            <strong>{proficiency.intermediate ?? 0}</strong>
          </div>

          <div className="gap-proficiency advanced">
            <span>Advanced</span>
            <strong>{proficiency.advanced ?? 0}</strong>
          </div>
        </div>
      </div>

      {/* Skill breakdown */}
      <div className="gap-panel">
        <h2>Skill-wise Gap Analysis</h2>

        {breakdown.length > 0 ? (
          <div className="gap-table-wrapper">
            <table className="gap-table">
              <thead>
                <tr>
                  <th>Skill</th>
                  <th>Students</th>
                  <th>Beginner</th>
                  <th>Intermediate</th>
                  <th>Advanced</th>
                  <th>Completed</th>
                  <th>Incomplete</th>
                  <th>Gap %</th>
                </tr>
              </thead>

              <tbody>
                {breakdown.map((skill, index) => (
                  <tr key={`${skill.skill_name}-${index}`}>
                    <td>{skill.skill_name}</td>
                    <td>{skill.student_count}</td>
                    <td>{skill.beginner}</td>
                    <td>{skill.intermediate}</td>
                    <td>{skill.advanced}</td>
                    <td>{skill.completed}</td>
                    <td>{skill.incomplete}</td>
                    <td>
                      <span className="gap-percentage-badge">
                        {skill.gap_percentage}%
                      </span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : (
          <div className="gap-empty">
            <span>📊</span>
            <p>No skill gap data available yet.</p>
          </div>
        )}
      </div>

      {/* Student details */}
      <div className="gap-panel">
        <div className="gap-student-heading">
          <h2>Student-wise Skill Gaps</h2>

          <input
            type="text"
            placeholder="Search students..."
            value={search}
            onChange={(event) => setSearch(event.target.value)}
          />
        </div>

        {filteredStudents.length > 0 ? (
          <div className="gap-student-list">
            {filteredStudents.map((item) => {
              const student = item.student || {};

              return (
                <div className="gap-student-card" key={student.id}>
                  <div className="gap-student-header">
                    <div className="gap-student-avatar">
                      {(student.name || "S").charAt(0).toUpperCase()}
                    </div>

                    <div>
                      <h3>{student.name || "Student"}</h3>
                      <p>{student.email || ""}</p>
                    </div>

                    <div className="gap-student-percentage">
                      {item.skill_gap_percentage}%
                      <small>Skill Gap</small>
                    </div>
                  </div>

                  <div className="gap-student-stats">
                    <span>
                      Total: <strong>{item.total_skills}</strong>
                    </span>
                    <span>
                      Completed: <strong>{item.completed_skills}</strong>
                    </span>
                    <span>
                      Incomplete: <strong>{item.incomplete_skills}</strong>
                    </span>
                  </div>

                  <div className="gap-student-progress-track">
                    <div
                      className="gap-student-progress-fill"
                      style={{
                        width: `${Math.min(
                          100,
                          Math.max(
                            0,
                            Number(item.completion_percentage) || 0
                          )
                        )}%`,
                      }}
                    />
                  </div>

                  <p className="gap-completion-label">
                    Skill Completion: {item.completion_percentage}%
                  </p>

                  {item.skills?.length > 0 ? (
                    <div className="gap-table-wrapper">
                      <table className="gap-detail-table">
                        <thead>
                          <tr>
                            <th>Skill</th>
                            <th>Category</th>
                            <th>Proficiency</th>
                            <th>Status</th>
                          </tr>
                        </thead>

                        <tbody>
                          {item.skills.map((skill) => (
                            <tr key={skill.id}>
                              <td>{skill.skill_name}</td>
                              <td>{skill.category}</td>
                              <td>
                                <span
                                  className={`gap-level ${(
                                    skill.proficiency || "beginner"
                                  ).toLowerCase()}`}
                                >
                                  {skill.proficiency}
                                </span>
                              </td>
                              <td>
                                <span
                                  className={
                                    skill.is_completed
                                      ? "gap-status completed"
                                      : "gap-status incomplete"
                                  }
                                >
                                  {skill.gap_status}
                                </span>
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  ) : (
                    <p className="gap-no-skills">
                      No skills recorded for this student.
                    </p>
                  )}
                </div>
              );
            })}
          </div>
        ) : (
          <div className="gap-empty">
            <span>👨‍🎓</span>
            <p>
              {search
                ? "No matching students found."
                : "No active assigned students found."}
            </p>
          </div>
        )}
      </div>
    </section>
  );
}

export default SkillGaps;
