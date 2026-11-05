
import React, { useCallback, useEffect, useState } from "react";
import "./SkillAnalysis.css";

const API_BASE_URL = "http://127.0.0.1:8000";

function SkillAnalysis() {
  const [analysisData, setAnalysisData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const fetchSkillAnalysis = useCallback(async () => {
    try {
      setLoading(true);
      setError("");

      const token = localStorage.getItem("skillsphere_access");

      if (!token) {
        throw new Error("Access token not found. Please login again.");
      }

      const response = await fetch(
        `${API_BASE_URL}/api/mentors/skill-analysis/`,
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
          throw new Error("Only mentors can access Skill Analysis.");
        }

        throw new Error(
          data.detail || data.message || "Unable to load Skill Analysis."
        );
      }

      setAnalysisData(data);
    } catch (err) {
      setError(err.message || "Something went wrong.");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchSkillAnalysis();
  }, [fetchSkillAnalysis]);

  if (loading) {
    return (
      <section className="skill-analysis-page">
        <div className="skill-analysis-message">
          <h2>Loading Skill Analysis...</h2>
          <p>Please wait while we retrieve student skill information.</p>
        </div>
      </section>
    );
  }

  if (error) {
    return (
      <section className="skill-analysis-page">
        <div className="skill-analysis-message">
          <h2>Unable to Load Skill Analysis</h2>
          <p>{error}</p>
          <button type="button" onClick={fetchSkillAnalysis}>
            Try Again
          </button>
        </div>
      </section>
    );
  }

  const summary = analysisData?.summary || {};
  const proficiency = summary.proficiency || {};
  const students = analysisData?.students || [];
  const skillBreakdown = analysisData?.skill_breakdown || [];

  const summaryCards = [
    {
      title: "Total Students",
      value: analysisData?.student_count ?? 0,
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
      icon: "⏳",
    },
  ];

  return (
    <section className="skill-analysis-page">
      <div className="skill-analysis-heading">
        <div>
          <h1>Student Skill Analysis</h1>
          <p>
            Monitor student skills, proficiency levels and assessment
            performance.
          </p>
        </div>

        <button type="button" onClick={fetchSkillAnalysis}>
          ↻ Refresh
        </button>
      </div>

      {/* Summary cards */}
      <div className="skill-analysis-summary">
        {summaryCards.map((card) => (
          <div className="skill-analysis-card" key={card.title}>
            <div className="skill-analysis-card-icon">{card.icon}</div>
            <div>
              <p>{card.title}</p>
              <h2>{card.value}</h2>
            </div>
          </div>
        ))}
      </div>

      {/* Proficiency overview */}
      <div className="skill-analysis-panel">
        <h2>Proficiency Overview</h2>

        <div className="skill-proficiency-grid">
          <div className="skill-proficiency-item beginner">
            <span>Beginner</span>
            <strong>{proficiency.beginner ?? 0}</strong>
          </div>

          <div className="skill-proficiency-item intermediate">
            <span>Intermediate</span>
            <strong>{proficiency.intermediate ?? 0}</strong>
          </div>

          <div className="skill-proficiency-item advanced">
            <span>Advanced</span>
            <strong>{proficiency.advanced ?? 0}</strong>
          </div>
        </div>
      </div>

      {/* Skill breakdown */}
      <div className="skill-analysis-panel">
        <h2>Skill-wise Analysis</h2>

        {skillBreakdown.length > 0 ? (
          <div className="skill-analysis-table-wrapper">
            <table className="skill-analysis-table">
              <thead>
                <tr>
                  <th>Skill</th>
                  <th>Students</th>
                  <th>Beginner</th>
                  <th>Intermediate</th>
                  <th>Advanced</th>
                  <th>Completed</th>
                  <th>Incomplete</th>
                  <th>Avg. Assessment</th>
                </tr>
              </thead>

              <tbody>
                {skillBreakdown.map((skill, index) => (
                  <tr key={`${skill.skill_name}-${index}`}>
                    <td>{skill.skill_name}</td>
                    <td>{skill.student_count}</td>
                    <td>{skill.beginner}</td>
                    <td>{skill.intermediate}</td>
                    <td>{skill.advanced}</td>
                    <td>{skill.completed}</td>
                    <td>{skill.incomplete}</td>
                    <td>
                      {skill.average_assessment_percentage !== null
                        ? `${skill.average_assessment_percentage}%`
                        : "Not assessed"}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : (
          <div className="skill-analysis-empty">
            <span>📊</span>
            <p>No skill breakdown available yet.</p>
          </div>
        )}
      </div>

      {/* Individual student skills */}
      <div className="skill-analysis-panel">
        <h2>Student-wise Skill Details</h2>

        {students.length > 0 ? (
          <div className="skill-student-list">
            {students.map((studentItem) => {
              const student = studentItem.student || {};
              const skills = studentItem.skills || [];

              return (
                <div
                  className="skill-student-card"
                  key={student.id}
                >
                  <div className="skill-student-header">
                    <div className="skill-student-avatar">
                      {(student.name || "S").charAt(0).toUpperCase()}
                    </div>

                    <div>
                      <h3>{student.name || "Student"}</h3>
                      <p>{student.email || ""}</p>
                    </div>
                  </div>

                  <div className="skill-student-stats">
                    <span>
                      Total Skills: <strong>{studentItem.total_skills}</strong>
                    </span>
                    <span>
                      Completed:{" "}
                      <strong>{studentItem.completed_skills}</strong>
                    </span>
                    <span>
                      Incomplete:{" "}
                      <strong>{studentItem.incomplete_skills}</strong>
                    </span>
                  </div>

                  {skills.length > 0 ? (
                    <div className="skill-detail-table-wrapper">
                      <table className="skill-detail-table">
                        <thead>
                          <tr>
                            <th>Skill</th>
                            <th>Category</th>
                            <th>Proficiency</th>
                            <th>Status</th>
                            <th>Assessments</th>
                          </tr>
                        </thead>

                        <tbody>
                          {skills.map((skill) => (
                            <tr key={skill.id}>
                              <td>{skill.skill_name}</td>
                              <td>{skill.category}</td>
                              <td>
                                <span
                                  className={`skill-level ${(
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
                                      ? "skill-status completed"
                                      : "skill-status incomplete"
                                  }
                                >
                                  {skill.is_completed
                                    ? "Completed"
                                    : "Incomplete"}
                                </span>
                              </td>
                              <td>{skill.assessment_count}</td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  ) : (
                    <p className="skill-analysis-empty-text">
                      No skills added by this student yet.
                    </p>
                  )}
                </div>
              );
            })}
          </div>
        ) : (
          <div className="skill-analysis-empty">
            <span>👨‍🎓</span>
            <p>No active assigned students found.</p>
            <small>
              Student skill analysis will appear after students are assigned
              to you.
            </small>
          </div>
        )}
      </div>
    </section>
  );
}

export default SkillAnalysis;
