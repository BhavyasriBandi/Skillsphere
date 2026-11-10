import React, {
  useCallback,
  useEffect,
  useMemo,
  useState,
} from "react";
import "./AdminInterviewPreparation.css";
import { showToast } from "../components/ToastProvider";

const API_URL =
  "https://skillsphere-u93o.onrender.com/api/interview-prep/admin/questions/";

const TOKEN_KEY = "skillsphere_access";

const CATEGORIES = [
  "Python",
  "Java",
  "C",
  "SQL",
  "React",
  "Django",
  "Data Structures",
  "Web Development",
  "HR",
  "Aptitude",
  "Other",
];

const DIFFICULTIES = [
  "Beginner",
  "Intermediate",
  "Advanced",
];

const EMPTY_FORM = {
  question: "",
  category: "Python",
  difficulty: "Beginner",
  suggested_answer: "",
  explanation: "",
  keywords: "",
  is_active: true,
};

function getHeaders() {
  const token = localStorage.getItem(TOKEN_KEY);

  return {
    Accept: "application/json",
    "Content-Type": "application/json",
    ...(token
      ? { Authorization: `Bearer ${token}` }
      : {}),
  };
}

async function readResponse(response) {
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
    const message =
      data?.detail ||
      Object.entries(data || {})
        .map(([key, value]) => {
          const readableValue = Array.isArray(value)
            ? value.join(", ")
            : typeof value === "object" && value !== null
              ? JSON.stringify(value)
              : String(value);

          return `${key}: ${readableValue}`;
        })
        .join("\n") ||
      `Request failed (${response.status})`;

    throw new Error(message);
  }

  return data;
}

