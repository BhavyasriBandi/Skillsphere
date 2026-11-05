
import React from "react";
import "./Features.css";

const features = [
  {
    number: "01",
    icon: "◎",
    title: "Discover Your Skills",
    description:
      "Understand your strengths, assess your current abilities, and identify the skills you need for your dream career.",
    link: "Explore skill assessment",
  },
  {
    number: "02",
    icon: "↗",
    title: "Find Your Career Path",
    description:
      "Explore career opportunities that align with your interests, abilities, and long-term professional goals.",
    link: "Explore career paths",
  },
  {
    number: "03",
    icon: "✳",
    title: "Build Your Future",
    description:
      "Follow a personalized learning roadmap, develop practical skills, and track your progress along the way.",
    link: "Start learning",
  },
];

const faqs = [
  {
    question: "What is SkillSphere?",
    answer:
      "SkillSphere helps students understand their skills, explore career opportunities, and plan their learning journey.",
  },
  {
    question: "Who can use SkillSphere?",
    answer:
      "Students and mentors can use the platform according to their assigned roles. Administrators manage the platform through authorized accounts.",
  },
  {
    question: "How can SkillSphere help my career?",
    answer:
      "It helps you identify skill gaps, explore career paths, and organize your learning goals so you can work toward your professional ambitions.",
  },
  {
    question: "Is SkillSphere suitable for beginners?",
    answer:
      "Yes. You can begin by understanding your current skills and gradually work toward your learning and career goals.",
  },
];

function Features() {
  return (
    <>
      {/* Introduction */}
      <section className="features-intro" id="how-it-works">
        <span className="features-eyebrow">
          YOUR FUTURE, YOUR WAY
        </span>

        <h2>
          Turn your potential
          <br />
          into progress.
        </h2>

        <p>
          Every great career begins with understanding where you are
          and deciding where you want to go. SkillSphere helps you
          take the next step with confidence.
        </p>
      </section>

      {/* Core features */}
      <section className="features-section" id="features">
        <div className="features-heading">
          <div>
            <span className="features-eyebrow">
              THE SKILLSPHERE JOURNEY
            </span>

            <h2>A clearer path to your goals.</h2>
          </div>

          <p>
            Small steps today.
            <br />
            A stronger future tomorrow.
          </p>
        </div>

        <div className="features-grid">
          {features.map((feature) => (
            <article
              className="feature-card"
              key={feature.number}
            >
              <div className="feature-card-top">
                <span
                  className="feature-card-icon"
                  aria-hidden="true"
                >
                  {feature.icon}
                </span>

                <span className="feature-card-number">
                  {feature.number}
                </span>
              </div>

              <h3>{feature.title}</h3>

              <p className="feature-card-description">
                {feature.description}
              </p>

              <a
                className="feature-card-link"
                href="/register"
                aria-label={`${feature.link} - Get started with SkillSphere`}
              >
                {feature.link}
                <span aria-hidden="true"> →</span>
              </a>
            </article>
          ))}
        </div>
      </section>

      {/* Mentor banner */}
      <section className="mentor-banner" id="mentors">
        <div className="mentor-banner-content">
          <span className="features-eyebrow">
            GROW WITH GUIDANCE
          </span>

          <h2>
            You don't have to figure
            <br />
            it all out alone.
          </h2>

          <p>
            Learn with purpose, track your progress, and take your next
            career step with guidance from mentors.
          </p>
        </div>

        <a
          className="mentor-banner-button"
          href="/register"
        >
          Begin your journey
          <span aria-hidden="true"> →</span>
        </a>
      </section>

      {/* Frequently asked questions */}
      <section className="features-faq" id="faqs">
        <span className="features-eyebrow">
          HAVE QUESTIONS?
        </span>

        <h2>Your journey starts with a question.</h2>

        <div className="features-faq-list">
          {faqs.map((faq, index) => (
            <details
              className="features-faq-item"
              key={faq.question}
              open={false}
            >
              <summary>{faq.question}</summary>

              <p>{faq.answer}</p>
            </details>
          ))}
        </div>
      </section>
    </>
  );
}

export default Features;
