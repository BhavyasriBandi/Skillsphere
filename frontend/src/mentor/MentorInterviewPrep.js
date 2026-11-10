
import React, { useEffect, useMemo, useState } from "react";
import "./MentorInterviewPrep.css";

const API_URL = "https://skillsphere-u93o.onrender.com/api/mentors/interview-prep/";

const CATEGORIES = [
  "All",
  "Python",
  "Java",
  "C",
  "SQL",
  "React",
  "Django",
  "Data Structures",
  "Web Development",
  "HR",
  "Aptitude",
  "Other",
];

const DIFFICULTIES = [
  "All",
  "Beginner",
  "Intermediate",
  "Advanced",
];

function MentorInterviewPrep() {
  const [practices, setPractices] = useState([]);
  const [statistics, setStatistics] = useState({
    total_practices: 0,
    practiced: 0,
    pending: 0,
    bookmarked: 0,
  });

  const [search, setSearch] = useState("");
  const [category, setCategory] = useState("All");
  const [difficulty, setDifficulty] = useState("All");
  const [practiceFilter, setPracticeFilter] = useState("All");

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchInterviewPrep = async () => {
      try {
        setLoading(true);
        setError("");

        const token = localStorage.getItem("skillsphere_access");

        if (!token) {
          throw new Error("Access token not found. Please log in again.");
        }

        const response = await fetch(API_URL, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${token}`,
          },
        });

        if (response.status === 401 || response.status === 403) {
          throw new Error(
            "You are not authorized to view interview preparation records."
          );
        }

        if (!response.ok) {
          throw new Error(
            `Unable to load interview preparation. Error: ${response.status}`
          );
        }

        const data = await response.json();

        setPractices(
          Array.isArray(data.practices) ? data.practices : []
        );

        setStatistics(
          data.statistics || {
            total_practices: 0,
            practiced: 0,
            pending: 0,
            bookmarked: 0,
          }
        );
      } catch (err) {
        setError(
          err.message || "Something went wrong while loading interview prep."
        );
      } finally {
        setLoading(false);
      }
    };

    fetchInterviewPrep();
  }, []);

  const filteredPractices = useMemo(() => {
    const searchText = search.trim().toLowerCase();

    return practices.filter((practice) => {
      const question = practice.question_details || {};

      const matchesSearch =
        !searchText ||
        question.question?.toLowerCase().includes(searchText) ||
        question.category?.toLowerCase().includes(searchText) ||
        practice.student_name?.toLowerCase().includes(searchText) ||
        practice.student_email?.toLowerCase().includes(searchText) ||
        practice.student_answer?.toLowerCase().includes(searchText);

      const matchesCategory =
        category === "All" || question.category === category;

      const matchesDifficulty =
        difficulty === "All" || question.difficulty === difficulty;

      const matchesPractice =
        practiceFilter === "All" ||
        (practiceFilter === "Practiced" && practice.is_practiced) ||
        (practiceFilter === "Pending" && !practice.is_practiced) ||
        (practiceFilter === "Bookmarked" && practice.is_bookmarked);

      return (
        matchesSearch &&
        matchesCategory &&
        matchesDifficulty &&
        matchesPractice
      );
    });
  }, [practices, search, category, difficulty, practiceFilter]);

  const formatDate = (dateString) => {
    if (!dateString) return "Not practiced yet";

    const date = new Date(dateString);

    if (Number.isNaN(date.getTime())) return "Not available";

    return date.toLocaleDateString("en-IN", {
      day: "2-digit",
      month: "short",
      year: "numeric",
    });
  };

  const getDifficultyClass = (value) => {
    switch (value) {
      case "Beginner":
        return "beginner";
      case "Intermediate":
        return "intermediate";
      case "Advanced":
        return "advanced";
      default:
        return "";
    }
  };

  if (loading) {
    return (
      <div className="mentor-interview-page">
        <div className="mentor-interview-loading">
          <div className="mentor-interview-spinner"></div>
          <p>Loading interview preparation...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="mentor-interview-page">
        <div className="mentor-interview-error">
          <span>!</span>
          <h3>Unable to Load Interview Prep</h3>
          <p>{error}</p>
          <button onClick={() => window.location.reload()}>
            Try Again
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="mentor-interview-page">
      <div className="mentor-interview-header">
        <div>
          <span className="mentor-interview-eyebrow">
            MENTOR WORKSPACE
          </span>
          <h2>Interview Preparation</h2>
          <p>
            Monitor your assigned students' interview practice and preparation.
          </p>
        </div>

        <div className="mentor-interview-total">
          <span>🎯</span>
          <div>
            <strong>{statistics.total_practices}</strong>
            <small>Total Practices</small>
          </div>
        </div>
      </div>

      <div className="mentor-interview-stats">
        <div className="mentor-interview-stat">
          <span>📚</span>
          <div>
            <strong>{statistics.total_practices}</strong>
            <small>Total Practices</small>
          </div>
        </div>

        <div className="mentor-interview-stat">
          <span>✅</span>
          <div>
            <strong>{statistics.practiced}</strong>
            <small>Practiced</small>
          </div>
        </div>

        <div className="mentor-interview-stat">
          <span>⏳</span>
          <div>
            <strong>{statistics.pending}</strong>
            <small>Pending</small>
          </div>
        </div>

        <div className="mentor-interview-stat">
          <span>⭐</span>
          <div>
            <strong>{statistics.bookmarked}</strong>
            <small>Bookmarked</small>
          </div>
        </div>
      </div>

      <div className="mentor-interview-filter-panel">
        <div className="mentor-interview-search">
          <span>⌕</span>
          <input
            type="text"
            placeholder="Search student, question or answer..."
            value={search}
            onChange={(event) => setSearch(event.target.value)}
          />
        </div>

        <select
          value={category}
          onChange={(event) => setCategory(event.target.value)}
          aria-label="Filter by category"
        >
          {CATEGORIES.map((item) => (
            <option key={item} value={item}>
              {item === "All" ? "All Categories" : item}
            </option>
          ))}
        </select>

        <select
          value={difficulty}
          onChange={(event) => setDifficulty(event.target.value)}
          aria-label="Filter by difficulty"
        >
          {DIFFICULTIES.map((item) => (
            <option key={item} value={item}>
              {item === "All" ? "All Difficulties" : item}
            </option>
          ))}
        </select>

        <select
          value={practiceFilter}
          onChange={(event) => setPracticeFilter(event.target.value)}
          aria-label="Filter by practice status"
        >
          <option value="All">All Practice</option>
          <option value="Practiced">Practiced</option>
          <option value="Pending">Pending</option>
          <option value="Bookmarked">Bookmarked</option>
        </select>
      </div>

      <div className="mentor-interview-results">
        <h3>Student Interview Practices</h3>
        <span>{filteredPractices.length} records found</span>
      </div>

      {filteredPractices.length === 0 ? (
        <div className="mentor-interview-empty">
          <span>🎯</span>
          <h3>No interview practices found</h3>
          <p>
            There are no matching practice records. Try changing your filters.
          </p>

          <button
            onClick={() => {
              setSearch("");
              setCategory("All");
              setDifficulty("All");
              setPracticeFilter("All");
            }}
          >
            Clear Filters
          </button>
        </div>
      ) : (
        <div className="mentor-interview-grid">
          {filteredPractices.map((practice) => {
            const question = practice.question_details || {};

            return (
              <article
                className="mentor-interview-card"
                key={practice.id}
              >
                <div className="mentor-interview-card-top">
                  <span className="mentor-interview-category">
                    {question.category || "Other"}
                  </span>

                  <span
                    className={`mentor-interview-difficulty ${getDifficultyClass(
                      question.difficulty
                    )}`}
                  >
                    {question.difficulty || "Not specified"}
                  </span>
                </div>

                <h3>{question.question || "Question not available"}</h3>

                <div className="mentor-interview-student">
                  <div className="mentor-interview-avatar">
                    {(practice.student_name || "S")
                      .charAt(0)
                      .toUpperCase()}
                  </div>

                  <div>
                    <strong>
                      {practice.student_name || "Student"}
                    </strong>
                    <span>
                      {practice.student_email || "Email not available"}
                    </span>
                  </div>
                </div>

                <div className="mentor-interview-answer">
                  <strong>Student's Answer</strong>
                  <p>
                    {practice.student_answer?.trim()
                      ? practice.student_answer
                      : "The student has not submitted an answer yet."}
                  </p>
                </div>

                {question.keywords?.length > 0 && (
                  <div className="mentor-interview-keywords">
                    <strong>Important Keywords</strong>
                    <div>
                      {question.keywords.map((keyword) => (
                        <span key={keyword}>{keyword}</span>
                      ))}
                    </div>
                  </div>
                )}

                <div className="mentor-interview-meta">
                  <span>
                    {practice.is_practiced ? "✓ Practiced" : "○ Pending"}
                  </span>

                  <span>
                    {practice.is_bookmarked ? "★ Bookmarked" : "Not bookmarked"}
                  </span>
                </div>

                <div className="mentor-interview-date">
                  Last practiced:{" "}
                  {formatDate(practice.last_practiced_at)}
                </div>

                {question.suggested_answer && (
                  <details className="mentor-interview-suggested">
                    <summary>View Suggested Answer</summary>
                    <p>{question.suggested_answer}</p>
                  </details>
                )}

                {question.explanation && (
                  <details className="mentor-interview-suggested">
                    <summary>View Explanation</summary>
                    <p>{question.explanation}</p>
                  </details>
                )}
              </article>
            );
          })}
        </div>
      )}
    </div>
  );
}

export default MentorInterviewPrep;
