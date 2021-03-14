import os
import pathlib
import dj_database_url
from .dev import *

############
# DATABASE #
############
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'bo1': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bo1',
        'USER': 'root',
        'PASSWORD': '@Dmin123',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    },
    'bo2': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bo2',
        'USER': 'root',
        'PASSWORD': '@Dmin123',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    },
    'data_write': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dataana',
        'USER': 'root',
        'PASSWORD': '@Dmin123',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}


############
# SECURITY #
############

DEBUG = bool(os.getenv('DJANGO_DEBUG', ''))

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', SECRET_KEY)

# Set to your Domain here (eg. 'django-vue-template-demo.herokuapp.com')
ALLOWED_HOSTS = ['*']