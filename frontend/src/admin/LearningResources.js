
import React, { useEffect, useMemo, useState } from "react";
import "./LearningResources.css";

const API_URL = "https://skillsphere-17hl.onrender.com/api/learning-resources/";
const SAVED_RESOURCES_KEY = "skillsphere_saved_learning_resources";

const CATEGORIES = [
  "All",
  "Programming",
  "Web Development",
  "Database",
  "Tools",
  "Computer Science",
];

function getInitialSavedIds() {
  try {
    const storedIds = localStorage.getItem(SAVED_RESOURCES_KEY);

    if (!storedIds) {
      return [];
    }

    const parsedIds = JSON.parse(storedIds);
    return Array.isArray(parsedIds) ? parsedIds : [];
  } catch (error) {
    console.error("Unable to read saved learning resources:", error);
    return [];
  }
}

export default function LearningResources() {
  const [search, setSearch] = useState("");
  const [category, setCategory] = useState("All");
  const [level, setLevel] = useState("All");

  // Restore saved resources when the page opens.
  const [savedIds, setSavedIds] = useState(getInitialSavedIds);

  const [activeTab, setActiveTab] = useState("All Resources");
  const [allResources, setAllResources] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  // Persist saved resource IDs whenever they change.
  useEffect(() => {
    try {
      localStorage.setItem(
        SAVED_RESOURCES_KEY,
        JSON.stringify(savedIds)
      );
    } catch (storageError) {
      console.error(
        "Unable to save learning resources:",
        storageError
      );
    }
  }, [savedIds]);

  // Fetch learning resources from Django using JWT authentication.
  useEffect(() => {
    const controller = new AbortController();

    const fetchResources = async () => {
      setLoading(true);
      setError("");

      const token =
        localStorage.getItem("skillsphere_access") ||
        localStorage.getItem("access");

      if (!token) {
        setError("Please log in to view learning resources.");
        setLoading(false);
        return;
      }

      try {
        const response = await fetch(API_URL, {
          method: "GET",
          headers: {
            Authorization: `Bearer ${token}`,
            Accept: "application/json",
          },
          signal: controller.signal,
        });

        if (response.status === 401) {
          throw new Error(
            "Your session may have expired. Please log in again."
          );
        }

        if (response.status === 403) {
          throw new Error(
            "You do not have permission to view these resources."
          );
        }

        if (!response.ok) {
          throw new Error(
            `Unable to load learning resources (HTTP ${response.status}).`
          );
        }

        const data = await response.json();
        const resourceList = Array.isArray(data)
          ? data
          : data.results;

        if (!Array.isArray(resourceList)) {
          throw new Error(
            "The server returned an unexpected response."
          );
        }

        const normalizedResources = resourceList.map((resource) => ({
          ...resource,
          id: resource.id,
          title: resource.title || "Untitled Resource",
          category: resource.category || "Programming",
          skill: resource.skill || "",
          level: resource.level || "Beginner",
          type: resource.resource_type || resource.type || "Tutorial",
          description: resource.description || "",
          url: resource.url || "#",
        }));

        setAllResources(normalizedResources);
      } catch (err) {
        if (err.name !== "AbortError") {
          setError(
            err.message ||
              "Something went wrong while loading learning resources."
          );
        }
      } finally {
        if (!controller.signal.aborted) {
          setLoading(false);
        }
      }
    };

    fetchResources();

    return () => controller.abort();
  }, []);

  const resources = useMemo(() => {
    return allResources.filter((resource) => {
      const query = search.trim().toLowerCase();

      const matchesSearch =
        !query ||
        resource.title.toLowerCase().includes(query) ||
        resource.skill.toLowerCase().includes(query) ||
        resource.description.toLowerCase().includes(query);

      const matchesCategory =
        category === "All" || resource.category === category;

      const matchesLevel =
        level === "All" || resource.level === level;

      const matchesTab =
        activeTab === "All Resources" ||
        (activeTab === "Saved" && savedIds.includes(resource.id));

      return (
        matchesSearch &&
        matchesCategory &&
        matchesLevel &&
        matchesTab
      );
    });
  }, [
    allResources,
    search,
    category,
    level,
    activeTab,
    savedIds,
  ]);

  const toggleSaved = (id) => {
    setSavedIds((previous) =>
      previous.includes(id)
        ? previous.filter((savedId) => savedId !== id)
        : [...previous, id]
    );
  };

  const resetFilters = () => {
    setSearch("");
    setCategory("All");
    setLevel("All");
  };

  return (
    <main className="learning-resources">
      <section className="lr-hero">
        <div className="lr-hero-content">
          <span className="lr-eyebrow">
            SKILLSPHERE LEARNING HUB
          </span>

          <h1>Learn today. Grow every day.</h1>

          <p>
            Discover trusted learning resources, strengthen your skills,
            and take the next step toward your career goals.
          </p>

          <div className="lr-hero-stats">
            <div>
              <strong>{allResources.length}</strong>
              <span>Resources</span>
            </div>

            <div>
              <strong>{savedIds.length}</strong>
              <span>Saved items</span>
            </div>

            <div>
              <strong>{CATEGORIES.length - 1}</strong>
              <span>Categories</span>
            </div>
          </div>
        </div>
      </section>

      <section className="lr-content">
        <div className="lr-section-heading">
          <div>
            <span className="lr-eyebrow">
              YOUR LEARNING JOURNEY
            </span>
            <h2>Learning Resources</h2>
            <p>Find the right material for your next skill.</p>
          </div>
        </div>

        <div className="lr-tabs">
          {["All Resources", "Saved"].map((tab) => (
            <button
              key={tab}
              type="button"
              className={`lr-tab ${activeTab === tab ? "active" : ""}`}
              onClick={() => setActiveTab(tab)}
            >
              {tab}

              {tab === "Saved" && (
                <span className="lr-tab-count">
                  {savedIds.length}
                </span>
              )}
            </button>
          ))}
        </div>

        <div className="lr-filters">
          <div className="lr-search">
            <span aria-hidden="true">⌕</span>
            <input
              type="search"
              value={search}
              onChange={(event) => setSearch(event.target.value)}
              placeholder="Search skills, topics, resources..."
              aria-label="Search learning resources"
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
            value={level}
            onChange={(event) => setLevel(event.target.value)}
            aria-label="Filter by difficulty"
          >
            <option value="All">All Levels</option>
            <option value="Beginner">Beginner</option>
            <option value="Intermediate">Intermediate</option>
            <option value="Advanced">Advanced</option>
          </select>

          <button
            type="button"
            className="lr-reset-button"
            onClick={resetFilters}
          >
            Reset
          </button>
        </div>

        <div className="lr-results-info">
          <span>
            Showing <strong>{resources.length}</strong> resource
            {resources.length !== 1 ? "s" : ""}
          </span>
        </div>

        {loading ? (
          <div className="lr-empty-state">
            <h3>Loading learning resources...</h3>
            <p>Please wait while we fetch your resources.</p>
          </div>
        ) : error ? (
          <div className="lr-empty-state">
            <h3>Unable to load resources</h3>
            <p>{error}</p>
            <button
              type="button"
              className="lr-open-button"
              onClick={() => window.location.reload()}
            >
              Try Again
            </button>
          </div>
        ) : resources.length > 0 ? (
          <div className="lr-grid">
            {resources.map((resource) => {
              const isSaved = savedIds.includes(resource.id);

              return (
                <article className="lr-card" key={resource.id}>
                  <div className="lr-card-top">
                    <span
                      className="lr-resource-icon"
                      aria-hidden="true"
                    >
                      {resource.category === "Programming"
                        ? "</>"
                        : resource.category === "Web Development"
                        ? "WEB"
                        : resource.category === "Database"
                        ? "DB"
                        : resource.category === "Tools"
                        ? "DEV"
                        : "DSA"}
                    </span>

                    <button
                      type="button"
                      className={`lr-save-button ${
                        isSaved ? "saved" : ""
                      }`}
                      onClick={() => toggleSaved(resource.id)}
                      aria-label={
                        isSaved
                          ? "Remove saved resource"
                          : "Save resource"
                      }
                      title={
                        isSaved
                          ? "Remove from saved"
                          : "Save resource"
                      }
                    >
                      {isSaved ? "♥" : "♡"}
                    </button>
                  </div>

                  <div className="lr-card-tags">
                    <span>{resource.category}</span>
                    <span>{resource.level}</span>
                  </div>

                  <h3>{resource.title}</h3>

                  <p className="lr-card-description">
                    {resource.description}
                  </p>

                  <div className="lr-card-footer">
                    <span className="lr-resource-type">
                      {resource.type}
                    </span>

                    <a
                      className="lr-open-button"
                      href={resource.url}
                      target="_blank"
                      rel="noopener noreferrer"
                    >
                      Start Learning <span aria-hidden="true">↗</span>
                    </a>
                  </div>
                </article>
              );
            })}
          </div>
        ) : (
          <div className="lr-empty-state">
            <div className="lr-empty-icon" aria-hidden="true">
              ⌕
            </div>

            <h3>No resources found</h3>

            <p>
              {activeTab === "Saved"
                ? "You have not saved any resources matching these filters."
                : "Try a different search term or reset your filters."}
            </p>

            <button
              type="button"
              className="lr-open-button"
              onClick={() => {
                resetFilters();
                setActiveTab("All Resources");
              }}
            >
              View all resources
            </button>
          </div>
        )}
      </section>
    </main>
  );
}
