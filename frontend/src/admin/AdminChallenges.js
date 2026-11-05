
import React, {
  useCallback,
  useEffect,
  useState,
} from "react";
import { createPortal } from "react-dom";
import { showToast } from "../components/ToastProvider";
import "./AdminChallenges.css";

const API_URL = "http://127.0.0.1:8000/api/challenges/";

const EMPTY_FORM = {
  title: "",
  description: "",
  category: "Programming",
  challenge_type: "Coding",
  difficulty: "Beginner",
  points: 100,
  duration_minutes: 30,
  instructions: "",
  starter_code: "",
  test_cases: [],
  skills: [],
  is_active: true,
  start_date: "",
  end_date: "",
};

const TYPES = [
  "Coding",
  "Quiz",
  "Project",
  "Problem Solving",
];

const DIFFICULTIES = [
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

  if (response.status === 204) return null;

  const contentType =
    response.headers.get("content-type") || "";

  if (!contentType.includes("application/json")) {
    throw new Error(
      `Unexpected server response (${response.status}). Check the Django API URL.`
    );
  }

  const data = await response.json();

  if (!response.ok) {
    const message =
      data.detail ||
      Object.values(data)
        .flat()
        .find((value) => typeof value === "string");

    throw new Error(
      message || `Request failed (${response.status}).`
    );
  }

  return data;
}

function toList(value) {
  return value
    .split("\n")
    .map((item) => item.trim())
    .filter(Boolean);
}

function toLines(value) {
  return Array.isArray(value)
    ? value.join("\n")
    : "";
}

function toDateInput(value) {
  if (!value) return "";

  const date = new Date(value);

  if (Number.isNaN(date.getTime())) return "";

  return new Date(
    date.getTime() -
      date.getTimezoneOffset() * 60000
  )
    .toISOString()
    .slice(0, 16);
}

function toISODate(value) {
  return value
    ? new Date(value).toISOString()
    : null;
}

