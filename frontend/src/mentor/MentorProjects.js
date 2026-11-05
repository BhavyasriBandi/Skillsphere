
import React, { useEffect, useMemo, useState } from "react";
import "./MentorProjects.css";

const API_URL = "http://127.0.0.1:8000/api/mentors/projects/";

const PROJECT_STATUSES = [
  "All",
  "Planning",
  "In Progress",
  "Completed",
  "On Hold",
];

const PROJECT_CATEGORIES = [
  "All",
  "Web Development",
  "Full Stack",
  "AI / Machine Learning",
  "Data Science",
  "Mobile Development",
  "Database",
  "Other",
];

function MentorProjects() {
  const [projects, setProjects] = useState([]);
  const [search, setSearch] = useState("");
  const [selectedStatus, setSelectedStatus] = useState("All");
  const [selectedCategory, setSelectedCategory] = useState("All");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const fetchProjects = async () => {
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
          "You are not authorized to view these projects. Please log in with your Mentor account."
        );
      }

      if (!response.ok) {
        throw new Error(`Unable to load projects. Error: ${response.status}`);
      }

      const data = await response.json();

      setProjects(Array.isArray(data.projects) ? data.projects : []);
    } catch (err) {
      setError(err.message || "Something went wrong while loading projects.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProjects();
  }, []);

  const filteredProjects = useMemo(() => {
    const searchText = search.trim().toLowerCase();

    return projects.filter((project) => {
      const matchesSearch =
        !searchText ||
        project.title?.toLowerCase().includes(searchText) ||
        project.description?.toLowerCase().includes(searchText) ||
        project.student_name?.toLowerCase().includes(searchText) ||
        project.student_email?.toLowerCase().includes(searchText) ||
        (project.technologies || []).some((technology) =>
          technology.toLowerCase().includes(searchText)
        );

      const matchesStatus =
        selectedStatus === "All" || project.status === selectedStatus;

      const matchesCategory =
        selectedCategory === "All" ||
        project.category === selectedCategory;

      return matchesSearch && matchesStatus && matchesCategory;
    });
  }, [projects, search, selectedStatus, selectedCategory]);

  const completedCount = projects.filter(
    (project) => project.status === "Completed"
  ).length;

  const inProgressCount = projects.filter(
    (project) => project.status === "In Progress"
  ).length;

  const planningCount = projects.filter(
    (project) => project.status === "Planning"
  ).length;

  const getStatusClass = (status) => {
    switch (status) {
      case "Completed":
        return "completed";
      case "In Progress":
        return "in-progress";
      case "On Hold":
        return "on-hold";
      case "Planning":
        return "planning";
      default:
        return "";
    }
  };

  const formatDate = (dateString) => {
    if (!dateString) return "Not available";

    const date = new Date(dateString);

    if (Number.isNaN(date.getTime())) return "Not available";

    return date.toLocaleDateString("en-IN", {
      day: "2-digit",
      month: "short",
      year: "numeric",
    });
  };

  if (loading) {
    return (
      <div className="mentor-projects-page">
        <div className="mentor-projects-loading">
          <div className="mentor-projects-spinner"></div>
          <p>Loading student projects...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="mentor-projects-page">
        <div className="mentor-projects-error">
          <span className="mentor-projects-error-icon">!</span>
          <h3>Unable to Load Projects</h3>
          <p>{error}</p>
          <button onClick={fetchProjects}>Try Again</button>
        </div>
      </div>
    );
  }

  return (
    <div className="mentor-projects-page">
      <div className="mentor-projects-header">
        <div>
          <span className="mentor-projects-eyebrow">
            MENTOR WORKSPACE
          </span>
          <h2>Student Projects</h2>
          <p>
            View and monitor projects submitted by your assigned students.
          </p>
        </div>

        <div className="mentor-projects-total">
          <span className="mentor-projects-total-icon">📁</span>
          <div>
            <strong>{projects.length}</strong>
            <span>Total Projects</span>
          </div>
        </div>
      </div>

      <div className="mentor-projects-stats">
        <div className="mentor-project-stat">
          <span className="mentor-project-stat-icon">📂</span>
          <div>
            <strong>{projects.length}</strong>
            <span>Total Projects</span>
          </div>
        </div>

        <div className="mentor-project-stat">
          <span className="mentor-project-stat-icon">🚀</span>
          <div>
            <strong>{inProgressCount}</strong>
            <span>In Progress</span>
          </div>
        </div>

        <div className="mentor-project-stat">
          <span className="mentor-project-stat-icon">✅</span>
          <div>
            <strong>{completedCount}</strong>
            <span>Completed</span>
          </div>
        </div>

        <div className="mentor-project-stat">
          <span className="mentor-project-stat-icon">📝</span>
          <div>
            <strong>{planningCount}</strong>
            <span>Planning</span>
          </div>
        </div>
      </div>

      <div className="mentor-projects-filter-panel">
        <div className="mentor-projects-search">
          <span>⌕</span>
          <input
            type="text"
            placeholder="Search project, student or technology..."
            value={search}
            onChange={(event) => setSearch(event.target.value)}
          />
        </div>

        <select
          value={selectedStatus}
          onChange={(event) => setSelectedStatus(event.target.value)}
          aria-label="Filter by project status"
        >
          {PROJECT_STATUSES.map((item) => (
            <option key={item} value={item}>
              {item === "All" ? "All Statuses" : item}
            </option>
          ))}
        </select>

        <select
          value={selectedCategory}
          onChange={(event) => setSelectedCategory(event.target.value)}
          aria-label="Filter by project category"
        >
          {PROJECT_CATEGORIES.map((item) => (
            <option key={item} value={item}>
              {item === "All" ? "All Categories" : item}
            </option>
          ))}
        </select>
      </div>

      <div className="mentor-projects-results">
        <h3>Projects Overview</h3>
        <span>{filteredProjects.length} projects found</span>
      </div>

      {filteredProjects.length === 0 ? (
        <div className="mentor-projects-empty">
          <span>📂</span>
          <h3>No projects found</h3>
          <p>
            There are no matching projects. Try changing your search or
            filters.
          </p>
          <button
            onClick={() => {
              setSearch("");
              setSelectedStatus("All");
              setSelectedCategory("All");
            }}
          >
            Clear Filters
          </button>
        </div>
      ) : (
        <div className="mentor-projects-grid">
          {filteredProjects.map((project) => (
            <article className="mentor-project-card" key={project.id}>
              <div className="mentor-project-card-top">
                <div className="mentor-project-icon">📁</div>

                <span
                  className={`mentor-project-status ${getStatusClass(
                    project.status
                  )}`}
                >
                  {project.status}
                </span>
              </div>

              <span className="mentor-project-category">
                {project.category}
              </span>

              <h3>{project.title}</h3>

              <p className="mentor-project-description">
                {project.description || "No project description provided."}
              </p>

              <div className="mentor-project-student">
                <div className="mentor-project-avatar">
                  {(project.student_name || "S")
                    .charAt(0)
                    .toUpperCase()}
                </div>

                <div>
                  <strong>{project.student_name || "Student"}</strong>
                  <span>{project.student_email || "Email not available"}</span>
                </div>
              </div>

              <div className="mentor-project-technologies">
                <strong>Technologies</strong>
                <div>
                  {(project.technologies || []).length > 0 ? (
                    project.technologies.map((technology) => (
                      <span key={technology}>{technology}</span>
                    ))
                  ) : (
                    <span>Not specified</span>
                  )}
                </div>
              </div>

              <div className="mentor-project-dates">
                <span>
                  Created: {formatDate(project.created_at)}
                </span>
                <span>
                  Updated: {formatDate(project.updated_at)}
                </span>
              </div>

              <div className="mentor-project-links">
                {project.github ? (
                  <a
                    href={project.github}
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    GitHub Repository ↗
                  </a>
                ) : (
                  <span className="mentor-project-no-link">
                    GitHub not provided
                  </span>
                )}

                {project.live_demo ? (
                  <a
                    href={project.live_demo}
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    Live Demo ↗
                  </a>
                ) : (
                  <span className="mentor-project-no-link">
                    Live demo not provided
                  </span>
                )}
              </div>
            </article>
          ))}
        </div>
      )}
    </div>
  );
}

export default MentorProjects;
