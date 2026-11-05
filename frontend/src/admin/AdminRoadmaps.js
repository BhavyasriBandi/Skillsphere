
import React, {
  useCallback,
  useEffect,
  useState,
} from "react";
import { createPortal } from "react-dom";
import { showToast } from "../components/ToastProvider";
import "./AdminRoadmaps.css";

const API_URL = "http://127.0.0.1:8000/api/roadmaps/";

const EMPTY_FORM = {
  title: "",
  description: "",
  category: "Web Development",
  target_role: "",
  level: "Beginner",
  duration: "",
  skills: [],
  learning_steps: [],
  image_url: "",
  is_active: true,
};

const CATEGORIES = [
  "Web Development",
  "Programming",
  "Data Science",
  "Database",
  "AI & Machine Learning",
  "Cybersecurity",
  "Cloud Computing",
  "Mobile Development",
];

const LEVELS = [
  "Beginner",
  "Intermediate",
  "Advanced",
];

function getToken() {
  return (
    localStorage.getItem("skillsphere_access") ||
    localStorage.getItem("access") ||
    ""
  );
}

async function apiRequest(url, options = {}) {
  const token = getToken();

  if (!token) {
    throw new Error(
      "Login session missing. Please log in again."
    );
  }

  const headers = {
    Authorization: `Bearer ${token}`,
    ...options.headers,
  };

  if (options.body) {
    headers["Content-Type"] = "application/json";
  }

  const response = await fetch(url, {
    ...options,
    headers,
  });

  if (response.status === 204) {
    return null;
  }

  const contentType =
    response.headers.get("content-type") || "";

  if (!contentType.includes("application/json")) {
    throw new Error(
      `The server returned an unexpected response (HTTP ${response.status}). Check the Django API URL and backend server.`
    );
  }

  const data = await response.json();

  if (!response.ok) {
    const detail =
      data.detail ||
      Object.values(data)
        .flat()
        .find((value) => typeof value === "string");

    throw new Error(
      detail ||
        `Request failed with status ${response.status}.`
    );
  }

  return data;
}

function toLines(value) {
  return Array.isArray(value)
    ? value.join("\n")
    : "";
}

function toList(value) {
  return value
    .split("\n")
    .map((item) => item.trim())
    .filter(Boolean);
}

