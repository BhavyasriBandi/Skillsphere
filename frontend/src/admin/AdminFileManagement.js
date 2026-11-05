
import React, { useCallback, useEffect, useRef, useState } from "react";
import { API_BASE_URL, useAuth } from "../auth/AuthContext";
import "./AdminFileManagement.css";

const MAX_FILE_SIZE = 10 * 1024 * 1024;

const ALLOWED_EXTENSIONS = [
  "pdf", "doc", "docx", "ppt", "pptx",
  "xls", "xlsx", "txt", "csv",
  "png", "jpg", "jpeg", "webp", "zip",
];

const PREVIEW_EXTENSIONS = [
  "pdf", "png", "jpg", "jpeg", "webp", "txt", "csv",
];

const CATEGORY_LABELS = {
  document: "Document",
  learning: "Learning Material",
  project: "Project File",
  other: "Other",
};

function getExtension(filename = "") {
  return filename.split(".").pop().toLowerCase();
}

function getFilename(file) {
  return file.original_filename || file.title || "download";
}

function validateSelectedFile(file) {
  if (!file) {
    return "Please choose a file to upload.";
  }

  if (file.size === 0) {
    return "Empty files cannot be uploaded.";
  }

  if (file.size > MAX_FILE_SIZE) {
    return "File size must not exceed 10 MB.";
  }

  const extension = getExtension(file.name);

  if (!ALLOWED_EXTENSIONS.includes(extension)) {
    return "This file type is not supported.";
  }

  return null;
}

