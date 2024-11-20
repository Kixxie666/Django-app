import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-4s$)jbf@=6b0n08bpca@f7l7qhbdzx)gmha(&-$k^=jm2*4bro')

# SECURITY WARNING: don't run with debug turned on in production!
WEBSITE_HOSTNAME = os.environ.get('WEBSITE_HOSTNAME', None)
DEBUG = WEBSITE_HOSTNAME == None

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'itreporting',
    'users.apps.UsersConfig',
    'crispy_forms',
    'crispy_bootstrap4',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'itapps.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'itapps.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DjangoDB1',
        'USER': 'C2025401',
        'PASSWORD': 'Password123!',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# Use environment variables if available
AZURE_SA_NAME = os.environ.get('AZURE_SA_NAME', 'your_default_storage_account_name')  # Fallback to a default if not set
AZURE_SA_KEY = os.environ.get('AZURE_SA_KEY', 'your_default_storage_account_key')  # Fallback to a default if not set
AZURE_CONNECTION_STRING = os.environ.get('AZURE_CONNECTION_STRING', None)  # Optionally use a connection string

# Optionally, you can use connection string for authentication (preferred method in some cases)
if AZURE_CONNECTION_STRING:
    storage_options = {
        "connection_string": AZURE_CONNECTION_STRING,
        "azure_container": "static",
    }
else:
    storage_options = {
        "account_name": AZURE_SA_NAME,
        "account_key": AZURE_SA_KEY,
        "azure_container": "static",
    }

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.azure_storage.AzureStorage",
        "OPTIONS": {
            **storage_options,
            "azure_container": "media",  # Container for media files
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.azure_storage.AzureStorage",
        "OPTIONS": {
            **storage_options,
            "azure_container": "static",  # Container for static files
        },
    },
}

STATIC_URL = f'https://{AZURE_SA_NAME}.blob.core.windows.net/static/'
MEDIA_URL = f'https://{AZURE_SA_NAME}.blob.core.windows.net/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap4'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_REDIRECT_URL = 'itreporting:home'
LOGIN_URL = 'itreporting:home'
