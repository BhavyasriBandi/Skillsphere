
import React, { useEffect, useState } from "react";
import "./Challenges.css";
import { showToast } from "../components/ToastProvider";

import {
  getChallengeProgress,
  saveChallengeProgress,
} from "./challengesApi";

const STORAGE_KEY = "skillsphere_challenges_progress";

const CHALLENGES = [
  {
    id: 1,
    title: "Even or Odd",
    category: "Python",
    difficulty: "Easy",
    points: 10,
    time: "10 min",
    question: "Write a program that checks whether an integer is even or odd.",
    hint: "Use the modulo operator (%) to check the remainder after division by 2.",
    sample: "Input: 7\nOutput: Odd",
    answer: "n = int(input())\nif n % 2 == 0:\n    print('Even')\nelse:\n    print('Odd')",
    keywords: ["%", "if", "else"],
  },
  {
    id: 2,
    title: "Reverse a String",
    category: "Python",
    difficulty: "Easy",
    points: 10,
    time: "15 min",
    question: "Write a program that prints a string in reverse order.",
    hint: "Python slicing supports a negative step.",
    sample: "Input: hello\nOutput: olleh",
    answer: "text = input()\nprint(text[::-1])",
    keywords: ["[::-1]"],
  },
  {
    id: 3,
    title: "Find the Largest Number",
    category: "Python",
    difficulty: "Easy",
    points: 10,
    time: "15 min",
    question: "Read three numbers and print the largest number.",
    hint: "Compare the numbers or use Python's built-in max() function.",
    sample: "Input: 4 9 2\nOutput: 9",
    answer: "numbers = list(map(int, input().split()))\nprint(max(numbers))",
    keywords: ["max("],
  },
  {
    id: 4,
    title: "Count Vowels",
    category: "Python",
    difficulty: "Medium",
    points: 20,
    time: "20 min",
    question:
      "Count the vowels in a string. Treat uppercase and lowercase letters equally.",
    hint:
      "Convert the string to lowercase and check each character against 'aeiou'.",
    sample: "Input: Education\nOutput: 5",
    answer:
      "text = input().lower()\ncount = sum(1 for ch in text if ch in 'aeiou')\nprint(count)",
    keywords: ["lower()", "aeiou"],
  },
  {
    id: 5,
    title: "Remove Duplicates",
    category: "Python",
    difficulty: "Medium",
    points: 20,
    time: "25 min",
    question:
      "Remove duplicate values from a list while preserving the original order.",
    hint:
      "Build a new list and append a value only if it has not appeared before.",
    sample: "Input: 1 2 1 3 2\nOutput: 1 2 3",
    answer:
      "numbers = list(map(int, input().split()))\nresult = []\nfor number in numbers:\n    if number not in result:\n        result.append(number)\nprint(*result)",
    keywords: ["result", "append", "not in"],
  },
  {
    id: 6,
    title: "Palindrome Check",
    category: "Python",
    difficulty: "Medium",
    points: 20,
    time: "20 min",
    question: "Check whether a word reads the same forward and backward.",
    hint: "Compare the word with its reversed version.",
    sample: "Input: madam\nOutput: Palindrome",
    answer:
      "word = input().strip().lower()\nif word == word[::-1]:\n    print('Palindrome')\nelse:\n    print('Not Palindrome')",
    keywords: ["[::-1]", "if"],
  },
  {
    id: 7,
    title: "Factorial",
    category: "Java",
    difficulty: "Easy",
    points: 10,
    time: "15 min",
    question: "Calculate the factorial of a non-negative integer.",
    hint:
      "Start the result at 1 and multiply it by every integer from 1 to n.",
    sample: "Input: 5\nOutput: 120",
    answer:
      "import java.util.Scanner;\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        long result = 1;\n        for (int i = 2; i <= n; i++) {\n            result *= i;\n        }\n        System.out.println(result);\n    }\n}",
    keywords: ["for", "result", "*="],
  },
  {
    id: 8,
    title: "Find Array Maximum",
    category: "Java",
    difficulty: "Easy",
    points: 10,
    time: "15 min",
    question: "Find the maximum value in an integer array.",
    hint:
      "Assume the first array element is the maximum, then compare the others.",
    sample: "Array: [4, 8, 2, 9]\nOutput: 9",
    answer:
      "int max = arr[0];\nfor (int value : arr) {\n    if (value > max) {\n        max = value;\n    }\n}\nSystem.out.println(max);",
    keywords: ["max", "if"],
  },
  {
    id: 9,
    title: "Count Positive Numbers",
    category: "C",
    difficulty: "Easy",
    points: 10,
    time: "15 min",
    question: "Count how many values in an array are greater than zero.",
    hint:
      "Loop through the array and increment a counter when a value is positive.",
    sample: "Array: [-1, 3, 0, 5]\nOutput: 2",
    answer:
      'int count = 0;\nfor (int i = 0; i < n; i++) {\n    if (arr[i] > 0) {\n        count++;\n    }\n}\nprintf("%d", count);',
    keywords: ["count", "arr[i] > 0"],
  },
  {
    id: 10,
    title: "Sum of Array Elements",
    category: "C",
    difficulty: "Easy",
    points: 10,
    time: "15 min",
    question: "Calculate the sum of all elements in an integer array.",
    hint: "Initialize a sum variable to zero and add each array element.",
    sample: "Array: [2, 3, 4]\nOutput: 9",
    answer:
      'int sum = 0;\nfor (int i = 0; i < n; i++) {\n    sum += arr[i];\n}\nprintf("%d", sum);',
    keywords: ["sum", "+=", "arr[i]"],
  },
  {
    id: 11,
    title: "Second Largest Value",
    category: "Python",
    difficulty: "Hard",
    points: 30,
    time: "30 min",
    question: "Find the second-largest distinct number in a list.",
    hint:
      "Remove duplicates, sort the numbers, and check that at least two distinct values exist.",
    sample: "Input: 4 8 8 2\nOutput: 4",
    answer:
      "numbers = sorted(set(map(int, input().split())))\nif len(numbers) >= 2:\n    print(numbers[-2])\nelse:\n    print('Not enough distinct values')",
    keywords: ["set(", "sorted(", "[-2]"],
  },
  {
    id: 12,
    title: "SQL Filtering",
    category: "SQL",
    difficulty: "Easy",
    points: 10,
    time: "10 min",
    question:
      "Write a query to retrieve employees whose salary is greater than 50000.",
    hint: "Use SELECT to choose columns and WHERE to filter rows.",
    sample: "Table: employees\nRequired condition: salary > 50000",
    answer: "SELECT *\nFROM employees\nWHERE salary > 50000;",
    keywords: ["select", "from", "where", "salary > 50000"],
  },
  {
    id: 13,
    title: "Department-wise Count",
    category: "SQL",
    difficulty: "Medium",
    points: 20,
    time: "20 min",
    question: "Count the number of employees in each department.",
    hint: "Group rows by department and count the rows in each group.",
    sample: "Table: employees\nRequired output: department and employee count",
    answer:
      "SELECT department, COUNT(*) AS employee_count\nFROM employees\nGROUP BY department;",
    keywords: ["count(", "group by", "department"],
  },
  {
    id: 14,
    title: "Find Duplicate Emails",
    category: "SQL",
    difficulty: "Hard",
    points: 30,
    time: "25 min",
    question: "Find email addresses that occur more than once in a users table.",
    hint:
      "Group by email and keep only groups with a count greater than one.",
    sample: "Table: users\nRequired output: duplicated email addresses",
    answer:
      "SELECT email\nFROM users\nGROUP BY email\nHAVING COUNT(*) > 1;",
    keywords: ["group by", "having", "count(*) > 1"],
  },
];

