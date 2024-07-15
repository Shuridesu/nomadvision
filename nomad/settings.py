from pathlib import Path
import os
from dotenv import load_dotenv
from os import getenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['127.0.0.1' ,'herokuapp.com','nomadvision-e83b637ecb0f.herokuapp.com','localhost', 'nomadvision.org']

INSTALLED_APPS = [
    'nomadApp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',
    'django_bootstrap_icons',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_bootstrap5',
    'django_ckeditor_5',
    'django.contrib.sites', 
    'rest_framework',
    "rest_framework.authtoken",
    "djoser",
    "corsheaders",
    'accounts',
    'social_django',
    
]

SITE_ID = 1

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

CORS_ALLOWED_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'nomad.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'nomad.wsgi.application'

import dj_database_url
import os

DATABASES = {
    'default': dj_database_url.config(
        default=getenv('DATABASE_URL')
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


STATIC_URL = "static/"
STATIC_ROOT = str(BASE_DIR / "staticfiles")

CLOUDINARY_STORAGE  = {
    'CLOUD_NAME':getenv('CLOUD_NAME'),
    'API_KEY': getenv('API_KEY'),
    'API_SECRET': getenv('API_SECRET')
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = getenv('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_HOST_USER = getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = getenv('EMAIL_HOST_PASSWORD1')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = getenv('DEFAULT_FROM_EMAIL')
DEFAULT_TO_EMAIL = getenv('TO_EMAIL')


AUTHENTICATION_BACKENDS=[
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

# Rest Framework
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "accounts.authentication.CustomJWTAuthentication",
    ],
}

from datetime import timedelta



# Djoser設定
DJOSER = {
    "LOGIN_FIELD": "email",
    "SEND_ACTIVATION_EMAIL": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "USER_CREATE_PASSWORD_RETYPE": True,
    "SET_USERNAME_RETYPE": True,
    "SET_PASSWORD_RETYPE": True,
    "ACTIVATION_URL": "activation/{uid}/{token}",
    "PASSWORD_RESET_CONFIRM_URL": "reset-password/{uid}/{token}",
    "SERIALIZERS": {
        "user_create": "accounts.serializers.UserSerializer",
        "user": "accounts.serializers.UserSerializer",
        "current_user": "accounts.serializers.UserSerializer",
    },
    "EMAIL": {
        "activation": "accounts.email.ActivationEmail",
        "confirmation": "accounts.email.ConfirmationEmail",
        "password_reset": "accounts.email.ForgotPasswordEmail",
        "password_changed_confirmation": "accounts.email.ResetPasswordEmail",
    },
    'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': getenv('REDIRECT_URIS').split(','),
}


AUTH_USER_MODEL = "accounts.UserAccount"

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "openid",
]


#cookie settings
AUTH_COOKIE = 'access'
AUTH_COOKIE_ACCESS_MAX_AGE = 60 * 5
AUTH_COOKIE_REFRESH_MAX_AGE = 60 * 60 * 24
AUTH_COOKIE_SECURE = getenv('AUTH_COOKIE_SECURE', 'True') == 'True'
AUTH_COOKIE_HTTP_ONLY = True
AUTH_COOKIE_PATH = '/'
AUTH_COOKIE_SAMESITE = 'None'

CORS_ALLOWED_ORIGINS = getenv(
    "CORS_ALLOW_ALL_ORIGINS", "http://localhost:3000,http://127.0.0.1:3000"
).split(",")

CORS_ALLOW_CREDENTIALS = True

SECRET_KEY = getenv('SECRET_KEY')

if not DEBUG:
    SECRET_KEY = getenv('SECRET_KEY')
    import django_heroku
    django_heroku.settings(locals())

SITE_DOMAIN = getenv('SITE_DOMAIN')
SITE_NAME = getenv('SITE_NAME')
