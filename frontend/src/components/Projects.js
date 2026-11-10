import React, {
  useCallback,
  useEffect,
  useMemo,
  useState,
} from "react";

import "./Projects.css";
import { showToast } from "../components/ToastProvider";

const API_URL = "https://skillsphere-u93o.onrender.com/api/projects/";

const PAGE_SIZE = 5;

const EMPTY_FORM = {
  title: "",
  description: "",
  category: "Web Development",
  technologies: "",
  status: "Planning",
  github: "",
  liveDemo: "",
};

const CATEGORIES = [
  "Web Development",
  "Full Stack",
  "AI / Machine Learning",
  "Data Science",
  "Mobile Development",
  "Database",
  "Other",
];

const STATUSES = [
  "Planning",
  "In Progress",
  "Completed",
  "On Hold",
];

function validOptionalUrl(value) {
  if (!value.trim()) return true;

  try {
    const url = new URL(value.trim());

    return (
      url.protocol === "http:" ||
      url.protocol === "https:"
    );
  } catch {
    return false;
  }
}

// Correct SkillSphere access token key
function getAccessToken() {
  return localStorage.getItem("skillsphere_access");
}

function mapProjectFromAPI(project) {
  return {
    id: project.id,
    title: project.title || "",
    description: project.description || "",
    category: project.category || "Other",

    technologies: Array.isArray(project.technologies)
      ? project.technologies
      : [],

    status: project.status || "Planning",
    github: project.github || "",
    liveDemo: project.live_demo || "",
    createdAt: project.created_at || "",
    updatedAt: project.updated_at || "",
  };
}

function getErrorMessage(data, fallback) {
  if (!data) return fallback;

  if (typeof data.detail === "string") {
    return data.detail;
  }

  for (const value of Object.values(data)) {
    if (typeof value === "string") {
      return value;
    }

    if (Array.isArray(value) && value.length > 0) {
      return String(value[0]);
    }
  }

  return fallback;
}

async function apiRequest(url, options = {}) {
  const token = getAccessToken();

  if (!token) {
    throw new Error(
      "Your session has expired. Please log in again."
    );
  }

  const response = await fetch(url, {
    ...options,

    headers: {
      Authorization: `Bearer ${token}`,

      ...(options.body
        ? { "Content-Type": "application/json" }
        : {}),

      ...options.headers,
    },
  });

  if (response.status === 204) {
    return null;
  }

  const contentType =
    response.headers.get("content-type") || "";

  const data = contentType.includes("application/json")
    ? await response.json()
    : null;

  if (!response.ok) {
    if (response.status === 401) {
      throw new Error(
        "Your session has expired. Please log in again."
      );
    }

    if (response.status === 403) {
      throw new Error(
        "You do not have permission to perform this action."
      );
    }

    if (response.status === 404) {
      throw new Error(
        "The requested project could not be found."
      );
    }

    throw new Error(
      getErrorMessage(
        data,
        "Something went wrong. Please try again."
      )
    );
  }

  return data;
}

