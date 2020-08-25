from .base import *

# https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/
DEBUG = False

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CONN_MAX_AGE = 3600

ALLOWED_HOSTS = ['.mag34.ru']


if os.getenv('GAE_APPLICATION', None):
    # Running on production App Engine, so connect to Google Cloud SQL using
    # the unix socket at /cloudsql/<your-cloudsql-connection string>
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/bezoder:us-central1:bezoder-mysql-micro',
            'USER': MYSQL_USER,
            'PASSWORD': MYSQL_USER_PASS,
            'NAME': 'ru_bezoder_db',
        }
    }
else:
    # Running locally so connect to either a local MySQL instance or connect to
    # Cloud SQL via the proxy. To start the proxy via command line:
    #
    #     $ cloud_sql_proxy -instances=bezoder:us-central1:bezoder-mysql-micro=tcp:3306
    #       No static after link required 
    #       gsutil -m rsync -r ./static gs://ru-bezoder-static

    #
    # See https://cloud.google.com/sql/docs/mysql-connect-proxy
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'NAME': 'ru_bezoder_db',
            'USER': MYSQL_USER,
            'PASSWORD': MYSQL_USER_PASS,
        }
    }


