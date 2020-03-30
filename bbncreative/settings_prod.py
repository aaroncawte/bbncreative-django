"""
Django settings for bbncreative project.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import django_filters.rest_framework

from bbncreative import secrets

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# bbncreative specific settings
NUM_TOP_PROJECTS = 3
NUM_TOP_FEEDS = 3


SECRET_KEY = secrets.DJANGO_SECRET

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "178.62.41.51", "bbncreative.co", "www.bbncreative.co"]

APPEND_SLASH = True

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "bbncreative_cms.apps.BbncreativeCmsConfig",
    "bbncreative_api.apps.BbncreativeApiConfig",
    "rest_framework",
    "django_filters",
    "lockdown",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "lockdown.middleware.LockdownMiddleware",
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ],
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
}

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True

SECURE_SSL_REDIRECT = True

SECURE_REFERRER_POLICY = "no-referrer-when-downgrade"

LOCKDOWN_ENABLED = False
LOCKDOWN_PASSWORDS = (secrets.LOCKDOWN_PASSWORD, "")

ROOT_URLCONF = "bbncreative.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "bbncreative_cms.context_processors.top_projects",
                "bbncreative_cms.context_processors.top_feeds",
                "bbncreative_cms.context_processors.permanent_feeds",
            ],
        },
    },
]

WSGI_APPLICATION = "bbncreative.wsgi.application"


# Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": secrets.POST_DB["NAME"],
        "USER": secrets.POST_DB["USER"],
        "PASSWORD": secrets.POST_DB["PASSWORD"],
        "HOST": secrets.POST_DB["HOST"],
        "PORT": secrets.POST_DB["PORT"],
    }
}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = False

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

# Uploadeded Content (Images, etc.)

MEDIA_ROOT = os.path.join(BASE_DIR, "../media")
MEDIA_URL = "https://bbncreative.co/media/"

# Logging

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": "django_debug.log",
        },
    },
    "loggers": {
        "django": {"handlers": ["file"], "level": "WARNING", "propagate": True,},
    },
}

# Email server

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = secrets.EMAIL_HOST
EMAIL_HOST_USER = secrets.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = secrets.EMAIL_HOST_PASSWORD
DEFAULT_FROM_EMAIL = secrets.EMAIL_HOST_USER
SERVER_EMAIL = secrets.EMAIL_HOST_USER
EMAIL_USE_TLS = True
EMAIL_PORT = 587