export default function AdminInterviewPreparation() {
  const [questions, setQuestions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");

  const [search, setSearch] = useState("");
  const [categoryFilter, setCategoryFilter] = useState("");
  const [difficultyFilter, setDifficultyFilter] = useState("");
  const [activeFilter, setActiveFilter] = useState("");

  const [modalOpen, setModalOpen] = useState(false);
  const [editingQuestion, setEditingQuestion] = useState(null);
  const [form, setForm] = useState({ ...EMPTY_FORM });
  const [deleteTarget, setDeleteTarget] = useState(null);

  const loadQuestions = useCallback(async () => {
    setLoading(true);
    setError("");

    try {
      const response = await fetch(API_URL, {
        headers: getHeaders(),
      });

      const data = await readResponse(response);

      const rows = Array.isArray(data)
        ? data
        : data?.results;

      if (!Array.isArray(rows)) {
        throw new Error(
          "Unexpected response from interview questions API."
        );
      }

      setQuestions(rows);
    } catch (err) {
      const message =
        err.message || "Unable to load interview questions.";

      setError(message);
      showToast(message, "error");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadQuestions();
  }, [loadQuestions]);

  const filteredQuestions = useMemo(() => {
    const query = search.trim().toLowerCase();

    return questions.filter((item) => {
      const matchesSearch =
        !query ||
        item.question?.toLowerCase().includes(query) ||
        item.category?.toLowerCase().includes(query) ||
        (Array.isArray(item.keywords) &&
          item.keywords.some((word) =>
            String(word).toLowerCase().includes(query)
          ));

      const matchesCategory =
        !categoryFilter ||
        item.category === categoryFilter;

      const matchesDifficulty =
        !difficultyFilter ||
        item.difficulty === difficultyFilter;

      const matchesStatus =
        activeFilter === "" ||
        String(Boolean(item.is_active)) === activeFilter;

      return (
        matchesSearch &&
        matchesCategory &&
        matchesDifficulty &&
        matchesStatus
      );
    });
  }, [
    questions,
    search,
    categoryFilter,
    difficultyFilter,
    activeFilter,
  ]);

  const stats = useMemo(
    () => ({
      total: questions.length,
      active: questions.filter(
        (item) => item.is_active
      ).length,
      inactive: questions.filter(
        (item) => !item.is_active
      ).length,
      categories: new Set(
        questions.map((item) => item.category)
      ).size,
    }),
    [questions]
  );

  function openCreateModal() {
    setEditingQuestion(null);
    setForm({ ...EMPTY_FORM });
    setError("");
    setModalOpen(true);
  }

  function openEditModal(item) {
    setEditingQuestion(item);

    setForm({
      question: item.question || "",
      category: item.category || "Other",
      difficulty: item.difficulty || "Beginner",
      suggested_answer: item.suggested_answer || "",
      explanation: item.explanation || "",
      keywords: Array.isArray(item.keywords)
        ? item.keywords.join(", ")
        : "",
      is_active: Boolean(item.is_active),
    });

    setError("");
    setModalOpen(true);
  }

  function handleFormChange(event) {
    const { name, value, type, checked } = event.target;

    setForm((previous) => ({
      ...previous,
      [name]: type === "checkbox" ? checked : value,
    }));
  }

  async function saveQuestion(event) {
    event.preventDefault();

    if (!form.question.trim()) {
      const message = "Please enter an interview question.";

      setError(message);
      showToast(message, "warning");
      return;
    }

    setSaving(true);
    setError("");

    const payload = {
      question: form.question.trim(),
      category: form.category,
      difficulty: form.difficulty,
      suggested_answer: form.suggested_answer.trim(),
      explanation: form.explanation.trim(),
      keywords: form.keywords
        .split(",")
        .map((word) => word.trim())
        .filter(Boolean),
      is_active: form.is_active,
    };

    try {
      const isEditing = Boolean(editingQuestion);

      const response = await fetch(
        isEditing
          ? `${API_URL}${editingQuestion.id}/`
          : API_URL,
        {
          method: isEditing ? "PATCH" : "POST",
          headers: getHeaders(),
          body: JSON.stringify(payload),
        }
      );

      await readResponse(response);

      setModalOpen(false);

      showToast(
        isEditing
          ? "Interview question updated successfully."
          : "Interview question created successfully.",
        "success"
      );

      await loadQuestions();
    } catch (err) {
      const message =
        err.message || "Unable to save the question.";

      setError(message);
      showToast(message, "error");
    } finally {
      setSaving(false);
    }
  }

  async function toggleActive(item) {
    setError("");

    try {
      const response = await fetch(
        `${API_URL}${item.id}/`,
        {
          method: "PATCH",
          headers: getHeaders(),
          body: JSON.stringify({
            is_active: !item.is_active,
          }),
        }
      );

      await readResponse(response);

      showToast(
        item.is_active
          ? "Question deactivated successfully."
          : "Question activated successfully.",
        "success"
      );

      await loadQuestions();
    } catch (err) {
      const message =
        err.message || "Unable to update question status.";

      setError(message);
      showToast(message, "error");
    }
  }

  async function deleteQuestion() {
    if (!deleteTarget) return;

    setSaving(true);
    setError("");

    try {
      const response = await fetch(
        `${API_URL}${deleteTarget.id}/`,
        {
          method: "DELETE",
          headers: getHeaders(),
        }
      );

      await readResponse(response);

      setDeleteTarget(null);

      showToast(
        "Interview question deleted successfully.",
        "success"
      );

      await loadQuestions();
    } catch (err) {
      const message =
        err.message || "Unable to delete the question.";

      setError(message);
      showToast(message, "error");
    } finally {
      setSaving(false);
    }
  }

  function clearFilters() {
    setSearch("");
    setCategoryFilter("");
    setDifficultyFilter("");
    setActiveFilter("");
  }

  return (
    <div className="aip-page">
      <div className="aip-heading">
        <div>
          <h1 className="aip-title">
            Interview Preparation
          </h1>

          <p className="aip-subtitle">
            Manage interview questions, categories and difficulty levels.
          </p>
        </div>

        <button
          className="aip-btn aip-btn-primary"
          onClick={openCreateModal}
          type="button"
        >
          + Add Question
        </button>
      </div>

      {error && (
        <div className="aip-message aip-error">
          {error}
        </div>
      )}

      <div className="aip-stats">
        <div className="aip-stat">
          <span>Total Questions</span>
          <strong>{stats.total}</strong>
        </div>

        <div className="aip-stat">
          <span>Active Questions</span>
          <strong>{stats.active}</strong>
        </div>

        <div className="aip-stat">
          <span>Inactive Questions</span>
          <strong>{stats.inactive}</strong>
        </div>

        <div className="aip-stat">
          <span>Categories Covered</span>
          <strong>{stats.categories}</strong>
        </div>
      </div>

      <section className="aip-panel">
        <div className="aip-filters">
          <input
            className="aip-field"
            type="search"
            placeholder="Search questions or keywords..."
            value={search}
            onChange={(event) =>
              setSearch(event.target.value)
            }
          />

          <select
            className="aip-field"
            value={categoryFilter}
            onChange={(event) =>
              setCategoryFilter(event.target.value)
            }
          >
            <option value="">All categories</option>

            {CATEGORIES.map((item) => (
              <option key={item} value={item}>
                {item}
              </option>
            ))}
          </select>

          <select
            className="aip-field"
            value={difficultyFilter}
            onChange={(event) =>
              setDifficultyFilter(event.target.value)
            }
          >
            <option value="">All difficulties</option>

            {DIFFICULTIES.map((item) => (
              <option key={item} value={item}>
                {item}
              </option>
            ))}
          </select>

          <select
            className="aip-field"
            value={activeFilter}
            onChange={(event) =>
              setActiveFilter(event.target.value)
            }
          >
            <option value="">All statuses</option>
            <option value="true">Active</option>
            <option value="false">Inactive</option>
          </select>
        </div>

        <div className="aip-toolbar">
          <span>
            Showing {filteredQuestions.length} of{" "}
            {questions.length} questions
          </span>

          <div className="aip-toolbar-actions">
            <button
              className="aip-btn"
              onClick={clearFilters}
              type="button"
            >
              Clear Filters
            </button>

            <button
              className="aip-btn"
              onClick={loadQuestions}
              disabled={loading}
              type="button"
            >
              {loading ? "Refreshing..." : "↻ Refresh"}
            </button>
          </div>
        </div>
      </section>

      <section className="aip-panel aip-table-panel">
        {loading ? (
          <div className="aip-empty">
            Loading interview questions...
          </div>
        ) : filteredQuestions.length === 0 ? (
          <div className="aip-empty">
            <h3>No interview questions found</h3>
            <p>
              Try different filters or add a new question.
            </p>
          </div>
        ) : (
          <div className="aip-table-wrap">
            <table className="aip-table">
              <thead>
                <tr>
                  <th>Question</th>
                  <th>Category</th>
                  <th>Difficulty</th>
                  <th>Status</th>
                  <th>Actions</th>
                </tr>
              </thead>

              <tbody>
                {filteredQuestions.map((item) => (
                  <tr key={item.id}>
                    <td>
                      <div className="aip-question">
                        {item.question}
                      </div>
                      <small>
                        Question ID: {item.id}
                      </small>
                    </td>

                    <td>{item.category}</td>

                    <td>
                      <span
                        className={`aip-badge aip-${String(
                          item.difficulty || ""
                        ).toLowerCase()}`}
                      >
                        {item.difficulty}
                      </span>
                    </td>

                    <td>
                      <span
                        className={`aip-badge ${
                          item.is_active
                            ? "aip-active"
                            : "aip-inactive"
                        }`}
                      >
                        {item.is_active
                          ? "Active"
                          : "Inactive"}
                      </span>
                    </td>

                    <td>
                      <div className="aip-actions">
                        <button
                          className="aip-action"
                          type="button"
                          onClick={() =>
                            openEditModal(item)
                          }
                        >
                          Edit
                        </button>

                        <button
                          className="aip-action"
                          type="button"
                          onClick={() =>
                            toggleActive(item)
                          }
                        >
                          {item.is_active
                            ? "Deactivate"
                            : "Activate"}
                        </button>

                        <button
                          className="aip-action aip-delete-action"
                          type="button"
                          onClick={() =>
                            setDeleteTarget(item)
                          }
                        >
                          Delete
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

      {modalOpen && (
        <div
          className="aip-backdrop"
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
            className="aip-modal"
            role="dialog"
            aria-modal="true"
          >
            <h2>
              {editingQuestion
                ? "Edit Interview Question"
                : "Add Interview Question"}
            </h2>

            <p className="aip-subtitle">
              Enter the question details below.
            </p>

            <form onSubmit={saveQuestion}>
              <div className="aip-form-grid">
                <div className="aip-full">
                  <label htmlFor="aip-question">
                    Question *
                  </label>

                  <textarea
                    id="aip-question"
                    className="aip-field aip-textarea"
                    name="question"
                    value={form.question}
                    onChange={handleFormChange}
                    required
                  />
                </div>

                <div>
                  <label htmlFor="aip-category">
                    Category
                  </label>

                  <select
                    id="aip-category"
                    className="aip-field"
                    name="category"
                    value={form.category}
                    onChange={handleFormChange}
                  >
                    {CATEGORIES.map((item) => (
                      <option key={item} value={item}>
                        {item}
                      </option>
                    ))}
                  </select>
                </div>

                <div>
                  <label htmlFor="aip-difficulty">
                    Difficulty
                  </label>

                  <select
                    id="aip-difficulty"
                    className="aip-field"
                    name="difficulty"
                    value={form.difficulty}
                    onChange={handleFormChange}
                  >
                    {DIFFICULTIES.map((item) => (
                      <option key={item} value={item}>
                        {item}
                      </option>
                    ))}
                  </select>
                </div>

                <div className="aip-full">
                  <label htmlFor="aip-answer">
                    Suggested Answer
                  </label>

                  <textarea
                    id="aip-answer"
                    className="aip-field aip-textarea"
                    name="suggested_answer"
                    value={form.suggested_answer}
                    onChange={handleFormChange}
                  />
                </div>

                <div className="aip-full">
                  <label htmlFor="aip-explanation">
                    Explanation
                  </label>

                  <textarea
                    id="aip-explanation"
                    className="aip-field aip-textarea"
                    name="explanation"
                    value={form.explanation}
                    onChange={handleFormChange}
                  />
                </div>

                <div className="aip-full">
                  <label htmlFor="aip-keywords">
                    Keywords (comma separated)
                  </label>

                  <input
                    id="aip-keywords"
                    className="aip-field"
                    name="keywords"
                    value={form.keywords}
                    onChange={handleFormChange}
                    placeholder="Python, functions, basics"
                  />
                </div>

                <label className="aip-checkbox aip-full">
                  <input
                    type="checkbox"
                    name="is_active"
                    checked={form.is_active}
                    onChange={handleFormChange}
                  />
                  Make this question available to students
                </label>
              </div>

              {error && (
                <div className="aip-message aip-error">
                  {error}
                </div>
              )}

              <div className="aip-modal-actions">
                <button
                  type="button"
                  className="aip-btn"
                  onClick={() => setModalOpen(false)}
                  disabled={saving}
                >
                  Cancel
                </button>

                <button
                  type="submit"
                  className="aip-btn aip-btn-primary"
                  disabled={saving}
                >
                  {saving
                    ? "Saving..."
                    : editingQuestion
                      ? "Save Changes"
                      : "Create Question"}
                </button>
              </div>
            </form>
          </section>
        </div>
      )}

      {deleteTarget && (
        <div className="aip-backdrop">
          <section
            className="aip-modal aip-delete-modal"
            role="alertdialog"
            aria-modal="true"
          >
            <h2>Delete interview question?</h2>

            <p className="aip-question">
              {deleteTarget.question}
            </p>

            <p className="aip-warning">
              Deleting this question may also delete student
              practice records linked to it under your current
              database relationship.
            </p>

            {error && (
              <div className="aip-message aip-error">
                {error}
              </div>
            )}

            <div className="aip-modal-actions">
              <button
                type="button"
                className="aip-btn"
                onClick={() => setDeleteTarget(null)}
                disabled={saving}
              >
                Cancel
              </button>

              <button
                type="button"
                className="aip-btn aip-btn-danger"
                onClick={deleteQuestion}
                disabled={saving}
              >
                {saving
                  ? "Deleting..."
                  : "Delete Permanently"}
              </button>
            </div>
          </section>
        </div>
      )}
    </div>
  );
}