import React from "react";
import { Link } from "react-router-dom";
import "./Navbar.css";

function Navbar() {
  return (
    <header className="navbar">
      <Link className="navbar-brand" to="/">
        <span className="navbar-logo" aria-hidden="true">
          <svg
            viewBox="0 0 24 24"
            width="25"
            height="25"
            fill="none"
            stroke="currentColor"
            strokeWidth="1.8"
            strokeLinecap="round"
            strokeLinejoin="round"
          >
            <path d="M2 9.5 12 4l10 5.5L12 15 2 9.5Z" />
            <path d="M6 12v5c3.5 3 8.5 3 12 0v-5" />
            <path d="M22 10v6" />
          </svg>
        </span>

        <span>SkillSphere</span>
      </Link>

      <nav
        className="navbar-links"
        aria-label="Main navigation"
      >
        <a href="/#how-it-works">How it works</a>
        <a href="/#features">Explore features</a>
        <a href="/#mentors">For mentors</a>
        <a href="/#faqs">FAQs</a>
      </nav>

      <div className="navbar-actions">
        <Link className="navbar-login" to="/login">
          Log in
        </Link>

        <Link
          className="navbar-register"
          to="/register"
        >
          Get Started
        </Link>
      </div>
    </header>
  );
}

export default Navbar;