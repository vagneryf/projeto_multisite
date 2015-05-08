"""
Django settings for projeto_multisite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# -*- coding: utf-8 -*-

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#pu3xq-22if$wc1skvx&e9782z9yq+b*yz(_!8yebr6g0hpuz6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', # default backend
    'guardian.backends.ObjectPermissionBackend', # guardian
    "site_permissions.backends.SitePermissionBackend", # site_permissions
]

ANONYMOUS_USER_ID = -1 # required for guardian


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'filebrowser',
    # 'tinymce',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'artigos',
    'categorias',
    'testes',

    'guardian',
    'site_permissions',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'projeto_multisite.urls'

WSGI_APPLICATION = 'projeto_multisite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'banco_dados.db'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

FILEBROWSER_DIRECTORY = 'uploads/'
# FILEBROWSER_DIRECTORY = getattr(settings, "FILEBROWSER_DIRECTORY", 'uploads/')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "_static")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "project_static"),
)

# Nome de exibicao pelo grappelli
GRAPPELLI_ADMIN_TITLE = u'Projeto Multisite'