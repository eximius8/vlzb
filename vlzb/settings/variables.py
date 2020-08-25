import os


SECRET_KEY = os.environ.get('SECRET_KEY')
KASSA_ID = os.environ.get('YANDEX_KASSA_ACC_ID')
KASSA_TOKEN = os.environ.get('YANDEX_KASSA_SECRET_KEY')
# http://michael-borisov.com/2014/10/09/yandex-smtp-and-django/

EMAIL_HOST = os.environ.get('EMAIL_SMTP')
EMAIL_HOST_USER = os.environ.get('SHOP_EMAIL')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
OSCAR_FROM_EMAIL = "Магазин 34 <" + os.environ.get('SHOP_EMAIL') + ">"
EMAIL_HOST_PASSWORD = os.environ.get('SHOP_EMAIL_PASSWORD')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SITE_ID = 1
# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Volgograd'
USE_I18N = True
USE_L10N = True
USE_TZ = True


SESSION_COOKIE_AGE = 600000

# age of connect ion to db
CONN_MAX_AGE = 1000