"""
Django settings for feedsubs project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
from datetime import timedelta
import os

from decouple import config
from spinach.brokers.redis import RedisBroker, recommended_socket_opts
from redis import StrictRedis


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')


ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
    'django.contrib.flatpages',

    'bulma',
    'allauth',
    'allauth.account',

    'spinachd.apps.SpinachdConfig',

    'reader.apps.ReaderConfig',
    'um.apps.UMConfig',
]


MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'um.middleware.user_management_middleware'
]

ROOT_URLCONF = 'feedsubs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_DIR, 'templates')],
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

WSGI_APPLICATION = 'feedsubs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='postgres'),
        'USER': config('DB_USER', default='postgres'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='postgres'),
        'PORT': config('DB_PORT', default=5432, cast=int),
        'CONN_MAX_AGE': config('DB_CONN_MAX_AGE', default=120, cast=int)
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
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
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

SITE_ID = 1
APPEND_SLASH = False
DEFAULT_HTTP_PROTOCOL = 'http'


SESSION_COOKIE_AGE = 60 * 60 * 24 * 30 * 3  # About 3 months
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

LOGIN_REDIRECT_URL = '/'
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_PRESERVE_USERNAME_CASING = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_USERNAME_MIN_LENGTH = 3
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_DEFAULT_HTTP_PROTOCOL = DEFAULT_HTTP_PROTOCOL
ACCOUNT_FORMS = {
    'signup': 'um.forms.SignupFormWithToS'
}

LOGGING = {
    'version': 1,
    'incremental': False,
    'disable_existing_loggers': False,
    'filters': {},
    'formatters': {
        'default': {
            'format': '[%(asctime)s %(levelname)-5.5s %(threadName)s %(name)s] %(message)s',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'django': {
            'level': 'INFO',
        },
        'spinach': {
            'level': 'INFO',
        },
        'PIL': {
            'level': 'INFO',
        },
    }
}

SPINACH_ENGINE = {
    'broker': RedisBroker(redis=StrictRedis.from_url(
        config('REDIS_SPINACH_URL', default='redis://'),
        **recommended_socket_opts
    )),
    'namespace': 'feedsubs'
}

SPINACH_WORKER = {
    'number': config('SPINACH_WORKER_NUMBER', default=5, cast=int)
}
SPINACH_CLEAR_SESSIONS_PERIODICITY = timedelta(weeks=1)
