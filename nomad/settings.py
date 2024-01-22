

from pathlib import Path
import os
from dotenv import load_dotenv

# .env ファイルから環境変数を読み込む
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = os.environ.get('DEBUG', False)

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
    'django.contrib.sites', 
    'rest_framework',
    "rest_framework.authtoken",
    "djoser",
    "corsheaders",
    'accounts',
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
]

CORS_ALLOWED_ORIGINS = ['http://localhost:3000','https://nomadvision.org',]

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
        default=os.environ.get('DATABASE_URL')
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
    'CLOUD_NAME':os.environ.get('CLOUD_NAME'),
    'API_KEY': os.environ.get('API_KEY'),
    'API_SECRET': os.environ.get('API_SECRET')
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD1')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')

# Rest Framework設定
REST_FRAMEWORK = {
    # 認証が必要
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    # JWT認証
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    # 日付
    "DATETIME_FORMAT": "%Y/%m/%d %H:%M",
}

from datetime import timedelta

# JWT設定
SIMPLE_JWT = {
    # アクセストークン(1日)
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    # リフレッシュトークン(5日)
    "REFRESH_TOKEN_LIFETIME": timedelta(days=5),
    # 認証タイプ
    "AUTH_HEADER_TYPES": ("JWT",),
    # 認証トークン
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}

# Djoser設定
DJOSER = {
    # メールアドレスでログイン
    "LOGIN_FIELD": "email",
    # アカウント本登録メール
    "SEND_ACTIVATION_EMAIL": True,
    # アカウント本登録完了メール
    "SEND_CONFIRMATION_EMAIL": True,
    # メールアドレス変更完了メール
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    # パスワード変更完了メール
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    # アカウント登録時に確認用パスワード必須
    "USER_CREATE_PASSWORD_RETYPE": True,
    # メールアドレス変更時に確認用メールアドレス必須
    "SET_USERNAME_RETYPE": True,
    # パスワード変更時に確認用パスワード必須
    "SET_PASSWORD_RETYPE": True,
    # アカウント本登録用URL
    "ACTIVATION_URL": "signup/{uid}/{token}",
    # パスワードリセット完了用URL
    "PASSWORD_RESET_CONFIRM_URL": "reset-password/{uid}/{token}",
    # カスタムユーザー用シリアライザー
    "SERIALIZERS": {
        "user_create": "accounts.serializers.UserSerializer",
        "user": "accounts.serializers.UserSerializer",
        "current_user": "accounts.serializers.UserSerializer",
    },
    "EMAIL": {
        # アカウント本登録
        "activation": "accounts.email.ActivationEmail",
        # アカウント本登録完了
        "confirmation": "accounts.email.ConfirmationEmail",
        # パスワード再設定
        "password_reset": "accounts.email.ForgotPasswordEmail",
        # パスワード再設定確認
        "password_changed_confirmation": "accounts.email.ResetPasswordEmail",
    },
}

AUTH_USER_MODEL = "accounts.UserAccount"

SECRET_KEY = os.environ.get('SECRET_KEY')

if not DEBUG:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    import django_heroku
    django_heroku.settings(locals())



SITE_DOMAIN = os.environ.get('SITE_DOMAIN')
SITE_NAME = os.environ.get('SITE_NAME')

