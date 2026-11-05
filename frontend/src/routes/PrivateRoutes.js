
import React from "react";
import { Navigate, Outlet } from "react-router-dom";
import { useAuth, getDashboardPath } from "../auth/AuthContext";

export default function PrivateRoute({ allowedRoles }) {
  const { loading, isAuthenticated, role } = useAuth();

  // Wait until authentication is restored.
  if (loading) {
    return (
      <div className="auth-loading">
        <p>Loading SkillSphere...</p>
      </div>
    );
  }

  // Redirect unauthenticated users to Login.
  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  // Restrict access based on the user's role.
  if (
    allowedRoles &&
    (!role || !allowedRoles.includes(role))
  ) {
    const dashboardPath = getDashboardPath(role);

    return (
      <Navigate
        to={dashboardPath || "/login"}
        replace
      />
    );
  }

  return <Outlet />;
}
