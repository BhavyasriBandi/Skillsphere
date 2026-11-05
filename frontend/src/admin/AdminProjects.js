
import React, {
  useCallback,
  useEffect,
  useState,
} from "react";
import { createPortal } from "react-dom";
import { showToast } from "../components/ToastProvider";
import "./AdminProjects.css";

const API_URL = "http://127.0.0.1:8000/api/projects/admin/";
const TOKEN_KEY = "skillsphere_access";

const EMPTY_FORM = {
  student: "",
  title: "",
  description: "",
  category: "Web Development",
  technologies: "",
  status: "Planning",
  github: "",
  live_demo: "",
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

async function readResponse(response) {
  const text = await response.text();
  let data = {};

  try {
    data = text ? JSON.parse(text) : {};
  } catch {
    data = {
      detail: text || "Unexpected server response.",
    };
  }

  if (!response.ok) {
    let message = data.detail;

    if (!message) {
      message = Object.values(data)
        .flat()
        .map((item) =>
          typeof item === "string"
            ? item
            : JSON.stringify(item)
        )
        .join(" ");
    }

    throw new Error(
      message || `Request failed (${response.status}).`
    );
  }

  return data;
}

function ProjectFields({
  form,
  onChange,
  prefix,
}) {
  return (
    <div className="ap-form">
      <div className="ap-field">
        <label htmlFor={`${prefix}-student`}>
          Student User ID *
        </label>
        <input
          id={`${prefix}-student`}
          name="student"
          type="number"
          min="1"
          value={form.student}
          onChange={onChange}
          placeholder="Enter the student's database ID"
          required
        />
      </div>

      <div className="ap-field">
        <label htmlFor={`${prefix}-title`}>
          Project Title *
        </label>
        <input
          id={`${prefix}-title`}
          name="title"
          value={form.title}
          onChange={onChange}
          placeholder="e.g. SkillSphere Career Platform"
          required
        />
      </div>

      <div className="ap-field">
        <label htmlFor={`${prefix}-category`}>
          Category
        </label>
        <select
          id={`${prefix}-category`}
          name="category"
          value={form.category}
          onChange={onChange}
        >
          {CATEGORIES.map((category) => (
            <option key={category} value={category}>
              {category}
            </option>
          ))}
        </select>
      </div>

      <div className="ap-field">
        <label htmlFor={`${prefix}-status`}>
          Project Status
        </label>
        <select
          id={`${prefix}-status`}
          name="status"
          value={form.status}
          onChange={onChange}
        >
          {STATUSES.map((status) => (
            <option key={status} value={status}>
              {status}
            </option>
          ))}
        </select>
      </div>

      <div className="ap-field ap-full">
        <label htmlFor={`${prefix}-description`}>
          Description *
        </label>
        <textarea
          id={`${prefix}-description`}
          name="description"
          value={form.description}
          onChange={onChange}
          placeholder="Describe the project and its objectives..."
          rows="4"
          required
        />
      </div>

      <div className="ap-field ap-full">
        <label htmlFor={`${prefix}-technologies`}>
          Technologies
        </label>
        <input
          id={`${prefix}-technologies`}
          name="technologies"
          value={form.technologies}
          onChange={onChange}
          placeholder="Python, Django, React, PostgreSQL"
        />
        <small>Separate technologies with commas.</small>
      </div>

      <div className="ap-field">
        <label htmlFor={`${prefix}-github`}>
          GitHub URL
        </label>
        <input
          id={`${prefix}-github`}
          name="github"
          type="url"
          value={form.github}
          onChange={onChange}
          placeholder="https://github.com/..."
        />
      </div>

      <div className="ap-field">
        <label htmlFor={`${prefix}-demo`}>
          Live Demo URL
        </label>
        <input
          id={`${prefix}-demo`}
          name="live_demo"
          type="url"
          value={form.live_demo}
          onChange={onChange}
          placeholder="https://..."
        />
      </div>
    </div>
  );
}

function AdminProjects() {
  const [projects, setProjects] = useState([]);
  const [form, setForm] = useState({ ...EMPTY_FORM });

  const [editForm, setEditForm] = useState({
    ...EMPTY_FORM,
  });

  const [editingId, setEditingId] = useState(null);
  const [editModalOpen, setEditModalOpen] =
    useState(false);

  const [search, setSearch] = useState("");
  const [statusFilter, setStatusFilter] = useState("");
  const [categoryFilter, setCategoryFilter] =
    useState("");

  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [deletingId, setDeletingId] = useState(null);

  const [error, setError] = useState("");
  const [notice, setNotice] = useState("");

  const getToken = () =>
    localStorage.getItem(TOKEN_KEY) ||
    localStorage.getItem("access");

  const request = useCallback(async (url, options = {}) => {
    const token = getToken();

    if (!token) {
      throw new Error(
        "Please log in again to access Admin Projects."
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

    return readResponse(response);
  }, []);

  const loadProjects = useCallback(
    async (showErrorToast = false) => {
      setLoading(true);
      setError("");

      try {
        const params = new URLSearchParams();

        if (search.trim()) {
          params.set("search", search.trim());
        }

        if (statusFilter) {
          params.set("status", statusFilter);
        }

        if (categoryFilter) {
          params.set("category", categoryFilter);
        }

        const query = params.toString();

        const data = await request(
          API_URL + (query ? `?${query}` : "")
        );

        setProjects(
          Array.isArray(data)
            ? data
            : data.results || []
        );
      } catch (err) {
        const message =
          err.message || "Unable to load projects.";

        setError(message);

        if (showErrorToast) {
          showToast(message, "error");
        }
      } finally {
        setLoading(false);
      }
    },
    [request, search, statusFilter, categoryFilter]
  );

  useEffect(() => {
    loadProjects();
  }, [loadProjects]);

  // Prevent background scrolling while the popup is open.
  useEffect(() => {
    if (!editModalOpen) return undefined;

    const previousOverflow =
      document.body.style.overflow;

    document.body.style.overflow = "hidden";

    return () => {
      document.body.style.overflow =
        previousOverflow;
    };
  }, [editModalOpen]);

  // Close popup with Escape.
  useEffect(() => {
    function handleEscape(event) {
      if (
        event.key === "Escape" &&
        editModalOpen &&
        !saving
      ) {
        closeEditModal();
      }
    }

    window.addEventListener("keydown", handleEscape);

    return () => {
      window.removeEventListener(
        "keydown",
        handleEscape
      );
    };
  }, [editModalOpen, saving]);

  const handleChange = (event) => {
    const { name, value } = event.target;

    setForm((previous) => ({
      ...previous,
      [name]: value,
    }));
  };

  const handleEditChange = (event) => {
    const { name, value } = event.target;

    setEditForm((previous) => ({
      ...previous,
      [name]: value,
    }));
  };

  const resetForm = () => {
    setForm({ ...EMPTY_FORM });
  };

  const closeEditModal = () => {
    if (saving) return;

    setEditModalOpen(false);
    setEditingId(null);
    setEditForm({ ...EMPTY_FORM });
  };

  const buildPayload = (currentForm) => {
    const payload = {
      student: Number(currentForm.student),
      title: currentForm.title.trim(),
      description: currentForm.description.trim(),
      category: currentForm.category,
      technologies: currentForm.technologies
        .split(",")
        .map((item) => item.trim())
        .filter(Boolean),
      status: currentForm.status,
      github: currentForm.github.trim(),
      live_demo: currentForm.live_demo.trim(),
    };

    if (
      !Number.isInteger(payload.student) ||
      payload.student < 1 ||
      !payload.title ||
      !payload.description
    ) {
      throw new Error(
        "Enter a valid Student ID, project title, and description."
      );
    }

    return payload;
  };

  // Create a new project.
  const handleSubmit = async (event) => {
    event.preventDefault();

    if (saving) return;

    let payload;

    try {
      payload = buildPayload(form);
    } catch (err) {
      showToast(err.message, "error");
      return;
    }

    setSaving(true);
    setError("");
    setNotice("");

    try {
      await request(API_URL, {
        method: "POST",
        body: JSON.stringify(payload),
      });

      showToast(
        "Project created successfully!",
        "success"
      );

      resetForm();
      await loadProjects();
    } catch (err) {
      const message =
        err.message || "Unable to save the project.";

      setError(message);
      showToast(message, "error");
    } finally {
      setSaving(false);
    }
  };

  // Open selected project in the edit popup.
  const handleEdit = (project) => {
    if (saving || deletingId !== null) return;

    setEditingId(project.id);

    setEditForm({
      student: String(project.student ?? ""),
      title: project.title || "",
      description: project.description || "",
      category: project.category || "Web Development",
      technologies: Array.isArray(project.technologies)
        ? project.technologies.join(", ")
        : "",
      status: project.status || "Planning",
      github: project.github || "",
      live_demo: project.live_demo || "",
    });

    setError("");
    setNotice("");
    setEditModalOpen(true);
  };

  // Save edited project.
  const handleEditSubmit = async (event) => {
    event.preventDefault();

    if (saving || editingId === null) return;

    let payload;

    try {
      payload = buildPayload(editForm);
    } catch (err) {
      showToast(err.message, "error");
      return;
    }

    setSaving(true);
    setError("");
    setNotice("");

    try {
      await request(`${API_URL}${editingId}/`, {
        method: "PUT",
        body: JSON.stringify(payload),
      });

      showToast(
        "Project updated successfully!",
        "success"
      );

      setEditModalOpen(false);
      setEditingId(null);
      setEditForm({ ...EMPTY_FORM });

      await loadProjects();
    } catch (err) {
      const message =
        err.message || "Unable to save the project.";

      setError(message);
      showToast(message, "error");
    } finally {
      setSaving(false);
    }
  };

  const handleDelete = async (project) => {
    if (deletingId !== null || saving) return;

    const confirmed = window.confirm(
      `Delete "${project.title}"? This cannot be undone.`
    );

    if (!confirmed) return;

    setError("");
    setNotice("");
    setDeletingId(project.id);

    try {
      await request(`${API_URL}${project.id}/`, {
        method: "DELETE",
      });

      showToast(
        "Project deleted successfully!",
        "success"
      );

      if (editingId === project.id) {
        setEditModalOpen(false);
        setEditingId(null);
        setEditForm({ ...EMPTY_FORM });
      }

      await loadProjects();
    } catch (err) {
      const message =
        err.message || "Unable to delete the project.";

      setError(message);
      showToast(message, "error");
    } finally {
      setDeletingId(null);
    }
  };

  return (
    <div className="ap-page">
      {/* HEADER */}
      <div className="ap-header">
        <div>
          <p className="ap-eyebrow">
            SKILLSPHERE ADMINISTRATION
          </p>

          <h1>Projects Management</h1>

          <p className="ap-subtitle">
            Manage student projects, technologies, and progress.
          </p>
        </div>

        <button
          type="button"
          className="ap-refresh"
          onClick={() => loadProjects(true)}
          disabled={loading}
        >
          ↻ Refresh
        </button>
      </div>

      {error && (
        <div className="ap-alert ap-error" role="alert">
          {error}
        </div>
      )}

      {notice && (
        <div
          className="ap-alert ap-success"
          role="status"
        >
          {notice}
        </div>
      )}

      {/* STATISTICS */}
      <div className="ap-stats">
        <div className="ap-stat">
          <span>Total Projects</span>
          <strong>{projects.length}</strong>
        </div>

        <div className="ap-stat">
          <span>Completed</span>
          <strong>
            {
              projects.filter(
                (p) => p.status === "Completed"
              ).length
            }
          </strong>
        </div>

        <div className="ap-stat">
          <span>In Progress</span>
          <strong>
            {
              projects.filter(
                (p) => p.status === "In Progress"
              ).length
            }
          </strong>
        </div>

        <div className="ap-stat">
          <span>Planning</span>
          <strong>
            {
              projects.filter(
                (p) => p.status === "Planning"
              ).length
            }
          </strong>
        </div>
      </div>

      {/* CREATE PROJECT */}
      <section className="ap-panel">
        <div className="ap-panel-heading">
          <div>
            <h2>Create New Project</h2>
            <p>
              Enter the student's project information below.
            </p>
          </div>
        </div>

        <form className="ap-form" onSubmit={handleSubmit}>
          <ProjectFields
            form={form}
            onChange={handleChange}
            prefix="ap-create"
          />

          <div className="ap-form-actions ap-full">
            <button
              className="ap-primary"
              type="submit"
              disabled={saving}
            >
              {saving ? "Saving..." : "Create Project"}
            </button>

            <button
              className="ap-secondary"
              type="button"
              onClick={resetForm}
              disabled={saving}
            >
              Clear Form
            </button>
          </div>
        </form>
      </section>

      {/* STUDENT PROJECTS */}
      <section className="ap-panel">
        <div className="ap-panel-heading">
          <div>
            <h2>Student Projects</h2>
            <p>
              Search, review, edit, or remove project records.
            </p>
          </div>

          <span className="ap-count">
            {projects.length} projects
          </span>
        </div>

        <div className="ap-filters">
          <input
            aria-label="Search projects"
            value={search}
            onChange={(event) =>
              setSearch(event.target.value)
            }
            placeholder="Search by project title..."
          />

          <select
            aria-label="Filter by status"
            value={statusFilter}
            onChange={(event) =>
              setStatusFilter(event.target.value)
            }
          >
            <option value="">All statuses</option>

            {STATUSES.map((status) => (
              <option key={status} value={status}>
                {status}
              </option>
            ))}
          </select>

          <select
            aria-label="Filter by category"
            value={categoryFilter}
            onChange={(event) =>
              setCategoryFilter(event.target.value)
            }
          >
            <option value="">All categories</option>

            {CATEGORIES.map((category) => (
              <option key={category} value={category}>
                {category}
              </option>
            ))}
          </select>
        </div>

        {loading ? (
          <div className="ap-empty">
            Loading projects...
          </div>
        ) : projects.length === 0 ? (
          <div className="ap-empty">
            <span className="ap-empty-icon">▤</span>
            <h3>No projects found</h3>
            <p>
              Create a project above or adjust your search filters.
            </p>
          </div>
        ) : (
          <div className="ap-table-wrap">
            <table className="ap-table">
              <thead>
                <tr>
                  <th>Project</th>
                  <th>Student ID</th>
                  <th>Category</th>
                  <th>Status</th>
                  <th>Technologies</th>
                  <th>Actions</th>
                </tr>
              </thead>

              <tbody>
                {projects.map((project) => (
                  <tr key={project.id}>
                    <td>
                      <strong>{project.title}</strong>
                      <span className="ap-description">
                        {project.description}
                      </span>
                    </td>

                    <td>{project.student}</td>
                    <td>{project.category}</td>

                    <td>
                      <span
                        className={`ap-status ap-status-${(
                          project.status || "planning"
                        )
                          .toLowerCase()
                          .replace(/\s+/g, "-")}`}
                      >
                        {project.status}
                      </span>
                    </td>

                    <td>
                      <div className="ap-tech-list">
                        {(project.technologies || []).length ? (
                          project.technologies.map((tech) => (
                            <span key={tech}>{tech}</span>
                          ))
                        ) : (
                          "—"
                        )}
                      </div>
                    </td>

                    <td>
                      <div className="ap-actions">
                        <button
                          type="button"
                          className="ap-edit"
                          onClick={() => handleEdit(project)}
                          disabled={
                            saving || deletingId !== null
                          }
                        >
                          Edit
                        </button>

                        <button
                          type="button"
                          className="ap-delete"
                          onClick={() => handleDelete(project)}
                          disabled={deletingId !== null}
                        >
                          {deletingId === project.id
                            ? "Deleting..."
                            : "Delete"}
                        </button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </section>

      {/* CENTRED EDIT POPUP */}
      {editModalOpen &&
        createPortal(
          <div
            className="ap-modal-backdrop"
            onMouseDown={(event) => {
              if (
                event.target === event.currentTarget &&
                !saving
              ) {
                closeEditModal();
              }
            }}
          >
            <section
              className="ap-edit-modal"
              role="dialog"
              aria-modal="true"
              aria-labelledby="ap-edit-modal-title"
            >
              <div className="ap-modal-header">
                <div>
                  <span className="ap-modal-kicker">
                    SKILLSPHERE ADMINISTRATION
                  </span>

                  <h2 id="ap-edit-modal-title">
                    Edit Project
                  </h2>

                  <p>
                    Update the selected student's project details.
                  </p>
                </div>

                <button
                  type="button"
                  className="ap-modal-close"
                  onClick={closeEditModal}
                  disabled={saving}
                  aria-label="Close popup"
                >
                  ×
                </button>
              </div>

              <form onSubmit={handleEditSubmit}>
                <ProjectFields
                  form={editForm}
                  onChange={handleEditChange}
                  prefix="ap-edit"
                />

                <div className="ap-modal-actions">
                  <button
                    type="button"
                    className="ap-modal-cancel"
                    onClick={closeEditModal}
                    disabled={saving}
                  >
                    Cancel
                  </button>

                  <button
                    type="submit"
                    className="ap-modal-save"
                    disabled={saving}
                  >
                    {saving
                      ? "Saving..."
                      : "Save Changes"}
                  </button>
                </div>
              </form>
            </section>
          </div>,
          document.body
        )}
    </div>
  );
}

export default AdminProjects;
