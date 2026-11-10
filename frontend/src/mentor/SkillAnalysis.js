
import React, { useCallback, useEffect, useMemo, useState } from "react";
import "./SkillAnalysis.css";

const API_BASE_URL = "https://skillsphere-u93o.onrender.com";

const formatNumber = (value) => {
  const number = Number(value);
  return Number.isFinite(number) ? number : 0;
};

const getInitials = (name = "Student") =>
  name
    .trim()
    .split(/\s+/)
    .slice(0, 2)
    .map((part) => part.charAt(0).toUpperCase())
    .join("");

function SkillAnalysis() {
  const [analysisData, setAnalysisData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [searchTerm, setSearchTerm] = useState("");
  const [selectedLevel, setSelectedLevel] = useState("all");

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

  const summary = analysisData?.summary || {};
  const proficiency = summary.proficiency || {};
  const students = Array.isArray(analysisData?.students)
    ? analysisData.students
    : [];
  const skillBreakdown = Array.isArray(analysisData?.skill_breakdown)
    ? analysisData.skill_breakdown
    : [];

  const filteredStudents = useMemo(() => {
    return students.filter((item) => {
      const student = item.student || {};
      const name = (student.name || "").toLowerCase();
      const email = (student.email || "").toLowerCase();
      const query = searchTerm.trim().toLowerCase();

      const matchesSearch =
        !query || name.includes(query) || email.includes(query);

      const skills = Array.isArray(item.skills) ? item.skills : [];
      const matchesLevel =
        selectedLevel === "all" ||
        skills.some(
          (skill) =>
            (skill.proficiency || "beginner").toLowerCase() === selectedLevel
        );

      return matchesSearch && matchesLevel;
    });
  }, [students, searchTerm, selectedLevel]);

  const summaryCards = [
    {
      title: "Assigned Students",
      value: analysisData?.student_count ?? 0,
      icon: "♙",
      tone: "blue",
      note: "Students assigned to you",
    },
    {
      title: "Total Skills",
      value: summary.total_skills ?? 0,
      icon: "✦",
      tone: "purple",
      note: "Skills across your students",
    },
    {
      title: "Completed Skills",
      value: summary.completed_skills ?? 0,
      icon: "✓",
      tone: "green",
      note: "Successfully completed",
    },
    {
      title: "Incomplete Skills",
      value: summary.incomplete_skills ?? 0,
      icon: "◷",
      tone: "orange",
      note: "Need more attention",
    },
  ];

  const totalProficiency =
    formatNumber(proficiency.beginner) +
    formatNumber(proficiency.intermediate) +
    formatNumber(proficiency.advanced);

  const proficiencyItems = [
    {
      label: "Beginner",
      value: formatNumber(proficiency.beginner),
      className: "beginner",
      color: "#e8a23a",
    },
    {
      label: "Intermediate",
      value: formatNumber(proficiency.intermediate),
      className: "intermediate",
      color: "#4388dc",
    },
    {
      label: "Advanced",
      value: formatNumber(proficiency.advanced),
      className: "advanced",
      color: "#27a879",
    },
  ];

  const assessedSkills = skillBreakdown
    .filter((skill) => skill.average_assessment_percentage !== null &&
      skill.average_assessment_percentage !== undefined)
    .map((skill) => ({
      ...skill,
      score: Math.min(
        100,
        Math.max(0, formatNumber(skill.average_assessment_percentage))
      ),
    }))
    .sort((a, b) => b.score - a.score);

  const topSkill = assessedSkills[0];
  const needsAttention = assessedSkills[assessedSkills.length - 1];

  if (loading) {
    return (
      <section className="mentor-skill-page">
        <div className="msa-state-card">
          <div className="msa-spinner" />
          <h2>Loading Skill Analysis</h2>
          <p>Retrieving your students' skill information...</p>
        </div>
      </section>
    );
  }

  if (error) {
    return (
      <section className="mentor-skill-page">
        <div className="msa-state-card msa-error-card">
          <div className="msa-state-icon">!</div>
          <h2>Unable to Load Skill Analysis</h2>
          <p>{error}</p>
          <button type="button" onClick={fetchSkillAnalysis}>
            Try Again
          </button>
        </div>
      </section>
    );
  }

  return (
    <section className="mentor-skill-page">
      {/* Page heading */}
      <header className="msa-header">
        <div>
          <div className="msa-eyebrow">
            <span className="msa-eyebrow-dot" />
            MENTOR WORKSPACE
          </div>
          <h1>Student Skill Analysis</h1>
          <p>
            Understand student capabilities, track skill completion and
            identify areas that need attention.
          </p>
        </div>

        <button
          className="msa-refresh-button"
          type="button"
          onClick={fetchSkillAnalysis}
        >
          <span>↻</span> Refresh Data
        </button>
      </header>

      {/* Summary cards */}
      <div className="msa-summary-grid">
        {summaryCards.map((card) => (
          <article className="msa-summary-card" key={card.title}>
            <div className={`msa-summary-icon ${card.tone}`}>
              {card.icon}
            </div>
            <div className="msa-summary-content">
              <span>{card.title}</span>
              <strong>{card.value}</strong>
              <small>{card.note}</small>
            </div>
            <div className={`msa-card-accent ${card.tone}`} />
          </article>
        ))}
      </div>

      {/* Proficiency and insights */}
      <div className="msa-overview-grid">
        <article className="msa-panel msa-proficiency-panel">
          <div className="msa-panel-heading">
            <div>
              <span className="msa-section-label">SKILL DISTRIBUTION</span>
              <h2>Proficiency Overview</h2>
              <p>Distribution of student skill levels</p>
            </div>
            <span className="msa-heading-icon">◉</span>
          </div>

          <div className="msa-proficiency-content">
            <div className="msa-donut-wrap">
              <div
                className="msa-donut"
                style={{
                  background: totalProficiency
                    ? `conic-gradient(
                        #e8a23a 0% ${
                          (formatNumber(proficiency.beginner) /
                            totalProficiency) *
                          100
                        }%,
                        #4388dc ${
                          (formatNumber(proficiency.beginner) /
                            totalProficiency) *
                          100
                        }% ${
                          ((formatNumber(proficiency.beginner) +
                            formatNumber(proficiency.intermediate)) /
                            totalProficiency) *
                          100
                        }%,
                        #27a879 ${
                          ((formatNumber(proficiency.beginner) +
                            formatNumber(proficiency.intermediate)) /
                            totalProficiency) *
                          100
                        }% 100%)`
                    : "#e9eef5",
                }}
              >
                <div className="msa-donut-center">
                  <strong>{totalProficiency}</strong>
                  <span>Total levels</span>
                </div>
              </div>
            </div>

            <div className="msa-proficiency-legend">
              {proficiencyItems.map((item) => (
                <div className="msa-legend-item" key={item.label}>
                  <div className="msa-legend-label">
                    <span
                      className={`msa-legend-dot ${item.className}`}
                    />
                    <span>{item.label}</span>
                  </div>
                  <strong>{item.value}</strong>
                </div>
              ))}
            </div>
          </div>
        </article>

        <article className="msa-panel msa-insights-panel">
          <div className="msa-panel-heading">
            <div>
              <span className="msa-section-label">PERFORMANCE INSIGHTS</span>
              <h2>Skill Highlights</h2>
              <p>Based on available assessment averages</p>
            </div>
            <span className="msa-heading-icon">✧</span>
          </div>

          {assessedSkills.length > 0 ? (
            <div className="msa-highlight-list">
              <div className="msa-highlight-item positive">
                <div className="msa-highlight-icon">↗</div>
                <div>
                  <span>Highest average assessment</span>
                  <strong>{topSkill.skill_name}</strong>
                  <small>{topSkill.score}% average score</small>
                </div>
              </div>

              <div className="msa-highlight-item attention">
                <div className="msa-highlight-icon">◎</div>
                <div>
                  <span>Lowest average assessment</span>
                  <strong>{needsAttention.skill_name}</strong>
                  <small>{needsAttention.score}% average score</small>
                </div>
              </div>
            </div>
          ) : (
            <div className="msa-mini-empty">
              <span>◎</span>
              <p>No assessment averages available yet.</p>
            </div>
          )}
        </article>
      </div>

      {/* Skill comparison */}
      <article className="msa-panel">
        <div className="msa-panel-heading msa-chart-heading">
          <div>
            <span className="msa-section-label">ASSESSMENT PERFORMANCE</span>
            <h2>Skill-wise Performance</h2>
            <p>Average assessment percentage for each skill</p>
          </div>
          <span className="msa-chart-unit">Score / 100</span>
        </div>

        {assessedSkills.length > 0 ? (
          <div className="msa-performance-chart">
            {assessedSkills.map((skill) => (
              <div className="msa-performance-row" key={skill.skill_name}>
                <div className="msa-performance-name" title={skill.skill_name}>
                  {skill.skill_name}
                </div>
                <div className="msa-performance-track">
                  <div
                    className="msa-performance-fill"
                    style={{ width: `${skill.score}%` }}
                  />
                </div>
                <strong className="msa-performance-score">
                  {skill.score}%
                </strong>
              </div>
            ))}
          </div>
        ) : (
          <div className="msa-empty-state">
            <span>▥</span>
            <h3>No assessment performance yet</h3>
            <p>Skill averages will appear here when assessment data is available.</p>
          </div>
        )}
      </article>

      {/* Skill breakdown table */}
      <article className="msa-panel">
        <div className="msa-panel-heading">
          <div>
            <span className="msa-section-label">OVERALL BREAKDOWN</span>
            <h2>Skill-wise Analysis</h2>
            <p>Compare proficiency and completion across all skills</p>
          </div>
          <span className="msa-count-badge">
            {skillBreakdown.length} Skills
          </span>
        </div>

        {skillBreakdown.length > 0 ? (
          <div className="msa-table-wrap">
            <table className="msa-table">
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
                    <td className="msa-table-skill">{skill.skill_name}</td>
                    <td>{formatNumber(skill.student_count)}</td>
                    <td>
                      <span className="msa-number-pill beginner">
                        {formatNumber(skill.beginner)}
                      </span>
                    </td>
                    <td>
                      <span className="msa-number-pill intermediate">
                        {formatNumber(skill.intermediate)}
                      </span>
                    </td>
                    <td>
                      <span className="msa-number-pill advanced">
                        {formatNumber(skill.advanced)}
                      </span>
                    </td>
                    <td>{formatNumber(skill.completed)}</td>
                    <td>{formatNumber(skill.incomplete)}</td>
                    <td>
                      {skill.average_assessment_percentage !== null &&
                      skill.average_assessment_percentage !== undefined ? (
                        <strong className="msa-table-score">
                          {skill.average_assessment_percentage}%
                        </strong>
                      ) : (
                        <span className="msa-not-assessed">Not assessed</span>
                      )}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ) : (
          <div className="msa-empty-state">
            <span>▤</span>
            <h3>No skill breakdown available</h3>
            <p>Skill statistics will appear here when student data is available.</p>
          </div>
        )}
      </article>

      {/* Student details */}
      <article className="msa-panel msa-students-panel">
        <div className="msa-panel-heading msa-students-heading">
          <div>
            <span className="msa-section-label">INDIVIDUAL PERFORMANCE</span>
            <h2>Student-wise Skill Details</h2>
            <p>Review each student's skills and proficiency levels</p>
          </div>
          <span className="msa-count-badge">
            {filteredStudents.length} Students
          </span>
        </div>

        <div className="msa-student-toolbar">
          <div className="msa-search-box">
            <span>⌕</span>
            <input
              type="search"
              placeholder="Search student by name or email..."
              value={searchTerm}
              onChange={(event) => setSearchTerm(event.target.value)}
            />
          </div>

          <select
            value={selectedLevel}
            onChange={(event) => setSelectedLevel(event.target.value)}
            aria-label="Filter students by proficiency"
          >
            <option value="all">All proficiency levels</option>
            <option value="beginner">Beginner</option>
            <option value="intermediate">Intermediate</option>
            <option value="advanced">Advanced</option>
          </select>
        </div>

        {filteredStudents.length > 0 ? (
          <div className="msa-student-list">
            {filteredStudents.map((studentItem, index) => {
              const student = studentItem.student || {};
              const skills = Array.isArray(studentItem.skills)
                ? studentItem.skills
                : [];

              return (
                <div
                  className="msa-student-card"
                  key={student.id || student.email || index}
                >
                  <div className="msa-student-top">
                    <div className="msa-student-identity">
                      <div className="msa-student-avatar">
                        {getInitials(student.name)}
                      </div>
                      <div>
                        <h3>{student.name || "Student"}</h3>
                        <p>{student.email || "Email not available"}</p>
                      </div>
                    </div>

                    <div className="msa-student-total">
                      <strong>{formatNumber(studentItem.total_skills)}</strong>
                      <span>Total skills</span>
                    </div>
                  </div>

                  <div className="msa-student-stats">
                    <div>
                      <span className="msa-stat-mark completed">✓</span>
                      <span>Completed</span>
                      <strong>
                        {formatNumber(studentItem.completed_skills)}
                      </strong>
                    </div>
                    <div>
                      <span className="msa-stat-mark incomplete">◷</span>
                      <span>Incomplete</span>
                      <strong>
                        {formatNumber(studentItem.incomplete_skills)}
                      </strong>
                    </div>
                  </div>

                  {skills.length > 0 ? (
                    <div className="msa-student-skills-wrap">
                      <div className="msa-student-skills-title">
                        <strong>Skill details</strong>
                        <span>{skills.length} records</span>
                      </div>

                      <div className="msa-table-wrap">
                        <table className="msa-table msa-student-table">
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
                            {skills.map((skill, skillIndex) => {
                              const level = (
                                skill.proficiency || "beginner"
                              ).toLowerCase();

                              return (
                                <tr key={skill.id || skillIndex}>
                                  <td className="msa-table-skill">
                                    {skill.skill_name}
                                  </td>
                                  <td>{skill.category || "—"}</td>
                                  <td>
                                    <span
                                      className={`msa-level-badge ${level}`}
                                    >
                                      {skill.proficiency || "Beginner"}
                                    </span>
                                  </td>
                                  <td>
                                    <span
                                      className={`msa-status-badge ${
                                        skill.is_completed
                                          ? "completed"
                                          : "incomplete"
                                      }`}
                                    >
                                      {skill.is_completed
                                        ? "Completed"
                                        : "Incomplete"}
                                    </span>
                                  </td>
                                  <td>
                                    {formatNumber(skill.assessment_count)}
                                  </td>
                                </tr>
                              );
                            })}
                          </tbody>
                        </table>
                      </div>
                    </div>
                  ) : (
                    <div className="msa-no-skills">
                      No skills added by this student yet.
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        ) : (
          <div className="msa-empty-state">
            <span>♙</span>
            <h3>No matching students found</h3>
            <p>
              Try changing the search term or proficiency filter.
            </p>
          </div>
        )}
      </article>
    </section>
  );
}

export default SkillAnalysis;
