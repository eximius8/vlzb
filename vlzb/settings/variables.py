import os

# app directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Secret keys and parameters
SECRET_KEY = os.environ.get('SECRET_KEY')
SECRET_ADMIN_URL = os.environ.get('SECRET_ADMIN_URL') 

# SQL settings
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_USER_PASS = os.environ.get('MYSQL_USER_PASS')
MYSQL_DB_NAME = os.environ.get('MYSQL_DB_NAME')

# yandex kassa
KASSA_ID = os.environ.get('YANDEX_KASSA_ACC_ID')
KASSA_TOKEN = os.environ.get('YANDEX_KASSA_SECRET_KEY')

# GCP credentials
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
GOOGLE_APPLICATION_CREDENTIALS = os.path.join(BASE_DIR, os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'))
#GS_CREDENTIALS = GOOGLE_APPLICATION_CREDENTIALS doesn't work

# Email sending credentials
EMAIL_HOST_USER = os.environ.get('SHOP_EMAIL')
EMAIL_HOST_PASSWORD = os.environ.get('SHOP_EMAIL_PASSWORD')
EMAIL_HOST = os.environ.get('EMAIL_SMTP')

EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Google Bucket settings
# gsutil cors set policy.json gs://mag34
# gsutil cors get gs://mag34 
# gsutil iam ch allUsers:objectViewer gs://mag34
# gsutil rsync -R static/  gs://mag34
GS_PROJECT_ID = 'bezoder'
GS_BUCKET_NAME = 'mag34'
GS_STATIC_BUCKET_NAME = 'mag34'
GS_MEDIA_BUCKET_NAME = 'mag34'

# Django settings
SITE_ID = 1
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Volgograd'
USE_I18N = True
USE_L10N = True
USE_TZ = True
BASE_URL = 'https://mag34.ru'

# allauth settings
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True


# Oscar variables
OSCAR_SHOP_NAME = 'ИП Бушнев'
OSCAR_SHOP_TAGLINE = "Лучшая электроника"
OSCAR_DEFAULT_CURRENCY = 'RUB'
OSCAR_FROM_EMAIL = "Магазин 34 <" + EMAIL_HOST_USER + ">"
OSCAR_REQUIRED_ADDRESS_FIELDS = ('first_name', 'last_name', 'postcode', 'state', 'phone_number')
OSCAR_INITIAL_ORDER_STATUS = 'Заказ создан'
OSCAR_INITIAL_LINE_STATUS = 'Заказ создан'
OSCAR_ORDER_STATUS_PIPELINE = {
                                'Заказ создан': ('Обработка', 'Отменен',),
                                'Обработка': ('Завершен', 'Отменен',),
                                'Отменен': (),
                                }

OSCAR_PAYMENT_METHODS = (
    ('cod', 'Оплата наличными при получении'),    
    ('yandex_kassa', 'Оплата онлайн'),
)

