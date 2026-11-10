
import React, { useEffect, useState } from "react";
import Toast, { showToast } from "./Toast";

const API_URL = "https://skillsphere-17hl.onrender.com/api/auth/profile/";

const emptyProfile = {
  fullName: "",
  email: "",
  phone: "",
  college: "",
  qualification: "",
  branch: "",
  graduationYear: "",
  location: "",
  careerInterest: "",
  bio: "",
};

function getRegisteredEmail() {
  try {
    return (
      sessionStorage.getItem("skillsphere_email") ||
      localStorage.getItem("skillsphere_saved_email") ||
      localStorage.getItem("email") ||
      ""
    );
  } catch {
    return "";
  }
}

function getAccessToken() {
  try {
    return (
      localStorage.getItem("skillsphere_access") ||
      localStorage.getItem("access") ||
      ""
    );
  } catch {
    return "";
  }
}

function getSavedProfile() {
  try {
    const saved = localStorage.getItem("skillsphere_student_profile");
    const parsed = saved ? JSON.parse(saved) : {};

    return {
      ...emptyProfile,
      ...(parsed && typeof parsed === "object" ? parsed : {}),
      email: getRegisteredEmail() || parsed?.email || "",
    };
  } catch {
    return {
      ...emptyProfile,
      email: getRegisteredEmail(),
    };
  }
}

function profileFromResponse(data, fallback = emptyProfile) {
  const source =
    data?.profile && typeof data.profile === "object"
      ? data.profile
      : data || {};

  const has = (key) =>
    Object.prototype.hasOwnProperty.call(source, key);

  const firstName = source.first_name || "";
  const lastName = source.last_name || "";

  let fullName = fallback.fullName || "";

  if (has("fullName")) {
    fullName = source.fullName || "";
  } else if (has("first_name") || has("last_name")) {
    fullName = `${firstName} ${lastName}`.trim();
  }

  return {
    fullName,
    email: has("email")
      ? source.email || ""
      : fallback.email || getRegisteredEmail(),

    phone: has("phone")
      ? source.phone ?? ""
      : fallback.phone || "",

    college: has("college")
      ? source.college ?? ""
      : fallback.college || "",

    qualification: has("qualification")
      ? source.qualification ?? ""
      : fallback.qualification || "",

    branch: has("branch")
      ? source.branch ?? ""
      : fallback.branch || "",

    graduationYear: has("graduationYear")
      ? source.graduationYear ?? ""
      : has("graduation_year")
        ? source.graduation_year ?? ""
        : fallback.graduationYear || "",

    location: has("location")
      ? source.location ?? ""
      : fallback.location || "",

    careerInterest: has("careerInterest")
      ? source.careerInterest ?? ""
      : has("career_interest")
        ? source.career_interest ?? ""
        : fallback.careerInterest || "",

    bio: has("bio")
      ? source.bio ?? ""
      : fallback.bio || "",
  };
}

function getInitials(name) {
  const cleanName = (name || "").trim();

  if (!cleanName) return "S";

  return cleanName
    .split(/\s+/)
    .slice(0, 2)
    .map((part) => part.charAt(0).toUpperCase())
    .join("");
}

function getErrorMessage(data, fallbackMessage) {
  if (data?.detail) return data.detail;
  if (data?.message) return data.message;

  if (data && typeof data === "object") {
    const messages = Object.values(data)
      .flat()
      .filter((item) => typeof item === "string");

    if (messages.length) return messages.join(" ");
  }

  return fallbackMessage;
}

