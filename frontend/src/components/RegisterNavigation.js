
import React from "react";
import "./RegisterNavigation.css";

function RegisterNavigation() {
  return (
    <div className="register-navigation">
      <a
        className="register-brand"
        href="/"
        aria-label="Return to SkillSphere home"
      >
        <span className="register-brand-icon" aria-hidden="true">
          ✦
        </span>
        <span>SkillSphere</span>
      </a>

      <a className="register-home-link" href="/">
        <span aria-hidden="true">←</span>
        Back to Home
      </a>
    </div>
  );
}

export default RegisterNavigation;
