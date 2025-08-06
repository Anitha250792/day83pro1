import os
from pathlib import Path

# --- Base Directory ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Security ---
SECRET_KEY = 'your-secret-key'  # Replace with real secret key in production
DEBUG = True

ALLOWED_HOSTS = ['*']  # ⚠️ For development/testing. Use specific domain in production.

# --- Installed Apps ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'directory',  # Your custom app
]

# --- Middleware ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For static files on Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --- URLs ---
ROOT_URLCONF = 'employee_directory.urls'

# --- Templates ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # optional
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# --- WSGI ---
WSGI_APPLICATION = 'employee_directory.wsgi.application'

# --- Database ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- Password Validation ---
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
]


# --- Internationalization ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# --- Static Files ---
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # for dev
STATIC_ROOT = BASE_DIR / 'staticfiles'   # for Render

# Enable WhiteNoise to serve static files in production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- Default Auto Field ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- Login / Logout ---
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
