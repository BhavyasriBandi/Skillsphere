
import React, { useCallback, useEffect, useState } from "react";
import { showToast } from "../components/ToastProvider";
import "./ReportsAnalytics.css";

const API_URL = "https://skillsphere-17hl.onrender.com/api/reports/analytics/";
const TOKEN_KEY = "skillsphere_access";

const EMPTY_METRICS = {
  total_users: 0,
  total_students: 0,
  total_mentors: 0,
  total_achievements: 0,
  earned_achievements: 0,
  active_users: 0,
};

function getToday() {
  const now = new Date();
  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, "0");
  const day = String(now.getDate()).padStart(2, "0");
  return `${year}-${month}-${day}`;
}

function getFirstDayOfYear() {
  return `${new Date().getFullYear()}-01-01`;
}

function getErrorMessage(data, fallback) {
  if (typeof data?.detail === "string") return data.detail;
  if (typeof data?.error === "string") return data.error;
  if (typeof data?.message === "string") return data.message;

  if (data && typeof data === "object") {
    const message = Object.values(data)
      .flat(Infinity)
      .find((value) => typeof value === "string");

    if (message) return message;
  }

  return fallback;
}

async function fetchReport(startDate, endDate) {
  const token =
    localStorage.getItem(TOKEN_KEY) ||
    localStorage.getItem("access");

  if (!token) {
    throw new Error("Your session has expired. Please log in again.");
  }

  const params = new URLSearchParams();

  if (startDate) params.set("start_date", startDate);
  if (endDate) params.set("end_date", endDate);

  const response = await fetch(
    `${API_URL}?${params.toString()}`,
    {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
        Accept: "application/json",
      },
    }
  );

  const data = await response.json().catch(() => ({}));

  if (!response.ok) {
    throw new Error(
      getErrorMessage(data, `Report request failed (${response.status}).`)
    );
  }

  if (!data.metrics || typeof data.metrics !== "object") {
    throw new Error("The reports API returned an unexpected response.");
  }

  return data;
}

function downloadCsv(report, startDate, endDate) {
  const rows = [
    ["SkillSphere Reports & Analytics"],
    ["Start Date", startDate || "All"],
    ["End Date", endDate || "All"],
    [],
    ["Metric", "Value"],
    ["Total Users", report.metrics.total_users ?? 0],
    ["Total Students", report.metrics.total_students ?? 0],
    ["Total Mentors", report.metrics.total_mentors ?? 0],
    ["Total Achievements", report.metrics.total_achievements ?? 0],
    ["Earned Achievements", report.metrics.earned_achievements ?? 0],
    ["Active Users", report.metrics.active_users ?? 0],
    [],
    ["Monthly Registrations"],
    ["Month", "Registrations"],
    ...(report.registrations || []).map((item) => [
      item.month ?? "",
      item.count ?? 0,
    ]),
    [],
    ["User Role Distribution"],
    ["Role", "Users"],
    ...(report.roles || []).map((item) => [
      item.role ?? "Unassigned",
      item.count ?? 0,
    ]),
  ];

  const csv = rows
    .map((row) =>
      row
        .map((value) => {
          const text = String(value ?? "");
          return `"${text.replace(/"/g, '""')}"`;
        })
        .join(",")
    )
    .join("\r\n");

  const blob = new Blob(["\uFEFF", csv], {
    type: "text/csv;charset=utf-8;",
  });

  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");

  link.href = url;
  link.download = `skillsphere-report-${getToday()}.csv`;
  document.body.appendChild(link);
  link.click();
  link.remove();
  URL.revokeObjectURL(url);
}

