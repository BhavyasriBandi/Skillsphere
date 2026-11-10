
const API_URL = "https://skillsphere-u93o.onrender.com/api/progress/learning-hub/";

function getAuthHeaders() {
  // SkillSphere JWT access token
  const token =
    localStorage.getItem("skillsphere_access") ||
    localStorage.getItem("access");

  if (!token) {
    throw new Error("Your session has expired. Please log in again.");
  }

  return {
    "Content-Type": "application/json",
    Authorization: `Bearer ${token}`,
  };
}

async function handleResponse(response) {
  if (response.status === 401) {
    throw new Error("Your session has expired. Please log in again.");
  }

  if (!response.ok) {
    const errorText = await response.text();

    throw new Error(
      `Learning Hub request failed (${response.status}). ${errorText}`
    );
  }

  if (response.status === 204) {
    return {};
  }

  return response.json();
}

export async function getLearningHubProgress() {
  const response = await fetch(API_URL, {
    method: "GET",
    headers: getAuthHeaders(),
  });

  const data = await handleResponse(response);

  return {
    completedLessons: Array.isArray(data.completedLessons)
      ? data.completedLessons
      : [],
    savedCourses: Array.isArray(data.savedCourses)
      ? data.savedCourses
      : [],
  };
}

export async function saveLearningHubProgress(progress) {
  const response = await fetch(API_URL, {
    method: "PATCH",
    headers: getAuthHeaders(),
    body: JSON.stringify({
      completedLessons: progress.completedLessons,
      savedCourses: progress.savedCourses,
    }),
  });

  return handleResponse(response);
}
