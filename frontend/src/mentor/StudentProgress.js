
import React, { useCallback, useEffect, useMemo, useState } from "react";
import "./StudentProgress.css";

const API_BASE_URL = "http://127.0.0.1:8000";

const StudentProgress = () => {
  const [students, setStudents] = useState([]);
  const [selectedStudentId, setSelectedStudentId] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const fetchProgress = useCallback(async () => {
    setLoading(true);
    setError("");

    try {
      const token = localStorage.getItem("skillsphere_access");

      if (!token) {
        throw new Error("Please login again. Access token not found.");
      }

      const response = await fetch(
        `${API_BASE_URL}/api/mentors/student-progress/`,
        {
          method: "GET",
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Unable to load student progress.");
      }

      const list = Array.isArray(data.students) ? data.students : [];
      setStudents(list);

      setSelectedStudentId((previous) => {
        if (list.some((item) => String(item.student.id) === String(previous))) {
          return previous;
        }
        return list.length ? String(list[0].student.id) : "";
      });
    } catch (err) {
      setError(err.message || "Something went wrong.");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchProgress();
  }, [fetchProgress]);

  const selectedStudent = useMemo(
    () =>
      students.find(
        (item) => String(item.student.id) === String(selectedStudentId)
      ),
    [students, selectedStudentId]
  );

  const assessmentResults = useMemo(() => {
    if (!selectedStudent) return [];

    const overall = (selectedStudent.assessments?.results || []).map(
      (result) => ({
        id: `overall-${result.id}`,
        skill: result.skill || "Assessment",
        score: Number(result.score_percentage),
        level: result.estimated_level || "—",
        date: result.created_at,
      })
    );

    const skill = (selectedStudent.skill_assessments?.results || []).map(
      (result) => ({
        id: `skill-${result.id}`,
        skill: result.skill || "Skill Assessment",
        score: Number(result.percentage),
        level: "Skill Assessment",
        date: result.completed_at,
      })
    );

    return [...overall, ...skill]
      .filter(
        (item) =>
          Number.isFinite(item.score) &&
          item.score >= 0 &&
          item.score <= 100
      )
      .sort((a, b) => {
        const first = a.date ? new Date(a.date).getTime() : 0;
        const second = b.date ? new Date(b.date).getTime() : 0;
        return first - second;
      });
  }, [selectedStudent]);

  const skillStats = selectedStudent?.skill_progress || {};
  const completedSkills = Number(skillStats.completed_skills || 0);
  const incompleteSkills = Number(skillStats.incomplete_skills || 0);
  const totalSkills = Number(skillStats.total_skills || 0);

  const completionPercentage = totalSkills
    ? Math.round((completedSkills / totalSkills) * 100)
    : 0;

  const averageScore = assessmentResults.length
    ? Math.round(
        assessmentResults.reduce((sum, item) => sum + item.score, 0) /
          assessmentResults.length
      )
    : 0;

  const assessmentTrend = assessmentResults.slice(-10);

  if (loading) {
    return (
      <div className="sp-page">
        <div className="sp-loading">Loading student progress...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="sp-page">
        <div className="sp-error">{error}</div>
        <button className="sp-primary-btn" onClick={fetchProgress}>
          Try Again
        </button>
      </div>
    );
  }

  return (
    <div className="sp-page">
      {/* HEADER */}
      <div className="sp-header">
        <div>
          <span className="sp-eyebrow">MENTOR ANALYTICS</span>
          <h2>Student Progress</h2>
          <p>
            Monitor your students' learning journey and performance.
          </p>
        </div>

        <button className="sp-refresh-btn" onClick={fetchProgress}>
          ↻ Refresh
        </button>
      </div>

      {/* OVERALL SUMMARY */}
      <div className="sp-summary-grid">
        <div className="sp-summary-card">
          <span>Total Students</span>
          <strong>{students.length}</strong>
          <small>Assigned to you</small>
        </div>

        <div className="sp-summary-card">
          <span>Total Assessments</span>
          <strong>
            {students.reduce(
              (sum, item) =>
                sum +
                (item.assessments?.total_assessments || 0) +
                (item.skill_assessments?.total_assessments || 0),
              0
            )}
          </strong>
          <small>Assessment attempts</small>
        </div>

        <div className="sp-summary-card">
          <span>Completed Skills</span>
          <strong>
            {students.reduce(
              (sum, item) =>
                sum + (item.skill_progress?.completed_skills || 0),
              0
            )}
          </strong>
          <small>Across all students</small>
        </div>

        <div className="sp-summary-card">
          <span>Completed Challenges</span>
          <strong>
            {students.reduce(
              (sum, item) => sum + (item.challenges?.completed_count || 0),
              0
            )}
          </strong>
          <small>Learning milestones</small>
        </div>
      </div>

      {students.length === 0 ? (
        <div className="sp-empty">
          <div className="sp-empty-icon">👨‍🎓</div>
          <h3>No Active Students Yet</h3>
          <p>
            Students will appear here after their assignments are accepted.
          </p>
        </div>
      ) : (
        <>
          {/* STUDENT SELECTOR */}
          <div className="sp-selector-card">
            <label htmlFor="sp-student-select">Select Student</label>
            <select
              id="sp-student-select"
              value={selectedStudentId}
              onChange={(event) => setSelectedStudentId(event.target.value)}
            >
              {students.map((item) => (
                <option key={item.student.id} value={item.student.id}>
                  {item.student.name} — {item.student.email}
                </option>
              ))}
            </select>
          </div>

          {selectedStudent && (
            <>
              {/* STUDENT PROFILE */}
              <div className="sp-student-card">
                <div className="sp-avatar">
                  {(selectedStudent.student.name || "S")
                    .charAt(0)
                    .toUpperCase()}
                </div>

                <div>
                  <h3>{selectedStudent.student.name}</h3>
                  <p>{selectedStudent.student.email}</p>
                  <span className="sp-active-label">Active Student</span>
                </div>

                <div className="sp-profile-completion">
                  <strong>{completionPercentage}%</strong>
                  <span>Skill completion</span>
                </div>
              </div>

              {/* SKILL PROGRESS */}
              <div className="sp-section">
                <div className="sp-section-heading">
                  <div>
                    <span className="sp-section-kicker">LEARNING OVERVIEW</span>
                    <h3>Skill Progress</h3>
                  </div>
                </div>

                <div className="sp-progress-grid">
                  <div className="sp-progress-card">
                    <span>Total Skills</span>
                    <strong>{totalSkills}</strong>
                  </div>

                  <div className="sp-progress-card">
                    <span>Completed</span>
                    <strong>{completedSkills}</strong>
                  </div>

                  <div className="sp-progress-card">
                    <span>Incomplete</span>
                    <strong>{incompleteSkills}</strong>
                  </div>
                </div>

                {/* SKILL COMPLETION CHART */}
                <div className="sp-chart-grid">
                  <div className="sp-chart-card">
                    <div className="sp-chart-title">
                      <div>
                        <h4>Skill Completion</h4>
                        <p>Completed vs incomplete skills</p>
                      </div>
                    </div>

                    {totalSkills > 0 ? (
                      <div className="sp-donut-layout">
                        <div
                          className="sp-donut-chart"
                          style={{
                            background: `conic-gradient(
                              #397bd1 0% ${completionPercentage}%,
                              #e8edf5 ${completionPercentage}% 100%
                            )`,
                          }}
                        >
                          <div className="sp-donut-inner">
                            <strong>{completionPercentage}%</strong>
                            <span>Completed</span>
                          </div>
                        </div>

                        <div className="sp-chart-legend">
                          <div>
                            <i className="sp-legend-blue" />
                            <span>Completed</span>
                            <strong>{completedSkills}</strong>
                          </div>
                          <div>
                            <i className="sp-legend-grey" />
                            <span>Incomplete</span>
                            <strong>{incompleteSkills}</strong>
                          </div>
                        </div>
                      </div>
                    ) : (
                      <div className="sp-chart-empty">
                        No skill data available yet.
                      </div>
                    )}
                  </div>

                  {/* ASSESSMENT SCORE SUMMARY */}
                  <div className="sp-chart-card">
                    <div className="sp-chart-title">
                      <div>
                        <h4>Assessment Summary</h4>
                        <p>Based on available assessment results</p>
                      </div>
                    </div>

                    <div className="sp-score-highlight">
                      <div className="sp-score-circle">
                        <strong>
                          {assessmentResults.length ? `${averageScore}%` : "—"}
                        </strong>
                      </div>

                      <div>
                        <span>Average Score</span>
                        <h3>{assessmentResults.length}</h3>
                        <p>Recorded assessment results</p>
                      </div>
                    </div>

                    <div className="sp-score-progress">
                      <div>
                        <span>Average performance</span>
                        <strong>
                          {assessmentResults.length ? `${averageScore}%` : "No data"}
                        </strong>
                      </div>
                      <div className="sp-score-track">
                        <div
                          style={{ width: `${averageScore}%` }}
                        />
                      </div>
                    </div>
                  </div>
                </div>

                {/* SKILL TABLE */}
                <div className="sp-subsection-heading">
                  <h4>Individual Skill Details</h4>
                  <span>
                    {(skillStats.skills || []).length} skills
                  </span>
                </div>

                <div className="sp-table-wrapper">
                  <table className="sp-table">
                    <thead>
                      <tr>
                        <th>Skill</th>
                        <th>Category</th>
                        <th>Proficiency</th>
                        <th>Status</th>
                      </tr>
                    </thead>

                    <tbody>
                      {(skillStats.skills || []).map((skill) => (
                        <tr key={skill.id}>
                          <td>{skill.skill_name}</td>
                          <td>{skill.category}</td>
                          <td>
                            <span className="sp-level">
                              {skill.proficiency}
                            </span>
                          </td>
                          <td>
                            <span
                              className={
                                skill.is_completed
                                  ? "sp-status completed"
                                  : "sp-status pending"
                              }
                            >
                              {skill.is_completed
                                ? "Completed"
                                : "In Progress"}
                            </span>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>

                  {!skillStats.skills?.length && (
                    <p className="sp-no-data">No skill records available.</p>
                  )}
                </div>
              </div>

              {/* ASSESSMENT ANALYTICS */}
              <div className="sp-section">
                <div className="sp-section-heading">
                  <div>
                    <span className="sp-section-kicker">PERFORMANCE</span>
                    <h3>Assessment Analytics</h3>
                  </div>
                </div>

                <div className="sp-progress-grid">
                  <div className="sp-progress-card">
                    <span>Overall Assessments</span>
                    <strong>
                      {selectedStudent.assessments?.total_assessments || 0}
                    </strong>
                  </div>

                  <div className="sp-progress-card">
                    <span>Skill Assessments</span>
                    <strong>
                      {selectedStudent.skill_assessments?.total_assessments || 0}
                    </strong>
                  </div>

                  <div className="sp-progress-card">
                    <span>Average Score</span>
                    <strong>
                      {assessmentResults.length ? `${averageScore}%` : "—"}
                    </strong>
                  </div>
                </div>

                {/* ACTUAL SCORE TREND */}
                <div className="sp-chart-card sp-trend-card">
                  <div className="sp-chart-title">
                    <div>
                      <h4>Assessment Performance Trend</h4>
                      <p>
                        Latest {assessmentTrend.length} recorded assessment
                        results, in chronological order
                      </p>
                    </div>

                    <span className="sp-chart-unit">Score (%)</span>
                  </div>

                  {assessmentTrend.length >= 2 ? (
                    <AssessmentLineChart results={assessmentTrend} />
                  ) : assessmentTrend.length === 1 ? (
                    <div className="sp-single-score">
                      <div className="sp-single-score-value">
                        {assessmentTrend[0].score}%
                      </div>
                      <strong>{assessmentTrend[0].skill}</strong>
                      <p>
                        One assessment result is available. Another attempt
                        will allow us to show a performance trend.
                      </p>
                    </div>
                  ) : (
                    <div className="sp-chart-empty">
                      No assessment score history is available yet.
                    </div>
                  )}
                </div>

                {/* ASSESSMENT TABLE */}
                <div className="sp-subsection-heading">
                  <h4>Assessment Results</h4>
                  <span>{assessmentResults.length} results</span>
                </div>

                <div className="sp-table-wrapper">
                  <table className="sp-table">
                    <thead>
                      <tr>
                        <th>Assessment</th>
                        <th>Score</th>
                        <th>Level</th>
                        <th>Date</th>
                      </tr>
                    </thead>

                    <tbody>
                      {assessmentResults.map((result) => (
                        <tr key={result.id}>
                          <td>{result.skill}</td>
                          <td>
                            <strong className="sp-score-value">
                              {result.score}%
                            </strong>
                          </td>
                          <td>{result.level}</td>
                          <td>
                            {result.date
                              ? new Date(result.date).toLocaleDateString()
                              : "—"}
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>

                  {!assessmentResults.length && (
                    <p className="sp-no-data">
                      No assessment results yet.
                    </p>
                  )}
                </div>
              </div>

              {/* LEARNING HUB */}
              <div className="sp-section">
                <div className="sp-section-heading">
                  <div>
                    <span className="sp-section-kicker">LEARNING ACTIVITY</span>
                    <h3>Learning Hub</h3>
                  </div>
                </div>

                <div className="sp-progress-grid">
                  <div className="sp-progress-card">
                    <span>Completed Lessons</span>
                    <strong>
                      {selectedStudent.learning_hub?.completed_lessons_count || 0}
                    </strong>
                  </div>

                  <div className="sp-progress-card">
                    <span>Saved Courses</span>
                    <strong>
                      {selectedStudent.learning_hub?.saved_courses_count || 0}
                    </strong>
                  </div>

                  <div className="sp-progress-card">
                    <span>Completed Challenges</span>
                    <strong>
                      {selectedStudent.challenges?.completed_count || 0}
                    </strong>
                  </div>
                </div>
              </div>
            </>
          )}
        </>
      )}
    </div>
  );
};

/* SVG chart: uses actual assessment scores and dates */
function AssessmentLineChart({ results }) {
  const width = 720;
  const height = 270;
  const paddingLeft = 42;
  const paddingRight = 24;
  const paddingTop = 25;
  const paddingBottom = 48;

  const chartWidth = width - paddingLeft - paddingRight;
  const chartHeight = height - paddingTop - paddingBottom;

  const points = results.map((result, index) => {
    const x =
      paddingLeft +
      (results.length === 1
        ? chartWidth / 2
        : (index / (results.length - 1)) * chartWidth);

    const y =
      paddingTop + ((100 - result.score) / 100) * chartHeight;

    return { ...result, x, y };
  });

  const linePath = points
    .map((point, index) =>
      `${index === 0 ? "M" : "L"} ${point.x} ${point.y}`
    )
    .join(" ");

  const areaPath = `${linePath} L ${points[points.length - 1].x} ${
    paddingTop + chartHeight
  } L ${points[0].x} ${paddingTop + chartHeight} Z`;

  return (
    <div className="sp-line-chart-wrap">
      <svg
        className="sp-line-chart"
        viewBox={`0 0 ${width} ${height}`}
        role="img"
        aria-label="Assessment scores over time"
      >
        <defs>
          <linearGradient id="spTrendFill" x1="0" x2="0" y1="0" y2="1">
            <stop offset="0%" stopColor="#397bd1" stopOpacity="0.24" />
            <stop offset="100%" stopColor="#397bd1" stopOpacity="0.015" />
          </linearGradient>
        </defs>

        {[0, 25, 50, 75, 100].map((value) => {
          const y = paddingTop + ((100 - value) / 100) * chartHeight;

          return (
            <g key={value}>
              <line
                x1={paddingLeft}
                y1={y}
                x2={width - paddingRight}
                y2={y}
                stroke="#e9eef5"
                strokeDasharray="4 5"
              />
              <text
                x={paddingLeft - 10}
                y={y + 4}
                textAnchor="end"
                fontSize="11"
                fill="#8795aa"
              >
                {value}
              </text>
            </g>
          );
        })}

        <path d={areaPath} fill="url(#spTrendFill)" />

        <path
          d={linePath}
          fill="none"
          stroke="#397bd1"
          strokeWidth="3"
          strokeLinecap="round"
          strokeLinejoin="round"
        />

        {points.map((point, index) => (
          <g key={point.id}>
            <circle
              cx={point.x}
              cy={point.y}
              r="8"
              fill="#397bd1"
              opacity="0.13"
            />
            <circle
              cx={point.x}
              cy={point.y}
              r="4"
              fill="#397bd1"
              stroke="#ffffff"
              strokeWidth="2"
            >
              <title>
                {point.skill}: {point.score}%
                {point.date
                  ? ` - ${new Date(point.date).toLocaleDateString()}`
                  : ""}
              </title>
            </circle>

            <text
              x={point.x}
              y={height - 19}
              textAnchor="middle"
              fontSize="10"
              fill="#8290a7"
            >
              {point.date
                ? new Date(point.date).toLocaleDateString(undefined, {
                    day: "numeric",
                    month: "short",
                  })
                : `#${index + 1}`}
            </text>
          </g>
        ))}
      </svg>

      <div className="sp-chart-footnote">
        <span><i /> Assessment score</span>
        <span>Oldest → Latest</span>
      </div>
    </div>
  );
}

export default StudentProgress;
