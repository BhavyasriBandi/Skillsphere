
import React, { useCallback, useEffect, useState } from "react";
import "./MentorProfile.css";

const API_BASE_URL = "http://127.0.0.1:8000";

const initialProfile = {
  phone: "",
  location: "",
  qualification: "",
  college: "",
  specialization: "",
  expertise: "",
  skills: "",
  experience: 0,
  bio: "",
};

function MentorProfile() {
  const [profile, setProfile] = useState(initialProfile);
  const [originalProfile, setOriginalProfile] = useState(initialProfile);
  const [mentorName, setMentorName] = useState("");
  const [email, setEmail] = useState("");

  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const [toastKey, setToastKey] = useState(0);
  const [isEditing, setIsEditing] = useState(false);

  useEffect(() => {
    if (!success && !error) return;

    const timer = setTimeout(() => {
      setSuccess("");
      setError("");
    }, 3000);

    return () => clearTimeout(timer);
  }, [success, error, toastKey]);

  const fetchProfile = useCallback(async () => {
    try {
      setLoading(true);
      setError("");

      const token = localStorage.getItem("skillsphere_access");
      if (!token) {
        throw new Error("Access token not found. Please login again.");
      }

      const response = await fetch(`${API_BASE_URL}/api/mentors/profile/`, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || data.message || "Unable to load mentor profile."
        );
      }

      const loadedProfile = {
        phone: data.phone || "",
        location: data.location || "",
        qualification: data.qualification || "",
        college: data.college || "",
        specialization: data.specialization || "",
        expertise: data.expertise || "",
        skills: data.skills || "",
        experience: data.experience ?? 0,
        bio: data.bio || "",
      };

      setMentorName(data.mentor_name || "");
      setEmail(data.email || "");
      setProfile(loadedProfile);
      setOriginalProfile(loadedProfile);
    } catch (err) {
      setError(err.message || "Something went wrong.");
      setToastKey((previous) => previous + 1);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchProfile();
  }, [fetchProfile]);

  const showSuccessToast = (message) => {
    setError("");
    setSuccess(message);
    setToastKey((previous) => previous + 1);
  };

  const showErrorToast = (message) => {
    setSuccess("");
    setError(message);
    setToastKey((previous) => previous + 1);
  };

  const handleEditOpen = () => {
    setProfile({ ...originalProfile });
    setError("");
    setSuccess("");
    setIsEditing(true);
  };

  const handleChange = (event) => {
    const { name, value } = event.target;

    setProfile((previous) => ({
      ...previous,
      [name]: value,
    }));
  };

  const handleCancel = () => {
    setProfile({ ...originalProfile });
    setIsEditing(false);
    setError("");
  };

  const handleSave = async (event) => {
    event.preventDefault();

    try {
      setSaving(true);
      setError("");

      const token = localStorage.getItem("skillsphere_access");
      if (!token) {
        throw new Error("Access token not found. Please login again.");
      }

      const payload = {
        ...profile,
        experience: Number(profile.experience),
      };

      const response = await fetch(`${API_BASE_URL}/api/mentors/profile/`, {
        method: "PATCH",
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      const data = await response.json();

      if (!response.ok) {
        const validationMessage =
          typeof data === "object"
            ? Object.entries(data)
                .map(([field, messages]) => {
                  const detail = Array.isArray(messages)
                    ? messages.join(", ")
                    : String(messages);
                  return `${field}: ${detail}`;
                })
                .join(" | ")
            : "Unable to save profile.";

        throw new Error(
          data.detail || data.message || validationMessage
        );
      }

      const savedProfile = data.profile || data;

      const updatedProfile = {
        phone: savedProfile.phone ?? payload.phone,
        location: savedProfile.location ?? payload.location,
        qualification: savedProfile.qualification ?? payload.qualification,
        college: savedProfile.college ?? payload.college,
        specialization: savedProfile.specialization ?? payload.specialization,
        expertise: savedProfile.expertise ?? payload.expertise,
        skills: savedProfile.skills ?? payload.skills,
        experience: savedProfile.experience ?? payload.experience,
        bio: savedProfile.bio ?? payload.bio,
      };

      setProfile(updatedProfile);
      setOriginalProfile(updatedProfile);
      setIsEditing(false);

      showSuccessToast(data.message || "Profile updated successfully!");
    } catch (err) {
      showErrorToast(err.message || "Unable to save profile.");
    } finally {
      setSaving(false);
    }
  };

  const closeToast = () => {
    setSuccess("");
    setError("");
  };

  const initials = (mentorName || "Mentor")
    .split(" ")
    .filter(Boolean)
    .map((part) => part.charAt(0))
    .join("")
    .slice(0, 2)
    .toUpperCase();

  const displayValue = (value) =>
    value !== undefined && value !== null && String(value).trim() !== ""
      ? value
      : "Not provided";

  if (loading) {
    return (
      <section className="mentor-profile-content">
        <div className="mentor-profile-message">Loading your profile...</div>
      </section>
    );
  }

  if (error && !email && !mentorName) {
    return (
      <section className="mentor-profile-content">
        <div className="mentor-profile-message">
          <h3>Unable to load profile</h3>
          <p>{error}</p>
          <button type="button" onClick={fetchProfile}>
            Try Again
          </button>
        </div>
      </section>
    );
  }

  return (
    <section className="mentor-profile-content">
      {success && (
        <div className="mentor-profile-toast success" role="status">
          <span className="mentor-toast-icon">✓</span>
          <div className="mentor-toast-text">
            <strong>SUCCESS</strong>
            <p>{success}</p>
          </div>
          <button type="button" onClick={closeToast} aria-label="Close">
            ×
          </button>
          <div className="mentor-toast-progress success-progress" />
        </div>
      )}

      {error && (
        <div className="mentor-profile-toast error" role="alert">
          <span className="mentor-toast-icon">!</span>
          <div className="mentor-toast-text">
            <strong>ERROR</strong>
            <p>{error}</p>
          </div>
          <button type="button" onClick={closeToast} aria-label="Close">
            ×
          </button>
          <div className="mentor-toast-progress error-progress" />
        </div>
      )}

      <div className="mentor-profile-heading">
        <div>
          <h1>My Profile</h1>
          <p>Manage your professional information and mentor details.</p>
        </div>

        <button
          type="button"
          className="mentor-profile-edit-button"
          onClick={handleEditOpen}
        >
          ✏️ Edit Profile
        </button>
      </div>

      <div className="mentor-profile-card">
        <div className="mentor-profile-banner">
          <div className="mentor-profile-avatar">{initials}</div>
          <div className="mentor-profile-identity">
            <h2>{mentorName || "Mentor"}</h2>
            <p>{email}</p>
            <span>Mentor</span>
          </div>
        </div>

        <div className="mentor-profile-section">
          <div className="mentor-profile-section-title">
            <h3>Personal Information</h3>
            <p>Your contact and personal details</p>
          </div>

          <div className="mentor-profile-grid">
            <div className="mentor-profile-field">
              <label>Full Name</label>
              <div className="mentor-profile-value">{displayValue(mentorName)}</div>
            </div>
            <div className="mentor-profile-field">
              <label>Email Address</label>
              <div className="mentor-profile-value">{displayValue(email)}</div>
            </div>
            <div className="mentor-profile-field">
              <label>Phone Number</label>
              <div className="mentor-profile-value">{displayValue(profile.phone)}</div>
            </div>
            <div className="mentor-profile-field">
              <label>Location</label>
              <div className="mentor-profile-value">{displayValue(profile.location)}</div>
            </div>
          </div>
        </div>

        <div className="mentor-profile-divider" />

        <div className="mentor-profile-section">
          <div className="mentor-profile-section-title">
            <h3>Educational Background</h3>
            <p>Your academic qualifications</p>
          </div>

          <div className="mentor-profile-grid">
            <div className="mentor-profile-field">
              <label>Qualification</label>
              <div className="mentor-profile-value">{displayValue(profile.qualification)}</div>
            </div>
            <div className="mentor-profile-field">
              <label>College / Institution</label>
              <div className="mentor-profile-value">{displayValue(profile.college)}</div>
            </div>
          </div>
        </div>

        <div className="mentor-profile-divider" />

        <div className="mentor-profile-section">
          <div className="mentor-profile-section-title">
            <h3>Professional Information</h3>
            <p>Your expertise and experience</p>
          </div>

          <div className="mentor-profile-grid">
            <div className="mentor-profile-field">
              <label>Specialization</label>
              <div className="mentor-profile-value">{displayValue(profile.specialization)}</div>
            </div>
            <div className="mentor-profile-field">
              <label>Years of Experience</label>
              <div className="mentor-profile-value">
                {profile.experience} years
              </div>
            </div>
            <div className="mentor-profile-field full-width">
              <label>Areas of Expertise</label>
              <div className="mentor-profile-value multiline">
                {displayValue(profile.expertise)}
              </div>
            </div>
            <div className="mentor-profile-field full-width">
              <label>Technical Skills</label>
              <div className="mentor-profile-value multiline">
                {displayValue(profile.skills)}
              </div>
            </div>
            <div className="mentor-profile-field full-width">
              <label>Professional Bio</label>
              <div className="mentor-profile-value multiline">
                {displayValue(profile.bio)}
              </div>
            </div>
          </div>
        </div>
      </div>

      {isEditing && (
        <div
          className="mentor-edit-modal-overlay"
          onMouseDown={(event) => {
            if (event.target === event.currentTarget && !saving) {
              handleCancel();
            }
          }}
        >
          <div
            className="mentor-edit-modal"
            role="dialog"
            aria-modal="true"
            aria-labelledby="mentor-edit-modal-title"
          >
            <div className="mentor-edit-modal-header">
              <div>
                <span className="mentor-edit-modal-eyebrow">PROFILE SETTINGS</span>
                <h2 id="mentor-edit-modal-title">Edit Profile</h2>
                <p>Update your personal, educational and professional details.</p>
              </div>

              <button
                type="button"
                className="mentor-edit-modal-close"
                onClick={handleCancel}
                disabled={saving}
                aria-label="Close edit profile"
              >
                ×
              </button>
            </div>

            <form onSubmit={handleSave} className="mentor-edit-form">
              <div className="mentor-edit-section-heading">
                <span>01</span>
                <div>
                  <h3>Personal Information</h3>
                  <p>Contact details</p>
                </div>
              </div>

              <div className="mentor-profile-grid">
                <div className="mentor-profile-field">
                  <label>Full Name</label>
                  <input value={mentorName} disabled />
                </div>

                <div className="mentor-profile-field">
                  <label>Email Address</label>
                  <input value={email} disabled />
                </div>

                <div className="mentor-profile-field">
                  <label>Phone Number</label>
                  <input
                    name="phone"
                    value={profile.phone}
                    onChange={handleChange}
                    placeholder="Enter phone number"
                  />
                </div>

                <div className="mentor-profile-field">
                  <label>Location</label>
                  <input
                    name="location"
                    value={profile.location}
                    onChange={handleChange}
                    placeholder="Enter your location"
                  />
                </div>
              </div>

              <div className="mentor-edit-section-heading">
                <span>02</span>
                <div>
                  <h3>Educational Background</h3>
                  <p>Your academic qualifications</p>
                </div>
              </div>

              <div className="mentor-profile-grid">
                <div className="mentor-profile-field">
                  <label>Qualification</label>
                  <input
                    name="qualification"
                    value={profile.qualification}
                    onChange={handleChange}
                    placeholder="e.g. B.Tech, M.Tech"
                  />
                </div>

                <div className="mentor-profile-field">
                  <label>College / Institution</label>
                  <input
                    name="college"
                    value={profile.college}
                    onChange={handleChange}
                    placeholder="Enter college name"
                  />
                </div>
              </div>

              <div className="mentor-edit-section-heading">
                <span>03</span>
                <div>
                  <h3>Professional Information</h3>
                  <p>Expertise, skills and experience</p>
                </div>
              </div>

              <div className="mentor-profile-grid">
                <div className="mentor-profile-field">
                  <label>Specialization</label>
                  <input
                    name="specialization"
                    value={profile.specialization}
                    onChange={handleChange}
                    placeholder="e.g. Full Stack Development"
                  />
                </div>

                <div className="mentor-profile-field">
                  <label>Years of Experience</label>
                  <input
                    type="number"
                    name="experience"
                    min="0"
                    max="60"
                    value={profile.experience}
                    onChange={handleChange}
                  />
                </div>

                <div className="mentor-profile-field full-width">
                  <label>Areas of Expertise</label>
                  <textarea
                    name="expertise"
                    value={profile.expertise}
                    onChange={handleChange}
                    placeholder="Describe your areas of expertise"
                    rows="3"
                  />
                </div>

                <div className="mentor-profile-field full-width">
                  <label>Technical Skills</label>
                  <textarea
                    name="skills"
                    value={profile.skills}
                    onChange={handleChange}
                    placeholder="e.g. Python, Django, React, PostgreSQL"
                    rows="3"
                  />
                </div>

                <div className="mentor-profile-field full-width">
                  <label>Professional Bio</label>
                  <textarea
                    name="bio"
                    value={profile.bio}
                    onChange={handleChange}
                    placeholder="Write a short introduction about yourself"
                    rows="4"
                    maxLength="1000"
                  />
                  <small>{profile.bio.length}/1000 characters</small>
                </div>
              </div>

              <div className="mentor-edit-modal-actions">
                <button
                  type="button"
                  className="mentor-profile-cancel-button"
                  onClick={handleCancel}
                  disabled={saving}
                >
                  Cancel
                </button>

                <button
                  type="submit"
                  className="mentor-profile-save-button"
                  disabled={saving}
                >
                  {saving ? "Saving..." : "Save Changes"}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </section>
  );
}

export default MentorProfile;