function Projects() {
  const [projects, setProjects] = useState([]);

  const [search, setSearch] = useState("");
  const [statusFilter, setStatusFilter] = useState("All");
  const [categoryFilter, setCategoryFilter] = useState("All");

  const [showForm, setShowForm] = useState(false);
  const [editingId, setEditingId] = useState(null);

  const [form, setForm] = useState(EMPTY_FORM);
  const [errors, setErrors] = useState({});

  const [deleteId, setDeleteId] = useState(null);

  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [pageError, setPageError] = useState("");

  // Pagination states
  const [currentPage, setCurrentPage] = useState(1);
  const [totalProjects, setTotalProjects] = useState(0);

  const totalPages = Math.max(
    1,
    Math.ceil(totalProjects / PAGE_SIZE)
  );

  // Load projects from backend
  const loadProjects = useCallback(async (page = 1) => {
    setLoading(true);
    setPageError("");

    try {
      const data = await apiRequest(
        `${API_URL}?page=${page}`
      );

      const list = Array.isArray(data)
        ? data
        : data?.results;

      if (!Array.isArray(list)) {
        throw new Error(
          "The server returned an unexpected project list."
        );
      }

      setProjects(list.map(mapProjectFromAPI));

      setTotalProjects(
        data.count ?? list.length
      );

      setCurrentPage(page);

    } catch (error) {
      setPageError(
        error.message || "Unable to load your projects."
      );

      showToast(
        error.message || "Unable to load your projects.",
        "error"
      );

    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadProjects(1);
  }, [loadProjects]);

  // Project statistics
  const completedCount = projects.filter(
    (project) => project.status === "Completed"
  ).length;

  const inProgressCount = projects.filter(
    (project) => project.status === "In Progress"
  ).length;

  const planningCount = projects.filter(
    (project) => project.status === "Planning"
  ).length;

  // Search and filters
  const filteredProjects = useMemo(() => {
    const query = search.trim().toLowerCase();

    return projects.filter((project) => {
      const matchesSearch =
        !query ||
        project.title.toLowerCase().includes(query) ||
        project.description.toLowerCase().includes(query) ||
        project.technologies.some((technology) =>
          technology.toLowerCase().includes(query)
        );

      const matchesStatus =
        statusFilter === "All" ||
        project.status === statusFilter;

      const matchesCategory =
        categoryFilter === "All" ||
        project.category === categoryFilter;

      return matchesSearch &&
        matchesStatus &&
        matchesCategory;
    });
  }, [
    projects,
    search,
    statusFilter,
    categoryFilter,
  ]);

  const closeForm = () => {
    setShowForm(false);
    setEditingId(null);
    setForm(EMPTY_FORM);
    setErrors({});
  };

  const openAddForm = () => {
    setEditingId(null);
    setForm(EMPTY_FORM);
    setErrors({});
    setShowForm(true);
  };

  const openEditForm = (project) => {
    setEditingId(project.id);

    setForm({
      title: project.title,
      description: project.description,
      category: project.category,
      technologies: project.technologies.join(", "),
      status: project.status,
      github: project.github || "",
      liveDemo: project.liveDemo || "",
    });

    setErrors({});
    setShowForm(true);
  };

  const updateField = (field, value) => {
    setForm((previous) => ({
      ...previous,
      [field]: value,
    }));

    setErrors((previous) => ({
      ...previous,
      [field]: "",
    }));
  };

  const validateForm = () => {
    const nextErrors = {};

    if (!form.title.trim()) {
      nextErrors.title =
        "Please enter a project title.";

    } else if (form.title.trim().length < 3) {
      nextErrors.title =
        "Title must contain at least 3 characters.";

    } else if (form.title.trim().length > 200) {
      nextErrors.title =
        "Title cannot exceed 200 characters.";
    }

    if (!form.description.trim()) {
      nextErrors.description =
        "Please describe your project.";

    } else if (form.description.trim().length < 15) {
      nextErrors.description =
        "Description must contain at least 15 characters.";
    }

    if (!form.technologies.trim()) {
      nextErrors.technologies =
        "Enter at least one technology.";
    }

    if (!validOptionalUrl(form.github)) {
      nextErrors.github =
        "Enter a valid URL starting with https:// or http://.";
    }

    if (!validOptionalUrl(form.liveDemo)) {
      nextErrors.liveDemo =
        "Enter a valid URL starting with https:// or http://.";
    }

    setErrors(nextErrors);

    return Object.keys(nextErrors).length === 0;
  };

  // Add and update projects
  const handleSubmit = async (event) => {
    event.preventDefault();

    if (saving) return;

    if (!validateForm()) {
      showToast(
        "Please fix the highlighted fields and try again.",
        "error"
      );

      return;
    }

    const technologies = [
      ...new Set(
        form.technologies
          .split(",")
          .map((technology) => technology.trim())
          .filter(Boolean)
      ),
    ];

    const projectData = {
      title: form.title.trim(),
      description: form.description.trim(),
      category: form.category,
      technologies,
      status: form.status,
      github: form.github.trim(),
      live_demo: form.liveDemo.trim(),
    };

    setSaving(true);

    try {
      if (editingId !== null) {
        const updated = await apiRequest(
          `${API_URL}${editingId}/`,
          {
            method: "PATCH",
            body: JSON.stringify(projectData),
          }
        );

        await loadProjects(currentPage);

        showToast(
          "Project updated successfully!",
          "success"
        );

      } else {
        await apiRequest(API_URL, {
          method: "POST",
          body: JSON.stringify(projectData),
        });

        await loadProjects(1);

        showToast(
          "Project added successfully!",
          "success"
        );
      }

      closeForm();

    } catch (error) {
      showToast(
        error.message || "Unable to save the project.",
        "error"
      );

    } finally {
      setSaving(false);
    }
  };

  // Update project status
  const updateStatus = async (projectId, newStatus) => {
    const project = projects.find(
      (item) => item.id === projectId
    );

    if (!project || project.status === newStatus) {
      return;
    }

    const previousStatus = project.status;

    setProjects((previous) =>
      previous.map((item) =>
        item.id === projectId
          ? { ...item, status: newStatus }
          : item
      )
    );

    try {
      const updated = await apiRequest(
        `${API_URL}${projectId}/`,
        {
          method: "PATCH",
          body: JSON.stringify({
            status: newStatus,
          }),
        }
      );

      setProjects((previous) =>
        previous.map((item) =>
          item.id === projectId
            ? mapProjectFromAPI(updated)
            : item
        )
      );

      showToast(
        `Project status changed to ${newStatus}.`,
        "success"
      );

    } catch (error) {
      setProjects((previous) =>
        previous.map((item) =>
          item.id === projectId
            ? { ...item, status: previousStatus }
            : item
        )
      );

      showToast(
        error.message || "Unable to update the project status.",
        "error"
      );
    }
  };

  // Delete project
  const confirmDelete = async () => {
    const project = projects.find(
      (item) => item.id === deleteId
    );

    if (!project) {
      setDeleteId(null);

      showToast(
        "Project could not be found.",
        "error"
      );

      return;
    }

    try {
      await apiRequest(
        `${API_URL}${deleteId}/`,
        {
          method: "DELETE",
        }
      );

      setDeleteId(null);

      const nextPage =
        projects.length === 1 && currentPage > 1
          ? currentPage - 1
          : currentPage;

      await loadProjects(nextPage);

      showToast(
        `"${project.title}" was deleted.`,
        "success"
      );

    } catch (error) {
      showToast(
        error.message || "Unable to delete the project.",
        "error"
      );
    }
  };

  const resetFilters = () => {
    setSearch("");
    setStatusFilter("All");
    setCategoryFilter("All");
  };

  const formatDate = (dateValue) => {
    if (!dateValue) return "Date unavailable";

    const date = new Date(dateValue);

    if (Number.isNaN(date.getTime())) {
      return "Date unavailable";
    }

    return date.toLocaleDateString("en-IN", {
      day: "numeric",
      month: "short",
      year: "numeric",
    });
  };

  const getStatusClass = (status) =>
    status.toLowerCase().replace(/\s+/g, "-");

  // Pagination handlers
  const goToPreviousPage = () => {
    if (currentPage > 1) {
      loadProjects(currentPage - 1);
    }
  };

  const goToNextPage = () => {
    if (currentPage < totalPages) {
      loadProjects(currentPage + 1);
    }
  };

  const goToPage = (page) => {
    if (page >= 1 && page <= totalPages) {
      loadProjects(page);
    }
  };

  return (
    <div className="sp-page">

      <section className="sp-hero">
        <div className="sp-hero-content">

          <span className="sp-eyebrow">
            <span className="sp-eyebrow-dot" />
            SKILLSPHERE WORKSPACE
          </span>

          <h1>
            Turn your ideas into <span>real projects.</span>
          </h1>

          <p>
            Document what you build, track your progress, and create a
            portfolio that reflects your skills and career journey.
          </p>

          <button
            type="button"
            className="sp-primary-button"
            onClick={openAddForm}
          >
            <span aria-hidden="true">＋</span> Add a project
          </button>

        </div>

        <div className="sp-hero-art" aria-hidden="true">

          <div className="sp-art-orbit sp-art-orbit-one" />
          <div className="sp-art-orbit sp-art-orbit-two" />

          <div className="sp-art-window">

            <div className="sp-art-window-top">
              <i />
              <i />
              <i />
            </div>

            <div className="sp-art-code">
              <span>01</span> const project = {"{"}
              <br />
              <span>02</span> &nbsp; ideas: "build",
              <br />
              <span>03</span> &nbsp; skills: "grow",
              <br />
              <span>04</span> &nbsp; future: "create"
              <br />
              <span>05</span> {"}"};
            </div>

          </div>

          <div className="sp-art-badge">
            ✦ Build something great
          </div>

        </div>
      </section>

      <section
        className="sp-stats"
        aria-label="Project statistics"
      >

        <div className="sp-stat-card">
          <div className="sp-stat-icon sp-stat-blue">▤</div>

          <div>
            <strong>{totalProjects}</strong>
            <span>Total projects</span>
          </div>
        </div>

        <div className="sp-stat-card">
          <div className="sp-stat-icon sp-stat-green">✓</div>

          <div>
            <strong>{completedCount}</strong>
            <span>Completed</span>
          </div>
        </div>

        <div className="sp-stat-card">
          <div className="sp-stat-icon sp-stat-purple">↗</div>

          <div>
            <strong>{inProgressCount}</strong>
            <span>In progress</span>
          </div>
        </div>

        <div className="sp-stat-card">
          <div className="sp-stat-icon sp-stat-orange">◷</div>

          <div>
            <strong>{planningCount}</strong>
            <span>Planning</span>
          </div>
        </div>

      </section>

      <section className="sp-project-section">

        <div className="sp-section-heading">

          <div>
            <span className="sp-section-label">
              YOUR WORKSPACE
            </span>

            <h2>My projects</h2>

            <p>
              Every project is another step towards your future.
            </p>
          </div>

          <button
            type="button"
            className="sp-add-secondary"
            onClick={openAddForm}
          >
            ＋ New project
          </button>

        </div>

        <div className="sp-filter-bar">

          <label className="sp-search">
            <span aria-hidden="true">⌕</span>

            <input
              type="search"
              value={search}
              onChange={(event) =>
                setSearch(event.target.value)
              }
              placeholder="Search projects or technologies..."
              aria-label="Search projects"
            />

            {search && (
              <button
                type="button"
                onClick={() => setSearch("")}
                aria-label="Clear search"
              >
                ×
              </button>
            )}
          </label>

          <label className="sp-select">
            <span className="sp-sr-only">
              Filter by project status
            </span>

            <select
              value={statusFilter}
              onChange={(event) =>
                setStatusFilter(event.target.value)
              }
            >
              <option value="All">All statuses</option>

              {STATUSES.map((status) => (
                <option key={status} value={status}>
                  {status}
                </option>
              ))}
            </select>
          </label>

          <label className="sp-select">
            <span className="sp-sr-only">
              Filter by category
            </span>

            <select
              value={categoryFilter}
              onChange={(event) =>
                setCategoryFilter(event.target.value)
              }
            >
              <option value="All">All categories</option>

              {CATEGORIES.map((category) => (
                <option key={category} value={category}>
                  {category}
                </option>
              ))}
            </select>
          </label>

          {(search ||
            statusFilter !== "All" ||
            categoryFilter !== "All") && (
            <button
              type="button"
              className="sp-clear-filters"
              onClick={resetFilters}
            >
              Clear filters
            </button>
          )}

        </div>

        <div className="sp-result-count">
          Showing <strong>{filteredProjects.length}</strong>{" "}
          {filteredProjects.length === 1
            ? "project"
            : "projects"}
        </div>

        {loading ? (

          <div className="sp-empty-state">
            <h3>Loading your projects...</h3>

            <p>
              Please wait while SkillSphere retrieves your saved projects.
            </p>
          </div>

        ) : pageError && projects.length === 0 ? (

          <div className="sp-empty-state">

            <span className="sp-empty-icon" aria-hidden="true">
              !
            </span>

            <h3>Unable to load your projects</h3>

            <p>{pageError}</p>

            <button
              type="button"
              className="sp-primary-button"
              onClick={() => loadProjects(currentPage)}
            >
              Try again
            </button>

          </div>

        ) : filteredProjects.length > 0 ? (

          <div className="sp-project-grid">

            {filteredProjects.map((project, index) => (

              <article
                className="sp-project-card"
                key={project.id}
              >

                <div
                  className={`sp-project-cover sp-cover-${index % 5}`}
                >

                  <div className="sp-cover-top">

                    <span className="sp-category-badge">
                      {project.category}
                    </span>

                    <span
                      className="sp-cover-symbol"
                      aria-hidden="true"
                    >
                      {project.category === "AI / Machine Learning"
                        ? "✧"
                        : project.category === "Database"
                        ? "▤"
                        : project.category === "Mobile Development"
                        ? "▯"
                        : project.category === "Data Science"
                        ? "⌁"
                        : "⌘"}
                    </span>

                  </div>

                  <div className="sp-cover-bottom">
                    <span>PROJECT</span>

                    <span>
                      {String(project.id)
                        .replace(/[^a-zA-Z0-9]/g, "")
                        .slice(-5)
                        .toUpperCase() || "BUILD"}
                    </span>
                  </div>

                </div>

                <div className="sp-project-body">

                  <div className="sp-project-title-row">

                    <h3>{project.title}</h3>

                    <span
                      className={`sp-status sp-status-${getStatusClass(
                        project.status
                      )}`}
                    >
                      {project.status}
                    </span>

                  </div>

                  <p className="sp-project-description">
                    {project.description}
                  </p>

                  <div className="sp-tech-list">

                    {project.technologies.map((technology) => (
                      <span key={technology}>
                        {technology}
                      </span>
                    ))}

                  </div>

                  <div className="sp-project-date">
                    <span aria-hidden="true">◷</span>
                    Added {formatDate(project.createdAt)}
                  </div>

                  <div className="sp-card-divider" />

                  <div className="sp-project-links">

                    {project.github && (
                      <a
                        href={project.github}
                        target="_blank"
                        rel="noreferrer"
                      >
                        GitHub ↗
                      </a>
                    )}

                    {project.liveDemo && (
                      <a
                        href={project.liveDemo}
                        target="_blank"
                        rel="noreferrer"
                      >
                        Live demo ↗
                      </a>
                    )}

                    {!project.github &&
                      !project.liveDemo && (
                        <span className="sp-no-links">
                          No links added yet
                        </span>
                      )}

                  </div>

                  <div className="sp-card-actions">

                    <label className="sp-status-control">

                      <span className="sp-sr-only">
                        Update status for {project.title}
                      </span>

                      <select
                        value={project.status}
                        onChange={(event) =>
                          updateStatus(
                            project.id,
                            event.target.value
                          )
                        }
                        aria-label={`Update status for ${project.title}`}
                      >
                        {STATUSES.map((status) => (
                          <option key={status} value={status}>
                            {status}
                          </option>
                        ))}
                      </select>

                    </label>

                    <button
                      type="button"
                      className="sp-edit-button"
                      onClick={() => openEditForm(project)}
                      aria-label={`Edit ${project.title}`}
                      title="Edit project"
                    >
                      ✎
                    </button>

                    <button
                      type="button"
                      className="sp-delete-button"
                      onClick={() => setDeleteId(project.id)}
                      aria-label={`Delete ${project.title}`}
                      title="Delete project"
                    >
                      ♲
                    </button>

                  </div>

                </div>

              </article>

            ))}

          </div>

        ) : (

          <div className="sp-empty-state">

            <span className="sp-empty-icon" aria-hidden="true">
              ⌘
            </span>

            <h3>
              {projects.length === 0
                ? "Your project journey starts here"
                : "No matching projects found"}
            </h3>

            <p>
              {projects.length === 0
                ? "Add your first project and start building a portfolio of your achievements."
                : "Try another search term or clear your filters to see your projects."}
            </p>

            {projects.length === 0 ? (

              <button
                type="button"
                className="sp-primary-button"
                onClick={openAddForm}
              >
                ＋ Create your first project
              </button>

            ) : (

              <button
                type="button"
                className="sp-add-secondary"
                onClick={resetFilters}
              >
                Clear filters
              </button>

            )}

          </div>

        )}

        {/* Pagination controls */}

        {!loading && !pageError && totalProjects > PAGE_SIZE && (

          <div className="sp-pagination">

            <button
              type="button"
              className="sp-add-secondary"
              onClick={goToPreviousPage}
              disabled={currentPage === 1}
            >
              Previous
            </button>

            {Array.from(
              { length: totalPages },
              (_, index) => index + 1
            ).map((page) => (

              <button
                key={page}
                type="button"
                className={
                  currentPage === page
                    ? "sp-primary-button"
                    : "sp-add-secondary"
                }
                onClick={() => goToPage(page)}
              >
                {page}
              </button>

            ))}

            <button
              type="button"
              className="sp-add-secondary"
              onClick={goToNextPage}
              disabled={currentPage === totalPages}
            >
              Next
            </button>

          </div>

        )}

      </section>

      <section className="sp-tip-banner">

        <div className="sp-tip-icon">💡</div>

        <div>
          <h3>Make every project count</h3>

          <p>
            Document what you built, explain the problem you solved,
            list your technologies, and add your GitHub or live demo
            link when available. These details can help strengthen
            your portfolio.
          </p>
        </div>

      </section>

      {/* Add / Edit Project Modal */}

      {showForm && (

        <div
          className="sp-modal-backdrop"
          role="presentation"
          onMouseDown={(event) => {
            if (
              event.target === event.currentTarget &&
              !saving
            ) {
              closeForm();
            }
          }}
        >

          <section
            className="sp-modal"
            role="dialog"
            aria-modal="true"
            aria-labelledby="sp-form-title"
          >

            <div className="sp-modal-header">

              <div>
                <span className="sp-section-label">
                  PROJECT WORKSPACE
                </span>

                <h2 id="sp-form-title">
                  {editingId !== null
                    ? "Edit project"
                    : "Create a new project"}
                </h2>

                <p>
                  {editingId !== null
                    ? "Update the details of your project."
                    : "Tell us about something you are building."}
                </p>
              </div>

              <button
                type="button"
                className="sp-modal-close"
                onClick={closeForm}
                aria-label="Close form"
                disabled={saving}
              >
                ×
              </button>

            </div>

            <form
              className="sp-project-form"
              onSubmit={handleSubmit}
              noValidate
            >

              <div className="sp-form-field">

                <label htmlFor="sp-title">
                  Project title *
                </label>

                <input
                  id="sp-title"
                  type="text"
                  maxLength={200}
                  value={form.title}
                  onChange={(event) =>
                    updateField("title", event.target.value)
                  }
                  placeholder="e.g. SkillSphere Career Platform"
                  aria-invalid={Boolean(errors.title)}
                />

                {errors.title && (
                  <span className="sp-field-error">
                    {errors.title}
                  </span>
                )}

              </div>

              <div className="sp-form-field">

                <label htmlFor="sp-description">
                  Project description *
                </label>

                <textarea
                  id="sp-description"
                  rows={4}
                  maxLength={1000}
                  value={form.description}
                  onChange={(event) =>
                    updateField("description", event.target.value)
                  }
                  placeholder="Describe the project, its purpose, and the problem it solves..."
                  aria-invalid={Boolean(errors.description)}
                />

                <span className="sp-character-count">
                  {form.description.length}/1000
                </span>

                {errors.description && (
                  <span className="sp-field-error">
                    {errors.description}
                  </span>
                )}

              </div>

              <div className="sp-form-row">

                <div className="sp-form-field">

                  <label htmlFor="sp-category">
                    Category
                  </label>

                  <select
                    id="sp-category"
                    value={form.category}
                    onChange={(event) =>
                      updateField("category", event.target.value)
                    }
                  >
                    {CATEGORIES.map((category) => (
                      <option key={category} value={category}>
                        {category}
                      </option>
                    ))}
                  </select>

                </div>

                <div className="sp-form-field">

                  <label htmlFor="sp-status">
                    Project status
                  </label>

                  <select
                    id="sp-status"
                    value={form.status}
                    onChange={(event) =>
                      updateField("status", event.target.value)
                    }
                  >
                    {STATUSES.map((status) => (
                      <option key={status} value={status}>
                        {status}
                      </option>
                    ))}
                  </select>

                </div>

              </div>

              <div className="sp-form-field">

                <label htmlFor="sp-technologies">
                  Technologies used *
                </label>

                <input
                  id="sp-technologies"
                  type="text"
                  value={form.technologies}
                  onChange={(event) =>
                    updateField("technologies", event.target.value)
                  }
                  placeholder="React, Django, PostgreSQL"
                  aria-invalid={Boolean(errors.technologies)}
                />

                <small>
                  Separate each technology with a comma.
                </small>

                {errors.technologies && (
                  <span className="sp-field-error">
                    {errors.technologies}
                  </span>
                )}

              </div>

              <div className="sp-form-field">

                <label htmlFor="sp-github">
                  GitHub repository URL
                </label>

                <input
                  id="sp-github"
                  type="url"
                  value={form.github}
                  onChange={(event) =>
                    updateField("github", event.target.value)
                  }
                  placeholder="https://github.com/username/project"
                  aria-invalid={Boolean(errors.github)}
                />

                {errors.github && (
                  <span className="sp-field-error">
                    {errors.github}
                  </span>
                )}

              </div>

              <div className="sp-form-field">

                <label htmlFor="sp-demo">
                  Live demo URL
                </label>

                <input
                  id="sp-demo"
                  type="url"
                  value={form.liveDemo}
                  onChange={(event) =>
                    updateField("liveDemo", event.target.value)
                  }
                  placeholder="https://your-project.example"
                  aria-invalid={Boolean(errors.liveDemo)}
                />

                {errors.liveDemo && (
                  <span className="sp-field-error">
                    {errors.liveDemo}
                  </span>
                )}

              </div>

              <div className="sp-form-footer">

                <button
                  type="button"
                  className="sp-cancel-button"
                  onClick={closeForm}
                  disabled={saving}
                >
                  Cancel
                </button>

                <button
                  type="submit"
                  className="sp-save-button"
                  disabled={saving}
                >
                  {saving
                    ? "Saving..."
                    : editingId !== null
                    ? "Save changes"
                    : "＋ Add project"}
                </button>

              </div>

            </form>

          </section>

        </div>

      )}

      {/* Delete Confirmation Modal */}

      {deleteId !== null && (

        <div
          className="sp-modal-backdrop sp-delete-backdrop"
          role="presentation"
          onMouseDown={(event) => {
            if (event.target === event.currentTarget) {
              setDeleteId(null);
            }
          }}
        >

          <section
            className="sp-delete-modal"
            role="alertdialog"
            aria-modal="true"
            aria-labelledby="sp-delete-title"
          >

            <div className="sp-delete-icon">!</div>

            <h2 id="sp-delete-title">
              Delete this project?
            </h2>

            <p>
              This will permanently remove the project from your
              SkillSphere account and database.
            </p>

            <div className="sp-delete-actions">

              <button
                type="button"
                className="sp-cancel-button"
                onClick={() => setDeleteId(null)}
              >
                Keep project
              </button>

              <button
                type="button"
                className="sp-confirm-delete"
                onClick={confirmDelete}
              >
                Delete project
              </button>

            </div>

          </section>

        </div>

      )}

    </div>
  );
}

export default Projects;