function ChallengeFields({
  form,
  skillsText,
  testCasesText,
  updateField,
  setSkillsText,
  setTestCasesText,
  prefix,
}) {
  return (
    <div className="ac-form-grid">
      <div className="ac-field">
        <label htmlFor={`${prefix}-title`}>
          Challenge Title *
        </label>

        <input
          id={`${prefix}-title`}
          name="title"
          value={form.title}
          onChange={updateField}
          placeholder="e.g. Two Sum Problem"
          required
        />
      </div>

      <div className="ac-field">
        <label htmlFor={`${prefix}-category`}>
          Category *
        </label>

        <input
          id={`${prefix}-category`}
          name="category"
          value={form.category}
          onChange={updateField}
          placeholder="e.g. Data Structures"
          required
        />
      </div>

      <div className="ac-field">
        <label htmlFor={`${prefix}-type`}>
          Challenge Type *
        </label>

        <select
          id={`${prefix}-type`}
          name="challenge_type"
          value={form.challenge_type}
          onChange={updateField}
          required
        >
          {TYPES.map((type) => (
            <option key={type} value={type}>
              {type}
            </option>
          ))}
        </select>
      </div>

      <div className="ac-field">
        <label htmlFor={`${prefix}-difficulty`}>
          Difficulty *
        </label>

        <select
          id={`${prefix}-difficulty`}
          name="difficulty"
          value={form.difficulty}
          onChange={updateField}
          required
        >
          {DIFFICULTIES.map((level) => (
            <option key={level} value={level}>
              {level}
            </option>
          ))}
        </select>
      </div>

      <div className="ac-field">
        <label htmlFor={`${prefix}-points`}>
          Points *
        </label>

        <input
          id={`${prefix}-points`}
          name="points"
          type="number"
          min="0"
          value={form.points}
          onChange={updateField}
          required
        />
      </div>

      <div className="ac-field">
        <label htmlFor={`${prefix}-duration`}>
          Duration (minutes) *
        </label>

        <input
          id={`${prefix}-duration`}
          name="duration_minutes"
          type="number"
          min="1"
          value={form.duration_minutes}
          onChange={updateField}
          required
        />
      </div>

      <div className="ac-field ac-field-full">
        <label htmlFor={`${prefix}-description`}>
          Description *
        </label>

        <textarea
          id={`${prefix}-description`}
          name="description"
          value={form.description}
          onChange={updateField}
          placeholder="Explain the challenge..."
          rows={4}
          required
        />
      </div>

      <div className="ac-field ac-field-full">
        <label htmlFor={`${prefix}-instructions`}>
          Instructions
        </label>

        <textarea
          id={`${prefix}-instructions`}
          name="instructions"
          value={form.instructions}
          onChange={updateField}
          placeholder="Explain what the student must do."
          rows={4}
        />
      </div>

      <div className="ac-field ac-field-full">
        <label htmlFor={`${prefix}-starter-code`}>
          Starter Code
        </label>

        <textarea
          id={`${prefix}-starter-code`}
          name="starter_code"
          value={form.starter_code}
          onChange={updateField}
          placeholder="Optional starter code..."
          rows={5}
        />
      </div>

      <div className="ac-field ac-field-full">
        <label htmlFor={`${prefix}-skills`}>
          Skills (one per line)
        </label>

        <textarea
          id={`${prefix}-skills`}
          value={skillsText}
          onChange={(event) =>
            setSkillsText(event.target.value)
          }
          placeholder={"Python\nArrays\nProblem Solving"}
          rows={3}
        />
      </div>

      <div className="ac-field ac-field-full">
        <label htmlFor={`${prefix}-test-cases`}>
          Test Cases (optional JSON array)
        </label>

        <textarea
          id={`${prefix}-test-cases`}
          value={testCasesText}
          onChange={(event) =>
            setTestCasesText(event.target.value)
          }
          placeholder={'[{"input": "2 3", "expected_output": "5"}]'}
          rows={5}
        />
      </div>

      <div className="ac-field">
        <label htmlFor={`${prefix}-start-date`}>
          Start Date (optional)
        </label>

        <input
          id={`${prefix}-start-date`}
          name="start_date"
          type="datetime-local"
          value={form.start_date}
          onChange={updateField}
        />
      </div>

      <div className="ac-field">
        <label htmlFor={`${prefix}-end-date`}>
          End Date (optional)
        </label>

        <input
          id={`${prefix}-end-date`}
          name="end_date"
          type="datetime-local"
          value={form.end_date}
          onChange={updateField}
        />
      </div>

      <div className="ac-field ac-field-full">
        <label className="ac-checkbox-label">
          <input
            type="checkbox"
            name="is_active"
            checked={form.is_active}
            onChange={updateField}
          />

          Challenge is active and visible to students
        </label>
      </div>
    </div>
  );
}

