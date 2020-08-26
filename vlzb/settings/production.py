from .base import *

# https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/


DEBUG = eval(os.getenv('DEBUG', "False"))

# age of connect ion to db
SESSION_COOKIE_AGE = 600000
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CONN_MAX_AGE = 3600

ALLOWED_HOSTS = ['.mag34.ru','www.mag34.ru']


