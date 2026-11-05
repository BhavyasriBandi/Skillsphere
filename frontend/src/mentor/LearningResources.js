
import React, { useEffect, useMemo, useState } from "react";
import "./LearningResources.css";

const API_URL = "http://127.0.0.1:8000/api/mentors/learning-resources/";

function LearningResources() {
  const [resources, setResources] = useState([]);
  const [search, setSearch] = useState("");
  const [category, setCategory] = useState("All");
  const [level, setLevel] = useState("All");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchResources = async () => {
      try {
        setLoading(true);
        setError("");

        const token = localStorage.getItem("skillsphere_access");

        if (!token) {
          setError("Please log in again. Your access token was not found.");
          return;
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
            "You are not authorized to view these resources. Please log in with your Mentor account."
          );
        }

        if (!response.ok) {
          throw new Error(`Unable to load resources. Error: ${response.status}`);
        }

        const data = await response.json();
        setResources(Array.isArray(data.resources) ? data.resources : []);
      } catch (err) {
        setError(err.message || "Something went wrong while loading resources.");
      } finally {
        setLoading(false);
      }
    };

    fetchResources();
  }, []);

  const categories = useMemo(() => {
    return [
      "All",
      ...new Set(resources.map((item) => item.category).filter(Boolean)),
    ];
  }, [resources]);

  const levels = useMemo(() => {
    return [
      "All",
      ...new Set(resources.map((item) => item.level).filter(Boolean)),
    ];
  }, [resources]);

  const filteredResources = useMemo(() => {
    const searchText = search.trim().toLowerCase();

    return resources.filter((item) => {
      const matchesSearch =
        !searchText ||
        item.title?.toLowerCase().includes(searchText) ||
        item.description?.toLowerCase().includes(searchText) ||
        (item.skills || []).some((skill) =>
          skill.toLowerCase().includes(searchText)
        );

      const matchesCategory =
        category === "All" || item.category === category;

      const matchesLevel = level === "All" || item.level === level;

      return matchesSearch && matchesCategory && matchesLevel;
    });
  }, [resources, search, category, level]);

  if (loading) {
    return (
      <div className="mentor-resources-page">
        <div className="mentor-resources-loading">
          <div className="mentor-resources-spinner"></div>
          <p>Loading learning resources...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="mentor-resources-page">
        <div className="mentor-resources-error">
          <span className="mentor-resources-error-icon">!</span>
          <h3>Unable to Load Resources</h3>
          <p>{error}</p>
          <button
            className="mentor-resources-retry"
            onClick={() => window.location.reload()}
          >
            Try Again
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="mentor-resources-page">
      <div className="mentor-resources-header">
        <div>
          <span className="mentor-resources-eyebrow">
            MENTOR WORKSPACE
          </span>
          <h2>Learning Resources</h2>
          <p>
            Explore learning materials and recommend useful resources to
            your students.
          </p>
        </div>

        <div className="mentor-resources-total">
          <span className="mentor-resources-total-icon">📚</span>
          <div>
            <strong>{resources.length}</strong>
            <span>Available Courses</span>
          </div>
        </div>
      </div>

      <div className="mentor-resources-search-panel">
        <div className="mentor-resources-search">
          <span>⌕</span>
          <input
            type="text"
            placeholder="Search courses, skills..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
        </div>

        <select
          value={category}
          onChange={(e) => setCategory(e.target.value)}
          aria-label="Filter by category"
        >
          {categories.map((item) => (
            <option key={item} value={item}>
              {item === "All" ? "All Categories" : item}
            </option>
          ))}
        </select>

        <select
          value={level}
          onChange={(e) => setLevel(e.target.value)}
          aria-label="Filter by level"
        >
          {levels.map((item) => (
            <option key={item} value={item}>
              {item === "All" ? "All Levels" : item}
            </option>
          ))}
        </select>
      </div>

      <div className="mentor-resources-results">
        <h3>Explore Courses</h3>
        <span>{filteredResources.length} courses found</span>
      </div>

      {filteredResources.length === 0 ? (
        <div className="mentor-resources-empty">
          <span>🔎</span>
          <h3>No courses found</h3>
          <p>Try changing your search or filter selections.</p>
          <button
            onClick={() => {
              setSearch("");
              setCategory("All");
              setLevel("All");
            }}
          >
            Clear Filters
          </button>
        </div>
      ) : (
        <div className="mentor-resources-grid">
          {filteredResources.map((course) => (
            <article className="mentor-resource-card" key={course.id}>
              <div className="mentor-resource-card-top">
                <div className="mentor-resource-icon">
                  {course.icon || "📘"}
                </div>
                <span className="mentor-resource-level">
                  {course.level}
                </span>
              </div>

              <span className="mentor-resource-category">
                {course.category}
              </span>

              <h3>{course.title}</h3>
              <p className="mentor-resource-description">
                {course.description}
              </p>

              <div className="mentor-resource-meta">
                <span>◷ {course.duration}</span>
                <span>▤ {course.lesson_count} Lessons</span>
              </div>

              <div className="mentor-resource-skills">
                <strong>Skills covered</strong>
                <div>
                  {(course.skills || []).map((skill) => (
                    <span key={skill}>{skill}</span>
                  ))}
                </div>
              </div>

              <div className="mentor-resource-links">
                <strong>Learning Materials</strong>

                {(course.resources || []).map((resource, index) => (
                  <a
                    key={`${course.id}-${index}`}
                    href={resource.url}
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    <span>{resource.title}</span>
                    <span>↗</span>
                  </a>
                ))}
              </div>
            </article>
          ))}
        </div>
      )}
    </div>
  );
}

export default LearningResources;