export default function AdminFileManagement() {
  const auth = useAuth();
  const fileInputRef = useRef(null);
  const toastTimerRef = useRef(null);
  const previewUrlRef = useRef(null);

  const [files, setFiles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [uploading, setUploading] = useState(false);
  const [title, setTitle] = useState("");
  const [category, setCategory] = useState("document");
  const [selectedFile, setSelectedFile] = useState(null);
  const [toast, setToast] = useState(null);
  const [preview, setPreview] = useState(null);
  const [previewLoading, setPreviewLoading] = useState(false);
  const [deletingId, setDeletingId] = useState(null);

  const token =
    auth?.accessToken ||
    auth?.access ||
    auth?.tokens?.access ||
    localStorage.getItem("skillsphere_access") ||
    localStorage.getItem("access");

  const showToast = useCallback((message, type = "success") => {
    window.clearTimeout(toastTimerRef.current);
    setToast({ message, type });

    toastTimerRef.current = window.setTimeout(() => {
      setToast(null);
    }, 3500);
  }, []);

  const request = useCallback(
    async (path, options = {}) => {
      const response = await fetch(`${API_BASE_URL}${path}`, {
        ...options,
        headers: {
          ...(token
            ? { Authorization: `Bearer ${token}` }
            : {}),
          ...options.headers,
        },
      });

      if (!response.ok) {
        let message = "Something went wrong. Please try again.";

        try {
          const data = await response.json();

          if (data.detail) {
            message = data.detail;
          } else if (data.file?.[0]) {
            message = data.file[0];
          } else if (data.title?.[0]) {
            message = data.title[0];
          } else if (data.category?.[0]) {
            message = data.category[0];
          } else if (data.message) {
            message = data.message;
          } else {
            const firstError = Object.values(data).flat()[0];

            if (typeof firstError === "string") {
              message = firstError;
            }
          }
        } catch {
          // Keep the fallback error message.
        }

        if (response.status === 401) {
          throw new Error(
            "Your session expired. Please log in again."
          );
        }

        if (response.status === 403) {
          throw new Error("Admin permission is required.");
        }

        throw new Error(message);
      }

      return response;
    },
    [token]
  );

  const loadFiles = useCallback(async () => {
    setLoading(true);

    try {
      const response = await request("/api/files/");
      const data = await response.json();
      const items = Array.isArray(data) ? data : data.results || [];

      setFiles(items);
      return true;
    } catch (error) {
      showToast(error.message || "Unable to load files.", "error");
      return false;
    } finally {
      setLoading(false);
    }
  }, [request, showToast]);

  useEffect(() => {
    loadFiles();

    return () => {
      window.clearTimeout(toastTimerRef.current);

      if (previewUrlRef.current) {
        URL.revokeObjectURL(previewUrlRef.current);
      }
    };
  }, [loadFiles]);

  function handleFileChange(event) {
    const file = event.target.files?.[0] || null;

    setSelectedFile(null);

    if (!file) return;

    const error = validateSelectedFile(file);

    if (error) {
      showToast(error, "error");
      event.target.value = "";
      return;
    }

    setSelectedFile(file);
    showToast("File selected successfully!", "success");
  }

  async function handleUpload(event) {
    event.preventDefault();

    if (uploading) return;

    if (!title.trim()) {
      showToast("Please enter a file title.", "error");
      return;
    }

    const fileError = validateSelectedFile(selectedFile);

    if (fileError) {
      showToast(fileError, "error");
      return;
    }

    const formData = new FormData();
    formData.append("title", title.trim());
    formData.append("category", category);
    formData.append("file", selectedFile);

    setUploading(true);

    try {
      await request("/api/files/", {
        method: "POST",
        body: formData,
      });

      setTitle("");
      setCategory("document");
      setSelectedFile(null);

      if (fileInputRef.current) {
        fileInputRef.current.value = "";
      }

      showToast("File uploaded successfully!", "success");
      await loadFiles();
    } catch (error) {
      showToast(error.message || "File upload failed.", "error");
    } finally {
      setUploading(false);
    }
  }

  async function handleDownload(file) {
    try {
      const response = await request(
        `/api/files/${file.id}/download/`
      );

      const blob = await response.blob();
      const url = URL.createObjectURL(blob);
      const anchor = document.createElement("a");

      anchor.href = url;
      anchor.download = getFilename(file);
      document.body.appendChild(anchor);
      anchor.click();
      anchor.remove();

      window.setTimeout(() => URL.revokeObjectURL(url), 1000);

      showToast("File downloaded successfully!", "success");
    } catch (error) {
      showToast(
        error.message || "Unable to download file.",
        "error"
      );
    }
  }

  function closePreview() {
    setPreview(null);
    setPreviewLoading(false);

    if (previewUrlRef.current) {
      URL.revokeObjectURL(previewUrlRef.current);
      previewUrlRef.current = null;
    }
  }

  async function handleView(file) {
    const filename = getFilename(file);
    const extension = getExtension(filename);

    if (!PREVIEW_EXTENSIONS.includes(extension)) {
      showToast(
        "Preview is unavailable for this file type. Please download it.",
        "error"
      );
      return;
    }

    closePreview();
    setPreviewLoading(true);

    try {
      const response = await request(
        `/api/files/${file.id}/download/`
      );

      const originalBlob = await response.blob();

      const mimeTypes = {
        pdf: "application/pdf",
        png: "image/png",
        jpg: "image/jpeg",
        jpeg: "image/jpeg",
        webp: "image/webp",
        txt: "text/plain",
        csv: "text/csv",
      };

      const blob = new Blob([originalBlob], {
        type: mimeTypes[extension] || originalBlob.type,
      });

      const url = URL.createObjectURL(blob);
      previewUrlRef.current = url;

      setPreview({
        id: file.id,
        title: file.title,
        filename,
        extension,
        url,
      });
    } catch (error) {
      showToast(
        error.message || "Unable to preview this file.",
        "error"
      );
    } finally {
      setPreviewLoading(false);
    }
  }

  async function handleDelete(file) {
    const confirmed = window.confirm(
      `Are you sure you want to delete "${file.title}"?`
    );

    if (!confirmed) return;

    setDeletingId(file.id);

    try {
      await request(`/api/files/${file.id}/`, {
        method: "DELETE",
      });

      setFiles((current) =>
        current.filter((item) => item.id !== file.id)
      );

      if (preview?.id === file.id) {
        closePreview();
      }

      showToast("File deleted successfully!", "success");
    } catch (error) {
      showToast(
        error.message || "Unable to delete file.",
        "error"
      );
    } finally {
      setDeletingId(null);
    }
  }

  return (
    <div className="admin-file-management">
      {toast && (
        <div
          className={`afm-toast afm-toast-${toast.type}`}
          role="status"
          aria-live="polite"
        >
          <span className="afm-toast-icon">
            {toast.type === "success" ? "✓" : "!"}
          </span>

          <span className="afm-toast-message">
            {toast.message}
          </span>

          <button
            type="button"
            className="afm-toast-close"
            onClick={() => {
              window.clearTimeout(toastTimerRef.current);
              setToast(null);
            }}
            aria-label="Close notification"
          >
            ×
          </button>
        </div>
      )}

      <div className="afm-header">
        <div>
          <h2>File Management</h2>
          <p>
            Upload, organize, preview, download and manage files.
          </p>
        </div>

        <button
          type="button"
          className="afm-refresh"
          onClick={loadFiles}
          disabled={loading}
        >
          <span aria-hidden="true">↻</span>
          {loading ? "Refreshing..." : "Refresh"}
        </button>
      </div>

      <form className="afm-upload-card" onSubmit={handleUpload}>
        <div className="afm-card-heading">
          <span className="afm-heading-icon" aria-hidden="true">
            ↑
          </span>

          <div>
            <h3>Upload a File</h3>
            <p>
              Add documents and learning resources to SkillSphere.
            </p>
          </div>
        </div>

        <div className="afm-form-grid">
          <div className="afm-field">
            <label htmlFor="afm-title">File title</label>

            <input
              id="afm-title"
              type="text"
              value={title}
              onChange={(event) => setTitle(event.target.value)}
              placeholder="Enter a file title"
              maxLength={200}
              required
            />
          </div>

          <div className="afm-field">
            <label htmlFor="afm-category">Category</label>

            <select
              id="afm-category"
              value={category}
              onChange={(event) => setCategory(event.target.value)}
            >
              <option value="document">Document</option>
              <option value="learning">Learning Material</option>
              <option value="project">Project File</option>
              <option value="other">Other</option>
            </select>
          </div>

          <div className="afm-field afm-file-field">
            <label htmlFor="afm-file">
              Choose file <span>(Maximum 10 MB)</span>
            </label>

            <input
              ref={fileInputRef}
              id="afm-file"
              type="file"
              accept=".pdf,.doc,.docx,.ppt,.pptx,.xls,.xlsx,.txt,.csv,.png,.jpg,.jpeg,.webp,.zip"
              onChange={handleFileChange}
              required
            />

            {selectedFile && (
              <p className="afm-selected-file">
                Selected: {selectedFile.name}
              </p>
            )}
          </div>
        </div>

        <div className="afm-upload-footer">
          <p>
            Supported documents, images, spreadsheets and ZIP files.
          </p>

          <button type="submit" disabled={uploading}>
            {uploading ? "Uploading..." : "↑  Upload File"}
          </button>
        </div>
      </form>

      <section className="afm-list-card">
        <div className="afm-list-heading">
          <div>
            <h3>Uploaded Files</h3>
            <p>View and manage your uploaded files.</p>
          </div>

          <span className="afm-count">
            {files.length} {files.length === 1 ? "file" : "files"}
          </span>
        </div>

        {loading ? (
          <div className="afm-empty">
            <span className="afm-loader" />
            <span>Loading files...</span>
          </div>
        ) : files.length === 0 ? (
          <div className="afm-empty">
            <span className="afm-empty-icon" aria-hidden="true">
              ▤
            </span>
            <strong>No files uploaded yet</strong>
            <span>Your uploaded files will appear here.</span>
          </div>
        ) : (
          <div className="afm-table-wrap">
            <table className="afm-table">
              <thead>
                <tr>
                  <th>File</th>
                  <th>Category</th>
                  <th>Uploaded By</th>
                  <th>Date</th>
                  <th>Actions</th>
                </tr>
              </thead>

              <tbody>
                {files.map((file) => (
                  <tr key={file.id}>
                    <td>
                      <div className="afm-file-info">
                        <span
                          className="afm-file-icon"
                          aria-hidden="true"
                        >
                          {getExtension(getFilename(file)) === "pdf"
                            ? "PDF"
                            : "FILE"}
                        </span>

                        <div className="afm-file-text">
                          <strong>{file.title}</strong>
                          <small>{getFilename(file)}</small>
                        </div>
                      </div>
                    </td>

                    <td>
                      <span className="afm-category">
                        {CATEGORY_LABELS[file.category] || file.category}
                      </span>
                    </td>

                    <td>{file.uploaded_by_email || "—"}</td>

                    <td>
                      {file.uploaded_at
                        ? new Date(file.uploaded_at).toLocaleDateString()
                        : "—"}
                    </td>

                    <td>
                      <div className="afm-actions">
                        <button
                          type="button"
                          className="afm-view"
                          onClick={() => handleView(file)}
                          disabled={previewLoading}
                        >
                          View
                        </button>

                        <button
                          type="button"
                          onClick={() => handleDownload(file)}
                        >
                          Download
                        </button>

                        <button
                          type="button"
                          className="afm-delete"
                          onClick={() => handleDelete(file)}
                          disabled={deletingId === file.id}
                        >
                          {deletingId === file.id
                            ? "Deleting..."
                            : "Delete"}
                        </button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </section>

      {preview && (
        <div
          className="afm-modal-backdrop"
          onMouseDown={(event) => {
            if (event.target === event.currentTarget) {
              closePreview();
            }
          }}
          role="presentation"
        >
          <section
            className="afm-preview-modal"
            role="dialog"
            aria-modal="true"
            aria-labelledby="afm-preview-title"
          >
            <header className="afm-preview-header">
              <div>
                <h3 id="afm-preview-title">{preview.title}</h3>
                <p>{preview.filename}</p>
              </div>

              <div className="afm-preview-controls">
                <button
                  type="button"
                  onClick={() => {
                    const anchor = document.createElement("a");
                    anchor.href = preview.url;
                    anchor.download = preview.filename;
                    anchor.click();
                  }}
                >
                  Download
                </button>

                <button
                  type="button"
                  className="afm-preview-close"
                  onClick={closePreview}
                  aria-label="Close preview"
                >
                  ×
                </button>
              </div>
            </header>

            <div className="afm-preview-content">
              {["png", "jpg", "jpeg", "webp"].includes(
                preview.extension
              ) ? (
                <img src={preview.url} alt={preview.title} />
              ) : (
                <iframe
                  src={preview.url}
                  title={`Preview: ${preview.title}`}
                />
              )}
            </div>
          </section>
        </div>
      )}
    </div>
  );
}
