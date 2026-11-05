
import json
import logging
import re
import urllib.error
import urllib.request

from difflib import SequenceMatcher
from django.conf import settings


logger = logging.getLogger(__name__)

QUESTION_COUNT = 10
OPTIONS_COUNT = 4

BATCH_SIZE = 5
MAX_BATCH_ATTEMPTS = 3

OLLAMA_BASE_URL = getattr(
    settings,
    "OLLAMA_BASE_URL",
    "http://127.0.0.1:11434",
)

# Use the smaller model for faster local generation.
OLLAMA_MODEL = getattr(
    settings,
    "OLLAMA_MODEL",
    "qwen2.5:3b",
)


PYTHON_TOPICS = [
    "Variables and Python data types",
    "Arithmetic and comparison operators",
    "Conditional statements",
    "For loops and while loops",
    "Functions and return statements",
    "Lists and list methods",
    "Tuples and indexing",
    "Dictionaries and key-value operations",
    "Sets and unique elements",
    "Exception handling",
]


def normalize_text(value):
    """Normalize question text for duplicate checking."""

    value = str(value).casefold()
    value = re.sub(r"\s+", " ", value)
    value = re.sub(r"[^\w\s]", " ", value)

    return " ".join(value.split())


def normalize_option(value):
    """Normalize options while preserving programming syntax."""

    value = str(value).casefold()
    return " ".join(value.split())


def questions_are_similar(first, second):
    """Detect exact and near-identical question wording."""

    first_normalized = normalize_text(first)
    second_normalized = normalize_text(second)

    if not first_normalized or not second_normalized:
        return True

    if first_normalized == second_normalized:
        return True

    similarity = SequenceMatcher(
        None,
        first_normalized,
        second_normalized,
    ).ratio()

    return similarity >= 0.95


def _validate_question(item):
    """Validate one generated MCQ."""

    if not isinstance(item, dict):
        raise ValueError("Question must be a JSON object.")

    question_text = item.get("question_text")
    options = item.get("options")
    answer = item.get("correct_answer")
    explanation = item.get("explanation")

    if (
        not isinstance(question_text, str)
        or not question_text.strip()
    ):
        raise ValueError("Question text is missing.")

    if (
        not isinstance(options, list)
        or len(options) != OPTIONS_COUNT
    ):
        raise ValueError("Exactly four options are required.")

    if not all(
        isinstance(option, str) and option.strip()
        for option in options
    ):
        raise ValueError("Empty options are not allowed.")

    normalized_options = [
        normalize_option(option)
        for option in options
    ]

    if len(set(normalized_options)) != OPTIONS_COUNT:
        raise ValueError("Duplicate options detected.")

    if all(
        option.strip().upper() in {"A", "B", "C", "D"}
        for option in options
    ):
        raise ValueError("Placeholder options are not allowed.")

    if (
        isinstance(answer, bool)
        or not isinstance(answer, int)
        or answer not in range(OPTIONS_COUNT)
    ):
        raise ValueError(
            "correct_answer must be an integer from 0 to 3."
        )

    if (
        not isinstance(explanation, str)
        or not explanation.strip()
    ):
        raise ValueError("Explanation is missing.")

    return {
        "question_text": question_text.strip(),
        "options": [
            option.strip()
            for option in options
        ],
        "correct_answer": answer,
        "explanation": explanation.strip(),
    }


