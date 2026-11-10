
import React, { useCallback, useEffect, useMemo, useState } from "react";
import "./Roadmaps.css";

const API_BASE_URL = "https://skillsphere-u93o.onrender.com";

function Roadmaps() {
  const [roadmaps, setRoadmaps] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [search, setSearch] = useState("");
  const [selectedLevel, setSelectedLevel] = useState("All");
  const [selectedRoadmap, setSelectedRoadmap] = useState(null);

  const fetchRoadmaps = useCallback(async () => {
    try {
      setLoading(true);
      setError("");

      const token = localStorage.getItem("skillsphere_access");

      if (!token) {
        throw new Error("Access token not found. Please login again.");
      }

      const response = await fetch(
        `${API_BASE_URL}/api/mentors/roadmaps/`,
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
          throw new Error("Only mentors can access Roadmaps.");
        }

        throw new Error(
          data.detail || data.message || "Unable to load roadmaps."
        );
      }

      setRoadmaps(
        Array.isArray(data.roadmaps) ? data.roadmaps : []
      );
    } catch (err) {
      setError(err.message || "Something went wrong.");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchRoadmaps();
  }, [fetchRoadmaps]);

  const filteredRoadmaps = useMemo(() => {
    const query = search.trim().toLowerCase();

    return roadmaps.filter((roadmap) => {
      const matchesSearch =
        !query ||
        (roadmap.title || "").toLowerCase().includes(query) ||
        (roadmap.target_role || "").toLowerCase().includes(query) ||
        (roadmap.category || "").toLowerCase().includes(query) ||
        (roadmap.description || "").toLowerCase().includes(query);

      const matchesLevel =
        selectedLevel === "All" ||
        roadmap.level === selectedLevel;

      return matchesSearch && matchesLevel;
    });
  }, [roadmaps, search, selectedLevel]);

  if (loading) {
    return (
      <section className="mentor-roadmaps-page">
        <div className="roadmaps-message">
          <h2>Loading Roadmaps...</h2>
          <p>Please wait while we retrieve career roadmaps.</p>
        </div>
      </section>
    );
  }

  if (error) {
    return (
      <section className="mentor-roadmaps-page">
        <div className="roadmaps-message">
          <h2>Unable to Load Roadmaps</h2>
          <p>{error}</p>
          <button type="button" onClick={fetchRoadmaps}>
            Try Again
          </button>
        </div>
      </section>
    );
  }

  return (
    <section className="mentor-roadmaps-page">
      {/* Page heading */}
      <div className="roadmaps-heading">
        <div>
          <h1>Career Roadmaps</h1>
          <p>
            Explore career paths, required skills and structured
            learning journeys for your students.
          </p>
        </div>

        <button
          type="button"
          className="roadmaps-refresh-button"
          onClick={fetchRoadmaps}
        >
          ↻ Refresh
        </button>
      </div>

      {/* Summary */}
      <div className="roadmaps-summary-grid">
        <div className="roadmaps-summary-card">
          <div className="roadmaps-summary-icon">🗺️</div>
          <div>
            <p>Available Roadmaps</p>
            <h2>{roadmaps.length}</h2>
          </div>
        </div>

        <div className="roadmaps-summary-card">
          <div className="roadmaps-summary-icon">🌱</div>
          <div>
            <p>Beginner</p>
            <h2>
              {roadmaps.filter((item) => item.level === "Beginner").length}
            </h2>
          </div>
        </div>

        <div className="roadmaps-summary-card">
          <div className="roadmaps-summary-icon">📘</div>
          <div>
            <p>Intermediate</p>
            <h2>
              {roadmaps.filter((item) => item.level === "Intermediate").length}
            </h2>
          </div>
        </div>

        <div className="roadmaps-summary-card">
          <div className="roadmaps-summary-icon">🚀</div>
          <div>
            <p>Advanced</p>
            <h2>
              {roadmaps.filter((item) => item.level === "Advanced").length}
            </h2>
          </div>
        </div>
      </div>

      {/* Search and filters */}
      <div className="roadmaps-filter-panel">
        <input
          type="text"
          placeholder="Search by roadmap, career role or category..."
          value={search}
          onChange={(event) => setSearch(event.target.value)}
        />

        <select
          value={selectedLevel}
          onChange={(event) => setSelectedLevel(event.target.value)}
        >
          <option value="All">All Levels</option>
          <option value="Beginner">Beginner</option>
          <option value="Intermediate">Intermediate</option>
          <option value="Advanced">Advanced</option>
        </select>
      </div>

      {/* Roadmap cards */}
      <div className="roadmaps-results-heading">
        <h2>Available Career Paths</h2>
        <span>{filteredRoadmaps.length} roadmaps found</span>
      </div>

      {filteredRoadmaps.length > 0 ? (
        <div className="roadmaps-grid">
          {filteredRoadmaps.map((roadmap) => (
            <article className="roadmap-card" key={roadmap.id}>
              {roadmap.image_url ? (
                <img
                  className="roadmap-card-image"
                  src={roadmap.image_url}
                  alt={roadmap.title}
                />
              ) : (
                <div className="roadmap-card-placeholder">
                  <span>🗺️</span>
                </div>
              )}

              <div className="roadmap-card-content">
                <div className="roadmap-card-top">
                  <span className="roadmap-category">
                    {roadmap.category || "Career"}
                  </span>

                  <span
                    className={`roadmap-level ${(
                      roadmap.level || "Beginner"
                    ).toLowerCase()}`}
                  >
                    {roadmap.level || "Beginner"}
                  </span>
                </div>

                <h3>{roadmap.title}</h3>

                <p className="roadmap-description">
                  {roadmap.description || "No description available."}
                </p>

                <div className="roadmap-card-info">
                  <div>
                    <span>🎯</span>
                    <p>
                      <small>Target Role</small>
                      <strong>{roadmap.target_role || "Not specified"}</strong>
                    </p>
                  </div>

                  <div>
                    <span>⏱️</span>
                    <p>
                      <small>Duration</small>
                      <strong>{roadmap.duration || "Not specified"}</strong>
                    </p>
                  </div>
                </div>

                <div className="roadmap-skills-preview">
                  <strong>Key Skills</strong>

                  <div className="roadmap-skill-tags">
                    {(roadmap.skills || []).slice(0, 4).map((skill, index) => (
                      <span key={`${roadmap.id}-skill-${index}`}>
                        {typeof skill === "string"
                          ? skill
                          : skill.name || skill.title || "Skill"}
                      </span>
                    ))}

                    {(roadmap.skills || []).length === 0 && (
                      <small>No skills listed</small>
                    )}

                    {(roadmap.skills || []).length > 4 && (
                      <span>
                        +{roadmap.skills.length - 4} more
                      </span>
                    )}
                  </div>
                </div>

                <button
                  type="button"
                  className="roadmap-view-button"
                  onClick={() => setSelectedRoadmap(roadmap)}
                >
                  View Roadmap Details →
                </button>
              </div>
            </article>
          ))}
        </div>
      ) : (
        <div className="roadmaps-empty">
          <span>🗺️</span>
          <h3>No Roadmaps Found</h3>
          <p>
            {roadmaps.length === 0
              ? "No active roadmaps are available yet."
              : "Try changing your search or level filter."}
          </p>
        </div>
      )}

      {/* Roadmap details modal */}
      {selectedRoadmap && (
        <div
          className="roadmap-modal-overlay"
          onClick={() => setSelectedRoadmap(null)}
        >
          <div
            className="roadmap-modal"
            onClick={(event) => event.stopPropagation()}
          >
            <div className="roadmap-modal-header">
              <div>
                <span className="roadmap-category">
                  {selectedRoadmap.category}
                </span>
                <h2>{selectedRoadmap.title}</h2>
              </div>

              <button
                type="button"
                className="roadmap-modal-close"
                onClick={() => setSelectedRoadmap(null)}
                aria-label="Close roadmap details"
              >
                ×
              </button>
            </div>

            <p className="roadmap-modal-description">
              {selectedRoadmap.description}
            </p>

            <div className="roadmap-modal-info">
              <div>
                <small>Target Role</small>
                <strong>{selectedRoadmap.target_role}</strong>
              </div>

              <div>
                <small>Level</small>
                <strong>{selectedRoadmap.level}</strong>
              </div>

              <div>
                <small>Duration</small>
                <strong>{selectedRoadmap.duration}</strong>
              </div>
            </div>

            <div className="roadmap-modal-section">
              <h3>Required Skills</h3>

              {selectedRoadmap.skills?.length > 0 ? (
                <div className="roadmap-skill-tags">
                  {selectedRoadmap.skills.map((skill, index) => (
                    <span key={`detail-skill-${index}`}>
                      {typeof skill === "string"
                        ? skill
                        : skill.name || skill.title || "Skill"}
                    </span>
                  ))}
                </div>
              ) : (
                <p>No skills listed for this roadmap.</p>
              )}
            </div>

            <div className="roadmap-modal-section">
              <h3>Learning Steps</h3>

              {selectedRoadmap.learning_steps?.length > 0 ? (
                <ol className="roadmap-learning-steps">
                  {selectedRoadmap.learning_steps.map((step, index) => (
                    <li key={`step-${index}`}>
                      <span className="roadmap-step-number">
                        {index + 1}
                      </span>

                      <div>
                        <strong>
                          {typeof step === "string"
                            ? step
                            : step.title || step.name || `Step ${index + 1}`}
                        </strong>

                        {typeof step === "object" && step.description && (
                          <p>{step.description}</p>
                        )}
                      </div>
                    </li>
                  ))}
                </ol>
              ) : (
                <p>No learning steps available.</p>
              )}
            </div>

            <button
              type="button"
              className="roadmap-modal-done"
              onClick={() => setSelectedRoadmap(null)}
            >
              Close Details
            </button>
          </div>
        </div>
      )}
    </section>
  );
}

export default Roadmaps;
