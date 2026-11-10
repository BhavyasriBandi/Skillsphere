
import React, { useCallback, useEffect, useMemo, useState } from "react";
import "./AdminAchievements.css";
import { showToast } from "../components/ToastProvider";

const API_URL = "https://skillsphere-17hl.onrender.com/api/achievements/admin/";

const CATEGORIES = [
  "Career",
  "Assessment",
  "Projects",
  "Challenges",
  "Learning",
  "Interview",
  "Skills",
  "Roadmap",
  "Special",
];

const EMPTY_FORM = {
  title: "",
  category: "Learning",
  description: "",
  criteria: "",
  points: 10,
  status: "Active",
};

function getAccessToken() {
  return localStorage.getItem("skillsphere_access");
}

async function apiRequest(url, options = {}) {
  const token = getAccessToken();

  if (!token) {
    throw new Error(
      "Your login token was not found. Please log in again."
    );
  }

  const response = await fetch(url, {
    ...options,
    headers: {
      Authorization: `Bearer ${token}`,
      ...(options.body ? { "Content-Type": "application/json" } : {}),
      ...options.headers,
    },
  });

  const text = await response.text();
  let data = null;

  if (text) {
    try {
      data = JSON.parse(text);
    } catch {
      data = { detail: text };
    }
  }

  if (!response.ok) {
    if (response.status === 401) {
      throw new Error("Your session expired. Please log in again.");
    }

    if (response.status === 403) {
      throw new Error(
        "Admin access is required. Check that your account belongs to the Admin group."
      );
    }

    const message =
      data?.detail ||
      data?.error ||
      Object.entries(data || {})
        .map(([key, value]) => {
          const detail = Array.isArray(value)
            ? value.join(", ")
            : typeof value === "string"
              ? value
              : JSON.stringify(value);

          return `${key}: ${detail}`;
        })
        .join(" | ") ||
      `Request failed with status ${response.status}.`;

    throw new Error(message);
  }

  return data;
}

function toFrontendAchievement(item) {
  return {
    ...item,
    criteria: item.requirement || "",
    points: Number(item.points || 0),
    status: item.is_active ? "Active" : "Inactive",
  };
}

function makeBadgeKey(title) {
  const slug = title
    .trim()
    .toLowerCase()
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");

  return slug || `achievement-${Date.now()}`;
}

function getErrorMessage(error) {
  return error instanceof Error
    ? error.message
    : "Something went wrong. Please try again.";
}

