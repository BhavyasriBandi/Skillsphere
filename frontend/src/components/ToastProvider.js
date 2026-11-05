
import React, {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useRef,
  useState,
} from "react";

import "./Toast.css";

const ToastContext = createContext(null);

const TOAST_DURATION = 3000;

export function showToast(message, type = "success") {
  if (typeof window === "undefined") return;

  window.dispatchEvent(
    new CustomEvent("skillsphere:toast", {
      detail: {
        message: String(message ?? ""),
        type,
      },
    })
  );
}

export function useToast() {
  return useContext(ToastContext);
}

export default function ToastProvider({ children }) {
  const [toast, setToast] = useState(null);
  const timerRef = useRef(null);
  const idRef = useRef(0);

  const dismissToast = useCallback(() => {
    if (timerRef.current) {
      clearTimeout(timerRef.current);
      timerRef.current = null;
    }

    setToast(null);
  }, []);

  const displayToast = useCallback((message, type = "success") => {
    if (timerRef.current) {
      clearTimeout(timerRef.current);
    }

    const validTypes = ["success", "error", "warning", "info"];

    const safeType = validTypes.includes(type)
      ? type
      : "success";

    const item = {
      id: ++idRef.current,
      message: String(message ?? ""),
      type: safeType,
      duration: TOAST_DURATION,
    };

    setToast(item);

    timerRef.current = setTimeout(() => {
      setToast((current) =>
        current?.id === item.id ? null : current
      );

      timerRef.current = null;
    }, TOAST_DURATION);
  }, []);

  useEffect(() => {
    const handleToast = (event) => {
      displayToast(
        event.detail?.message,
        event.detail?.type || "success"
      );
    };

    window.addEventListener(
      "skillsphere:toast",
      handleToast
    );

    return () => {
      window.removeEventListener(
        "skillsphere:toast",
        handleToast
      );

      if (timerRef.current) {
        clearTimeout(timerRef.current);
        timerRef.current = null;
      }
    };
  }, [displayToast]);

  return (
    <ToastContext.Provider
      value={{
        showToast: displayToast,
        dismissToast,
      }}
    >
      {children}

      {toast && (
        <div
          key={toast.id}
          className={`skillsphere-toast toast-${toast.type}`}
          role={toast.type === "error" ? "alert" : "status"}
          aria-live={
            toast.type === "error" ? "assertive" : "polite"
          }
          style={{
            position: "fixed",
            top: "24px",
            right: "24px",
            bottom: "auto",
            left: "auto",
            zIndex: 100000,
          }}
        >
          <div className="skillsphere-toast-icon">
            {toast.type === "error"
              ? "!"
              : toast.type === "warning"
                ? "⚠"
                : toast.type === "info"
                  ? "i"
                  : "✓"}
          </div>

          <div className="skillsphere-toast-content">
            <span className="skillsphere-toast-title">
              {toast.type === "error"
                ? "Error"
                : toast.type === "warning"
                  ? "Warning"
                  : toast.type === "info"
                    ? "Information"
                    : "Success"}
            </span>

            <span className="skillsphere-toast-message">
              {toast.message}
            </span>
          </div>

          <button
            type="button"
            className="skillsphere-toast-close"
            onClick={dismissToast}
            aria-label="Close notification"
          >
            ×
          </button>

          <div
            key={toast.id}
            className="skillsphere-toast-progress"
            style={{
              animationDuration: `${toast.duration}ms`,
            }}
          />
        </div>
      )}
    </ToastContext.Provider>
  );
}
