
import React, { useCallback, useEffect, useState } from "react";
import { showToast } from "../components/ToastProvider";
import "./AssessmentQuestionManagement.css";

const API_URL = "https://skillsphere-u93o.onrender.com/api/assessments/admin/questions/";

const EMPTY_FORM = {
  skill: "Python",
  question: "",
  options: ["", "", "", ""],
  correct_answer: 0,
  explanation: "",
  is_active: true,
};

function getAccessToken() {
  return (
    localStorage.getItem("skillsphere_access") ||
    localStorage.getItem("access") ||
    ""
  );
}

function normalizeQuestions(data) {
  if (Array.isArray(data)) {
    return data;
  }

  if (!data || typeof data !== "object") {
    return [];
  }

  if (Array.isArray(data.questions)) {
    return data.questions;
  }

  if (Array.isArray(data.results)) {
    return data.results;
  }

  if (Array.isArray(data.data)) {
    return data.data;
  }

  return [];
}

function AssessmentQuestionManagement() {
  const [questions, setQuestions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");
  const [skillFilter, setSkillFilter] = useState("");
  const [search, setSearch] = useState("");
  const [editingId, setEditingId] = useState(null);
  const [formOpen, setFormOpen] = useState(false);
  const [form, setForm] = useState({ ...EMPTY_FORM });
  const [deleteId, setDeleteId] = useState(null);

  const getHeaders = () => {
    const token = getAccessToken();

    if (!token) {
      throw new Error(
        "Your session has expired. Please log in again."
      );
    }

    return {
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json",
      Accept: "application/json",
    };
  };

  const readResponse = async (response) => {
    const data = await response.json().catch(() => ({}));

    if (!response.ok) {
      if (response.status === 401 || response.status === 403) {
        throw new Error(
          "Access denied. Please log in with your administrator account."
        );
      }

      const message =
        data.detail ||
        data.message ||
        Object.entries(data)
          .map(([key, value]) =>
            `${key}: ${
              Array.isArray(value)
                ? value.join(", ")
                : typeof value === "object"
                ? JSON.stringify(value)
                : value
            }`
          )
          .join(" | ") ||
        "The request could not be completed.";

      throw new Error(message);
    }

    return data;
  };

  const loadQuestions = useCallback(async () => {
    setLoading(true);
    setError("");

    try {
      const params = new URLSearchParams();

      if (skillFilter) {
        params.set("skill", skillFilter);
      }

      const url = params.toString()
        ? `${API_URL}?${params.toString()}`
        : API_URL;

      const response = await fetch(url, {
        method: "GET",
        headers: getHeaders(),
      });

      const data = await readResponse(response);
      const items = normalizeQuestions(data);

      setQuestions(items);
    } catch (err) {
      setError(
        err.message || "Unable to load assessment questions."
      );
      setQuestions([]);
    } finally {
      setLoading(false);
    }
  }, [skillFilter]);

  useEffect(() => {
    loadQuestions();
  }, [loadQuestions]);

  const visibleQuestions = questions.filter((item) => {
    const text =
      `${item.question || item.question_text || ""} ` +
      `${item.skill || ""}`;

    return text
      .toLowerCase()
      .includes(search.trim().toLowerCase());
  });

  const updateFormField = (field, value) => {
    setForm((current) => ({
      ...current,
      [field]: value,
    }));
  };

  const updateOption = (index, value) => {
    setForm((current) => ({
      ...current,
      options: current.options.map((option, i) =>
        i === index ? value : option
      ),
    }));
  };

  const openAddForm = () => {
    setEditingId(null);
    setForm({
      ...EMPTY_FORM,
      options: ["", "", "", ""],
    });
    setFormOpen(true);
  };

  const openEditForm = (item) => {
    setEditingId(item.id);

    setForm({
      skill: item.skill || "Python",
      question: item.question || item.question_text || "",
      options: Array.isArray(item.options)
        ? [...item.options]
        : ["", "", "", ""],
      correct_answer: Number(item.correct_answer ?? 0),
      explanation: item.explanation || "",
      is_active: item.is_active ?? true,
    });

    setFormOpen(true);
  };

  const saveQuestion = async (event) => {
    event.preventDefault();

    const options = form.options.map((option) =>
      option.trim()
    );

    if (!form.question.trim()) {
      showToast("Please enter the question.", "error");
      return;
    }

    if (
      options.length < 2 ||
      options.some((option) => !option)
    ) {
      showToast(
        "Please fill in at least two answer options.",
        "error"
      );
      return;
    }

    if (
      !Number.isInteger(Number(form.correct_answer)) ||
      Number(form.correct_answer) < 0 ||
      Number(form.correct_answer) >= options.length
    ) {
      showToast(
        "Please select a valid correct answer.",
        "error"
      );
      return;
    }

    const payload = {
      skill: form.skill,
      question: form.question.trim(),
      options,
      correct_answer: Number(form.correct_answer),
      explanation: form.explanation.trim(),
      is_active: form.is_active,
    };

    setSaving(true);

    try {
      const response = await fetch(
        editingId
          ? `${API_URL}${editingId}/`
          : API_URL,
        {
          method: editingId ? "PATCH" : "POST",
          headers: getHeaders(),
          body: JSON.stringify(payload),
        }
      );

      await readResponse(response);

      showToast(
        editingId
          ? "Assessment question updated successfully."
          : "Assessment question added successfully.",
        "success"
      );

      setFormOpen(false);
      setEditingId(null);
      setForm({
        ...EMPTY_FORM,
        options: ["", "", "", ""],
      });

      await loadQuestions();
    } catch (err) {
      showToast(
        err.message || "Unable to save the question.",
        "error"
      );
    } finally {
      setSaving(false);
    }
  };

  const deleteQuestion = async () => {
    if (deleteId === null) {
      return;
    }

    try {
      const response = await fetch(
        `${API_URL}${deleteId}/`,
        {
          method: "DELETE",
          headers: getHeaders(),
        }
      );

      if (!response.ok) {
        await readResponse(response);
      }

      showToast(
        "Assessment question deleted successfully.",
        "success"
      );

      setDeleteId(null);
      await loadQuestions();
    } catch (err) {
      showToast(
        err.message || "Unable to delete the question.",
        "error"
      );
    }
  };

  return (
    <section className="aqm-page">
      <div className="aqm-heading">
        <div>
          <span className="aqm-kicker">
            LEARNING MANAGEMENT
          </span>
          <h1>Assessment Questions</h1>
          <p>
            Create, review, edit, and manage SkillSphere skill
            questions.
          </p>
        </div>

        <button
          className="aqm-primary"
          onClick={openAddForm}
          type="button"
        >
          <span aria-hidden="true">＋</span> Add Question
        </button>
      </div>

      <div className="aqm-stats">
        <article className="aqm-stat-card">
          <span>Total questions</span>
          <strong>{questions.length}</strong>
        </article>

        <article className="aqm-stat-card">
          <span>Active questions</span>
          <strong>
            {
              questions.filter(
                (item) => item.is_active !== false
              ).length
            }
          </strong>
        </article>

        <article className="aqm-stat-card">
          <span>Inactive questions</span>
          <strong>
            {
              questions.filter(
                (item) => item.is_active === false
              ).length
            }
          </strong>
        </article>
      </div>

      <div className="aqm-toolbar">
        <input
          type="search"
          value={search}
          onChange={(event) => setSearch(event.target.value)}
          placeholder="Search questions..."
          aria-label="Search assessment questions"
        />

        <select
          value={skillFilter}
          onChange={(event) =>
            setSkillFilter(event.target.value)
          }
          aria-label="Filter questions by skill"
        >
          <option value="">All skills</option>
          <option value="Python">Python</option>
          <option value="Java">Java</option>
          <option value="C">C</option>
          <option value="SQL">SQL</option>
        </select>

        <button
          className="aqm-secondary"
          type="button"
          onClick={loadQuestions}
          disabled={loading}
        >
          {loading ? "Loading..." : "↻ Refresh"}
        </button>
      </div>

      {error && (
        <div className="aqm-error" role="alert">
          <strong>Could not load questions</strong>
          <p>{error}</p>
          <button
            type="button"
            onClick={loadQuestions}
          >
            Try again
          </button>
        </div>
      )}

      <div className="aqm-table-card">
        <div className="aqm-table-heading">
          <div>
            <h2>Question bank</h2>
            <p>
              {visibleQuestions.length} question(s) displayed
            </p>
          </div>
        </div>

        {loading ? (
          <div className="aqm-empty">
            Loading assessment questions...
          </div>
        ) : !error && visibleQuestions.length === 0 ? (
          <div className="aqm-empty">
            <span aria-hidden="true">◇</span>
            <strong>No questions found</strong>
            <p>
              Try another search or add a new question.
            </p>
          </div>
        ) : (
          <div className="aqm-table-wrap">
            <table className="aqm-table">
              <thead>
                <tr>
                  <th>Question</th>
                  <th>Skill</th>
                  <th>Options</th>
                  <th>Status</th>
                  <th>Actions</th>
                </tr>
              </thead>

              <tbody>
                {visibleQuestions.map((item) => (
                  <tr key={item.id}>
                    <td>
                      <strong>
                        {item.question ||
                          item.question_text ||
                          "Question text unavailable"}
                      </strong>
                      <small>ID: {item.id}</small>
                    </td>

                    <td>
                      <span className="aqm-skill">
                        {item.skill || "Not specified"}
                      </span>
                    </td>

                    <td>
                      {Array.isArray(item.options)
                        ? item.options.length
                        : 0}{" "}
                      options
                    </td>

                    <td>
                      <span
                        className={`aqm-status ${
                          item.is_active === false
                            ? "is-inactive"
                            : "is-active"
                        }`}
                      >
                        {item.is_active === false
                          ? "Inactive"
                          : "Active"}
                      </span>
                    </td>

                    <td>
                      <div className="aqm-actions">
                        <button
                          type="button"
                          className="aqm-edit"
                          onClick={() =>
                            openEditForm(item)
                          }
                        >
                          Edit
                        </button>

                        <button
                          type="button"
                          className="aqm-delete"
                          onClick={() =>
                            setDeleteId(item.id)
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
      </div>

      {formOpen && (
        <div className="aqm-modal-backdrop">
          <div
            className="aqm-modal"
            role="dialog"
            aria-modal="true"
            aria-labelledby="aqm-form-title"
          >
            <div className="aqm-modal-heading">
              <div>
                <span className="aqm-kicker">
                  QUESTION BANK
                </span>
                <h2 id="aqm-form-title">
                  {editingId
                    ? "Edit question"
                    : "Add new question"}
                </h2>
              </div>

              <button
                type="button"
                className="aqm-close"
                onClick={() => setFormOpen(false)}
                aria-label="Close form"
              >
                ×
              </button>
            </div>

            <form onSubmit={saveQuestion}>
              <label>
                Skill
                <select
                  value={form.skill}
                  onChange={(event) =>
                    updateFormField(
                      "skill",
                      event.target.value
                    )
                  }
                >
                  <option value="Python">Python</option>
                  <option value="Java">Java</option>
                  <option value="C">C</option>
                  <option value="SQL">SQL</option>
                </select>
              </label>

              <label>
                Question
                <textarea
                  value={form.question}
                  onChange={(event) =>
                    updateFormField(
                      "question",
                      event.target.value
                    )
                  }
                  placeholder="Enter the assessment question..."
                  rows={3}
                  required
                />
              </label>

              <div className="aqm-options-heading">
                <strong>Answer options</strong>

                <button
                  type="button"
                  className="aqm-add-option"
                  onClick={() =>
                    updateFormField("options", [
                      ...form.options,
                      "",
                    ])
                  }
                >
                  + Add option
                </button>
              </div>

              {form.options.map((option, index) => (
                <div
                  className="aqm-option-row"
                  key={index}
                >
                  <input
                    type="radio"
                    name="correctAnswer"
                    checked={
                      Number(form.correct_answer) === index
                    }
                    onChange={() =>
                      updateFormField(
                        "correct_answer",
                        index
                      )
                    }
                    aria-label={`Mark option ${
                      index + 1
                    } as correct`}
                    title="Mark as correct answer"
                  />

                  <input
                    value={option}
                    onChange={(event) =>
                      updateOption(
                        index,
                        event.target.value
                      )
                    }
                    placeholder={`Option ${index + 1}`}
                    required
                  />

                  <button
                    type="button"
                    className="aqm-remove-option"
                    disabled={form.options.length <= 2}
                    onClick={() => {
                      const nextOptions =
                        form.options.filter(
                          (_, i) => i !== index
                        );

                      const oldCorrect = Number(
                        form.correct_answer
                      );

                      updateFormField(
                        "options",
                        nextOptions
                      );

                      updateFormField(
                        "correct_answer",
                        oldCorrect === index
                          ? 0
                          : oldCorrect > index
                          ? oldCorrect - 1
                          : oldCorrect
                      );
                    }}
                    aria-label={`Remove option ${
                      index + 1
                    }`}
                  >
                    ×
                  </button>
                </div>
              ))}

              <p className="aqm-hint">
                Select the radio button next to the correct
                answer.
              </p>

              <label>
                Explanation
                <textarea
                  value={form.explanation}
                  onChange={(event) =>
                    updateFormField(
                      "explanation",
                      event.target.value
                    )
                  }
                  placeholder="Explain why this answer is correct..."
                  rows={2}
                />
              </label>

              <label className="aqm-checkbox-label">
                <input
                  type="checkbox"
                  checked={form.is_active}
                  onChange={(event) =>
                    updateFormField(
                      "is_active",
                      event.target.checked
                    )
                  }
                />
                Active — available to students
              </label>

              <div className="aqm-modal-actions">
                <button
                  type="button"
                  className="aqm-secondary"
                  onClick={() => setFormOpen(false)}
                  disabled={saving}
                >
                  Cancel
                </button>

                <button
                  type="submit"
                  className="aqm-primary"
                  disabled={saving}
                >
                  {saving
                    ? "Saving..."
                    : editingId
                    ? "Save changes"
                    : "Add question"}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {deleteId !== null && (
        <div className="aqm-modal-backdrop">
          <div
            className="aqm-confirm-modal"
            role="dialog"
            aria-modal="true"
          >
            <div className="aqm-confirm-icon">!</div>

            <h2>Delete this question?</h2>

            <p>
              This action cannot be undone. The question will
              be removed from the question bank.
            </p>

            <div className="aqm-modal-actions">
              <button
                type="button"
                className="aqm-secondary"
                onClick={() => setDeleteId(null)}
              >
                Cancel
              </button>

              <button
                type="button"
                className="aqm-delete-confirm"
                onClick={deleteQuestion}
              >
                Delete question
              </button>
            </div>
          </div>
        </div>
      )}
    </section>
  );
}

export default AssessmentQuestionManagement;
