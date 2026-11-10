
const API_URL = "https://skillsphere-u93o.onrender.com/api/progress/challenges/";

const TOKEN_KEY = "skillsphere_access";
const FALLBACK_TOKEN_KEY = "access";

// Get JWT authentication headers
function getAuthHeaders() {
  const token =
    localStorage.getItem(TOKEN_KEY) ||
    localStorage.getItem(FALLBACK_TOKEN_KEY);

  if (!token) {
    throw new Error(
      "Your session has expired. Please log in again."
    );
  }

  return {
    "Content-Type": "application/json",
    Authorization: `Bearer ${token}`,
  };
}

// Handle API responses
async function handleResponse(response) {
  if (response.status === 401) {
    throw new Error(
      "Your session has expired. Please log in again."
    );
  }

  if (response.status === 403) {
    throw new Error(
      "You do not have permission to access challenge progress."
    );
  }

  if (response.status === 404) {
    throw new Error(
      "Challenge progress API endpoint was not found."
    );
  }

  if (!response.ok) {
    let message;

    try {
      const data = await response.json();

      message =
        data.detail ||
        data.message ||
        JSON.stringify(data);
    } catch {
      message = await response.text();
    }

    throw new Error(
      `Challenge API error (${response.status}): ${message}`
    );
  }

  if (response.status === 204) {
    return {};
  }

  const contentType =
    response.headers.get("content-type") || "";

  if (!contentType.includes("application/json")) {
    return {};
  }

  return response.json();
}

// Normalize progress returned by backend
function normalizeProgress(data) {
  const ids = Array.isArray(data?.completedIds)
    ? data.completedIds
    : Array.isArray(data?.completed_ids)
      ? data.completed_ids
      : [];

  return {
    completedIds: [
      ...new Set(
        ids
          .map(Number)
          .filter(
            (id) => Number.isInteger(id) && id > 0
          )
      ),
    ],
  };
}

// GET: Retrieve logged-in student's challenge progress
export async function getChallengeProgress() {
  try {
    const response = await fetch(API_URL, {
      method: "GET",
      headers: getAuthHeaders(),
    });

    const data = await handleResponse(response);

    return normalizeProgress(data);
  } catch (error) {
    console.error(
      "Get challenge progress error:",
      error
    );

    throw error;
  }
}

// PATCH: Save logged-in student's completed challenges
export async function saveChallengeProgress(completedIds) {
  try {
    if (!Array.isArray(completedIds)) {
      throw new Error(
        "Invalid challenge progress data."
      );
    }

    const normalizedIds = [
      ...new Set(
        completedIds
          .map(Number)
          .filter(
            (id) => Number.isInteger(id) && id > 0
          )
      ),
    ];

    const response = await fetch(API_URL, {
      method: "PATCH",
      headers: getAuthHeaders(),
      body: JSON.stringify({
        completed_ids: normalizedIds,
      }),
    });

    const data = await handleResponse(response);

    if (
      !Array.isArray(data?.completedIds) &&
      !Array.isArray(data?.completed_ids)
    ) {
      return {
        completedIds: normalizedIds,
      };
    }

    return normalizeProgress(data);
  } catch (error) {
    console.error(
      "Save challenge progress error:",
      error
    );

    throw error;
  }
}
