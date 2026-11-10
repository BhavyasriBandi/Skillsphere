
import React, {
  useCallback,
  useEffect,
  useState,
} from "react";
import { createPortal } from "react-dom";
import { showToast } from "../components/ToastProvider";
import "./AdminLearningResources.css";

const API_URL =
  "https://skillsphere-u93o.onrender.com/api/learning-resources/";

const EMPTY_FORM = {
  title: "",
  category: "Programming",
  skill: "",
  level: "Beginner",
  resource_type: "Tutorial",
  description: "",
  url: "",
  is_active: true,
};

const CATEGORIES = [
  "Programming",
  "Web Development",
  "Database",
  "Tools",
  "Computer Science",
];

const LEVELS = [
  "Beginner",
  "Intermediate",
  "Advanced",
];

const TYPES = [
  "Course",
  "Tutorial",
  "Documentation",
  "Practice",
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
      "Your login session is missing. Please log in again."
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

  const data = await response.json().catch(() => ({}));

  if (!response.ok) {
    const message =
      data.detail ||
      Object.values(data)
        .flat()
        .find((value) => typeof value === "string") ||
      `Request failed (${response.status}).`;

    throw new Error(message);
  }

  return data;
}

function ResourceFields({
  form,
  updateField,
  prefix,
}) {
  return (
    <div className="alr-form-grid">
      <label htmlFor={`${prefix}-title`}>
        Resource title *
        <input
          id={`${prefix}-title`}
          name="title"
          value={form.title}
          onChange={updateField}
          maxLength={200}
          required
          placeholder="e.g. Python Official Tutorial"
        />
      </label>

      <label htmlFor={`${prefix}-skill`}>
        Skill *
        <input
          id={`${prefix}-skill`}
          name="skill"
          value={form.skill}
          onChange={updateField}
          maxLength={100}
          required
          placeholder="e.g. Python"
        />
      </label>

      <label htmlFor={`${prefix}-category`}>
        Category *
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

          {CATEGORIES.map((item) => (
            <option key={item} value={item}>
              {item}
            </option>
          ))}
        </select>
      </label>

      <label htmlFor={`${prefix}-level`}>
        Difficulty level *
        <select
          id={`${prefix}-level`}
          name="level"
          value={form.level}
          onChange={updateField}
          required
        >
          {!LEVELS.includes(form.level) &&
            form.level && (
              <option value={form.level}>
                {form.level}
              </option>
            )}

          {LEVELS.map((item) => (
            <option key={item} value={item}>
              {item}
            </option>
          ))}
        </select>
      </label>

      <label htmlFor={`${prefix}-type`}>
        Resource type *
        <select
          id={`${prefix}-type`}
          name="resource_type"
          value={form.resource_type}
          onChange={updateField}
          required
        >
          {!TYPES.includes(form.resource_type) &&
            form.resource_type && (
              <option value={form.resource_type}>
                {form.resource_type}
              </option>
            )}

          {TYPES.map((item) => (
            <option key={item} value={item}>
              {item}
            </option>
          ))}
        </select>
      </label>

      <label htmlFor={`${prefix}-url`}>
        Resource URL *
        <input
          id={`${prefix}-url`}
          type="url"
          name="url"
          value={form.url}
          onChange={updateField}
          maxLength={500}
          required
          placeholder="https://example.com/learn"
        />
      </label>

      <label
        className="alr-full"
        htmlFor={`${prefix}-description`}
      >
        Description *
        <textarea
          id={`${prefix}-description`}
          name="description"
          value={form.description}
          onChange={updateField}
          required
          rows={3}
          placeholder="Describe what students will learn..."
        />
      </label>

      <label className="alr-active-check">
        <input
          type="checkbox"
          name="is_active"
          checked={form.is_active}
          onChange={updateField}
        />
        Make this resource visible to students
      </label>
    </div>
  );
}

