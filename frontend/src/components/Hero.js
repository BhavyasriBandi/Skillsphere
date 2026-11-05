
import React from "react";
import "./Hero.css";

function Hero() {
  return (
    <section className="hero-section" id="home">
      <div className="hero-content">
        <div className="hero-eyebrow">
          <span className="hero-eyebrow-dot"></span>
          A PURPOSEFUL PATH TO YOUR CAREER
        </div>

        <h1 className="hero-title">
          Know Your Skills.
          <br />
          Shape Your
          <br />
          <span>Future.</span>
        </h1>

        <p className="hero-description">
          Discover where you stand, choose where you want to go,
          and build the skills to get there—with a personalized
          roadmap and a mentor by your side.
        </p>

        <div className="hero-trust-note">
          <span className="hero-trust-icon" aria-hidden="true">
            ✓
          </span>
          Your skills. Your goals. Your future.
        </div>
      </div>

      <div className="hero-visual">
        <div className="hero-image-wrapper">
          <img
            className="hero-image"
            src="https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=1200&q=85"
            alt="Students collaborating and learning together"
          />

          <div className="hero-image-overlay"></div>
        </div>

        <div className="hero-floating-card">
          <div className="hero-card-icon" aria-hidden="true">
            ✦
          </div>

          <div className="hero-card-content">
            <span className="hero-card-label">
              YOUR NEXT CHAPTER
            </span>

            <h2>From curiosity to career readiness.</h2>

            <div className="hero-card-steps">
              <span>Assess</span>
              <span className="hero-step-arrow" aria-hidden="true">
                →
              </span>
              <span>Learn</span>
              <span className="hero-step-arrow" aria-hidden="true">
                →
              </span>
              <span>Grow</span>
            </div>
          </div>
        </div>

        <div
          className="hero-decoration hero-decoration-one"
          aria-hidden="true"
        ></div>

        <div
          className="hero-decoration hero-decoration-two"
          aria-hidden="true"
        ></div>
      </div>
    </section>
  );
}

export default Hero;
