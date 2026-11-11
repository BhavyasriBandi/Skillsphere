import os
from pathlib import Path
from datetime import timedelta
from urllib.parse import urlparse, unquote, parse_qs

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")


# =====================================================
# ENVIRONMENT VARIABLES
# =====================================================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# =====================================================
# DJANGO CORE SETTINGS
# =====================================================

SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-skillsphere-development-key",
)

DEBUG = os.getenv("DEBUG", "True").lower() in ("true", "1", "yes")


# Allowed hosts
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]

extra_hosts = os.getenv("ALLOWED_HOSTS", "")
if extra_hosts:
    ALLOWED_HOSTS.extend(
        host.strip()
        for host in extra_hosts.split(",")
        if host.strip()
    )

render_hostname = os.getenv("RENDER_EXTERNAL_HOSTNAME")
if render_hostname:
    ALLOWED_HOSTS.append(render_hostname)


# =====================================================
# INSTALLED APPLICATIONS
# =====================================================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "drf_spectacular",
    "corsheaders",

    "accounts",
    "files.apps.FilesConfig",
    "skills",
    "careers",
    "resources",
    "notifications",
    "assessments",
    "progress",
    "mentors",
    "tasks",
    "learning_goals",
    "study_planner",
    "certificates",
    "skill_endorsements",
    "activity_feed",
    "feedback",
    "bookmarks",
    "support",
    "user_preferences",
    "career_comparison",
    "job_opportunities",
    "portfolios",
    "leaderboard",
    "study_streaks",
    "achievements",
    "projects",
    "interview_prep",
    "learning_resources",
    "roadmaps",
    "challenges",
    "reports",
]


# =====================================================
# MIDDLEWARE
# =====================================================

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =====================================================
# URL CONFIGURATION
# =====================================================

ROOT_URLCONF = "config.urls"


# =====================================================
# TEMPLATES
# =====================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "config.wsgi.application"


# =====================================================
# DATABASE CONFIGURATION
# =====================================================

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    db_url = urlparse(DATABASE_URL)
    query_params = parse_qs(db_url.query)

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": db_url.path.lstrip("/"),
            "USER": unquote(db_url.username or ""),
            "PASSWORD": unquote(db_url.password or ""),
            "HOST": db_url.hostname,
            "PORT": db_url.port or "5432",
            "OPTIONS": {
                "sslmode": query_params.get(
                    "sslmode", ["require"]
                )[0],
            },
        }
    }

else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DB_NAME", "skillsphere"),
            "USER": os.getenv("DB_USER", "postgres"),
            "PASSWORD": os.getenv("DB_PASSWORD", ""),
            "HOST": os.getenv("DB_HOST", "localhost"),
            "PORT": os.getenv("DB_PORT", "5432"),
        }
    }


# =====================================================
# PASSWORD VALIDATION
# =====================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# =====================================================
# INTERNATIONALIZATION
# =====================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True


# =====================================================
# STATIC AND MEDIA FILES
# =====================================================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": (
            "whitenoise.storage.CompressedManifestStaticFilesStorage"
        ),
    },
}


# =====================================================
# DEFAULT PRIMARY KEY
# =====================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# =====================================================
# DJANGO REST FRAMEWORK
# =====================================================

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": (
        "drf_spectacular.openapi.AutoSchema"
    ),

    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),

    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.AllowAny",
    ),

    "DEFAULT_PAGINATION_CLASS": (
        "rest_framework.pagination.PageNumberPagination"
    ),

    "PAGE_SIZE": 5,

    "DEFAULT_THROTTLE_RATES": {
        "login": "5/minute",
    },
}


# =====================================================
# SWAGGER / OPENAPI
# =====================================================

SPECTACULAR_SETTINGS = {
    "TITLE": "SkillSphere API",
    "DESCRIPTION": "API documentation for the SkillSphere platform",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}


# =====================================================
# JWT AUTHENTICATION
# =====================================================

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,
}


# =====================================================
# CORS CONFIGURATION
# =====================================================

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

frontend_url = os.getenv("FRONTEND_URL")

FRONTEND_URL = frontend_url.rstrip("/") if frontend_url else ""

if frontend_url:
    CORS_ALLOWED_ORIGINS.append(frontend_url.rstrip("/"))


# =====================================================
# CSRF CONFIGURATION
# =====================================================

CSRF_TRUSTED_ORIGINS = []

if frontend_url:
    CSRF_TRUSTED_ORIGINS.append(frontend_url.rstrip("/"))


# =====================================================
# PROXY / HTTPS CONFIGURATION
# =====================================================

SECURE_PROXY_SSL_HEADER = (
    "HTTP_X_FORWARDED_PROTO",
    "https",
)


# =====================================================
# EMAIL CONFIGURATION
# =====================================================

EMAIL_HOST = os.getenv(
    "EMAIL_HOST",
    "smtp.gmail.com",
)

EMAIL_PORT = int(
    os.getenv("EMAIL_PORT", "587")
)

EMAIL_USE_TLS = os.getenv(
    "EMAIL_USE_TLS",
    "True",
).lower() in ("true", "1", "yes")

EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")

EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")

if EMAIL_HOST_USER and EMAIL_HOST_PASSWORD:

    EMAIL_BACKEND = (
        "django.core.mail.backends.smtp.EmailBackend"
    )

    DEFAULT_FROM_EMAIL = os.getenv(
        "DEFAULT_FROM_EMAIL",
        EMAIL_HOST_USER,
    )

else:

    EMAIL_BACKEND = (
        "django.core.mail.backends.console.EmailBackend"
    )

    DEFAULT_FROM_EMAIL = "skillsphere@example.com"