export default function AdminLearningResources() {
  const [resources, setResources] = useState([]);

  // Create form remains on the page.
  const [form, setForm] = useState({
    ...EMPTY_FORM,
  });

  // Edit form is separate and appears in a popup.
  const [editForm, setEditForm] = useState({
    ...EMPTY_FORM,
  });

  const [editingId, setEditingId] = useState(null);
  const [editModalOpen, setEditModalOpen] =
    useState(false);

  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");

  const [deleteTarget, setDeleteTarget] =
    useState(null);

  const [deleting, setDeleting] = useState(false);
  const [updatingId, setUpdatingId] =
    useState(null);

  const loadResources = useCallback(async () => {
    setLoading(true);
    setError("");

    try {
      const data = await apiRequest(API_URL);

      setResources(
        Array.isArray(data)
          ? data
          : Array.isArray(data.results)
          ? data.results
          : []
      );
    } catch (err) {
      setError(
        err.message ||
          "Unable to load learning resources."
      );
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadResources();
  }, [loadResources]);

  // Prevent background scrolling when a popup opens.
  useEffect(() => {
    if (!editModalOpen && !deleteTarget) {
      return undefined;
    }

    const previousOverflow =
      document.body.style.overflow;

    document.body.style.overflow = "hidden";

    return () => {
      document.body.style.overflow =
        previousOverflow;
    };
  }, [editModalOpen, deleteTarget]);

  // Close popups with Escape.
  useEffect(() => {
    function handleEscape(event) {
      if (event.key !== "Escape") return;

      if (saving || deleting) return;

      if (deleteTarget) {
        setDeleteTarget(null);
      } else if (editModalOpen) {
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
  }, [
    editModalOpen,
    deleteTarget,
    saving,
    deleting,
  ]);

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
  }

  // Open selected resource in a centred modal.
  function startEdit(resource) {
    if (saving || deleting) return;

    setEditingId(resource.id);

    setEditForm({
      title: resource.title || "",
      category:
        resource.category || "Programming",
      skill: resource.skill || "",
      level: resource.level || "Beginner",
      resource_type:
        resource.resource_type || "Tutorial",
      description: resource.description || "",
      url: resource.url || "",
      is_active: resource.is_active ?? true,
    });

    setEditModalOpen(true);
  }

  function closeEditModal() {
    if (saving) return;

    setEditModalOpen(false);
    setEditingId(null);

    setEditForm({
      ...EMPTY_FORM,
    });
  }

  // Add new resource.
  async function handleSubmit(event) {
    event.preventDefault();

    if (saving) return;

    setSaving(true);

    try {
      await apiRequest(API_URL, {
        method: "POST",
        body: JSON.stringify(form),
      });

      showToast(
        "Learning resource added successfully.",
        "success"
      );

      resetForm();
      await loadResources();
    } catch (err) {
      showToast(
        err.message ||
          "Could not add the resource.",
        "error"
      );
    } finally {
      setSaving(false);
    }
  }

  // Save changes from the popup.
  async function handleEditSubmit(event) {
    event.preventDefault();

    if (saving || editingId === null) {
      return;
    }

    setSaving(true);

    try {
      await apiRequest(
        `${API_URL}${editingId}/`,
        {
          method: "PATCH",
          body: JSON.stringify(editForm),
        }
      );

      showToast(
        "Learning resource updated successfully.",
        "success"
      );

      setEditModalOpen(false);
      setEditingId(null);

      setEditForm({
        ...EMPTY_FORM,
      });

      await loadResources();
    } catch (err) {
      showToast(
        err.message ||
          "Could not update the resource.",
        "error"
      );
    } finally {
      setSaving(false);
    }
  }

  // Open custom delete confirmation.
  function handleDelete(resource) {
    setDeleteTarget(resource);
  }

  // Confirm deletion.
  async function confirmDelete() {
    if (!deleteTarget || deleting) {
      return;
    }

    const resource = deleteTarget;

    setDeleting(true);

    try {
      await apiRequest(
        `${API_URL}${resource.id}/`,
        {
          method: "DELETE",
        }
      );

      setResources((current) =>
        current.filter(
          (item) => item.id !== resource.id
        )
      );

      if (editingId === resource.id) {
        setEditModalOpen(false);
        setEditingId(null);
      }

      setDeleteTarget(null);

      showToast(
        "Learning resource deleted.",
        "success"
      );
    } catch (err) {
      showToast(
        err.message ||
          "Could not delete the resource.",
        "error"
      );
    } finally {
      setDeleting(false);
    }
  }

  // Activate or deactivate resource.
  async function toggleActive(resource) {
    if (updatingId !== null) return;

    setUpdatingId(resource.id);

    try {
      await apiRequest(
        `${API_URL}${resource.id}/`,
        {
          method: "PATCH",
          body: JSON.stringify({
            is_active: !resource.is_active,
          }),
        }
      );

      showToast(
        resource.is_active
          ? "Resource deactivated."
          : "Resource activated.",
        "success"
      );

      await loadResources();
    } catch (err) {
      showToast(
        err.message ||
          "Could not update resource status.",
        "error"
      );
    } finally {
      setUpdatingId(null);
    }
  }

  const filteredResources = resources.filter(
    (resource) => {
      const text = [
        resource.title,
        resource.skill,
        resource.category,
        resource.resource_type,
      ]
        .filter(Boolean)
        .join(" ")
        .toLowerCase();

      return text.includes(
        search.trim().toLowerCase()
      );
    }
  );

  return (
    <section className="alr-page">
      {/* PAGE HEADER */}
      <div className="alr-summary">
        <div>
          <span className="alr-kicker">
            CONTENT MANAGEMENT
          </span>

          <h2>Learning Resources</h2>

          <p>
            Add and maintain learning materials
            available to students.
          </p>
        </div>

        <button
          type="button"
          className="alr-refresh"
          onClick={loadResources}
          disabled={loading}
        >
          {loading
            ? "Loading..."
            : "↻ Refresh"}
        </button>
      </div>

      {/* STATISTICS */}
      <div className="alr-stats">
        <article>
          <span>Total resources</span>
          <strong>
            {resources.length}
          </strong>
        </article>

        <article>
          <span>Active resources</span>
          <strong>
            {
              resources.filter(
                (resource) =>
                  resource.is_active
              ).length
            }
          </strong>
        </article>

        <article>
          <span>Inactive resources</span>
          <strong>
            {
              resources.filter(
                (resource) =>
                  !resource.is_active
              ).length
            }
          </strong>
        </article>
      </div>

      {/* ADD RESOURCE FORM */}
      <form
        id="admin-resource-form"
        className="alr-panel alr-form"
        onSubmit={handleSubmit}
      >
        <div className="alr-panel-heading">
          <div>
            <h3>Add New Resource</h3>

            <p>
              Complete the details below to
              publish a learning resource.
            </p>
          </div>
        </div>

        <ResourceFields
          form={form}
          updateField={updateField}
          prefix="alr-create"
        />

        <div className="alr-form-actions">
          <button
            className="alr-primary"
            type="submit"
            disabled={saving}
          >
            {saving
              ? "Saving..."
              : "Add Resource"}
          </button>

          <button
            className="alr-secondary"
            type="button"
            onClick={resetForm}
            disabled={saving}
          >
            Clear Form
          </button>
        </div>
      </form>

      {/* RESOURCE LIST */}
      <section className="alr-panel alr-list-panel">
        <div className="alr-panel-heading alr-list-heading">
          <div>
            <h3>
              All Learning Resources
            </h3>

            <p>
              Manage the resources stored
              in your database.
            </p>
          </div>

          <input
            className="alr-search"
            type="search"
            value={search}
            onChange={(event) =>
              setSearch(event.target.value)
            }
            placeholder="Search resources..."
            aria-label="Search learning resources"
          />
        </div>

        {error && (
          <div className="alr-error">
            <p>{error}</p>

            <button
              type="button"
              onClick={loadResources}
            >
              Try again
            </button>
          </div>
        )}

        {loading ? (
          <p className="alr-message">
            Loading resources...
          </p>
        ) : !error &&
          filteredResources.length === 0 ? (
          <div className="alr-empty">
            <span aria-hidden="true">
              ▣
            </span>

            <h4>
              {search
                ? "No matching resources"
                : "No resources yet"}
            </h4>

            <p>
              {search
                ? "Try another search term."
                : "Use the form above to add your first learning resource."}
            </p>
          </div>
        ) : (
          <div className="alr-table-wrap">
            <table className="alr-table">
              <thead>
                <tr>
                  <th>Resource</th>
                  <th>Category</th>
                  <th>Level</th>
                  <th>Status</th>
                  <th>Actions</th>
                </tr>
              </thead>

              <tbody>
                {filteredResources.map(
                  (resource) => (
                    <tr key={resource.id}>
                      <td>
                        <strong>
                          {resource.title}
                        </strong>

                        <span className="alr-resource-skill">
                          {resource.skill}
                          {" · "}
                          {resource.resource_type}
                        </span>

                        <a
                          className="alr-resource-link"
                          href={resource.url}
                          target="_blank"
                          rel="noreferrer"
                        >
                          Open resource ↗
                        </a>
                      </td>

                      <td>
                        {resource.category}
                      </td>

                      <td>
                        {resource.level}
                      </td>

                      <td>
                        <span
                          className={`alr-status ${
                            resource.is_active
                              ? "is-active"
                              : "is-inactive"
                          }`}
                        >
                          {resource.is_active
                            ? "Active"
                            : "Inactive"}
                        </span>
                      </td>

                      <td>
                        <div className="alr-row-actions">
                          <button
                            type="button"
                            className="alr-edit"
                            onClick={() =>
                              startEdit(resource)
                            }
                            disabled={saving || deleting}
                          >
                            Edit
                          </button>

                          <button
                            type="button"
                            className="alr-toggle"
                            onClick={() =>
                              toggleActive(resource)
                            }
                            disabled={
                              updatingId !== null
                            }
                          >
                            {updatingId === resource.id
                              ? "Updating..."
                              : resource.is_active
                              ? "Deactivate"
                              : "Activate"}
                          </button>

                          <button
                            type="button"
                            className="alr-delete"
                            onClick={() =>
                              handleDelete(resource)
                            }
                            disabled={saving || deleting}
                          >
                            Delete
                          </button>
                        </div>
                      </td>
                    </tr>
                  )
                )}
              </tbody>
            </table>
          </div>
        )}
      </section>

      {/* EDIT RESOURCE MODAL */}
      {editModalOpen &&
        createPortal(
          <div
            className="alr-modal-backdrop"
            onMouseDown={(event) => {
              if (
                event.target ===
                  event.currentTarget &&
                !saving
              ) {
                closeEditModal();
              }
            }}
          >
            <section
              className="alr-modal"
              role="dialog"
              aria-modal="true"
              aria-labelledby="alr-modal-title"
            >
              <div className="alr-modal-header">
                <div>
                  <span className="alr-modal-kicker">
                    CONTENT MANAGEMENT
                  </span>

                  <h3 id="alr-modal-title">
                    Edit Learning Resource
                  </h3>

                  <p>
                    Update the selected
                    resource details.
                  </p>
                </div>

                <button
                  type="button"
                  className="alr-modal-close"
                  aria-label="Close popup"
                  onClick={closeEditModal}
                  disabled={saving}
                >
                  ×
                </button>
              </div>

              <form
                onSubmit={handleEditSubmit}
              >
                <ResourceFields
                  form={editForm}
                  updateField={updateEditField}
                  prefix="alr-edit"
                />

                <div className="alr-modal-actions">
                  <button
                    type="button"
                    className="alr-modal-cancel"
                    onClick={closeEditModal}
                    disabled={saving}
                  >
                    Cancel
                  </button>

                  <button
                    type="submit"
                    className="alr-modal-save"
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

      {/* DELETE CONFIRMATION MODAL */}
      {deleteTarget &&
        createPortal(
          <div
            className="alr-modal-backdrop"
            onMouseDown={(event) => {
              if (
                event.target ===
                  event.currentTarget &&
                !deleting
              ) {
                setDeleteTarget(null);
              }
            }}
          >
            <section
              className="alr-modal alr-delete-modal"
              role="alertdialog"
              aria-modal="true"
              aria-labelledby="alr-delete-title"
            >
              <div className="alr-modal-header">
                <div>
                  <span className="alr-modal-kicker">
                    CONTENT MANAGEMENT
                  </span>

                  <h3 id="alr-delete-title">
                    Delete Resource?
                  </h3>
                </div>

                <button
                  type="button"
                  className="alr-modal-close"
                  onClick={() =>
                    setDeleteTarget(null)
                  }
                  disabled={deleting}
                  aria-label="Close popup"
                >
                  ×
                </button>
              </div>

              <p className="alr-delete-message">
                Are you sure you want to delete
                {" "}
                <strong>
                  {deleteTarget.title}
                </strong>
                ? This action cannot be undone.
              </p>

              <div className="alr-modal-actions">
                <button
                  type="button"
                  className="alr-modal-cancel"
                  onClick={() =>
                    setDeleteTarget(null)
                  }
                  disabled={deleting}
                >
                  Cancel
                </button>

                <button
                  type="button"
                  className="alr-modal-delete"
                  onClick={confirmDelete}
                  disabled={deleting}
                >
                  {deleting
                    ? "Deleting..."
                    : "Yes, Delete"}
                </button>
              </div>
            </section>
          </div>,
          document.body
        )}
    </section>
  );
}
