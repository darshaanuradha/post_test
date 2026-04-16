"""
Django settings for myproject project.
Refactored for Production Best Practices using Environment Variables.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from a .env file if it exists
load_dotenv(BASE_DIR / ".env")

# ==========================================
# SECURITY SETTINGS
# ==========================================

# SECURITY WARNING: keep the secret key used in production secret!
# Pulls from .env, falls back to a dummy key ONLY for local development
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-local-dev-key-only")

# SECURITY WARNING: don't run with debug turned on in production!
# Expects exactly "True" in the .env file to enable debug mode
DEBUG = os.getenv("DEBUG", "False") == "True"

# Dynamically loads allowed hosts from .env (e.g., "103.253.145.64,yourdomain.com")
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",")


# ==========================================
# APPLICATION DEFINITION
# ==========================================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "posts",
    "users",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "myproject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
            BASE_DIR / "users" / "templates",
            BASE_DIR / "posts" / "templates",
        ],
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

WSGI_APPLICATION = "myproject.wsgi.application"


# ==========================================
# DATABASE CONFIGURATION
# ==========================================

if DEBUG:
    # Local Development Database
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    # Production Database (Pulls credentials securely from .env)
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.getenv("DB_NAME", "anuradhadb"),
            "USER": os.getenv("DB_USER", "useranuradha"),
            "PASSWORD": os.getenv("DB_PASSWORD"),
            "HOST": os.getenv("DB_HOST", "localhost"),
            "PORT": os.getenv("DB_PORT", "3306"),
        }
    }


# ==========================================
# PASSWORD VALIDATION
# ==========================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# ==========================================
# INTERNATIONALIZATION
# ==========================================

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Colombo"
USE_I18N = True
USE_TZ = True


# ==========================================
# STATIC & MEDIA FILES
# ==========================================

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "assets"
STATICFILES_DIRS = [BASE_DIR / "static"]

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"


# ==========================================
# PRODUCTION SECURITY ENFORCEMENT
# ==========================================
# These settings activate automatically when DEBUG is False to secure your live site.

if not DEBUG:
    # Prevents browsers from guessing the content type
    SECURE_CONTENT_TYPE_NOSNIFF = True
    # Enables XSS filtering in the browser
    SECURE_BROWSER_XSS_FILTER = True
    # Ensures cookies are only sent over HTTPS (Enable these once you have an SSL certificate!)
    # CSRF_COOKIE_SECURE = True
    # SESSION_COOKIE_SECURE = True
    # SECURE_SSL_REDIRECT = True
