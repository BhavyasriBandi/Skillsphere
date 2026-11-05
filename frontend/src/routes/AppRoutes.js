
import React from "react";
import {
  Routes,
  Route,
  Link,
  Navigate
} from "react-router-dom";

import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import Features from "../components/Features";

import Login from "../pages/Login";
import Register from "../pages/Register";
import EmailVerification from "../pages/EmailVerification";

import StudentDashboard from "../components/StudentDashboard";
import AdminDashboard from "../admin/AdminDashboard";
import MentorDashboard from "../mentor/MentorDashboard";

import ToastProvider from "../components/ToastProvider";
import PrivateRoute from "./PrivateRoutes";

// Landing Page
function HomePage() {
  return (
    <>
      <Navbar />
      <Hero />
      <Features />
    </>
  );
}

// 404 Page
function NotFound() {
  return (
    <main className="not-found-page">
      <h1>404 - Page Not Found</h1>
      <p>The requested page could not be found.</p>
      <Link to="/">Return to SkillSphere home</Link>
    </main>
  );
}

export default function AppRoutes() {
  return (
    <>
      <ToastProvider />

      <Routes>

        {/* PUBLIC ROUTES */}

        <Route path="/" element={<HomePage />} />

        <Route path="/login" element={<Login />} />

        <Route path="/register" element={<Register />} />

        <Route
          path="/verify-email"
          element={<EmailVerification />}
        />


        {/* STUDENT PRIVATE ROUTES */}

        <Route
          element={
            <PrivateRoute allowedRoles={["student"]} />
          }
        >
          <Route
            path="/student/dashboard"
            element={<StudentDashboard />}
          />

          <Route
            path="/student-dashboard"
            element={
              <Navigate
                to="/student/dashboard"
                replace
              />
            }
          />

          <Route path="/student/profile" element={<StudentDashboard />} />
          <Route path="/student/career-goal" element={<StudentDashboard />} />
          <Route path="/student/skill-assessment" element={<StudentDashboard />} />
          <Route path="/student/skill-analysis" element={<StudentDashboard />} />
          <Route path="/student/skill-gap" element={<StudentDashboard />} />
          <Route path="/student/roadmap" element={<StudentDashboard />} />
          <Route path="/student/learning-hub" element={<StudentDashboard />} />
          <Route path="/student/challenges" element={<StudentDashboard />} />
          <Route path="/student/projects" element={<StudentDashboard />} />
          <Route path="/student/interview-prep" element={<StudentDashboard />} />
          <Route path="/student/progress" element={<StudentDashboard />} />
          <Route path="/student/achievements" element={<StudentDashboard />} />
          <Route path="/student/portfolio" element={<StudentDashboard />} />
          <Route path="/student/notifications" element={<StudentDashboard />} />
          <Route path="/student/settings" element={<StudentDashboard />} />
        </Route>


        {/* MENTOR PRIVATE ROUTES */}

        <Route
          element={
            <PrivateRoute allowedRoles={["mentor"]} />
          }
        >
          <Route
            path="/mentor"
            element={
              <Navigate
                to="/mentor/dashboard"
                replace
              />
            }
          />

          <Route
            path="/mentor/dashboard"
            element={<MentorDashboard />}
          />

          <Route path="/mentor/profile" element={<MentorDashboard />} />
          <Route path="/mentor/students" element={<MentorDashboard />} />
          <Route path="/mentor/student-progress" element={<MentorDashboard />} />
          <Route path="/mentor/assessments" element={<MentorDashboard />} />
          <Route path="/mentor/skill-analysis" element={<MentorDashboard />} />
          <Route path="/mentor/skill-gaps" element={<MentorDashboard />} />
          <Route path="/mentor/roadmaps" element={<MentorDashboard />} />
          <Route path="/mentor/resources" element={<MentorDashboard />} />
          <Route path="/mentor/projects" element={<MentorDashboard />} />
          <Route path="/mentor/interview-prep" element={<MentorDashboard />} />
          <Route path="/mentor/messages" element={<MentorDashboard />} />
          <Route path="/mentor/notifications" element={<MentorDashboard />} />
          <Route path="/mentor/settings" element={<MentorDashboard />} />
        </Route>


        {/* ADMIN PRIVATE ROUTES */}

        <Route
          element={
            <PrivateRoute allowedRoles={["admin"]} />
          }
        >
          <Route
            path="/admin"
            element={
              <Navigate
                to="/admin/dashboard"
                replace
              />
            }
          />

          <Route
            path="/admin/dashboard"
            element={<AdminDashboard />}
          />

          <Route
            path="/admin/users"
            element={<AdminDashboard />}
          />

          <Route
            path="/admin/:section"
            element={<AdminDashboard />}
          />
        </Route>


        {/* 404 ROUTE */}

        <Route
          path="*"
          element={<NotFound />}
        />

      </Routes>
    </>
  );
}