def _generate_question_batch(
    skill_name,
    difficulty,
    topics,
    previous_questions,
    batch_number,
):
    """Generate multiple MCQs in one Ollama request."""

    previous_text = "\n".join(
        f"- {str(question)[:300]}"
        for question in previous_questions[-20:]
        if question
    ) or "No previous questions."

    topic_text = "\n".join(
        f"{index + 1}. {topic}"
        for index, topic in enumerate(topics)
    )

    expected_count = len(topics)

    prompt = f"""
You are an expert technical examination question creator.

Generate EXACTLY {expected_count} different multiple-choice questions.

SKILL: {skill_name}
DIFFICULTY: {difficulty}

TOPICS:
{topic_text}

STRICT REQUIREMENTS:

1. Generate exactly {expected_count} questions.
2. Cover the supplied topics.
3. Every question must be technically accurate.
4. Each question must have exactly four complete options.
5. All four options must be different.
6. Exactly one option must be correct.
7. correct_answer must be an integer from 0 to 3.
8. Index 0 means the first option.
9. Index 1 means the second option.
10. Index 2 means the third option.
11. Index 3 means the fourth option.
12. Provide a technically correct explanation.
13. Do not use placeholder options like A, B, C, D.
14. Do not use "All of the above".
15. Do not use "None of the above".
16. Do not repeat previous questions.
17. Do not repeat the same question in this batch.
18. Make incorrect options plausible.
19. Preserve programming syntax in code questions.
20. Match the requested difficulty.
21. Return valid JSON only.
22. Do not use Markdown or code fences.

PREVIOUSLY USED QUESTIONS:
{previous_text}

IMPORTANT:
The explanation must identify and explain the option selected by
correct_answer. Check that both agree before returning the result.

Return this exact JSON structure:

{{
  "questions": [
    {{
      "question_text": "Complete question",
      "options": [
        "First actual answer",
        "Second actual answer",
        "Third actual answer",
        "Fourth actual answer"
      ],
      "correct_answer": 0,
      "explanation": "Explanation of the correct answer"
    }}
  ]
}}
"""

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "format": "json",
        "keep_alive": "10m",
        "options": {
            "temperature": 0.4,
            "num_predict": 4000,
            "num_ctx": 4096,
        },
    }

    request = urllib.request.Request(
        url=OLLAMA_BASE_URL.rstrip("/") + "/api/generate",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(
            request,
            timeout=300,
        ) as response:
            response_data = json.loads(
                response.read().decode("utf-8")
            )

        content = response_data.get("response")

        if not content:
            raise ValueError("Ollama returned an empty response.")

        result = json.loads(content)

        if not isinstance(result, dict):
            raise ValueError("Invalid batch response.")

        questions = result.get("questions")

        if (
            not isinstance(questions, list)
            or len(questions) != expected_count
        ):
            raise ValueError(
                f"Expected {expected_count} questions, "
                f"received {len(questions) if isinstance(questions, list) else 0}."
            )

        validated_questions = [
            _validate_question(item)
            for item in questions
        ]

        logger.info(
            "Ollama generated batch %s: %s questions for %s (%s).",
            batch_number,
            len(validated_questions),
            skill_name,
            difficulty,
        )

        return validated_questions

    except urllib.error.HTTPError as error:
        details = error.read().decode(
            "utf-8",
            errors="replace",
        )

        logger.error(
            "Ollama HTTP error %s: %s",
            error.code,
            details,
        )

        raise RuntimeError(
            f"Ollama returned HTTP error {error.code}."
        ) from error

    except urllib.error.URLError as error:
        logger.exception("Ollama connection failed.")

        raise RuntimeError(
            "Cannot connect to Ollama. "
            "Please make sure Ollama is running."
        ) from error


def generate_assessment_questions(
    skill_name,
    difficulty="intermediate",
    previous_questions=None,
):
    """
    Generate exactly 10 unique MCQs using Ollama.

    Generates five questions per request instead of
    making ten separate requests.
    """

    if (
        not isinstance(skill_name, str)
        or not skill_name.strip()
    ):
        raise ValueError("A valid skill name is required.")

    skill_name = skill_name.strip()

    difficulty = (
        difficulty or "intermediate"
    ).lower().strip()

    if difficulty not in [
        "beginner",
        "intermediate",
        "advanced",
    ]:
        raise ValueError("Invalid assessment difficulty.")

    previous_questions = previous_questions or []

    if not isinstance(previous_questions, list):
        raise ValueError("previous_questions must be a list.")

    used_questions = []

    for item in previous_questions:
        if isinstance(item, str):
            text = item
        elif isinstance(item, dict):
            text = item.get("question_text", "")
        else:
            continue

        if isinstance(text, str) and text.strip():
            used_questions.append(text.strip())

    if skill_name.casefold() == "python":
        topics = PYTHON_TOPICS.copy()
    else:
        topics = [
            f"{skill_name} fundamentals and practical applications: "
            f"topic {number}"
            for number in range(1, QUESTION_COUNT + 1)
        ]

    all_questions = []
    batch_number = 0

    while len(all_questions) < QUESTION_COUNT:
        batch_number += 1

        remaining = QUESTION_COUNT - len(all_questions)
        batch_count = min(BATCH_SIZE, remaining)

        start_index = len(all_questions)

        batch_topics = topics[
            start_index:start_index + batch_count
        ]

        # If duplicates were rejected, reuse the remaining
        # topics with a fresh request.
        if len(batch_topics) < batch_count:
            batch_topics = (
                batch_topics
                + topics[:batch_count - len(batch_topics)]
            )

        accepted_batch = False

        for attempt in range(1, MAX_BATCH_ATTEMPTS + 1):
            logger.info(
                "Generating batch %s, attempt %s, "
                "%s questions for %s (%s).",
                batch_number,
                attempt,
                batch_count,
                skill_name,
                difficulty,
            )

            try:
                generated = _generate_question_batch(
                    skill_name=skill_name,
                    difficulty=difficulty,
                    topics=batch_topics,
                    previous_questions=used_questions,
                    batch_number=batch_number,
                )

                new_questions = []

                for question in generated:
                    question_text = question["question_text"]

                    duplicate = any(
                        questions_are_similar(
                            question_text,
                            existing,
                        )
                        for existing in (
                            used_questions + [
                                item["question_text"]
                                for item in new_questions
                            ]
                        )
                    )

                    if duplicate:
                        logger.warning(
                            "Rejected duplicate question in batch %s.",
                            batch_number,
                        )
                        continue

                    new_questions.append(question)

                if len(new_questions) != batch_count:
                    raise ValueError(
                        "Batch contained duplicate questions. "
                        "Retrying the batch."
                    )

                all_questions.extend(new_questions)

                used_questions.extend(
                    question["question_text"]
                    for question in new_questions
                )

                accepted_batch = True

                logger.info(
                    "Batch %s accepted. Total questions: %s/%s.",
                    batch_number,
                    len(all_questions),
                    QUESTION_COUNT,
                )

                break

            except (
                ValueError,
                json.JSONDecodeError,
            ) as error:
                logger.warning(
                    "Batch %s attempt %s failed: %s",
                    batch_number,
                    attempt,
                    error,
                )

        if not accepted_batch:
            raise ValueError(
                f"Unable to generate a valid batch for "
                f"{skill_name} ({difficulty}) after "
                f"{MAX_BATCH_ATTEMPTS} attempts."
            )

    if len(all_questions) != QUESTION_COUNT:
        raise ValueError(
            f"Expected {QUESTION_COUNT} questions, "
            f"received {len(all_questions)}."
        )

    logger.info(
        "Successfully generated %s questions for %s (%s) using %s.",
        len(all_questions),
        skill_name,
        difficulty,
        OLLAMA_MODEL,
    )

    return all_questions