/* Reusable roadmap fields */
function RoadmapFields({
  form,
  skillsText,
  stepsText,
  updateField,
  setSkillsText,
  setStepsText,
  prefix,
}) {
  return (
    <div className="ar-form-grid">
      <div className="ar-field">
        <label htmlFor={`${prefix}-title`}>
          Roadmap Title *
        </label>

        <input
          id={`${prefix}-title`}
          name="title"
          value={form.title}
          onChange={updateField}
          placeholder="e.g. Full Stack Web Development"
          required
        />
      </div>

      <div className="ar-field">
        <label htmlFor={`${prefix}-target-role`}>
          Target Role *
        </label>

        <input
          id={`${prefix}-target-role`}
          name="target_role"
          value={form.target_role}
          onChange={updateField}
          placeholder="e.g. Full Stack Developer"
          required
        />
      </div>

      <div className="ar-field">
        <label htmlFor={`${prefix}-category`}>
          Category *
        </label>

        <select
          id={`${prefix}-category`}
          name="category"
          value={form.category}
          onChange={updateField}
          required
        >
          {!CATEGORIES.includes(form.category) &&
            form.category && (
              <option value={form.category}>
                {form.category}
              </option>
            )}

          {CATEGORIES.map((category) => (
            <option key={category} value={category}>
              {category}
            </option>
          ))}
        </select>
      </div>

      <div className="ar-field">
        <label htmlFor={`${prefix}-level`}>
          Difficulty Level *
        </label>

        <select
          id={`${prefix}-level`}
          name="level"
          value={form.level}
          onChange={updateField}
          required
        >
          {LEVELS.map((level) => (
            <option key={level} value={level}>
              {level}
            </option>
          ))}
        </select>
      </div>

      <div className="ar-field">
        <label htmlFor={`${prefix}-duration`}>
          Duration *
        </label>

        <input
          id={`${prefix}-duration`}
          name="duration"
          value={form.duration}
          onChange={updateField}
          placeholder="e.g. 12 weeks"
          required
        />
      </div>

      <div className="ar-field">
        <label htmlFor={`${prefix}-image`}>
          Image URL (optional)
        </label>

        <input
          id={`${prefix}-image`}
          name="image_url"
          type="url"
          value={form.image_url}
          onChange={updateField}
          placeholder="https://example.com/image.jpg"
        />
      </div>

      <div className="ar-field ar-field-full">
        <label htmlFor={`${prefix}-description`}>
          Description *
        </label>

        <textarea
          id={`${prefix}-description`}
          name="description"
          value={form.description}
          onChange={updateField}
          placeholder="Describe the learning roadmap..."
          rows={4}
          required
        />
      </div>

      <div className="ar-field ar-field-full">
        <label htmlFor={`${prefix}-skills`}>
          Skills (one skill per line)
        </label>

        <textarea
          id={`${prefix}-skills`}
          value={skillsText}
          onChange={(event) =>
            setSkillsText(event.target.value)
          }
          placeholder={"HTML\nCSS\nJavaScript\nReact"}
          rows={4}
        />
      </div>

      <div className="ar-field ar-field-full">
        <label htmlFor={`${prefix}-steps`}>
          Learning Steps (one step per line)
        </label>

        <textarea
          id={`${prefix}-steps`}
          value={stepsText}
          onChange={(event) =>
            setStepsText(event.target.value)
          }
          placeholder={
            "Step 1: Learn the fundamentals\nStep 2: Practise projects"
          }
          rows={5}
        />
      </div>

      <div className="ar-field ar-field-full">
        <label className="ar-checkbox-label">
          <input
            type="checkbox"
            name="is_active"
            checked={form.is_active}
            onChange={updateField}
          />

          Roadmap is active and visible to students
        </label>
      </div>
    </div>
  );
}

