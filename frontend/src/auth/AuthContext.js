
import React, {
  createContext,
  useContext,
  useEffect,
  useState,
  useCallback,
} from "react";

export const API_BASE_URL = "https://skillsphere-u93o.onrender.com";

const ACCESS_KEY = "skillsphere_access";
const REFRESH_KEY = "skillsphere_refresh";
const USER_KEY = "skillsphere_user";

const AuthContext = createContext(null);


// =====================================================
// READ API RESPONSE
// =====================================================

async function readResponse(response) {
  const data = await response.json().catch(() => ({}));

  if (!response.ok) {
    throw new Error(
      data.detail ||
        data.message ||
        data.error ||
        `Request failed with status ${response.status}.`
    );
  }

  return data;
}


// =====================================================
// GET STORED TOKENS
// =====================================================

function getStoredRefreshToken() {
  return (
    localStorage.getItem(REFRESH_KEY) ||
    localStorage.getItem("refresh") ||
    ""
  );
}

function getStoredAccessToken() {
  return (
    localStorage.getItem(ACCESS_KEY) ||
    localStorage.getItem("access") ||
    ""
  );
}


// =====================================================
// SAVE TOKENS
// =====================================================

function saveAccessToken(token) {
  localStorage.setItem(ACCESS_KEY, token);
  localStorage.setItem("access", token);
}

function saveRefreshToken(token) {
  localStorage.setItem(REFRESH_KEY, token);
  localStorage.setItem("refresh", token);
}

function saveUser(user) {
  localStorage.setItem(USER_KEY, JSON.stringify(user));
}


// =====================================================
// CLEAR SESSION
// =====================================================

function clearSession() {
  [
    ACCESS_KEY,
    REFRESH_KEY,
    USER_KEY,
    "access",
    "refresh",
    "user",
  ].forEach((key) => localStorage.removeItem(key));

  sessionStorage.removeItem("skillsphere_email");
}


// =====================================================
// REFRESH ACCESS TOKEN
// =====================================================

export async function refreshAccessToken() {
  const refreshToken = getStoredRefreshToken();

  if (!refreshToken) {
    throw new Error("No refresh token found. Please log in again.");
  }

  const response = await fetch(
    `${API_BASE_URL}/api/auth/token/refresh/`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        refresh: refreshToken,
      }),
    }
  );

  const data = await response.json().catch(() => ({}));

  if (!response.ok || !data.access) {
    throw new Error(
      data.detail ||
        data.message ||
        "Your session has expired. Please log in again."
    );
  }

  saveAccessToken(data.access);

  if (data.refresh) {
    saveRefreshToken(data.refresh);
  }

  return data.access;
}


// =====================================================
// FETCH CURRENT USER
// =====================================================

async function fetchCurrentUser(token) {
  const response = await fetch(`${API_BASE_URL}/api/auth/me/`, {
    method: "GET",
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json",
    },
  });

  return readResponse(response);
}


// =====================================================
// AUTHENTICATED API REQUEST
// =====================================================

export async function apiFetch(path, options = {}) {
  let token = getStoredAccessToken();

  if (!token) {
    throw new Error("You are not logged in. Please log in again.");
  }

  const makeRequest = (accessToken) => {
    const headers = new Headers(options.headers || {});

    headers.set("Authorization", `Bearer ${accessToken}`);

    if (
      options.body &&
      !(options.body instanceof FormData) &&
      !headers.has("Content-Type")
    ) {
      headers.set("Content-Type", "application/json");
    }

    return fetch(
      path.startsWith("http") ? path : `${API_BASE_URL}${path}`,
      {
        ...options,
        headers,
      }
    );
  };

  let response = await makeRequest(token);

  if (response.status !== 401) {
    return response;
  }

  token = await refreshAccessToken();

  response = await makeRequest(token);

  if (response.status === 401) {
    throw new Error(
      "Authentication failed after refreshing the token. Please log in again."
    );
  }

  return response;
}


// =====================================================
// GET USER ROLE
// =====================================================

export function getUserRole(user) {
  if (!user) return null;

  const candidates = [
    user.role,
    user.user_role,
    user.user_type,
  ];

  if (Array.isArray(user.groups)) {
    candidates.push(
      ...user.groups.map((group) =>
        typeof group === "string" ? group : group?.name
      )
    );
  } else if (typeof user.groups === "string") {
    candidates.push(user.groups);
  }

  for (const candidate of candidates) {
    if (typeof candidate !== "string") continue;

    const role = candidate.trim().toLowerCase();

    if (["admin", "administrator"].includes(role)) {
      return "admin";
    }

    if (role === "mentor") {
      return "mentor";
    }

    if (role === "student") {
      return "student";
    }
  }

  if (user.is_superuser === true || user.is_staff === true) {
    return "admin";
  }

  return null;
}


// =====================================================
// GET DASHBOARD PATH
// =====================================================

