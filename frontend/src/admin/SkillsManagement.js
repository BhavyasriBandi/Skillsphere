import React, { useCallback, useEffect, useMemo, useState } from "react";
import { apiFetch } from "../auth/AuthContext";
import { showToast } from "../components/ToastProvider";
import "./SkillsManagement.css";

const API_BASE = "/api/skills/";

const EMPTY_CATEGORY = {
  name: "",
  description: "",
};

const EMPTY_SKILL = {
  name: "",
  description: "",
  category: "",
};

function getErrorMessage(data, fallback) {
  if (typeof data?.detail === "string") return data.detail;
  if (typeof data?.message === "string") return data.message;

  if (data && typeof data === "object") {
    const firstError = Object.values(data).flat(Infinity).find(
      (value) => typeof value === "string"
    );

    if (firstError) return firstError;
  }

  return fallback;
}

async function apiRequest(endpoint, options = {}) {
  const response = await apiFetch(`${API_BASE}${endpoint}`, {
    ...options,
    headers: {
      Accept: "application/json",
      ...options.headers,
    },
  });

  const data = await response.json().catch(() => ({}));

  if (!response.ok) {
    throw new Error(
      getErrorMessage(data, `Request failed (${response.status}).`)
    );
  }

  return data;
}

function SkillsManagement() {
  const [categories, setCategories] = useState([]);
  const [skills, setSkills] = useState([]);

  const [activeTab, setActiveTab] = useState("skills");
  const [searchTerm, setSearchTerm] = useState("");
  const [categoryFilter, setCategoryFilter] = useState("all");

  const [categoryForm, setCategoryForm] = useState(EMPTY_CATEGORY);
  const [skillForm, setSkillForm] = useState(EMPTY_SKILL);

  const [editingCategory, setEditingCategory] = useState(null);
  const [editingSkill, setEditingSkill] = useState(null);

  const [loading, setLoading] = useState(true);
  const [savingCategory, setSavingCategory] = useState(false);
  const [savingSkill, setSavingSkill] = useState(false);
  const [deletingItem, setDeletingItem] = useState(null);
  const [confirmDelete, setConfirmDelete] = useState(null);
  const [error, setError] = useState("");

  // LOAD SKILLS AND CATEGORIES
  const loadData = useCallback(async () => {
    setLoading(true);
    setError("");

    try {
      const [categoryData, skillData] = await Promise.all([
        apiRequest("categories/"),
        apiRequest(""),
      ]);

      setCategories(
        Array.isArray(categoryData.categories)
          ? categoryData.categories
          : []
      );

      setSkills(
        Array.isArray(skillData.skills) ? skillData.skills : []
      );
    } catch (requestError) {
      setError(requestError.message || "Unable to load skills data.");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadData();
  }, [loadData]);

  // ACTIVE SKILLS
  const activeSkills = useMemo(
    () => skills.filter((skill) => skill.is_active !== false),
    [skills]
  );

  // SEARCH AND FILTER
  const filteredSkills = useMemo(() => {
    const query = searchTerm.trim().toLowerCase();

    return activeSkills.filter((skill) => {
      const matchesSearch =
        !query ||
        skill.name?.toLowerCase().includes(query) ||
        skill.description?.toLowerCase().includes(query) ||
        skill.category_name?.toLowerCase().includes(query);

      const matchesCategory =
        categoryFilter === "all" ||
        String(skill.category) === String(categoryFilter);

      return matchesSearch && matchesCategory;
    });
  }, [activeSkills, searchTerm, categoryFilter]);

  // EDIT CATEGORY
  function startEditCategory(category) {
    setEditingCategory(category);

    setCategoryForm({
      name: category.name || "",
      description: category.description || "",
    });

    setEditingSkill(null);
    setActiveTab("categories");
  }

  function cancelEditCategory() {
    setEditingCategory(null);
    setCategoryForm(EMPTY_CATEGORY);
  }

  // EDIT SKILL
  function startEditSkill(skill) {
    setEditingSkill(skill);

    setSkillForm({
      name: skill.name || "",
      description: skill.description || "",
      category: String(skill.category || ""),
    });

    setEditingCategory(null);
    setActiveTab("skills");
  }

  function cancelEditSkill() {
    setEditingSkill(null);
    setSkillForm(EMPTY_SKILL);
  }

  // CREATE OR UPDATE CATEGORY
  async function handleSaveCategory(event) {
    event.preventDefault();

    const name = categoryForm.name.trim();

    if (!name) {
      showToast("Please enter a category name.", "error");
      return;
    }

    setSavingCategory(true);

    try {
      const endpoint = editingCategory
        ? `categories/${editingCategory.id}/`
        : "categories/";

      await apiRequest(endpoint, {
        method: editingCategory ? "PATCH" : "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name,
          description: categoryForm.description.trim(),
        }),
      });

      showToast(
        editingCategory
          ? "Category updated successfully."
          : "Category created successfully.",
        "success"
      );

      cancelEditCategory();
      await loadData();
    } catch (requestError) {
      showToast(
        requestError.message || "Unable to save category.",
        "error"
      );
    } finally {
      setSavingCategory(false);
    }
  }

  // CREATE OR UPDATE SKILL
  async function handleSaveSkill(event) {
    event.preventDefault();

    if (!skillForm.name.trim()) {
      showToast("Please enter a skill name.", "error");
      return;
    }

    if (!skillForm.category) {
      showToast("Please select a category.", "error");
      return;
    }

    setSavingSkill(true);

    try {
      const endpoint = editingSkill
        ? `${editingSkill.id}/`
        : "";

      await apiRequest(endpoint, {
        method: editingSkill ? "PATCH" : "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: skillForm.name.trim(),
          description: skillForm.description.trim(),
          category: Number(skillForm.category),
          is_active: true,
        }),
      });

      showToast(
        editingSkill
          ? "Skill updated successfully."
          : "Skill created successfully.",
        "success"
      );

      cancelEditSkill();
      setSearchTerm("");
      setCategoryFilter("all");
      await loadData();
    } catch (requestError) {
      showToast(
        requestError.message || "Unable to save skill.",
        "error"
      );
    } finally {
      setSavingSkill(false);
    }
  }

  // OPEN CATEGORY DELETE CONFIRMATION
  function handleDeleteCategory(category) {
    const hasSkills = activeSkills.some(
      (skill) => String(skill.category) === String(category.id)
    );

    const message = hasSkills
      ? `Category "${category.name}" has active skills. The server may prevent deleting it until its associated skills are removed or reassigned. Continue?`
      : `Are you sure you want to delete the category "${category.name}"?`;

    setConfirmDelete({
      type: "category",
      item: category,
      title: "Delete Category?",
      message,
    });
  }

  // OPEN SKILL DELETE CONFIRMATION
  function handleDeleteSkill(skill) {
    setConfirmDelete({
      type: "skill",
      item: skill,
      title: "Delete Skill?",
      message: `Are you sure you want to deactivate "${skill.name}"? It will no longer appear in the active skills catalog.`,
    });
  }

  // CONFIRM AND DELETE
  async function confirmDeleteItem() {
    if (!confirmDelete || deletingItem) return;

    const { type, item } = confirmDelete;
    const deleteKey = `${type}-${item.id}`;

    setDeletingItem(deleteKey);

    try {
      if (type === "category") {
        await apiRequest(`categories/${item.id}/`, {
          method: "DELETE",
        });

        if (editingCategory?.id === item.id) {
          cancelEditCategory();
        }

        showToast("Category deleted successfully.", "success");
      } else {
        await apiRequest(`${item.id}/`, {
          method: "DELETE",
        });

        if (editingSkill?.id === item.id) {
          cancelEditSkill();
        }

        showToast("Skill deactivated successfully.", "success");
      }

      setConfirmDelete(null);
      await loadData();
    } catch (requestError) {
      showToast(
        requestError.message || "Unable to delete item.",
        "error"
      );
    } finally {
      setDeletingItem(null);
    }
  }

  return (
    <section className="skills-management">

      {/* PAGE HEADING */}
      <div className="skills-page-intro">
        <div>
          <span className="skills-eyebrow">
            LEARNING MANAGEMENT
          </span>

          <h1>Skills &amp; Categories</h1>

          <p>
            Organize the skills available to students across SkillSphere.
          </p>
        </div>

        <button
          type="button"
          className="skills-refresh-button"
          onClick={loadData}
          disabled={loading}
        >
          <span aria-hidden="true">↻</span>
          {loading ? "Refreshing..." : "Refresh"}
        </button>
      </div>

      {/* STATISTICS */}
      <div className="skills-stat-grid">
        <article className="skills-stat-card">
          <div className="skills-stat-icon skills-stat-blue">◇</div>
          <div>
            <span>Total categories</span>
            <strong>{loading ? "—" : categories.length}</strong>
          </div>
        </article>

        <article className="skills-stat-card">
          <div className="skills-stat-icon skills-stat-purple">✦</div>
          <div>
            <span>Active skills</span>
            <strong>{loading ? "—" : activeSkills.length}</strong>
          </div>
        </article>

        <article className="skills-stat-card">
          <div className="skills-stat-icon skills-stat-green">✓</div>
          <div>
            <span>Categories in use</span>
            <strong>
              {loading
                ? "—"
                : new Set(
                    activeSkills.map((skill) => String(skill.category))
                  ).size}
            </strong>
          </div>
        </article>
      </div>

      {/* ERROR MESSAGE */}
      {error && (
        <div className="skills-error-banner" role="alert">
          <span aria-hidden="true">!</span>

          <div>
            <strong>Unable to load Skills &amp; Categories</strong>
            <p>{error}</p>
          </div>

          <button type="button" onClick={loadData}>
            Try again
          </button>
        </div>
      )}

      <div className="skills-workspace">

        {/* SKILL CATALOG */}
        <section className="skills-panel skills-catalog-panel">

          <div className="skills-panel-heading">
            <div>
              <h2>Skill Catalog</h2>
              <p>Browse and organize your learning catalog.</p>
            </div>
          </div>

          {/* TABS */}
          <div className="skills-tabs" role="tablist">
            <button
              type="button"
              role="tab"
              aria-selected={activeTab === "skills"}
              className={activeTab === "skills" ? "active" : ""}
              onClick={() => setActiveTab("skills")}
            >
              All Skills <span>{activeSkills.length}</span>
            </button>

            <button
              type="button"
              role="tab"
              aria-selected={activeTab === "categories"}
              className={activeTab === "categories" ? "active" : ""}
              onClick={() => setActiveTab("categories")}
            >
              Categories <span>{categories.length}</span>
            </button>
          </div>

          {/* SKILLS TAB */}
          {activeTab === "skills" ? (
            <>
              <div className="skills-filter-row">
                <label className="skills-search-field">
                  <span aria-hidden="true">⌕</span>

                  <input
                    type="search"
                    value={searchTerm}
                    onChange={(event) => setSearchTerm(event.target.value)}
                    placeholder="Search skills..."
                    aria-label="Search skills"
                  />
                </label>

                <select
                  value={categoryFilter}
                  onChange={(event) => setCategoryFilter(event.target.value)}
                  aria-label="Filter skills by category"
                >
                  <option value="all">All categories</option>

                  {categories.map((category) => (
                    <option key={category.id} value={String(category.id)}>
                      {category.name}
                    </option>
                  ))}
                </select>
              </div>

              {loading ? (
                <div className="skills-state">
                  <span className="skills-spinner" />
                  <p>Loading skills...</p>
                </div>
              ) : filteredSkills.length === 0 ? (
                <div className="skills-empty-state">
                  <span aria-hidden="true">◇</span>
                  <h3>No skills found</h3>

                  <p>
                    {activeSkills.length === 0
                      ? "Create your first skill using the form."
                      : "Try another search term or category."}
                  </p>
                </div>
              ) : (
                <div className="skills-table-wrap">
                  <table className="skills-table">
                    <thead>
                      <tr>
                        <th>Skill</th>
                        <th>Category</th>
                        <th>Status</th>
                        <th>Actions</th>
                      </tr>
                    </thead>

                    <tbody>
                      {filteredSkills.map((skill) => (
                        <tr key={skill.id}>
                          <td>
                            <div className="skills-name-cell">
                              <span className="skills-name-icon">◇</span>

                              <div>
                                <strong>{skill.name}</strong>

                                {skill.description && (
                                  <p>{skill.description}</p>
                                )}
                              </div>
                            </div>
                          </td>

                          <td>
                            <span className="skills-category-chip">
                              {skill.category_name ||
                                categories.find(
                                  (category) =>
                                    String(category.id) ===
                                    String(skill.category)
                                )?.name ||
                                "Uncategorized"}
                            </span>
                          </td>

                          <td>
                            <span className="skills-status">
                              <span />
                              Active
                            </span>
                          </td>

                          <td>
                            <div
                              style={{
                                display: "flex",
                                flexWrap: "wrap",
                                gap: "8px",
                              }}
                            >
                              <button
                                type="button"
                                className="skills-refresh-button"
                                onClick={() => startEditSkill(skill)}
                                disabled={Boolean(deletingItem)}
                                aria-label={`Edit ${skill.name}`}
                              >
                                Edit
                              </button>

                              <button
                                type="button"
                                className="skills-refresh-button"
                                onClick={() => handleDeleteSkill(skill)}
                                disabled={Boolean(deletingItem)}
                                aria-label={`Deactivate ${skill.name}`}
                              >
                                {deletingItem === `skill-${skill.id}`
                                  ? "Deactivating..."
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
            </>
          ) : loading ? (
            <div className="skills-state">
              <span className="skills-spinner" />
              <p>Loading categories...</p>
            </div>
          ) : categories.length === 0 ? (
            <div className="skills-empty-state">
              <span aria-hidden="true">▦</span>
              <h3>No categories yet</h3>
              <p>Create a category using the form.</p>
            </div>
          ) : (
            <div className="skills-category-grid">
              {categories.map((category, index) => {
                const count = activeSkills.filter(
                  (skill) =>
                    String(skill.category) === String(category.id)
                ).length;

                return (
                  <article className="skills-category-card" key={category.id}>
                    <div
                      className={`skills-category-symbol skills-category-symbol-${index % 4}`}
                    >
                      ◇
                    </div>

                    <h3>{category.name}</h3>

                    <p>
                      {category.description || "No description provided."}
                    </p>

                    <div className="skills-category-card-footer">
                      <span>{count} skills</span>
                      <span>Category #{category.id}</span>
                    </div>

                    <div
                      style={{
                        display: "flex",
                        gap: "8px",
                        marginTop: "14px",
                        flexWrap: "wrap",
                      }}
                    >
                      <button
                        type="button"
                        className="skills-refresh-button"
                        onClick={() => startEditCategory(category)}
                        disabled={Boolean(deletingItem)}
                      >
                        Edit
                      </button>

                      <button
                        type="button"
                        className="skills-refresh-button"
                        onClick={() => handleDeleteCategory(category)}
                        disabled={Boolean(deletingItem)}
                      >
                        {deletingItem === `category-${category.id}`
                          ? "Deleting..."
                          : "Delete"}
                      </button>
                    </div>
                  </article>
                );
              })}
            </div>
          )}

          <div className="skills-panel-footer">
            <span>
              Showing{" "}
              {activeTab === "skills"
                ? filteredSkills.length
                : categories.length}{" "}
              {activeTab === "skills" ? "skills" : "categories"}
            </span>

            <span className="skills-footer-dot" />
            <span>SkillSphere catalog</span>
          </div>
        </section>

        {/* CREATE FORMS */}
        {!editingCategory && !editingSkill && (
          <aside className="skills-forms-column">

            {/* CREATE CATEGORY FORM */}
            <section className="skills-panel skills-form-panel">
              <div className="skills-panel-heading">
                <div>
                  <span className="skills-form-kicker">NEW CATEGORY</span>
                  <h2>Create Category</h2>
                  <p>Group related skills together.</p>
                </div>
                <span className="skills-form-heading-icon">▦</span>
              </div>

              <form onSubmit={handleSaveCategory}>
                <label className="skills-field">
                  <span>Category name <b>*</b></span>
                  <input
                    type="text"
                    value={categoryForm.name}
                    onChange={(event) =>
                      setCategoryForm((previous) => ({
                        ...previous,
                        name: event.target.value,
                      }))
                    }
                    placeholder="e.g. Programming"
                    maxLength={100}
                    required
                  />
                </label>

                <label className="skills-field">
                  <span>Description</span>
                  <textarea
                    value={categoryForm.description}
                    onChange={(event) =>
                      setCategoryForm((previous) => ({
                        ...previous,
                        description: event.target.value,
                      }))
                    }
                    placeholder="What does this category cover?"
                    rows={3}
                  />
                </label>

                <button
                  className="skills-primary-button"
                  type="submit"
                  disabled={savingCategory}
                >
                  {savingCategory ? "Saving..." : "+ Create Category"}
                </button>
              </form>
            </section>

            {/* CREATE SKILL FORM */}
            <section className="skills-panel skills-form-panel">
              <div className="skills-panel-heading">
                <div>
                  <span className="skills-form-kicker">NEW SKILL</span>
                  <h2>Add a Skill</h2>
                  <p>Add a skill to a category.</p>
                </div>
                <span className="skills-form-heading-icon">◇</span>
              </div>

              <form onSubmit={handleSaveSkill}>
                <label className="skills-field">
                  <span>Skill name <b>*</b></span>
                  <input
                    type="text"
                    value={skillForm.name}
                    onChange={(event) =>
                      setSkillForm((previous) => ({
                        ...previous,
                        name: event.target.value,
                      }))
                    }
                    placeholder="e.g. Python"
                    maxLength={100}
                    required
                  />
                </label>

                <label className="skills-field">
                  <span>Category <b>*</b></span>
                  <select
                    value={skillForm.category}
                    onChange={(event) =>
                      setSkillForm((previous) => ({
                        ...previous,
                        category: event.target.value,
                      }))
                    }
                    required
                  >
                    <option value="">Select a category</option>
                    {categories.map((category) => (
                      <option
                        key={category.id}
                        value={String(category.id)}
                      >
                        {category.name}
                      </option>
                    ))}
                  </select>

                  {categories.length === 0 && (
                    <small>
                      Create a category before adding a skill.
                    </small>
                  )}
                </label>

                <label className="skills-field">
                  <span>Description</span>
                  <textarea
                    value={skillForm.description}
                    onChange={(event) =>
                      setSkillForm((previous) => ({
                        ...previous,
                        description: event.target.value,
                      }))
                    }
                    placeholder="Describe this skill..."
                    rows={3}
                  />
                </label>

                <button
                  className="skills-primary-button"
                  type="submit"
                  disabled={savingSkill || categories.length === 0}
                >
                  {savingSkill ? "Saving..." : "+ Add Skill"}
                </button>
              </form>
            </section>
          </aside>
        )}
      </div>

      {/* CENTRED EDIT MODAL */}
      {(editingCategory || editingSkill) && (
        <div
          className="skills-edit-overlay"
          onMouseDown={(event) => {
            if (
              event.target === event.currentTarget &&
              !savingCategory &&
              !savingSkill
            ) {
              if (editingCategory) cancelEditCategory();
              if (editingSkill) cancelEditSkill();
            }
          }}
        >
          <section
            className="skills-edit-modal"
            role="dialog"
            aria-modal="true"
            aria-labelledby="skills-edit-title"
          >
            <div className="skills-edit-header">
              <div>
                <span className="skills-edit-eyebrow">
                  LEARNING MANAGEMENT
                </span>

                <h2 id="skills-edit-title">
                  {editingCategory ? "Edit Category" : "Edit Skill"}
                </h2>
              </div>

              <button
                type="button"
                className="skills-edit-close"
                aria-label="Close edit dialog"
                disabled={savingCategory || savingSkill}
                onClick={() =>
                  editingCategory
                    ? cancelEditCategory()
                    : cancelEditSkill()
                }
              >
                ×
              </button>
            </div>

            {editingCategory ? (
              <form onSubmit={handleSaveCategory}>
                <label className="skills-field">
                  <span>Category name <b>*</b></span>
                  <input
                    autoFocus
                    type="text"
                    value={categoryForm.name}
                    onChange={(event) =>
                      setCategoryForm((previous) => ({
                        ...previous,
                        name: event.target.value,
                      }))
                    }
                    placeholder="e.g. Programming"
                    maxLength={100}
                    required
                  />
                </label>

                <label className="skills-field">
                  <span>Description</span>
                  <textarea
                    value={categoryForm.description}
                    onChange={(event) =>
                      setCategoryForm((previous) => ({
                        ...previous,
                        description: event.target.value,
                      }))
                    }
                    placeholder="What does this category cover?"
                    rows={3}
                  />
                </label>

                <div className="skills-edit-actions">
                  <button
                    type="button"
                    className="skills-edit-cancel"
                    disabled={savingCategory}
                    onClick={cancelEditCategory}
                  >
                    Cancel
                  </button>

                  <button
                    type="submit"
                    className="skills-edit-save"
                    disabled={savingCategory}
                  >
                    {savingCategory ? "Saving..." : "Save Changes"}
                  </button>
                </div>
              </form>
            ) : (
              <form onSubmit={handleSaveSkill}>
                <label className="skills-field">
                  <span>Skill name <b>*</b></span>
                  <input
                    autoFocus
                    type="text"
                    value={skillForm.name}
                    onChange={(event) =>
                      setSkillForm((previous) => ({
                        ...previous,
                        name: event.target.value,
                      }))
                    }
                    placeholder="e.g. Python"
                    maxLength={100}
                    required
                  />
                </label>

                <label className="skills-field">
                  <span>Category <b>*</b></span>
                  <select
                    value={skillForm.category}
                    onChange={(event) =>
                      setSkillForm((previous) => ({
                        ...previous,
                        category: event.target.value,
                      }))
                    }
                    required
                  >
                    <option value="">Select a category</option>

                    {categories.map((category) => (
                      <option
                        key={category.id}
                        value={String(category.id)}
                      >
                        {category.name}
                      </option>
                    ))}
                  </select>
                </label>

                <label className="skills-field">
                  <span>Description</span>
                  <textarea
                    value={skillForm.description}
                    onChange={(event) =>
                      setSkillForm((previous) => ({
                        ...previous,
                        description: event.target.value,
                      }))
                    }
                    placeholder="Describe this skill..."
                    rows={3}
                  />
                </label>

                <div className="skills-edit-actions">
                  <button
                    type="button"
                    className="skills-edit-cancel"
                    disabled={savingSkill}
                    onClick={cancelEditSkill}
                  >
                    Cancel
                  </button>

                  <button
                    type="submit"
                    className="skills-edit-save"
                    disabled={savingSkill}
                  >
                    {savingSkill ? "Saving..." : "Save Changes"}
                  </button>
                </div>
              </form>
            )}
          </section>
        </div>
      )}

      {/* CENTRED DELETE CONFIRMATION MODAL */}
      {confirmDelete && (
        <div
          className="skills-confirm-overlay"
          onMouseDown={(event) => {
            if (
              event.target === event.currentTarget &&
              !deletingItem
            ) {
              setConfirmDelete(null);
            }
          }}
        >
          <div
            className="skills-confirm-modal"
            role="dialog"
            aria-modal="true"
            aria-labelledby="skills-confirm-title"
          >
            <div className="skills-confirm-icon">!</div>

            <h3 id="skills-confirm-title">
              {confirmDelete.title}
            </h3>

            <p>{confirmDelete.message}</p>

            <div className="skills-confirm-actions">
              <button
                type="button"
                className="skills-confirm-cancel"
                disabled={Boolean(deletingItem)}
                onClick={() => setConfirmDelete(null)}
              >
                Cancel
              </button>

              <button
                type="button"
                className="skills-confirm-delete"
                disabled={Boolean(deletingItem)}
                onClick={confirmDeleteItem}
              >
                {deletingItem ? "Deleting..." : "Yes, Delete"}
              </button>
            </div>
          </div>
        </div>
      )}
    </section>
  );
}

export default SkillsManagement;