export default function AdminRoadmaps() {
  const [roadmaps, setRoadmaps] = useState([]);

  // Create form state
  const [form, setForm] = useState({
    ...EMPTY_FORM,
  });

  const [skillsText, setSkillsText] = useState("");
  const [stepsText, setStepsText] = useState("");

  // Edit popup state
  const [editForm, setEditForm] = useState({
    ...EMPTY_FORM,
  });

  const [editSkillsText, setEditSkillsText] =
    useState("");

  const [editStepsText, setEditStepsText] =
    useState("");

  const [editingId, setEditingId] = useState(null);
  const [editModalOpen, setEditModalOpen] =
    useState(false);

  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");

  const [deletingId, setDeletingId] = useState(null);
  const [updatingId, setUpdatingId] = useState(null);

  const loadRoadmaps = useCallback(async () => {
    setLoading(true);
    setError("");

    try {
      const data = await apiRequest(API_URL);

      const items = Array.isArray(data)
        ? data
        : Array.isArray(data.results)
        ? data.results
        : [];

      setRoadmaps(items);
    } catch (err) {
      setError(
        err.message || "Unable to load roadmaps."
      );
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadRoadmaps();
  }, [loadRoadmaps]);

  // Prevent background scrolling when modal is open.
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

  // Close edit popup using Escape.
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

    window.addEventListener(
      "keydown",
      handleEscape
    );

    return () => {
      window.removeEventListener(
        "keydown",
        handleEscape
      );
    };
  }, [editModalOpen, saving]);

  function updateField(event) {
    const {
      name,
      value,
      type,
      checked,
    } = event.target;

    setForm((current) => ({
      ...current,
      [name]:
        type === "checkbox" ? checked : value,
    }));
  }

  function updateEditField(event) {
    const {
      name,
      value,
      type,
      checked,
    } = event.target;

    setEditForm((current) => ({
      ...current,
      [name]:
        type === "checkbox" ? checked : value,
    }));
  }

  function resetForm() {
    setForm({
      ...EMPTY_FORM,
    });

    setSkillsText("");
    setStepsText("");
  }

  // Open selected roadmap in centred edit popup.
  function startEdit(roadmap) {
    if (saving) return;

    setEditingId(roadmap.id);

    setEditForm({
      title: roadmap.title || "",
      description: roadmap.description || "",
      category:
        roadmap.category || "Web Development",
      target_role: roadmap.target_role || "",
      level: roadmap.level || "Beginner",
      duration: roadmap.duration || "",
      skills: Array.isArray(roadmap.skills)
        ? roadmap.skills
        : [],
      learning_steps: Array.isArray(
        roadmap.learning_steps
      )
        ? roadmap.learning_steps
        : [],
      image_url: roadmap.image_url || "",
      is_active: roadmap.is_active ?? true,
    });

    setEditSkillsText(
      toLines(roadmap.skills)
    );

    setEditStepsText(
      toLines(roadmap.learning_steps)
    );

    setEditModalOpen(true);
  }

  function closeEditModal() {
    if (saving) return;

    setEditModalOpen(false);
    setEditingId(null);

    setEditForm({
      ...EMPTY_FORM,
    });

    setEditSkillsText("");
    setEditStepsText("");
  }

  function buildPayload(currentForm, skills, steps) {
    return {
      ...currentForm,
      title: currentForm.title.trim(),
      description: currentForm.description.trim(),
      category: currentForm.category.trim(),
      target_role: currentForm.target_role.trim(),
      duration: currentForm.duration.trim(),
      image_url: currentForm.image_url.trim(),
      skills: toList(skills),
      learning_steps: toList(steps),
    };
  }

  // Create roadmap.
  async function handleSubmit(event) {
    event.preventDefault();

    if (saving) return;

    if (
      !form.title.trim() ||
      !form.description.trim()
    ) {
      showToast(
        "Please enter a roadmap title and description.",
        "error"
      );
      return;
    }

    setSaving(true);

    const payload = buildPayload(
      form,
      skillsText,
      stepsText
    );

    try {
      await apiRequest(API_URL, {
        method: "POST",
        body: JSON.stringify(payload),
      });

      showToast(
        "Roadmap created successfully.",
        "success"
      );

      resetForm();
      await loadRoadmaps();
    } catch (err) {
      showToast(
        err.message || "Unable to create roadmap.",
        "error"
      );
    } finally {
      setSaving(false);
    }
  }

  // Update roadmap from edit popup.
  async function handleEditSubmit(event) {
    event.preventDefault();

    if (saving || editingId === null) return;

    if (
      !editForm.title.trim() ||
      !editForm.description.trim()
    ) {
      showToast(
        "Please enter a roadmap title and description.",
        "error"
      );
      return;
    }

    setSaving(true);

    const payload = buildPayload(
      editForm,
      editSkillsText,
      editStepsText
    );

    try {
      await apiRequest(
        `${API_URL}${editingId}/`,
        {
          method: "PATCH",
          body: JSON.stringify(payload),
        }
      );

      showToast(
        "Roadmap updated successfully.",
        "success"
      );

      setEditModalOpen(false);
      setEditingId(null);

      setEditForm({
        ...EMPTY_FORM,
      });

      setEditSkillsText("");
      setEditStepsText("");

      await loadRoadmaps();
    } catch (err) {
      showToast(
        err.message || "Unable to update roadmap.",
        "error"
      );
    } finally {
      setSaving(false);
    }
  }

  async function handleDelete(roadmap) {
    if (deletingId !== null) return;

    const confirmed = window.confirm(
      `Delete "${roadmap.title}"? This cannot be undone.`
    );

    if (!confirmed) return;

    setDeletingId(roadmap.id);

    try {
      await apiRequest(
        `${API_URL}${roadmap.id}/`,
        {
          method: "DELETE",
        }
      );

      setRoadmaps((current) =>
        current.filter(
          (item) => item.id !== roadmap.id
        )
      );

      if (editingId === roadmap.id) {
        closeEditModal();
      }

      showToast(
        "Roadmap deleted successfully.",
        "success"
      );
    } catch (err) {
      showToast(
        err.message || "Unable to delete roadmap.",
        "error"
      );
    } finally {
      setDeletingId(null);
    }
  }

  async function toggleActive(roadmap) {
    if (updatingId !== null) return;

    setUpdatingId(roadmap.id);

    try {
      await apiRequest(
        `${API_URL}${roadmap.id}/`,
        {
          method: "PATCH",
          body: JSON.stringify({
            is_active: !roadmap.is_active,
          }),
        }
      );

      showToast(
        roadmap.is_active
          ? "Roadmap deactivated."
          : "Roadmap activated.",
        "success"
      );

      await loadRoadmaps();
    } catch (err) {
      showToast(
        err.message ||
          "Unable to change roadmap status.",
        "error"
      );
    } finally {
      setUpdatingId(null);
    }
  }

  const filteredRoadmaps = roadmaps.filter(
    (roadmap) =>
      [
        roadmap.title,
        roadmap.category,
        roadmap.target_role,
        roadmap.level,
        roadmap.duration,
      ]
        .join(" ")
        .toLowerCase()
        .includes(search.trim().toLowerCase())
  );

  return (
    <section className="ar-page">
      {/* PAGE HEADER */}
      <div className="ar-heading">
        <div>
          <h1>Roadmaps Management</h1>

          <p>
            Create, update, and manage learning
            roadmaps for SkillSphere students.
          </p>
        </div>

        <button
          type="button"
          className="ar-secondary"
          onClick={loadRoadmaps}
          disabled={loading}
        >
          {loading ? "Loading..." : "Refresh"}
        </button>
      </div>

      {/* STATISTICS */}
      <div className="ar-stats">
        <div className="ar-panel">
          <h3>Total Roadmaps</h3>
          <p>{roadmaps.length}</p>
        </div>

        <div className="ar-panel">
          <h3>Active Roadmaps</h3>
          <p>
            {
              roadmaps.filter(
                (item) => item.is_active
              ).length
            }
          </p>
        </div>

        <div className="ar-panel">
          <h3>Inactive Roadmaps</h3>
          <p>
            {
              roadmaps.filter(
                (item) => !item.is_active
              ).length
            }
          </p>
        </div>
      </div>

      {/* CREATE ROADMAP FORM */}
      <div className="ar-panel">
        <div className="ar-section-heading">
          <div>
            <h2>Create New Roadmap</h2>

            <p>
              Add a structured learning path
              for students.
            </p>
          </div>
        </div>

        <form onSubmit={handleSubmit}>
          <RoadmapFields
            form={form}
            skillsText={skillsText}
            stepsText={stepsText}
            updateField={updateField}
            setSkillsText={setSkillsText}
            setStepsText={setStepsText}
            prefix="create-roadmap"
          />

          <div className="ar-form-actions">
            <button
              type="submit"
              className="ar-primary"
              disabled={saving}
            >
              {saving
                ? "Saving..."
                : "Create Roadmap"}
            </button>

            <button
              type="button"
              className="ar-secondary"
              onClick={resetForm}
              disabled={saving}
            >
              Clear Form
            </button>
          </div>
        </form>
      </div>

      {/* ALL ROADMAPS */}
      <div className="ar-panel">
        <div className="ar-section-heading">
          <div>
            <h2>All Roadmaps</h2>

            <p>
              Search and manage existing learning
              roadmaps.
            </p>
          </div>

          <div className="ar-search">
            <input
              type="search"
              value={search}
              onChange={(event) =>
                setSearch(event.target.value)
              }
              placeholder="Search roadmaps..."
              aria-label="Search roadmaps"
            />
          </div>
        </div>

        {error && (
          <div className="ar-error" role="alert">
            <p>{error}</p>

            <button
              type="button"
              className="ar-secondary"
              onClick={loadRoadmaps}
            >
              Try Again
            </button>
          </div>
        )}

        {loading ? (
          <p className="ar-empty">
            Loading roadmaps...
          </p>
        ) : filteredRoadmaps.length === 0 ? (
          <div className="ar-empty">
            <h3>No roadmaps found</h3>

            <p>
              {search
                ? "Try another search term."
                : "Create your first roadmap using the form above."}
            </p>
          </div>
        ) : (
          <div className="ar-table-wrap">
            <table className="ar-table">
              <thead>
                <tr>
                  <th>Roadmap</th>
                  <th>Target Role</th>
                  <th>Level</th>
                  <th>Duration</th>
                  <th>Status</th>
                  <th>Actions</th>
                </tr>
              </thead>

              <tbody>
                {filteredRoadmaps.map((roadmap) => (
                  <tr key={roadmap.id}>
                    <td>
                      <div className="ar-roadmap-title">
                        <strong>
                          {roadmap.title}
                        </strong>

                        <span>
                          {roadmap.category}
                        </span>
                      </div>
                    </td>

                    <td>
                      {roadmap.target_role || "—"}
                    </td>

                    <td>{roadmap.level}</td>

                    <td>
                      {roadmap.duration || "—"}
                    </td>

                    <td>
                      <span
                        className={
                          roadmap.is_active
                            ? "ar-status ar-status-active"
                            : "ar-status ar-status-inactive"
                        }
                      >
                        {roadmap.is_active
                          ? "Active"
                          : "Inactive"}
                      </span>
                    </td>

                    <td>
                      <div className="ar-row-actions">
                        <button
                          type="button"
                          className="ar-secondary"
                          onClick={() =>
                            startEdit(roadmap)
                          }
                          disabled={
                            saving ||
                            deletingId !== null
                          }
                        >
                          Edit
                        </button>

                        <button
                          type="button"
                          className="ar-secondary"
                          onClick={() =>
                            toggleActive(roadmap)
                          }
                          disabled={
                            updatingId !== null
                          }
                        >
                          {updatingId === roadmap.id
                            ? "Updating..."
                            : roadmap.is_active
                            ? "Deactivate"
                            : "Activate"}
                        </button>

                        <button
                          type="button"
                          className="ar-danger"
                          onClick={() =>
                            handleDelete(roadmap)
                          }
                          disabled={
                            deletingId !== null
                          }
                        >
                          {deletingId === roadmap.id
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
      </div>

      {/* CENTRED EDIT ROADMAP MODAL */}
      {editModalOpen &&
        createPortal(
          <div
            className="ar-modal-backdrop"
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
              className="ar-edit-modal"
              role="dialog"
              aria-modal="true"
              aria-labelledby="ar-edit-modal-title"
            >
              <div className="ar-modal-header">
                <div>
                  <span className="ar-modal-kicker">
                    ROADMAP MANAGEMENT
                  </span>

                  <h2 id="ar-edit-modal-title">
                    Edit Roadmap
                  </h2>

                  <p>
                    Update the selected roadmap details.
                  </p>
                </div>

                <button
                  type="button"
                  className="ar-modal-close"
                  onClick={closeEditModal}
                  disabled={saving}
                  aria-label="Close edit popup"
                >
                  ×
                </button>
              </div>

              <form onSubmit={handleEditSubmit}>
                <RoadmapFields
                  form={editForm}
                  skillsText={editSkillsText}
                  stepsText={editStepsText}
                  updateField={updateEditField}
                  setSkillsText={setEditSkillsText}
                  setStepsText={setEditStepsText}
                  prefix="edit-roadmap"
                />

                <div className="ar-modal-actions">
                  <button
                    type="button"
                    className="ar-modal-cancel"
                    onClick={closeEditModal}
                    disabled={saving}
                  >
                    Cancel
                  </button>

                  <button
                    type="submit"
                    className="ar-modal-save"
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
    </section>
  );
}