export function getDashboardPath(roleOrUser) {
  const role =
    typeof roleOrUser === "string"
      ? roleOrUser.trim().toLowerCase()
      : getUserRole(roleOrUser);

  if (role === "student") return "/student/dashboard";

  if (role === "mentor") return "/mentor/dashboard";

  if (["admin", "administrator"].includes(role)) {
    return "/admin/dashboard";
  }

  return null;
}


// =====================================================
// AUTH PROVIDER
// =====================================================

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [accessToken, setAccessToken] = useState("");
  const [loading, setLoading] = useState(true);


  // ===================================================
  // RESTORE SESSION
  // ===================================================

  const restoreSession = useCallback(async () => {
    setLoading(true);

    let token = getStoredAccessToken();

    if (!token) {
      setUser(null);
      setAccessToken("");
      setLoading(false);
      return;
    }

    try {
      let currentUser;

      try {
        currentUser = await fetchCurrentUser(token);
      } catch (error) {
        if (
          error.message.toLowerCase().includes("token") ||
          error.message.toLowerCase().includes("authentication") ||
          error.message.includes("401")
        ) {
          token = await refreshAccessToken();
          currentUser = await fetchCurrentUser(token);
        } else {
          throw error;
        }
      }

      saveUser(currentUser);
      setUser(currentUser);
      setAccessToken(token);
    } catch (error) {
      console.error(
        "SkillSphere session restoration failed:",
        error.message
      );

      clearSession();
      setUser(null);
      setAccessToken("");
    } finally {
      setLoading(false);
    }
  }, []);


  // ===================================================
  // INITIALIZE SESSION
  // ===================================================

  useEffect(() => {
    let active = true;

    async function initialize() {
      let token = getStoredAccessToken();

      if (!token) {
        if (active) {
          setUser(null);
          setAccessToken("");
          setLoading(false);
        }

        return;
      }

      try {
        let currentUser;

        try {
          currentUser = await fetchCurrentUser(token);
        } catch (error) {
          if (!active) return;

          token = await refreshAccessToken();
          currentUser = await fetchCurrentUser(token);
        }

        if (active) {
          saveUser(currentUser);
          setUser(currentUser);
          setAccessToken(token);
        }
      } catch (error) {
        console.error(
          "SkillSphere session restoration failed:",
          error.message
        );

        if (active) {
          clearSession();
          setUser(null);
          setAccessToken("");
        }
      } finally {
        if (active) {
          setLoading(false);
        }
      }
    }

    initialize();

    return () => {
      active = false;
    };
  }, []);


  // ===================================================
  // LOGIN
  // ===================================================

  const login = useCallback(async (email, password) => {
    const response = await fetch(`${API_BASE_URL}/api/auth/login/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email: email.trim(),
        password,
      }),
    });

    const data = await readResponse(response);

    if (!data.access) {
      throw new Error(
        "Login succeeded, but the response has no access token."
      );
    }

    saveAccessToken(data.access);

    if (data.refresh) {
      saveRefreshToken(data.refresh);
    } else {
      localStorage.removeItem(REFRESH_KEY);
      localStorage.removeItem("refresh");
    }

    setAccessToken(data.access);

    try {
      const currentUser = data.user || await fetchCurrentUser(data.access);

      saveUser(currentUser);
      setUser(currentUser);

      return currentUser;
    } catch (error) {
      console.error(
        "SkillSphere could not load the current user:",
        error.message
      );

      throw new Error(
        `Login returned a token, but loading your profile failed: ${error.message}`
      );
    }
  }, []);


  // ===================================================
  // LOGOUT - BACKEND REFRESH TOKEN BLACKLIST
  // ===================================================

  const logout = useCallback(async () => {
    const refreshToken = getStoredRefreshToken();
    const currentAccessToken = getStoredAccessToken();

    try {
      if (refreshToken && currentAccessToken) {
        const response = await fetch(
          `${API_BASE_URL}/api/auth/logout/`,
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              Authorization: `Bearer ${currentAccessToken}`,
            },
            body: JSON.stringify({
              refresh: refreshToken,
            }),
          }
        );

        const data = await response.json().catch(() => ({}));

        if (!response.ok) {
          console.error(
            "Backend logout failed:",
            data.detail || response.status
          );
        } else {
          console.log("SkillSphere backend logout successful.");
        }
      }
    } catch (error) {
      console.error("Logout request failed:", error);
    } finally {
      clearSession();
      setAccessToken("");
      setUser(null);
      setLoading(false);
    }
  }, []);


  // ===================================================
  // AUTH CONTEXT VALUE
  // ===================================================

  const value = {
    user,
    accessToken,
    loading,
    isAuthenticated: Boolean(accessToken),
    role: getUserRole(user),
    login,
    logout,
    restoreSession,
    apiFetch,
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
}


// =====================================================
// USE AUTH
// =====================================================

export function useAuth() {
  const context = useContext(AuthContext);

  if (!context) {
    throw new Error(
      "useAuth must be used inside an AuthProvider."
    );
  }

  return context;
}