export default function AdminChallenges() {
  const [challenges, setChallenges] = useState([]);

  // Create form
  const [form, setForm] = useState({
    ...EMPTY_FORM,
  });

  const [skillsText, setSkillsText] = useState("");
  const [testCasesText, setTestCasesText] = useState("");

  // Separate edit popup form
  const [editForm, setEditForm] = useState({
    ...EMPTY_FORM,
  });

  const [editSkillsText, setEditSkillsText] =
    useState("");

  const [editTestCasesText, setEditTestCasesText] =
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

  const loadChallenges = useCallback(async () => {
    setLoading(true);
    setError("");

    try {
      const data = await apiRequest(API_URL);

      setChallenges(
        Array.isArray(data)
          ? data
          : Array.isArray(data.results)
          ? data.results
          : []
      );
    } catch (err) {
      setError(
        err.message || "Unable to load challenges."
      );
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadChallenges();
  }, [loadChallenges]);

  // Prevent background scrolling while popup is open.
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

  // Escape key closes popup.
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
        type === "checkbox"
          ? checked
          : type === "number"
          ? value === ""
            ? ""
            : Number(value)
          : value,
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
        type === "checkbox"
          ? checked
          : type === "number"
          ? value === ""
            ? ""
            : Number(value)
          : value,
    }));
  }

  function resetForm() {
    setForm({ ...EMPTY_FORM });
    setSkillsText("");
    setTestCasesText("");
  }

  // Open selected challenge in the edit popup.
  function startEdit(challenge) {
    if (saving || deletingId !== null) return;

    setEditingId(challenge.id);

    setEditForm({
      ...EMPTY_FORM,
      ...challenge,
      start_date: toDateInput(challenge.start_date),
      end_date: toDateInput(challenge.end_date),
    });

    setEditSkillsText(toLines(challenge.skills));

    setEditTestCasesText(
      Array.isArray(challenge.test_cases)
        ? JSON.stringify(challenge.test_cases, null, 2)
        : ""
    );

    setEditModalOpen(true);
  }

  function closeEditModal() {
    if (saving) return;

    setEditModalOpen(false);
    setEditingId(null);

    setEditForm({ ...EMPTY_FORM });
    setEditSkillsText("");
    setEditTestCasesText("");
  }

  function buildPayload(
    currentForm,
    currentSkillsText,
    currentTestCasesText
  ) {
    let testCases = [];

    if (currentTestCasesText.trim()) {
      testCases = JSON.parse(
        currentTestCasesText
      );

      if (!Array.isArray(testCases)) {
        throw new Error(
          "Test cases must be a JSON array."
        );
      }
    }

    if (
      currentForm.end_date &&
      currentForm.start_date &&
      new Date(currentForm.end_date) <=
        new Date(currentForm.start_date)
    ) {
      throw new Error(
        "End date must be later than start date."
      );
    }

    return {
      ...currentForm,
      title: currentForm.title.trim(),
      description: currentForm.description.trim(),
      category: currentForm.category.trim(),
      instructions: currentForm.instructions.trim(),
      starter_code: currentForm.starter_code,
      skills: toList(currentSkillsText),
      test_cases: testCases,
      start_date: toISODate(currentForm.start_date),
      end_date: toISODate(currentForm.end_date),
    };
  }

  // Create challenge.
  async function handleSubmit(event) {
    event.preventDefault();

    if (saving) return;

    let payload;

    try {
      payload = buildPayload(
        form,
        skillsText,
        testCasesText
      );
    } catch (err) {
      showToast(
        err.message || "Please check the challenge details.",
        "error"
      );
      return;
    }

    setSaving(true);

    try {
      await apiRequest(API_URL, {
        method: "POST",
        body: JSON.stringify(payload),
      });

      showToast(
        "Challenge created successfully.",
        "success"
      );

      resetForm();
      await loadChallenges();
    } catch (err) {
      showToast(
        err.message || "Unable to create challenge.",
        "error"
      );
    } finally {
      setSaving(false);
    }
  }

  // Save edited challenge.
  async function handleEditSubmit(event) {
    event.preventDefault();

    if (saving || editingId === null) return;

    let payload;

    try {
      payload = buildPayload(
        editForm,
        editSkillsText,
        editTestCasesText
      );
    } catch (err) {
      showToast(
        err.message || "Please check the challenge details.",
        "error"
      );
      return;
    }

    setSaving(true);

    try {
      await apiRequest(
        `${API_URL}${editingId}/`,
        {
          method: "PATCH",
          body: JSON.stringify(payload),
        }
      );

      showToast(
        "Challenge updated successfully.",
        "success"
      );

      setEditModalOpen(false);
      setEditingId(null);
      setEditForm({ ...EMPTY_FORM });
      setEditSkillsText("");
      setEditTestCasesText("");

      await loadChallenges();
    } catch (err) {
      showToast(
        err.message || "Unable to update challenge.",
        "error"
      );
    } finally {
      setSaving(false);
    }
  }

  async function handleDelete(challenge) {
    if (deletingId !== null || saving) return;

    const confirmed = window.confirm(
      `Delete "${challenge.title}"? This cannot be undone.`
    );

    if (!confirmed) return;

    setDeletingId(challenge.id);

    try {
      await apiRequest(
        `${API_URL}${challenge.id}/`,
        {
          method: "DELETE",
        }
      );

      setChallenges((current) =>
        current.filter(
          (item) => item.id !== challenge.id
        )
      );

      if (editingId === challenge.id) {
        setEditModalOpen(false);
        setEditingId(null);
      }

      showToast(
        "Challenge deleted successfully.",
        "success"
      );
    } catch (err) {
      showToast(
        err.message || "Unable to delete challenge.",
        "error"
      );
    } finally {
      setDeletingId(null);
    }
  }

  async function toggleActive(challenge) {
    if (updatingId !== null) return;

    setUpdatingId(challenge.id);

    try {
      await apiRequest(
        `${API_URL}${challenge.id}/`,
        {
          method: "PATCH",
          body: JSON.stringify({
            is_active: !challenge.is_active,
          }),
        }
      );

      showToast(
        challenge.is_active
          ? "Challenge deactivated."
          : "Challenge activated.",
        "success"
      );

      await loadChallenges();
    } catch (err) {
      showToast(
        err.message ||
          "Unable to update challenge status.",
        "error"
      );
    } finally {
      setUpdatingId(null);
    }
  }

  const filteredChallenges = challenges.filter(
    (challenge) =>
      [
        challenge.title,
        challenge.description,
        challenge.category,
        challenge.challenge_type,
        challenge.difficulty,
      ]
        .join(" ")
        .toLowerCase()
        .includes(search.trim().toLowerCase())
  );

  return (
    <section className="ac-page">
      {/* PAGE HEADER */}
      <div className="ac-heading">
        <div>
          <h1>Challenges Management</h1>

          <p>
            Create and manage coding, quiz, and project challenges.
          </p>
        </div>

        <button
          type="button"
          className="ac-secondary"
          onClick={loadChallenges}
          disabled={loading}
        >
          {loading ? "Loading..." : "Refresh"}
        </button>
      </div>

      {/* STATISTICS */}
      <div className="ac-stats">
        <div className="ac-panel">
          <h3>Total Challenges</h3>
          <p>{challenges.length}</p>
        </div>

        <div className="ac-panel">
          <h3>Active Challenges</h3>
          <p>
            {
              challenges.filter(
                (item) => item.is_active
              ).length
            }
          </p>
        </div>

        <div className="ac-panel">
          <h3>Inactive Challenges</h3>
          <p>
            {
              challenges.filter(
                (item) => !item.is_active
              ).length
            }
          </p>
        </div>
      </div>

      {/* CREATE CHALLENGE FORM */}
      <div className="ac-panel">
        <div className="ac-section-heading">
          <div>
            <h2>Create New Challenge</h2>
            <p>Enter the challenge details below.</p>
          </div>
        </div>

        <form onSubmit={handleSubmit}>
          <ChallengeFields
            form={form}
            skillsText={skillsText}
            testCasesText={testCasesText}
            updateField={updateField}
            setSkillsText={setSkillsText}
            setTestCasesText={setTestCasesText}
            prefix="create-challenge"
          />

          <div className="ac-form-actions">
            <button
              type="submit"
              className="ac-primary"
              disabled={saving}
            >
              {saving ? "Saving..." : "Create Challenge"}
            </button>

            <button
              type="button"
              className="ac-secondary"
              onClick={resetForm}
              disabled={saving}
            >
              Clear Form
            </button>
          </div>
        </form>
      </div>

      {/* ALL CHALLENGES */}
      <div className="ac-panel">
        <div className="ac-section-heading">
          <div>
            <h2>All Challenges</h2>
            <p>Search and manage your challenges.</p>
          </div>

          <div className="ac-search">
            <input
              type="search"
              aria-label="Search challenges"
              value={search}
              onChange={(event) =>
                setSearch(event.target.value)
              }
              placeholder="Search challenges..."
            />
          </div>
        </div>

        {error && (
          <div className="ac-error" role="alert">
            <p>{error}</p>

            <button
              type="button"
              className="ac-secondary"
              onClick={loadChallenges}
            >
              Try Again
            </button>
          </div>
        )}

        {loading ? (
          <p className="ac-empty">
            Loading challenges...
          </p>
        ) : filteredChallenges.length === 0 ? (
          <div className="ac-empty">
            <h3>No challenges found</h3>

            <p>
              {search
                ? "Try a different search term."
                : "Create your first challenge using the form above."}
            </p>
          </div>
        ) : (
          <div className="ac-table-wrap">
            <table className="ac-table">
              <thead>
                <tr>
                  <th>Challenge</th>
                  <th>Type</th>
                  <th>Difficulty</th>
                  <th>Points</th>
                  <th>Status</th>
                  <th>Actions</th>
                </tr>
              </thead>

              <tbody>
                {filteredChallenges.map((challenge) => (
                  <tr key={challenge.id}>
                    <td>
                      <div className="ac-challenge-title">
                        <strong>{challenge.title}</strong>
                        <span>{challenge.category}</span>
                      </div>
                    </td>

                    <td>{challenge.challenge_type}</td>
                    <td>{challenge.difficulty}</td>
                    <td>{challenge.points}</td>

                    <td>
                      <span
                        className={
                          challenge.is_active
                            ? "ac-status ac-status-active"
                            : "ac-status ac-status-inactive"
                        }
                      >
                        {challenge.is_active
                          ? "Active"
                          : "Inactive"}
                      </span>
                    </td>

                    <td>
                      <div className="ac-row-actions">
                        <button
                          type="button"
                          className="ac-secondary"
                          onClick={() =>
                            startEdit(challenge)
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
                          className="ac-secondary"
                          onClick={() =>
                            toggleActive(challenge)
                          }
                          disabled={updatingId !== null}
                        >
                          {updatingId === challenge.id
                            ? "Updating..."
                            : challenge.is_active
                            ? "Deactivate"
                            : "Activate"}
                        </button>

                        <button
                          type="button"
                          className="ac-danger"
                          onClick={() =>
                            handleDelete(challenge)
                          }
                          disabled={deletingId !== null}
                        >
                          {deletingId === challenge.id
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

      {/* CENTRED EDIT POPUP */}
      {editModalOpen &&
        createPortal(
          <div
            className="ac-modal-backdrop"
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
              className="ac-edit-modal"
              role="dialog"
              aria-modal="true"
              aria-labelledby="ac-edit-modal-title"
            >
              <div className="ac-modal-header">
                <div>
                  <span className="ac-modal-kicker">
                    CHALLENGE MANAGEMENT
                  </span>

                  <h2 id="ac-edit-modal-title">
                    Edit Challenge
                  </h2>

                  <p>
                    Update the selected challenge details.
                  </p>
                </div>

                <button
                  type="button"
                  className="ac-modal-close"
                  onClick={closeEditModal}
                  disabled={saving}
                  aria-label="Close popup"
                >
                  ×
                </button>
              </div>

              <form onSubmit={handleEditSubmit}>
                <ChallengeFields
                  form={editForm}
                  skillsText={editSkillsText}
                  testCasesText={editTestCasesText}
                  updateField={updateEditField}
                  setSkillsText={setEditSkillsText}
                  setTestCasesText={setEditTestCasesText}
                  prefix="edit-challenge"
                />

                <div className="ac-modal-actions">
                  <button
                    type="button"
                    className="ac-modal-cancel"
                    onClick={closeEditModal}
                    disabled={saving}
                  >
                    Cancel
                  </button>

                  <button
                    type="submit"
                    className="ac-modal-save"
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