export default function AdminAchievements() {
  const [achievements, setAchievements] = useState([]);
  const [search, setSearch] = useState("");
  const [categoryFilter, setCategoryFilter] = useState("");
  const [statusFilter, setStatusFilter] = useState("");
  const [modalOpen, setModalOpen] = useState(false);
  const [editingItem, setEditingItem] = useState(null);
  const [deleteItem, setDeleteItem] = useState(null);
  const [form, setForm] = useState({ ...EMPTY_FORM });
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);

  const loadAchievements = useCallback(async () => {
    setLoading(true);

    try {
      const data = await apiRequest(API_URL);
      const records = Array.isArray(data)
        ? data
        : Array.isArray(data?.results)
          ? data.results
          : [];

      setAchievements(records.map(toFrontendAchievement));
    } catch (error) {
      showToast(getErrorMessage(error), "error");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadAchievements();
  }, [loadAchievements]);

  const filteredAchievements = useMemo(() => {
    const query = search.trim().toLowerCase();

    return achievements.filter((item) => {
      const matchesSearch =
        !query ||
        (item.title || "").toLowerCase().includes(query) ||
        (item.description || "").toLowerCase().includes(query) ||
        (item.criteria || "").toLowerCase().includes(query);

      const matchesCategory =
        !categoryFilter || item.category === categoryFilter;

      const matchesStatus =
        !statusFilter || item.status === statusFilter;

      return matchesSearch && matchesCategory && matchesStatus;
    });
  }, [achievements, search, categoryFilter, statusFilter]);

  const stats = useMemo(
    () => ({
      total: achievements.length,
      active: achievements.filter((item) => item.status === "Active").length,
      inactive: achievements.filter(
        (item) => item.status === "Inactive"
      ).length,
      points: achievements.reduce(
        (total, item) => total + Number(item.points || 0),
        0
      ),
    }),
    [achievements]
  );

  function openAddModal() {
    setEditingItem(null);
    setForm({ ...EMPTY_FORM });
    setModalOpen(true);
  }

  function openEditModal(item) {
    setEditingItem(item);
    setForm({
      title: item.title || "",
      category: item.category || "Special",
      description: item.description || "",
      criteria: item.requirement || "",
      points: item.points ?? 0,
      status: item.is_active ? "Active" : "Inactive",
    });
    setModalOpen(true);
  }

  function handleChange(event) {
    const { name, value } = event.target;

    setForm((previous) => ({
      ...previous,
      [name]: value,
    }));
  }

  async function saveAchievement(event) {
    event.preventDefault();

    if (
      !form.title.trim() ||
      !form.description.trim() ||
      !form.criteria.trim()
    ) {
      showToast(
        "Please complete the title, description, and recognition criteria.",
        "warning"
      );
      return;
    }

    if (form.points === "" || Number(form.points) < 0) {
      showToast("Points must be zero or greater.", "warning");
      return;
    }

    const payload = {
      badge_key:
        editingItem?.badge_key || makeBadgeKey(form.title),
      title: form.title.trim(),
      description: form.description.trim(),
      icon: editingItem?.icon || "🏆",
      category: form.category,
      tier: editingItem?.tier || "bronze",
      requirement: form.criteria.trim(),
      target: Number(editingItem?.target || 1),
      points: Number(form.points),
      is_active: form.status === "Active",
    };

    setSaving(true);

    try {
      if (editingItem) {
        const updated = await apiRequest(
          `${API_URL}${editingItem.id}/`,
          {
            method: "PATCH",
            body: JSON.stringify(payload),
          }
        );

        setAchievements((previous) =>
          previous.map((item) =>
            item.id === editingItem.id
              ? toFrontendAchievement(updated)
              : item
          )
        );

        showToast("Achievement updated successfully.", "success");
      } else {
        const created = await apiRequest(API_URL, {
          method: "POST",
          body: JSON.stringify(payload),
        });

        setAchievements((previous) => [
          toFrontendAchievement(created),
          ...previous,
        ]);

        showToast("Achievement created successfully.", "success");
      }

      setModalOpen(false);
      setEditingItem(null);
    } catch (error) {
      showToast(getErrorMessage(error), "error");
    } finally {
      setSaving(false);
    }
  }

  async function toggleStatus(item) {
    const nextStatus = item.status !== "Active";

    try {
      const updated = await apiRequest(
        `${API_URL}${item.id}/activation/`,
        {
          method: "PATCH",
          body: JSON.stringify({ is_active: nextStatus }),
        }
      );

      setAchievements((previous) =>
        previous.map((achievement) =>
          achievement.id === item.id
            ? toFrontendAchievement(updated)
            : achievement
        )
      );

      showToast(
        `Achievement ${nextStatus ? "activated" : "deactivated"} successfully.`,
        "success"
      );
    } catch (error) {
      showToast(getErrorMessage(error), "error");
    }
  }

  async function confirmDelete() {
    if (!deleteItem) return;

    try {
      await apiRequest(`${API_URL}${deleteItem.id}/`, {
        method: "DELETE",
      });

      setAchievements((previous) =>
        previous.map((item) =>
          item.id === deleteItem.id
            ? { ...item, is_active: false, status: "Inactive" }
            : item
        )
      );

      showToast(
        "Achievement deactivated. Existing student records were preserved.",
        "success"
      );
      setDeleteItem(null);
    } catch (error) {
      showToast(getErrorMessage(error), "error");
    }
  }

  function clearFilters() {
    setSearch("");
    setCategoryFilter("");
    setStatusFilter("");
  }

  return (
    <div className="aa-page">
      <header className="aa-heading">
        <div>
          <span className="aa-eyebrow">SKILLSPHERE / ADMIN</span>
          <h1>Achievements</h1>
          <p>
            Manage achievement categories and recognition milestones.
          </p>
        </div>

        <button
          className="aa-button aa-button-primary"
          type="button"
          onClick={openAddModal}
        >
          + Add Achievement
        </button>
      </header>

      <section className="aa-stats">
        <article className="aa-stat-card">
          <span>Total Achievements</span>
          <strong>{stats.total}</strong>
          <small>All configured achievements</small>
        </article>

        <article className="aa-stat-card">
          <span>Active Achievements</span>
          <strong>{stats.active}</strong>
          <small>Currently available</small>
        </article>

        <article className="aa-stat-card">
          <span>Inactive Achievements</span>
          <strong>{stats.inactive}</strong>
          <small>Currently disabled</small>
        </article>

        <article className="aa-stat-card">
          <span>Total Points</span>
          <strong>{stats.points}</strong>
          <small>Points across configured items</small>
        </article>
      </section>

      <section className="aa-panel">
        <div className="aa-filters">
          <input
            className="aa-field"
            type="search"
            placeholder="Search achievements..."
            value={search}
            onChange={(event) => setSearch(event.target.value)}
          />

          <select
            className="aa-field"
            value={categoryFilter}
            onChange={(event) => setCategoryFilter(event.target.value)}
          >
            <option value="">All categories</option>
            {CATEGORIES.map((category) => (
              <option key={category} value={category}>
                {category}
              </option>
            ))}
          </select>

          <select
            className="aa-field"
            value={statusFilter}
            onChange={(event) => setStatusFilter(event.target.value)}
          >
            <option value="">All statuses</option>
            <option value="Active">Active</option>
            <option value="Inactive">Inactive</option>
          </select>

          <button
            className="aa-button"
            type="button"
            onClick={clearFilters}
          >
            Clear Filters
          </button>
        </div>

        <div className="aa-table-heading">
          <div>
            <h2>Achievement Management</h2>
            <p>
              Showing {filteredAchievements.length} of{" "}
              {achievements.length} achievements
            </p>
          </div>
        </div>

        <div className="aa-table-wrap">
          <table className="aa-table">
            <thead>
              <tr>
                <th>Achievement</th>
                <th>Category</th>
                <th>Recognition Criteria</th>
                <th>Points</th>
                <th>Status</th>
                <th>Actions</th>
              </tr>
            </thead>

            <tbody>
              {loading ? (
                <tr>
                  <td colSpan="6" className="aa-empty">
                    <strong>Loading achievements...</strong>
                    <p>Fetching records from the SkillSphere backend.</p>
                  </td>
                </tr>
              ) : (
                <>
                  {filteredAchievements.map((item) => (
                    <tr key={item.id}>
                      <td>
                        <div className="aa-achievement-name">
                          <span className="aa-star">
                            {item.icon || "☆"}
                          </span>
                          <div>
                            <strong>{item.title}</strong>
                            <small>{item.description}</small>
                          </div>
                        </div>
                      </td>

                      <td>
                        <span className="aa-category">
                          {item.category}
                        </span>
                      </td>

                      <td>{item.criteria}</td>

                      <td>
                        <strong>{item.points}</strong>
                      </td>

                      <td>
                        <span
                          className={`aa-status ${
                            item.status === "Active"
                              ? "aa-status-active"
                              : "aa-status-inactive"
                          }`}
                        >
                          {item.status}
                        </span>
                      </td>

                      <td>
                        <div className="aa-actions">
                          <button
                            type="button"
                            className="aa-text-button"
                            onClick={() => openEditModal(item)}
                          >
                            Edit
                          </button>

                          <button
                            type="button"
                            className="aa-text-button"
                            onClick={() => toggleStatus(item)}
                          >
                            {item.status === "Active" ? "Disable" : "Enable"}
                          </button>

                          <button
                            type="button"
                            className="aa-text-button aa-delete"
                            onClick={() => setDeleteItem(item)}
                          >
                            Delete
                          </button>
                        </div>
                      </td>
                    </tr>
                  ))}

                  {filteredAchievements.length === 0 && (
                    <tr>
                      <td colSpan="6" className="aa-empty">
                        <div className="aa-empty-icon">☆</div>
                        <strong>
                          {achievements.length === 0
                            ? "No achievements configured yet"
                            : "No achievements found"}
                        </strong>
                        <p>
                          Change your filters or add an achievement.
                        </p>
                      </td>
                    </tr>
                  )}
                </>
              )}
            </tbody>
          </table>
        </div>
      </section>

      {modalOpen && (
        <div
          className="aa-overlay"
          onMouseDown={(event) => {
            if (
              event.target === event.currentTarget &&
              !saving
            ) {
              setModalOpen(false);
            }
          }}
        >
          <section
            className="aa-modal"
            role="dialog"
            aria-modal="true"
            aria-labelledby="aa-modal-title"
          >
            <div className="aa-modal-heading">
              <div>
                <span className="aa-eyebrow">ACHIEVEMENT SETTINGS</span>
                <h2 id="aa-modal-title">
                  {editingItem ? "Edit Achievement" : "Add Achievement"}
                </h2>
                <p>
                  Configure the milestone and its recognition criteria.
                </p>
              </div>

              <button
                type="button"
                className="aa-close"
                aria-label="Close"
                disabled={saving}
                onClick={() => setModalOpen(false)}
              >
                ×
              </button>
            </div>

            <form onSubmit={saveAchievement}>
              <div className="aa-form-grid">
                <div className="aa-form-full">
                  <label htmlFor="aa-title">Achievement title *</label>
                  <input
                    id="aa-title"
                    className="aa-field"
                    name="title"
                    value={form.title}
                    onChange={handleChange}
                    placeholder="e.g. Problem Solver"
                    required
                  />
                </div>

                <div>
                  <label htmlFor="aa-category">Category *</label>
                  <select
                    id="aa-category"
                    className="aa-field"
                    name="category"
                    value={form.category}
                    onChange={handleChange}
                    required
                  >
                    {CATEGORIES.map((category) => (
                      <option key={category} value={category}>
                        {category}
                      </option>
                    ))}
                  </select>
                </div>

                <div>
                  <label htmlFor="aa-points">Points *</label>
                  <input
                    id="aa-points"
                    className="aa-field"
                    type="number"
                    name="points"
                    min="0"
                    value={form.points}
                    onChange={handleChange}
                    required
                  />
                </div>

                <div className="aa-form-full">
                  <label htmlFor="aa-description">Description *</label>
                  <textarea
                    id="aa-description"
                    className="aa-field aa-textarea"
                    name="description"
                    value={form.description}
                    onChange={handleChange}
                    placeholder="Describe what this achievement represents."
                    required
                  />
                </div>

                <div className="aa-form-full">
                  <label htmlFor="aa-criteria">
                    Recognition criteria *
                  </label>
                  <textarea
                    id="aa-criteria"
                    className="aa-field aa-textarea"
                    name="criteria"
                    value={form.criteria}
                    onChange={handleChange}
                    placeholder="What must a student complete to earn it?"
                    required
                  />
                </div>

                <div className="aa-form-full">
                  <label htmlFor="aa-status">Status</label>
                  <select
                    id="aa-status"
                    className="aa-field"
                    name="status"
                    value={form.status}
                    onChange={handleChange}
                  >
                    <option value="Active">Active</option>
                    <option value="Inactive">Inactive</option>
                  </select>
                </div>
              </div>

              <div className="aa-modal-actions">
                <button
                  type="button"
                  className="aa-button"
                  disabled={saving}
                  onClick={() => setModalOpen(false)}
                >
                  Cancel
                </button>

                <button
                  type="submit"
                  className="aa-button aa-button-primary"
                  disabled={saving}
                >
                  {saving
                    ? "Saving..."
                    : editingItem
                      ? "Save Changes"
                      : "Create Achievement"}
                </button>
              </div>
            </form>
          </section>
        </div>
      )}

      {deleteItem && (
        <div className="aa-overlay">
          <section
            className="aa-modal aa-confirm-modal"
            role="alertdialog"
            aria-modal="true"
            aria-labelledby="aa-delete-title"
          >
            <span className="aa-delete-icon">!</span>
            <h2 id="aa-delete-title">Deactivate achievement?</h2>
            <p>
              Are you sure you want to deactivate{" "}
              <strong>{deleteItem.title}</strong>?
            </p>
            <p className="aa-muted">
              This preserves existing student achievement records.
            </p>

            <div className="aa-modal-actions">
              <button
                type="button"
                className="aa-button"
                onClick={() => setDeleteItem(null)}
              >
                Cancel
              </button>

              <button
                type="button"
                className="aa-button aa-button-danger"
                onClick={confirmDelete}
              >
                Deactivate Achievement
              </button>
            </div>
          </section>
        </div>
      )}
    </div>
  );
}
