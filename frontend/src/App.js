
import React, { useEffect, useState } from "react";
import AppRoutes from "./routes/AppRoutes";
import { AuthProvider } from "./auth/AuthContext";
import "./App.css";

const SETTINGS_KEY = "skillsphere_student_settings";

function getSavedTheme() {
  try {
    const saved = JSON.parse(
      localStorage.getItem(SETTINGS_KEY) || "{}"
    );

    return saved.theme === "dark" ? "dark" : "light";
  } catch {
    return "light";
  }
}

function App() {
  const [theme, setTheme] = useState(getSavedTheme);

  useEffect(() => {
    const applyTheme = (nextTheme) => {
      const selectedTheme =
        nextTheme === "dark" ? "dark" : "light";

      document.documentElement.setAttribute(
        "data-theme",
        selectedTheme
      );

      document.body.setAttribute(
        "data-theme",
        selectedTheme
      );

      setTheme(selectedTheme);
    };

    // Initial theme
    applyTheme(getSavedTheme());

    // Same-tab theme changes
    const handleThemeChange = (event) => {
      const newTheme =
        event.detail?.theme || getSavedTheme();

      applyTheme(newTheme);
    };

    // Other-tab theme changes
    const handleStorageChange = (event) => {
      if (
        event.key === SETTINGS_KEY ||
        event.key === null
      ) {
        applyTheme(getSavedTheme());
      }
    };

    window.addEventListener(
      "skillsphere-theme-change",
      handleThemeChange
    );

    window.addEventListener(
      "storage",
      handleStorageChange
    );

    return () => {
      window.removeEventListener(
        "skillsphere-theme-change",
        handleThemeChange
      );

      window.removeEventListener(
        "storage",
        handleStorageChange
      );
    };
  }, []);

  return (
    <AuthProvider>
      <div
        className="skillsphere-app"
        data-theme={theme}
      >
        <AppRoutes />
      </div>
    </AuthProvider>
  );
}

export default App;
