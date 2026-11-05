
import React from "react";
import "./Panel.css";

function Panel({
  title,
  subtitle,
  action,
  icon,
  variant = "default",
  className = "",
  children,
}) {
  return (
    <section
      className={`ss-panel ss-panel--${variant} ${className}`.trim()}
    >
      {(title || subtitle || action || icon) && (
        <header className="ss-panel-header">
          <div className="ss-panel-heading">
            {icon && (
              <span className="ss-panel-icon" aria-hidden="true">
                {icon}
              </span>
            )}

            <div>
              {title && <h2 className="ss-panel-title">{title}</h2>}

              {subtitle && (
                <p className="ss-panel-subtitle">{subtitle}</p>
              )}
            </div>
          </div>

          {action && (
            <div className="ss-panel-action">
              {action}
            </div>
          )}
        </header>
      )}

      <div className="ss-panel-content">{children}</div>
    </section>
  );
}

export default Panel;