export default function ReportsAnalytics() {
  const [startDate, setStartDate] = useState(getFirstDayOfYear);
  const [endDate, setEndDate] = useState(getToday);

  const [metrics, setMetrics] = useState({ ...EMPTY_METRICS });
  const [registrations, setRegistrations] = useState([]);
  const [roles, setRoles] = useState([]);

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [hasLoaded, setHasLoaded] = useState(false);

  const loadReport = useCallback(
    async (showSuccessToast = false) => {
      if (startDate && endDate && startDate > endDate) {
        const message = "Start date cannot be later than end date.";
        setError(message);
        showToast(message, "error");
        return;
      }

      setLoading(true);
      setError("");

      try {
        const data = await fetchReport(startDate, endDate);

        setMetrics({
          ...EMPTY_METRICS,
          ...data.metrics,
        });

        setRegistrations(
          Array.isArray(data.registrations) ? data.registrations : []
        );

        setRoles(Array.isArray(data.roles) ? data.roles : []);
        setHasLoaded(true);

        if (showSuccessToast) {
          showToast("Report generated successfully.", "success");
        }
      } catch (err) {
        const message =
          err.message || "Unable to generate the report.";

        setError(message);
        showToast(message, "error");
      } finally {
        setLoading(false);
      }
    },
    [startDate, endDate]
  );

  useEffect(() => {
    loadReport(false);
  }, [loadReport]);

  function handleGenerateReport(event) {
    event.preventDefault();
    loadReport(true);
  }

  function handleExportCsv() {
    if (!hasLoaded) {
      showToast("Generate a report before exporting CSV.", "error");
      return;
    }

    try {
      downloadCsv({ metrics, registrations, roles }, startDate, endDate);
      showToast("CSV exported successfully.", "success");
    } catch (err) {
      showToast(
        err.message || "Unable to export the CSV file.",
        "error"
      );
    }
  }

  const metricCards = [
    {
      label: "Total Users",
      value: metrics.total_users,
      icon: "👥",
    },
    {
      label: "Students",
      value: metrics.total_students,
      icon: "🎓",
    },
    {
      label: "Mentors",
      value: metrics.total_mentors,
      icon: "🧑‍🏫",
    },
    {
      label: "Total Achievements",
      value: metrics.total_achievements,
      icon: "🏆",
    },
    {
      label: "Earned Achievements",
      value: metrics.earned_achievements,
      icon: "⭐",
    },
    {
      label: "Active Users",
      value: metrics.active_users,
      icon: "📈",
    },
  ];

  return (
    <div className="reports-analytics">
      <div className="reports-header">
        <div>
          <h1>Reports &amp; Analytics</h1>
          <p>
            Review SkillSphere platform activity and analytics.
          </p>
        </div>

        <button
          type="button"
          className="reports-export-btn"
          onClick={handleExportCsv}
          disabled={loading}
        >
          Export CSV
        </button>
      </div>

      <form
        className="reports-filters"
        onSubmit={handleGenerateReport}
      >
        <div className="reports-date-field">
          <label htmlFor="reports-start-date">Start Date</label>
          <input
            id="reports-start-date"
            type="date"
            value={startDate}
            max={endDate || undefined}
            onChange={(event) => setStartDate(event.target.value)}
          />
        </div>

        <div className="reports-date-field">
          <label htmlFor="reports-end-date">End Date</label>
          <input
            id="reports-end-date"
            type="date"
            value={endDate}
            min={startDate || undefined}
            max={getToday()}
            onChange={(event) => setEndDate(event.target.value)}
          />
        </div>

        <button
          type="submit"
          className="reports-generate-btn"
          disabled={loading}
        >
          {loading ? "Generating..." : "Generate Report"}
        </button>
      </form>

      {error && (
        <div className="reports-error" role="alert">
          {error}
        </div>
      )}

      <section className="reports-metrics">
        {metricCards.map((card) => (
          <article className="reports-metric-card" key={card.label}>
            <div className="reports-metric-icon">{card.icon}</div>
            <div>
              <p>{card.label}</p>
              <h2>{Number(card.value || 0).toLocaleString()}</h2>
            </div>
          </article>
        ))}
      </section>

      <div className="reports-charts">
        <section className="reports-panel">
          <div className="reports-panel-heading">
            <h2>Monthly Registrations</h2>
            <p>New user registrations by month</p>
          </div>

          {registrations.length === 0 ? (
            <div className="reports-empty">
              No registrations found for this date range.
            </div>
          ) : (
            <div className="reports-registration-list">
              {registrations.map((item) => (
                <div
                  className="reports-registration-row"
                  key={item.month}
                >
                  <span>{item.month}</span>
                  <div className="reports-bar-track">
                    <div
                      className="reports-bar-fill"
                      style={{
                        width: `${
                          (Number(item.count || 0) /
                            Math.max(
                              ...registrations.map((row) =>
                                Number(row.count || 0)
                              ),
                              1
                            )) *
                          100
                        }%`,
                      }}
                    />
                  </div>
                  <strong>{item.count}</strong>
                </div>
              ))}
            </div>
          )}
        </section>

        <section className="reports-panel">
          <div className="reports-panel-heading">
            <h2>User Role Distribution</h2>
            <p>Users grouped by their assigned role</p>
          </div>

          {roles.length === 0 ? (
            <div className="reports-empty">
              No role data found for this date range.
            </div>
          ) : (
            <div className="reports-role-list">
              {roles.map((item) => {
                const total = Math.max(
                  ...roles.map((role) => Number(role.count || 0)),
                  1
                );

                return (
                  <div className="reports-role-row" key={item.role}>
                    <div className="reports-role-label">
                      <span>{item.role || "Unassigned"}</span>
                      <strong>{item.count}</strong>
                    </div>
                    <div className="reports-bar-track">
                      <div
                        className="reports-bar-fill reports-role-fill"
                        style={{
                          width: `${
                            (Number(item.count || 0) / total) * 100
                          }%`,
                        }}
                      />
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </section>
      </div>
    </div>
  );
}
