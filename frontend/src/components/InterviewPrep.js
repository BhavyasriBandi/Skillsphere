
import React, {
  useCallback,
  useEffect,
  useMemo,
  useRef,
  useState,
} from "react";
import "./InterviewPrep.css";
import { showToast } from "../components/ToastProvider";

const API_BASE = "http://127.0.0.1:8000/api/interview-prep";

const TOPICS = [
  "All Topics",
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
  "All Levels",
  "Easy",
  "Medium",
  "Hard",
];

// ============================================
// GET JWT ACCESS TOKEN
// ============================================

function getToken() {
  return (
    localStorage.getItem("skillsphere_access") ||
    localStorage.getItem("access") ||
    localStorage.getItem("access_token") ||
    localStorage.getItem("accessToken") ||
    ""
  );
}

// ============================================
// API REQUEST HANDLER
// ============================================

async function apiRequest(path, options = {}) {
  const token = getToken();

  if (!token) {
    throw new Error(
      "Your session has expired. Please log in again."
    );
  }

  const response = await fetch(`${API_BASE}${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
      ...(options.headers || {}),
    },
  });

  const responseText = await response.text();
  let data = null;

  if (responseText) {
    try {
      data = JSON.parse(responseText);
    } catch {
      data = responseText;
    }
  }

  if (response.status === 401) {
    throw new Error(
      "Your session has expired. Please log in again."
    );
  }

  if (response.status === 403) {
    throw new Error(
      "You do not have permission to access this resource."
    );
  }

  if (!response.ok) {
    const message =
      data && typeof data === "object"
        ? data.detail ||
          data.message ||
          data.question_id?.[0] ||
          data.non_field_errors?.[0] ||
          `Request failed (${response.status}).`
        : `Request failed (${response.status}).`;

    throw new Error(message);
  }

  return data;
}

// ============================================
// NORMALIZE API DATA
// ============================================

function normalizeList(data) {
  if (Array.isArray(data)) return data;

  if (Array.isArray(data?.results)) {
    return data.results;
  }

  return [];
}

// Convert existing backend difficulty values
// into Easy, Medium and Hard.

function normalizeDifficulty(value) {
  const level = String(value || "").trim().toLowerCase();

  if (["easy", "beginner"].includes(level)) {
    return "Easy";
  }

  if (["medium", "intermediate"].includes(level)) {
    return "Medium";
  }

  if (["hard", "advanced"].includes(level)) {
    return "Hard";
  }

  return "Easy";
}

function normalizeQuestion(item) {
  return {
    id: item.id,
    topic: item.category || "Other",
    difficulty: normalizeDifficulty(item.difficulty),
    question: item.question || "",
    answer: item.suggested_answer || "",
    keywords: Array.isArray(item.keywords)
      ? item.keywords
      : [],
  };
}

// ============================================
// INTERVIEW PREP COMPONENT
// ============================================

function InterviewPrep() {
  const [questions, setQuestions] = useState([]);
  const [practiceRecords, setPracticeRecords] = useState({});
  const [topic, setTopic] = useState("All Topics");
  const [difficulty, setDifficulty] = useState("All Levels");
  const [search, setSearch] = useState("");
  const [activeTab, setActiveTab] = useState("Practice");
  const [revealed, setRevealed] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [loading, setLoading] = useState(true);
  const [savingIds, setSavingIds] = useState([]);
  const [loadError, setLoadError] = useState("");

  const practiceSectionRef = useRef(null);

  // ============================================
  // LOAD QUESTIONS AND PRACTICE RECORDS
  // ============================================

  const loadData = useCallback(async (showSuccessToast = false) => {
    setLoading(true);
    setLoadError("");

    try {
      const [questionData, practiceData] = await Promise.all([
        apiRequest("/questions/"),
        apiRequest("/practice/"),
      ]);

      const loadedQuestions = normalizeList(questionData)
        .map(normalizeQuestion)
        .filter(
          (item) =>
            item.id !== undefined &&
            item.question
        );

      const loadedRecords = normalizeList(practiceData);
      const recordMap = {};

      loadedRecords.forEach((record) => {
        const questionId =
          record.question_details?.id ??
          record.question ??
          record.question_id;

        if (
          questionId !== undefined &&
          questionId !== null
        ) {
          recordMap[String(questionId)] = record;
        }
      });

      setQuestions(loadedQuestions);
      setPracticeRecords(recordMap);
      setCurrentIndex(0);
      setRevealed([]);

      if (loadedQuestions.length === 0) {
        const message =
          "No active interview questions were returned by the API.";

        setLoadError(message);

        if (showSuccessToast) {
          showToast(
            "No active interview questions were found.",
            "warning"
          );
        }
      } else if (showSuccessToast) {
        showToast(
          `Questions refreshed successfully! ${loadedQuestions.length} questions loaded.`,
          "success"
        );
      }
    } catch (error) {
      const message =
        error.message ||
        "Could not load interview questions.";

      setLoadError(message);
      showToast(message, "error");

      console.error("Interview Prep loading error:", error);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadData(false);
  }, [loadData]);

  // ============================================
  // PRACTICED AND BOOKMARKED QUESTIONS
  // ============================================

  const practicedIds = useMemo(
    () =>
      Object.keys(practiceRecords).filter(
        (id) => practiceRecords[id]?.is_practiced
      ),
    [practiceRecords]
  );

  const bookmarkedIds = useMemo(
    () =>
      Object.keys(practiceRecords).filter(
        (id) => practiceRecords[id]?.is_bookmarked
      ),
    [practiceRecords]
  );

  // ============================================
  // FILTER QUESTIONS
  // ============================================

  const filteredQuestions = useMemo(() => {
    const query = search.trim().toLowerCase();

    return questions.filter((item) => {
      const record = practiceRecords[String(item.id)];

      const matchesTopic =
        topic === "All Topics" ||
        item.topic === topic;

      const matchesDifficulty =
        difficulty === "All Levels" ||
        item.difficulty === difficulty;

      const matchesSearch =
        !query ||
        item.question.toLowerCase().includes(query) ||
        item.topic.toLowerCase().includes(query) ||
        item.answer.toLowerCase().includes(query) ||
        item.keywords.some((keyword) =>
          String(keyword).toLowerCase().includes(query)
        );

      const matchesTab =
        activeTab === "Practice" ||
        (activeTab === "Bookmarked" &&
          Boolean(record?.is_bookmarked)) ||
        (activeTab === "Practiced" &&
          Boolean(record?.is_practiced));

      return (
        matchesTopic &&
        matchesDifficulty &&
        matchesSearch &&
        matchesTab
      );
    });
  }, [
    questions,
    practiceRecords,
    topic,
    difficulty,
    search,
    activeTab,
  ]);

  useEffect(() => {
    setCurrentIndex(0);
    setRevealed([]);
  }, [topic, difficulty, search, activeTab]);

  const currentQuestion =
    filteredQuestions[currentIndex] || null;

  const practicedCount = practicedIds.length;
  const bookmarkedCount = bookmarkedIds.length;

  const completionPercentage = questions.length
    ? Math.min(
        100,
        Math.round(
          (practicedCount / questions.length) * 100
        )
      )
    : 0;

  const isRevealed = (id) =>
    revealed.includes(String(id));

  // ============================================
  // SAVE PRACTICE AND BOOKMARK RECORD
  // ============================================

  const saveRecord = async (question, changes) => {
    const id = String(question.id);

    if (savingIds.includes(id)) {
      return null;
    }

    setSavingIds((previous) => [
      ...previous,
      id,
    ]);

    try {
      const existing = practiceRecords[id];
      let savedRecord;

      if (existing?.id) {
        savedRecord = await apiRequest(
          `/practice/${existing.id}/`,
          {
            method: "PATCH",
            body: JSON.stringify(changes),
          }
        );
      } else {
        savedRecord = await apiRequest(
          "/practice/",
          {
            method: "POST",
            body: JSON.stringify({
              question_id: question.id,
              student_answer: "",
              is_practiced: false,
              is_bookmarked: false,
              ...changes,
            }),
          }
        );
      }

      setPracticeRecords((previous) => ({
        ...previous,
        [id]: savedRecord,
      }));

      return savedRecord;
    } catch (error) {
      showToast(
        error.message ||
          "Could not save your practice progress.",
        "error"
      );

      console.error("Save practice record error:", error);

      throw error;
    } finally {
      setSavingIds((previous) =>
        previous.filter((item) => item !== id)
      );
    }
  };

  // ============================================
  // MARK QUESTION AS PRACTICED
  // ============================================

  const togglePracticed = async (question) => {
    const id = String(question.id);

    const alreadyPracticed = Boolean(
      practiceRecords[id]?.is_practiced
    );

    try {
      const result = await saveRecord(question, {
        is_practiced: !alreadyPracticed,
      });

      if (!result) return;

      showToast(
        alreadyPracticed
          ? "Question removed from practiced list."
          : "Question marked as practiced. Keep going!",
        alreadyPracticed ? "info" : "success"
      );
    } catch {
      // saveRecord already displays the error toast.
    }
  };

  // ============================================
  // BOOKMARK QUESTION
  // ============================================

  const toggleBookmark = async (question) => {
    const id = String(question.id);

    const alreadySaved = Boolean(
      practiceRecords[id]?.is_bookmarked
    );

    try {
      const result = await saveRecord(question, {
        is_bookmarked: !alreadySaved,
      });

      if (!result) return;

      showToast(
        alreadySaved
          ? "Question removed from bookmarks."
          : "Question saved to bookmarks.",
        alreadySaved ? "info" : "success"
      );
    } catch {
      // saveRecord already displays the error toast.
    }
  };

  // ============================================
  // REVEAL ANSWER
  // ============================================

  const toggleAnswer = (id) => {
    const key = String(id);

    setRevealed((previous) =>
      previous.includes(key)
        ? previous.filter((item) => item !== key)
        : [...previous, key]
    );
  };

  // ============================================
  // QUESTION NAVIGATION
  // ============================================

  const goToQuestion = (direction) => {
    if (!filteredQuestions.length) return;

    setCurrentIndex((previous) => {
      if (direction === "next") {
        return (
          (previous + 1) % filteredQuestions.length
        );
      }

      return (
        (previous - 1 + filteredQuestions.length) %
        filteredQuestions.length
      );
    });

    setRevealed([]);
  };

  // ============================================
  // RANDOM QUESTION
  // ============================================

  const chooseRandomQuestion = () => {
    if (filteredQuestions.length <= 1) {
      showToast(
        "Try another topic or filter to explore more questions.",
        "info"
      );

      return;
    }

    let nextIndex = currentIndex;

    while (nextIndex === currentIndex) {
      nextIndex = Math.floor(
        Math.random() * filteredQuestions.length
      );
    }

    setCurrentIndex(nextIndex);
    setRevealed([]);
  };

  // ============================================
  // CLEAR FILTERS
  // ============================================

  const clearFilters = () => {
    setTopic("All Topics");
    setDifficulty("All Levels");
    setSearch("");
  };

  // ============================================
  // CHANGE TABS
  // ============================================

  const selectTab = (tab) => {
    setActiveTab(tab);
    setCurrentIndex(0);
    setRevealed([]);
  };

  // ============================================
  // START PRACTICING
  // ============================================

  const startPractising = () => {
    setActiveTab("Practice");
    setTopic("All Topics");
    setDifficulty("All Levels");
    setSearch("");
    setCurrentIndex(0);
    setRevealed([]);

    window.setTimeout(() => {
      practiceSectionRef.current?.scrollIntoView({
        behavior: "smooth",
        block: "start",
      });
    }, 150);
  };

  // ============================================
  // UI
  // ============================================

  return (
    <div className="ip-page">

      {/* HERO SECTION */}

      <header className="ip-hero">
        <div className="ip-hero-copy">
          <span className="ip-eyebrow">
            <span className="ip-eyebrow-dot" />
            SKILLSPHERE CAREER PREPARATION
          </span>

          <h1>
            Prepare today. <span>Shine tomorrow.</span>
          </h1>

          <p>
            Build confidence with technical interview questions,
            clear explanations, and focused daily practice.
          </p>

          <button
            type="button"
            className="ip-hero-button"
            onClick={startPractising}
          >
            Start practising{" "}
            <span aria-hidden="true">→</span>
          </button>
        </div>

        <div className="ip-hero-art" aria-hidden="true">
          <div className="ip-orbit ip-orbit-one" />
          <div className="ip-orbit ip-orbit-two" />
          <div className="ip-hero-icon">🎯</div>

          <div className="ip-float-card ip-float-top">
            <span>✓</span> Practice makes progress
          </div>

          <div className="ip-float-card ip-float-bottom">
            <span>✦</span> Your next opportunity
          </div>
        </div>
      </header>

      {/* STATISTICS */}

      <section className="ip-stats">
        <div className="ip-stat-card">
          <span className="ip-stat-icon ip-blue">❔</span>

          <div>
            <strong>{questions.length}</strong>
            <span>Interview questions</span>
          </div>
        </div>

        <div className="ip-stat-card">
          <span className="ip-stat-icon ip-green">✓</span>

          <div>
            <strong>{practicedCount}</strong>
            <span>Questions practised</span>
          </div>
        </div>

        <div className="ip-stat-card">
          <span className="ip-stat-icon ip-purple">🔖</span>

          <div>
            <strong>{bookmarkedCount}</strong>
            <span>Saved questions</span>
          </div>
        </div>

        <div className="ip-stat-card">
          <span className="ip-stat-icon ip-orange">↗</span>

          <div>
            <strong>{completionPercentage}%</strong>
            <span>Practice coverage</span>
          </div>
        </div>
      </section>

      {/* PROGRESS PANEL */}

      <section className="ip-progress-panel">
        <div className="ip-progress-icon">🚀</div>

        <div className="ip-progress-main">
          <div className="ip-progress-heading">
            <div>
              <h2>Your interview preparation</h2>
              <p>
                Practise consistently to build confidence.
              </p>
            </div>

            <strong>{completionPercentage}%</strong>
          </div>

          <div
            className="ip-progress-track"
            role="progressbar"
            aria-label="Interview question practice coverage"
            aria-valuenow={completionPercentage}
            aria-valuemin={0}
            aria-valuemax={100}
          >
            <div
              style={{
                width: `${completionPercentage}%`,
              }}
            />
          </div>

          <span>
            {practicedCount} of {questions.length} questions marked
            as practised
          </span>
        </div>
      </section>

      {/* PRACTICE SECTION */}

      <section
        className="ip-practice-section"
        ref={practiceSectionRef}
      >
        <div className="ip-section-heading">
          <div>
            <span className="ip-section-label">
              YOUR PRACTICE SPACE
            </span>

            <h2>Technical interview practice</h2>

            <p>
              Think through the answer before revealing the
              explanation.
            </p>
          </div>

          <button
            type="button"
            className="ip-clear-filter"
            onClick={() => loadData(true)}
            disabled={loading}
          >
            {loading ? "Loading..." : "Refresh questions"}
          </button>
        </div>

        {/* TABS */}

        <div
          className="ip-tabs"
          role="tablist"
          aria-label="Question lists"
        >
          <button
            type="button"
            role="tab"
            aria-selected={activeTab === "Practice"}
            className={
              activeTab === "Practice" ? "active" : ""
            }
            onClick={() => selectTab("Practice")}
          >
            All questions
          </button>

          <button
            type="button"
            role="tab"
            aria-selected={activeTab === "Practiced"}
            className={
              activeTab === "Practiced" ? "active" : ""
            }
            onClick={() => selectTab("Practiced")}
          >
            Practised <span>{practicedCount}</span>
          </button>

          <button
            type="button"
            role="tab"
            aria-selected={activeTab === "Bookmarked"}
            className={
              activeTab === "Bookmarked" ? "active" : ""
            }
            onClick={() => selectTab("Bookmarked")}
          >
            Bookmarked <span>{bookmarkedCount}</span>
          </button>
        </div>

        {/* FILTERS */}

        <div className="ip-filters">
          <label className="ip-search">
            <span aria-hidden="true">⌕</span>

            <input
              type="search"
              value={search}
              onChange={(event) =>
                setSearch(event.target.value)
              }
              placeholder="Search interview questions..."
              aria-label="Search interview questions"
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

          <label className="ip-select">
            <span className="ip-sr-only">
              Filter by topic
            </span>

            <select
              value={topic}
              onChange={(event) =>
                setTopic(event.target.value)
              }
            >
              {TOPICS.map((item) => (
                <option key={item} value={item}>
                  {item}
                </option>
              ))}
            </select>
          </label>

          <label className="ip-select">
            <span className="ip-sr-only">
              Filter by difficulty
            </span>

            <select
              value={difficulty}
              onChange={(event) =>
                setDifficulty(event.target.value)
              }
            >
              {DIFFICULTIES.map((item) => (
                <option key={item} value={item}>
                  {item}
                </option>
              ))}
            </select>
          </label>

          {(search ||
            topic !== "All Topics" ||
            difficulty !== "All Levels") && (
            <button
              type="button"
              className="ip-clear-filter"
              onClick={clearFilters}
            >
              Clear filters
            </button>
          )}
        </div>

        <div className="ip-question-count">
          Showing <strong>{filteredQuestions.length}</strong>{" "}
          {filteredQuestions.length === 1
            ? "question"
            : "questions"}
        </div>

        {/* LOADING */}

        {loading ? (
          <div className="ip-empty-state">
            <h3>Loading interview questions...</h3>
            <p>
              Connecting to your SkillSphere question bank.
            </p>
          </div>

        ) : loadError && questions.length === 0 ? (

          <div className="ip-empty-state">
            <span>⚠️</span>

            <h3>Unable to load interview questions</h3>

            <p>{loadError}</p>

            <button
              type="button"
              onClick={() => loadData(true)}
            >
              Try again
            </button>
          </div>

        ) : currentQuestion ? (

          <article className="ip-featured-question">
            <div className="ip-question-top">
              <div className="ip-question-tags">
                <span className="ip-topic-badge">
                  {currentQuestion.topic}
                </span>

                <span
                  className={`ip-difficulty ip-difficulty-${currentQuestion.difficulty.toLowerCase()}`}
                >
                  {currentQuestion.difficulty}
                </span>

                {practiceRecords[
                  String(currentQuestion.id)
                ]?.is_practiced && (
                  <span className="ip-practiced-badge">
                    ✓ Practised
                  </span>
                )}
              </div>

              <button
                type="button"
                className={`ip-bookmark-button ${
                  practiceRecords[
                    String(currentQuestion.id)
                  ]?.is_bookmarked
                    ? "saved"
                    : ""
                }`}
                onClick={() =>
                  toggleBookmark(currentQuestion)
                }
                disabled={savingIds.includes(
                  String(currentQuestion.id)
                )}
                aria-label={
                  practiceRecords[
                    String(currentQuestion.id)
                  ]?.is_bookmarked
                    ? "Remove bookmark"
                    : "Bookmark question"
                }
                title={
                  practiceRecords[
                    String(currentQuestion.id)
                  ]?.is_bookmarked
                    ? "Remove bookmark"
                    : "Save question"
                }
              >
                {practiceRecords[
                  String(currentQuestion.id)
                ]?.is_bookmarked
                  ? "★"
                  : "☆"}
              </button>
            </div>

            <div className="ip-question-number">
              QUESTION{" "}
              {String(currentIndex + 1).padStart(2, "0")}{" "}
              OF {filteredQuestions.length}
            </div>

            <h3>{currentQuestion.question}</h3>

            <p className="ip-question-prompt">
              Take a moment to form your answer. Try explaining it
              aloud as if you were speaking to an interviewer.
            </p>

            {isRevealed(currentQuestion.id) ? (
              <div className="ip-answer-panel">
                <div className="ip-answer-heading">
                  <span className="ip-answer-check">✓</span>
                  <h4>Suggested answer</h4>
                </div>

                <p>{currentQuestion.answer}</p>

                {currentQuestion.keywords.length > 0 && (
                  <div className="ip-keywords">
                    <span>Key points to remember</span>

                    <div>
                      {currentQuestion.keywords.map(
                        (keyword) => (
                          <span key={keyword}>
                            {keyword}
                          </span>
                        )
                      )}
                    </div>
                  </div>
                )}
              </div>
            ) : (
              <div className="ip-reveal-panel">
                <span className="ip-reveal-icon">💭</span>

                <div>
                  <strong>
                    Can you answer this question?
                  </strong>

                  <p>
                    Try answering in your own words before
                    checking.
                  </p>
                </div>
              </div>
            )}

            <div className="ip-question-actions">
              <button
                type="button"
                className="ip-reveal-button"
                onClick={() =>
                  toggleAnswer(currentQuestion.id)
                }
              >
                {isRevealed(currentQuestion.id)
                  ? "Hide answer"
                  : "Reveal answer"}

                <span aria-hidden="true">
                  {isRevealed(currentQuestion.id)
                    ? "↑"
                    : "↓"}
                </span>
              </button>

              <button
                type="button"
                className={`ip-practice-button ${
                  practiceRecords[
                    String(currentQuestion.id)
                  ]?.is_practiced
                    ? "marked"
                    : ""
                }`}
                onClick={() =>
                  togglePracticed(currentQuestion)
                }
                disabled={savingIds.includes(
                  String(currentQuestion.id)
                )}
              >
                {savingIds.includes(
                  String(currentQuestion.id)
                )
                  ? "Saving..."
                  : practiceRecords[
                      String(currentQuestion.id)
                    ]?.is_practiced
                  ? "✓ Practised"
                  : "✓ Mark as practised"}
              </button>
            </div>

            <div className="ip-question-navigation">
              <button
                type="button"
                onClick={() =>
                  goToQuestion("previous")
                }
                disabled={filteredQuestions.length <= 1}
              >
                ← Previous
              </button>

              <button
                type="button"
                className="ip-random-button"
                onClick={chooseRandomQuestion}
                disabled={filteredQuestions.length <= 1}
              >
                ⤨ Random question
              </button>

              <button
                type="button"
                onClick={() =>
                  goToQuestion("next")
                }
                disabled={filteredQuestions.length <= 1}
              >
                Next question →
              </button>
            </div>
          </article>

        ) : (

          <div className="ip-empty-state">
            <span>🔎</span>

            <h3>
              {activeTab === "Bookmarked"
                ? "No bookmarked questions yet"
                : activeTab === "Practiced"
                ? "Your practice journey starts here"
                : "No matching questions"}
            </h3>

            <p>
              {activeTab === "Bookmarked"
                ? "Bookmark questions you want to revise later."
                : activeTab === "Practiced"
                ? "Open a question and mark it as practised when you have reviewed it."
                : "Try changing your search term, topic, or difficulty."}
            </p>

            {activeTab !== "Practice" ? (
              <button
                type="button"
                onClick={() => selectTab("Practice")}
              >
                Explore all questions
              </button>
            ) : (
              <button
                type="button"
                onClick={clearFilters}
              >
                Reset filters
              </button>
            )}
          </div>
        )}
      </section>

      {/* INTERVIEW TIPS */}

      <section className="ip-tips-section">
        <div className="ip-section-heading">
          <div>
            <span className="ip-section-label">
              INTERVIEW SMARTER
            </span>

            <h2>Simple habits, stronger answers</h2>
          </div>
        </div>

        <div className="ip-tips-grid">
          <article className="ip-tip-card">
            <span className="ip-tip-icon ip-tip-blue">
              💬
            </span>

            <h3>Explain in your own words</h3>

            <p>
              Understand the concept first, then describe it
              clearly with a simple example.
            </p>
          </article>

          <article className="ip-tip-card">
            <span className="ip-tip-icon ip-tip-purple">
              ⌨️
            </span>

            <h3>Practise with code</h3>

            <p>
              For programming topics, write small programs
              and explain the output and logic.
            </p>
          </article>

          <article className="ip-tip-card">
            <span className="ip-tip-icon ip-tip-green">
              🔁
            </span>

            <h3>Revise regularly</h3>

            <p>
              Bookmark difficult questions and revisit them
              until you can explain the answer confidently.
            </p>
          </article>
        </div>
      </section>
    </div>
  );
}

export default InterviewPrep;
