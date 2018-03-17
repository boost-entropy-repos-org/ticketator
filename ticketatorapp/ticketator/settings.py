"""
Django settings for ticketator project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = True if os.environ["DEBUG"] in ("true", "True") else False

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_extensions',
    'core',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ticketator.urls'

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
                'core.context_processors.logo_company',
            ],
        },
    },
]

WSGI_APPLICATION = 'ticketator.wsgi.application'

# Databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'tickets_db'),
        'USER': os.getenv('POSTGRES_USER', 'ticket_user_db'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'ticket4everyone'),
        'HOST': os.getenv('POSTGRES_HOST', '127.0.0.1'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-en'
TIME_ZONE = 'Europe/Madrid'
USE_I18N = True
USE_L10N = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_ROOT = "/var/www/media/"
if DEBUG:
    MEDIA_ROOT = "media/"  # folder to store media elements
MEDIA_URL = "/media/"  # url to serve media


SITE_NAME = 'Ticketator '
SITE_VERSION = '0.2'
DATE_INPUT_FORMATS = ['%d/%m/%y']
DATE_FORMAT = ['%d/%m/%y']

# Pagination seq
PAGINATE_BY = 15

# Auth settings
LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/login"

# Auth custom settings
AUTH_USER_MODEL = 'core.User'

# Logo ticketator
LOGO_COMPANY = STATIC_URL + 'images/logo/tk-tiny.png'

GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}