function readProgress() {
  try {
    const saved = localStorage.getItem(STORAGE_KEY);

    if (!saved) {
      return { completedIds: [] };
    }

    const parsed = JSON.parse(saved);

    return {
      completedIds: Array.isArray(parsed.completedIds)
        ? parsed.completedIds.map(Number)
        : [],
    };
  } catch {
    return { completedIds: [] };
  }
}

function normalizeCode(value) {
  return value.toLowerCase().replace(/\s+/g, "").replace(/["']/g, "");
}

function Challenges() {
  const [progress, setProgress] = useState(readProgress);
  const [selectedCategory, setSelectedCategory] = useState("All");
  const [selectedDifficulty, setSelectedDifficulty] = useState("All");
  const [activeChallenge, setActiveChallenge] = useState(null);
  const [code, setCode] = useState("");
  const [showHint, setShowHint] = useState(false);
  const [feedback, setFeedback] = useState("");
  const [feedbackType, setFeedbackType] = useState("info");
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);

  const completedIds = Array.isArray(progress.completedIds)
    ? progress.completedIds
    : [];

  // Load progress from backend
  useEffect(() => {
    let cancelled = false;

    async function loadProgress() {
      try {
        const data = await getChallengeProgress();

        if (cancelled) return;

        const ids = Array.isArray(data.completedIds)
          ? data.completedIds
              .map(Number)
              .filter((id) =>
                CHALLENGES.some((challenge) => challenge.id === id)
              )
          : [];

        const nextProgress = {
          completedIds: [...new Set(ids)],
        };

        setProgress(nextProgress);

        localStorage.setItem(
          STORAGE_KEY,
          JSON.stringify(nextProgress)
        );
      } catch (error) {
        if (!cancelled) {
          console.error(
            "Could not load challenge progress:",
            error
          );

          const message =
            error.message ||
            "Could not load challenge progress.";

          setFeedback(message);
          setFeedbackType("error");
          showToast(message, "error");
        }
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    }

    loadProgress();

    return () => {
      cancelled = true;
    };
  }, []);

  const completedCount = completedIds.length;

  const earnedPoints = CHALLENGES.reduce(
    (sum, challenge) =>
      completedIds.includes(challenge.id)
        ? sum + challenge.points
        : sum,
    0
  );

  const filteredChallenges = CHALLENGES.filter((challenge) => {
    const categoryMatches =
      selectedCategory === "All" ||
      challenge.category === selectedCategory;

    const difficultyMatches =
      selectedDifficulty === "All" ||
      challenge.difficulty === selectedDifficulty;

    return categoryMatches && difficultyMatches;
  });

  // Save progress to backend
  async function saveProgress(nextProgress) {
    setSaving(true);

    try {
      const ids = [
        ...new Set(
          (nextProgress.completedIds || []).map(Number)
        ),
      ];

      const data = await saveChallengeProgress(ids);

      const savedIds = Array.isArray(data.completedIds)
        ? data.completedIds.map(Number)
        : ids;

      const savedProgress = {
        completedIds: savedIds,
      };

      setProgress(savedProgress);

      localStorage.setItem(
        STORAGE_KEY,
        JSON.stringify(savedProgress)
      );

      return true;
    } catch (error) {
      console.error(
        "Challenge progress save error:",
        error
      );

      const message =
        error.message ||
        "Unable to save progress to the server.";

      setFeedback(message);
      setFeedbackType("error");
      showToast(message, "error");

      return false;
    } finally {
      setSaving(false);
    }
  }

  function openChallenge(challenge) {
    setActiveChallenge(challenge);
    setCode("");
    setShowHint(false);
    setFeedback("");
    setFeedbackType("info");
  }

  // Check submitted solution
  async function checkAnswer() {
    if (!activeChallenge || saving || loading) {
      return;
    }

    const normalized = normalizeCode(code);

    if (!normalized.trim()) {
      const message = "Write your solution before checking it.";

      setFeedback(message);
      setFeedbackType("error");
      showToast(message, "error");

      return;
    }

    const keywordsFound = activeChallenge.keywords.filter(
      (keyword) =>
        normalized.includes(normalizeCode(keyword))
    );

    const requiredCount = Math.min(
      activeChallenge.category === "SQL" ? 3 : 2,
      activeChallenge.keywords.length
    );

    if (keywordsFound.length >= requiredCount) {
      const nextProgress = {
        completedIds: [
          ...new Set([
            ...completedIds,
            activeChallenge.id,
          ]),
        ],
      };

      if (await saveProgress(nextProgress)) {
        const message =
          "Your code contains the expected concepts. Review the sample solution and test your code in a real compiler or interpreter.";

        setFeedback(message);
        setFeedbackType("success");

        showToast(
          `Challenge "${activeChallenge.title}" completed successfully!`,
          "success"
        );
      }
    } else {
      const message =
        "Some expected concepts may be missing. Review the hint and try again. This checker uses keywords, not actual code execution.";

      setFeedback(message);
      setFeedbackType("error");

      showToast(
        "Some expected concepts are missing. Review the hint and try again.",
        "error"
      );
    }
  }

  // Reset progress
  async function resetProgress() {
    if (
      completedCount === 0 ||
      saving ||
      loading
    ) {
      return;
    }

    if (await saveProgress({ completedIds: [] })) {
      setFeedback("Challenge progress has been reset.");
      setFeedbackType("info");

      showToast(
        "Challenge progress has been reset.",
        "success"
      );
    }
  }

  return (
    <div className="challenges-page">
      <header className="challenges-header">
        <div>
          <span className="challenges-eyebrow">
            PRACTISE · SOLVE · LEVEL UP
          </span>

          <h1>Coding Challenges</h1>

          <p>
            Strengthen your programming skills through small,
            focused challenges. Track your completed tasks as you learn.
          </p>
        </div>

        <div
          className="challenges-header-icon"
          aria-hidden="true"
        >
          {"</>"}
        </div>
      </header>

      <section className="challenges-stats">
        <article className="challenge-stat-card">
          <span className="challenge-stat-icon blue">▤</span>

          <div>
            <span>Available challenges</span>
            <strong>{CHALLENGES.length}</strong>
          </div>
        </article>

        <article className="challenge-stat-card">
          <span className="challenge-stat-icon green">✓</span>

          <div>
            <span>Completed</span>
            <strong>{completedCount}</strong>
          </div>
        </article>

        <article className="challenge-stat-card">
          <span className="challenge-stat-icon purple">★</span>

          <div>
            <span>Points earned</span>
            <strong>{earnedPoints}</strong>
          </div>
        </article>
      </section>

      <section className="challenges-progress-panel">
        <div className="challenges-progress-heading">
          <div>
            <h2>Your challenge progress</h2>
            <p>
              Every completed challenge is a step forward.
            </p>
          </div>

          <strong>
            {Math.round(
              (completedCount / CHALLENGES.length) * 100
            )}%
          </strong>
        </div>

        <div className="challenges-progress-track">
          <div
            className="challenges-progress-fill"
            style={{
              width: `${
                (completedCount / CHALLENGES.length) * 100
              }%`,
            }}
          />
        </div>
      </section>

      <section className="challenges-library">
        <div className="challenges-library-heading">
          <div>
            <h2>Challenge library</h2>

            <p>
              Choose a problem, write a solution, and check your approach.
            </p>
          </div>

          <button
            type="button"
            className="challenge-reset-button"
            onClick={resetProgress}
            disabled={
              completedCount === 0 ||
              saving ||
              loading
            }
          >
            Reset progress
          </button>
        </div>

        <div className="challenge-filters">
          <label>
            <span>Programming language</span>

            <select
              value={selectedCategory}
              onChange={(event) =>
                setSelectedCategory(event.target.value)
              }
            >
              <option>All</option>
              <option>Python</option>
              <option>Java</option>
              <option>C</option>
              <option>SQL</option>
            </select>
          </label>

          <label>
            <span>Difficulty</span>

            <select
              value={selectedDifficulty}
              onChange={(event) =>
                setSelectedDifficulty(event.target.value)
              }
            >
              <option>All</option>
              <option>Easy</option>
              <option>Medium</option>
              <option>Hard</option>
            </select>
          </label>
        </div>

        {loading && (
          <p role="status">
            Loading your saved challenge progress…
          </p>
        )}

        {saving && (
          <p role="status">
            Saving progress to your account…
          </p>
        )}

        <div className="challenge-grid">
          {filteredChallenges.map((challenge) => {
            const completed = completedIds.includes(
              challenge.id
            );

            return (
              <article
                key={challenge.id}
                className={`challenge-card ${
                  completed ? "challenge-card-completed" : ""
                }`}
              >
                <div className="challenge-card-top">
                  <span
                    className={`challenge-language challenge-language-${challenge.category.toLowerCase()}`}
                  >
                    {challenge.category}
                  </span>

                  {completed && (
                    <span className="challenge-completed-badge">
                      ✓ Done
                    </span>
                  )}
                </div>

                <h3>{challenge.title}</h3>

                <p className="challenge-description">
                  {challenge.question}
                </p>

                <div className="challenge-card-meta">
                  <span
                    className={`challenge-difficulty difficulty-${challenge.difficulty.toLowerCase()}`}
                  >
                    {challenge.difficulty}
                  </span>

                  <span>◷ {challenge.time}</span>

                  <span>★ {challenge.points} pts</span>
                </div>

                <button
                  type="button"
                  className="challenge-open-button"
                  onClick={() => openChallenge(challenge)}
                >
                  {completed
                    ? "Review challenge"
                    : "Solve challenge"}

                  <span>→</span>
                </button>
              </article>
            );
          })}
        </div>

        {filteredChallenges.length === 0 && (
          <div className="challenge-empty">
            No challenges match these filters.
          </div>
        )}
      </section>

      {activeChallenge && (
        <div
          className="challenge-modal-backdrop"
          onClick={(event) => {
            if (event.target === event.currentTarget) {
              setActiveChallenge(null);
            }
          }}
        >
          <section
            className="challenge-modal"
            role="dialog"
            aria-modal="true"
            aria-labelledby="challenge-modal-title"
          >
            <div className="challenge-modal-header">
              <div>
                <span className="challenges-eyebrow">
                  {activeChallenge.category} ·{" "}
                  {activeChallenge.difficulty}
                </span>

                <h2 id="challenge-modal-title">
                  {activeChallenge.title}
                </h2>
              </div>

              <button
                type="button"
                className="challenge-modal-close"
                onClick={() => setActiveChallenge(null)}
                aria-label="Close challenge"
              >
                ×
              </button>
            </div>

            <p className="challenge-modal-question">
              {activeChallenge.question}
            </p>

            <div className="challenge-example">
              <span>EXAMPLE</span>
              <pre>{activeChallenge.sample}</pre>
            </div>

            <label
              className="challenge-code-label"
              htmlFor="challenge-code"
            >
              Your solution
            </label>

            <textarea
              id="challenge-code"
              className="challenge-code-editor"
              value={code}
              onChange={(event) =>
                setCode(event.target.value)
              }
              placeholder="Write your solution here..."
              spellCheck="false"
              rows={9}
            />

            <div className="challenge-editor-actions">
              <button
                type="button"
                className="challenge-hint-button"
                onClick={() =>
                  setShowHint((current) => !current)
                }
              >
                {showHint ? "Hide hint" : "Show hint"}
              </button>

              <button
                type="button"
                className="challenge-solution-button"
                onClick={() => {
                  setCode(activeChallenge.answer);
                  setFeedback("");
                  setFeedbackType("info");
                }}
              >
                View sample solution
              </button>
            </div>

            {showHint && (
              <div className="challenge-hint-box">
                <strong>Hint</strong>
                <p>{activeChallenge.hint}</p>
              </div>
            )}

            {feedback && (
              <div
                className={`challenge-feedback feedback-${feedbackType}`}
                role="status"
              >
                {feedback}
              </div>
            )}

            <div className="challenge-modal-footer">
              <span>
                Reward: {activeChallenge.points} points
              </span>

              <button
                type="button"
                className="challenge-check-button"
                onClick={checkAnswer}
                disabled={saving || loading}
              >
                {saving ? "Saving…" : "Check approach"}
              </button>
            </div>

            <p className="challenge-checker-disclaimer">
              The current checker looks for expected keywords;
              it does not compile or execute your code. A passing
              result is not proof that every test case works.
            </p>
          </section>
        </div>
      )}
    </div>
  );
}

export default Challenges;
