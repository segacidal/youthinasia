"""
Django settings for youthinasia project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(__file__)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j8z^f^soaxl$(jl4=$#-(h5a4dk5i**9vhc5j%e3g(npr(nr08'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
   # os.path.join(os.path.dirname(__file__), 'templates'),
   '/home/clint/wwwDjango/youthinasia/templates',
)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gallery',
    'battleship',
    'pullups',
    'gymlog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'youthinasia.urls'

WSGI_APPLICATION = 'youthinasia.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


# Some simple database control - will need to imrpove this later
if os.getcwd() != '/home/clint/wwwDjango/youthinasia':
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'dev_db',
            #'ENGINE': 'django.db.backends.mysql',
            #'NAME': 'Django',
            #'USER': 'root',
            #'PASSWORD': 'Hanshot1st',
            #'HOST': 'localhost'
        }
    }
else:
    DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'mydatabase',
            #'ENGINE': 'django.db.backends.mysql',
            #'NAME': 'Django',
            #'USER': 'root',
            #'PASSWORD': 'Hanshot1st',
            #'HOST': 'localhost'
        }
    }


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(PROJECT_DIR, 'static'),)

MEDIA_ROOT = '/home/clint/wwwDjango/youthinasia/youthinasia/static/'
MEDIA_URL = ''
