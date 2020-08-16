from .base import *

import os

DEBUG = True

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# http://michael-borisov.com/2014/10/09/yandex-smtp-and-django/

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = os.environ.get('BEZODER_EMAIL_SMTP')
EMAIL_HOST_USER = os.environ.get('BEZODER_EMAIL') 
EMAIL_PORT = 587
EMAIL_USE_TLS = True
OSCAR_FROM_EMAIL = os.environ.get('BEZODER_EMAIL')


EMAIL_HOST_PASSWORD = os.environ.get('BEZODER_EMAIL_PASSWORD')


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



ALLOWED_HOSTS = ['*']



