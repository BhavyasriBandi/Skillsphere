
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
        throw new Error(
          data.detail || "Unable to load student progress."
        );
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
      <div className="sp-header">
        <div>
          <h2>Student Progress</h2>
          <p>Monitor your students' learning journey and performance.</p>
        </div>

        <button className="sp-refresh-btn" onClick={fetchProgress}>
          ↻ Refresh
        </button>
      </div>

      <div className="sp-summary-grid">
        <div className="sp-summary-card">
          <span>Total Students</span>
          <strong>{students.length}</strong>
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
        </div>
        <div className="sp-summary-card">
          <span>Completed Challenges</span>
          <strong>
            {students.reduce(
              (sum, item) => sum + (item.challenges?.completed_count || 0),
              0
            )}
          </strong>
        </div>
      </div>

      {students.length === 0 ? (
        <div className="sp-empty">
          <div className="sp-empty-icon">👨‍🎓</div>
          <h3>No Active Students Yet</h3>
          <p>Students will appear here after their assignments are accepted.</p>
        </div>
      ) : (
        <>
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
              </div>

              <div className="sp-section">
                <h3>Skill Progress</h3>
                <div className="sp-progress-grid">
                  <div className="sp-progress-card">
                    <span>Total Skills</span>
                    <strong>
                      {selectedStudent.skill_progress?.total_skills || 0}
                    </strong>
                  </div>
                  <div className="sp-progress-card">
                    <span>Completed</span>
                    <strong>
                      {selectedStudent.skill_progress?.completed_skills || 0}
                    </strong>
                  </div>
                  <div className="sp-progress-card">
                    <span>Incomplete</span>
                    <strong>
                      {selectedStudent.skill_progress?.incomplete_skills || 0}
                    </strong>
                  </div>
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
                      {(selectedStudent.skill_progress?.skills || []).map(
                        (skill) => (
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
                                {skill.is_completed ? "Completed" : "In Progress"}
                              </span>
                            </td>
                          </tr>
                        )
                      )}
                    </tbody>
                  </table>
                </div>
              </div>

              <div className="sp-section">
                <h3>Assessment Results</h3>
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
                      {(selectedStudent.assessments?.results || []).map(
                        (result) => (
                          <tr key={`overall-${result.id}`}>
                            <td>{result.skill}</td>
                            <td>{result.score_percentage}%</td>
                            <td>{result.estimated_level}</td>
                            <td>
                              {result.created_at
                                ? new Date(result.created_at).toLocaleDateString()
                                : "—"}
                            </td>
                          </tr>
                        )
                      )}
                      {(selectedStudent.skill_assessments?.results || []).map(
                        (result) => (
                          <tr key={`skill-${result.id}`}>
                            <td>{result.skill}</td>
                            <td>{result.percentage}%</td>
                            <td>Skill Assessment</td>
                            <td>
                              {result.completed_at
                                ? new Date(
                                    result.completed_at
                                  ).toLocaleDateString()
                                : "—"}
                            </td>
                          </tr>
                        )
                      )}
                    </tbody>
                  </table>
                  {!selectedStudent.assessments?.results?.length &&
                    !selectedStudent.skill_assessments?.results?.length && (
                      <p className="sp-no-data">No assessment results yet.</p>
                    )}
                </div>
              </div>

              <div className="sp-section">
                <h3>Learning Hub</h3>
                <div className="sp-progress-grid">
                  <div className="sp-progress-card">
                    <span>Completed Lessons</span>
                    <strong>
                      {selectedStudent.learning_hub?.completed_lessons_count ||
                        0}
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

export default StudentProgress;
