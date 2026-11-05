
import React, { useEffect, useState } from "react";
import "./Toast.css";

let toastListeners = [];
let nextToastId = 0;

// Global toast support for other components
export function showToast(message, type = "success") {
  const toast = {
    id: ++nextToastId,
    message: String(message ?? ""),
    type,
  };

  toastListeners.forEach((listener) => listener(toast));
}

function subscribeToToast(listener) {
  toastListeners.push(listener);

  return () => {
    toastListeners = toastListeners.filter(
      (currentListener) => currentListener !== listener
    );
  };
}

export default function Toast({
  message,
  type = "success",
  onClose,
}) {
  const isControlled = message !== undefined;

  const [globalToast, setGlobalToast] = useState(null);

  // Listen to global toast calls when props are not supplied
  useEffect(() => {
    if (isControlled) return undefined;

    const unsubscribe = subscribeToToast((newToast) => {
      setGlobalToast(newToast);
    });

    return unsubscribe;
  }, [isControlled]);

  const activeToast = isControlled
    ? message
      ? {
          id: "controlled",
          message: String(message),
          type,
        }
      : null
    : globalToast;

  // Automatically close toast after 3.5 seconds
  useEffect(() => {
    if (!activeToast) return undefined;

    const timer = window.setTimeout(() => {
      if (isControlled) {
        onClose?.();
      } else {
        setGlobalToast((current) =>
          current?.id === activeToast.id ? null : current
        );
      }
    }, 3500);

    return () => window.clearTimeout(timer);
  }, [activeToast, isControlled, onClose]);

  if (!activeToast) return null;

  const toastType = [
    "success",
    "error",
    "warning",
    "info",
  ].includes(activeToast.type)
    ? activeToast.type
    : "success";

  const icons = {
    success: "✓",
    error: "✕",
    warning: "!",
    info: "i",
  };

  const titles = {
    success: "Success",
    error: "Error",
    warning: "Warning",
    info: "Information",
  };

  const handleClose = () => {
    if (isControlled) {
      onClose?.();
    } else {
      setGlobalToast(null);
    }
  };

  return (
    <div
      key={activeToast.id}
      className={`skillsphere-toast toast-${toastType}`}
      role={toastType === "error" ? "alert" : "status"}
      aria-live={toastType === "error" ? "assertive" : "polite"}
    >
      <div className="skillsphere-toast-icon">
        {icons[toastType]}
      </div>

      <div className="skillsphere-toast-content">
        <div className="skillsphere-toast-title">
          {titles[toastType]}
        </div>

        <div className="skillsphere-toast-message">
          {activeToast.message}
        </div>
      </div>

      <button
        type="button"
        className="skillsphere-toast-close"
        aria-label="Close notification"
        onClick={handleClose}
      >
        ×
      </button>

      <div
        key={activeToast.id}
        className="skillsphere-toast-progress"
      />
    </div>
  );
}