function StudentProfile() {
  const [profile, setProfile] = useState(getSavedProfile);
  const [savedProfile, setSavedProfile] = useState(getSavedProfile);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);

  // Load the latest saved profile from Django.
  useEffect(() => {
    let cancelled = false;

    async function loadProfile() {
      const token = getAccessToken();

      if (!token) {
        if (!cancelled) {
          setLoading(false);
          showToast(
            "Please log in again to load your profile.",
            "error"
          );
        }
        return;
      }

      try {
        const response = await fetch(API_URL, {
          method: "GET",
          headers: {
            Authorization: `Bearer ${token}`,
            "Content-Type": "application/json",
          },
        });

        const data = await response.json().catch(() => ({}));

        if (!response.ok) {
          throw new Error(
            getErrorMessage(data, "Unable to load your profile.")
          );
        }

        if (cancelled) return;

        const updatedProfile = profileFromResponse(
          data,
          getSavedProfile()
        );

        setProfile(updatedProfile);
        setSavedProfile(updatedProfile);

        localStorage.setItem(
          "skillsphere_student_profile",
          JSON.stringify(updatedProfile)
        );
      } catch (error) {
        if (!cancelled) {
          showToast(
            error.message || "Unable to load your profile.",
            "error"
          );
        }
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    }

    loadProfile();

    return () => {
      cancelled = true;
    };
  }, []);

  function handleChange(event) {
    const { name, value } = event.target;

    setProfile((current) => ({
      ...current,
      [name]: value,
    }));
  }

  async function handleSave(event) {
    event.preventDefault();

    if (!profile.fullName.trim()) {
      showToast("Please enter your full name.", "warning");
      return;
    }

    if (
      profile.email &&
      !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(profile.email)
    ) {
      showToast("Please enter a valid email address.", "error");
      return;
    }

    if (profile.graduationYear) {
      const year = Number(profile.graduationYear);

      if (
        !Number.isInteger(year) ||
        year < 1990 ||
        year > 2100
      ) {
        showToast(
          "Please enter a valid graduation year.",
          "warning"
        );
        return;
      }
    }

    const token = getAccessToken();

    if (!token) {
      showToast(
        "Please log in again to update your profile.",
        "error"
      );
      return;
    }

    const nameParts = profile.fullName.trim().split(/\s+/);
    const firstName = nameParts.shift() || "";
    const lastName = nameParts.join(" ");

    const payload = {
      fullName: profile.fullName.trim(),
      first_name: firstName,
      last_name: lastName,
      phone: profile.phone,
      college: profile.college,
      qualification: profile.qualification,
      branch: profile.branch,
      graduationYear: profile.graduationYear,
      location: profile.location,
      careerInterest: profile.careerInterest,
      bio: profile.bio,
    };

    setSaving(true);

    try {
      const response = await fetch(API_URL, {
        method: "PATCH",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      const data = await response.json().catch(() => ({}));

      if (!response.ok) {
        throw new Error(
          getErrorMessage(data, "Unable to update your profile.")
        );
      }

      // Use the server response, preserving submitted values
      // if the response does not include a particular field.
      const updatedProfile = profileFromResponse(data, {
        ...profile,
        ...emptyProfile,
      });

      setProfile(updatedProfile);
      setSavedProfile(updatedProfile);

      localStorage.setItem(
        "skillsphere_student_profile",
        JSON.stringify(updatedProfile)
      );

      showToast(
        data.message || "Profile updated successfully!",
        "success"
      );
    } catch (error) {
      showToast(
        error.message || "Unable to update your profile.",
        "error"
      );
    } finally {
      setSaving(false);
    }
  }

  function handleReset() {
    setProfile({ ...savedProfile });
    showToast(
      "Your saved profile has been restored.",
      "info"
    );
  }

  const initials = getInitials(profile.fullName);
  const registeredEmail = getRegisteredEmail();

  return (
    <section className="student-profile-page">
      <Toast />

      <div className="profile-page-heading">
        <div>
          <span className="eyebrow">YOUR ACCOUNT</span>
          <h1>My Profile</h1>
          <p>
            Manage your personal details and career information.
          </p>
        </div>

        <div className="profile-heading-avatar">{initials}</div>
      </div>

      <div className="profile-summary-card">
        <div className="profile-summary-avatar">{initials}</div>

        <div className="profile-summary-details">
          <h2>{profile.fullName.trim() || "Your Name"}</h2>
          <p>{profile.email || "Add your email address"}</p>
          <span className="profile-account-badge">
            Student Account
          </span>
        </div>
      </div>

      {loading ? (
        <div className="profile-form-card">
          <p>Loading your profile...</p>
        </div>
      ) : (
        <form
          className="student-profile-form"
          onSubmit={handleSave}
        >
          <section className="profile-form-card">
            <div className="profile-card-heading">
              <div className="profile-card-icon">◉</div>
              <div>
                <h2>Personal Information</h2>
                <p>Keep your contact details up to date.</p>
              </div>
            </div>

            <div className="profile-form-grid">
              <div className="profile-field">
                <label htmlFor="profile-fullName">Full Name</label>
                <input
                  id="profile-fullName"
                  type="text"
                  name="fullName"
                  placeholder="Enter your full name"
                  value={profile.fullName}
                  onChange={handleChange}
                  maxLength={100}
                />
              </div>

              <div className="profile-field">
                <label htmlFor="profile-email">Email Address</label>
                <input
                  id="profile-email"
                  type="email"
                  name="email"
                  placeholder="Enter your email address"
                  value={profile.email}
                  onChange={handleChange}
                  readOnly={Boolean(registeredEmail)}
                />
              </div>

              <div className="profile-field">
                <label htmlFor="profile-phone">Phone Number</label>
                <input
                  id="profile-phone"
                  type="tel"
                  name="phone"
                  placeholder="Enter your phone number"
                  value={profile.phone}
                  onChange={handleChange}
                  maxLength={20}
                />
              </div>

              <div className="profile-field">
                <label htmlFor="profile-location">Location</label>
                <input
                  id="profile-location"
                  type="text"
                  name="location"
                  placeholder="City, State"
                  value={profile.location}
                  onChange={handleChange}
                  maxLength={100}
                />
              </div>
            </div>
          </section>

          <section className="profile-form-card">
            <div className="profile-card-heading">
              <div className="profile-card-icon">▤</div>
              <div>
                <h2>Education Details</h2>
                <p>Tell us about your academic background.</p>
              </div>
            </div>

            <div className="profile-form-grid">
              <div className="profile-field">
                <label htmlFor="profile-college">
                  College / University
                </label>
                <input
                  id="profile-college"
                  type="text"
                  name="college"
                  placeholder="Enter your college name"
                  value={profile.college}
                  onChange={handleChange}
                  maxLength={150}
                />
              </div>

              <div className="profile-field">
                <label htmlFor="profile-qualification">
                  Qualification
                </label>
                <select
                  id="profile-qualification"
                  name="qualification"
                  value={profile.qualification}
                  onChange={handleChange}
                >
                  <option value="">Select qualification</option>
                  <option value="Intermediate">Intermediate</option>
                  <option value="Diploma">Diploma</option>
                  <option value="B.Tech">B.Tech</option>
                  <option value="B.E.">B.E.</option>
                  <option value="B.Sc">B.Sc</option>
                  <option value="B.Com">B.Com</option>
                  <option value="BCA">BCA</option>
                  <option value="MCA">MCA</option>
                  <option value="M.Tech">M.Tech</option>
                  <option value="Other">Other</option>
                </select>
              </div>

              <div className="profile-field">
                <label htmlFor="profile-branch">
                  Branch / Specialization
                </label>
                <input
                  id="profile-branch"
                  type="text"
                  name="branch"
                  placeholder="e.g. Computer Science"
                  value={profile.branch}
                  onChange={handleChange}
                  maxLength={100}
                />
              </div>

              <div className="profile-field">
                <label htmlFor="profile-graduationYear">
                  Graduation Year
                </label>
                <input
                  id="profile-graduationYear"
                  type="number"
                  name="graduationYear"
                  placeholder="e.g. 2027"
                  min="1990"
                  max="2100"
                  value={profile.graduationYear}
                  onChange={handleChange}
                />
              </div>
            </div>
          </section>

          <section className="profile-form-card">
            <div className="profile-card-heading">
              <div className="profile-card-icon">↗</div>
              <div>
                <h2>Career Information</h2>
                <p>
                  Share your interests and career aspirations.
                </p>
              </div>
            </div>

            <div className="profile-form-grid">
              <div className="profile-field profile-field-full">
                <label htmlFor="profile-careerInterest">
                  Career Interest
                </label>
                <select
                  id="profile-careerInterest"
                  name="careerInterest"
                  value={profile.careerInterest}
                  onChange={handleChange}
                >
                  <option value="">
                    Select your career interest
                  </option>
                  <option value="Software Developer">
                    Software Developer
                  </option>
                  <option value="Full Stack Developer">
                    Full Stack Developer
                  </option>
                  <option value="Data Scientist">
                    Data Scientist
                  </option>
                  <option value="AI / ML Engineer">
                    AI / ML Engineer
                  </option>
                  <option value="Web Developer">
                    Web Developer
                  </option>
                  <option value="Cybersecurity">
                    Cybersecurity
                  </option>
                  <option value="Cloud Engineer">
                    Cloud Engineer
                  </option>
                  <option value="Other">Other</option>
                </select>
              </div>

              <div className="profile-field profile-field-full">
                <label htmlFor="profile-bio">About Me</label>
                <textarea
                  id="profile-bio"
                  name="bio"
                  placeholder="Write a short introduction about yourself, your skills, and your goals..."
                  rows={4}
                  value={profile.bio}
                  onChange={handleChange}
                  maxLength={500}
                />

                <small className="profile-character-count">
                  {profile.bio.length}/500 characters
                </small>
              </div>
            </div>
          </section>

          <div className="profile-form-actions">
            <button
              type="button"
              className="profile-reset-button"
              onClick={handleReset}
              disabled={saving}
            >
              Reset Changes
            </button>

            <button
              type="submit"
              className="profile-save-button"
              disabled={saving}
            >
              <span aria-hidden="true">✓</span>{" "}
              {saving ? "Saving..." : "Save Changes"}
            </button>
          </div>
        </form>
      )}
    </section>
  );
}

export default StudentProfile;
