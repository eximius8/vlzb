import os

from oscar.defaults import *
from .variables import *


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SESSION_ENGINE =  'django.contrib.sessions.backends.signed_cookies' 

ROOT_URLCONF = 'vlzb.urls'

WSGI_APPLICATION = 'vlzb.wsgi.application'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.flatpages',

    'oscar.config.Shop',
    'oscar.apps.analytics.apps.AnalyticsConfig',
    #'oscar.apps.checkout.apps.CheckoutConfig',
    'myapps.checkout.apps.CheckoutConfig',
    'oscar.apps.address.apps.AddressConfig',
    #'oscar.apps.shipping.apps.ShippingConfig',
    'myapps.shipping.apps.ShippingConfig',
    'oscar.apps.catalogue.apps.CatalogueConfig',
    'oscar.apps.catalogue.reviews.apps.CatalogueReviewsConfig',
    'oscar.apps.communication.apps.CommunicationConfig',
    'oscar.apps.partner.apps.PartnerConfig',
    'oscar.apps.basket.apps.BasketConfig',
    'oscar.apps.payment.apps.PaymentConfig',
    'oscar.apps.offer.apps.OfferConfig',
    #'oscar.apps.order.apps.OrderConfig',
    'myapps.order.apps.OrderConfig',
    'oscar.apps.customer.apps.CustomerConfig',
    'oscar.apps.search.apps.SearchConfig',
    'oscar.apps.voucher.apps.VoucherConfig',
    'oscar.apps.wishlists.apps.WishlistsConfig',
    'oscar.apps.dashboard.apps.DashboardConfig',
    'oscar.apps.dashboard.reports.apps.ReportsDashboardConfig',
    'oscar.apps.dashboard.users.apps.UsersDashboardConfig',
    'oscar.apps.dashboard.orders.apps.OrdersDashboardConfig',
    'oscar.apps.dashboard.catalogue.apps.CatalogueDashboardConfig',
    'oscar.apps.dashboard.offers.apps.OffersDashboardConfig',
    'oscar.apps.dashboard.partners.apps.PartnersDashboardConfig',
    'oscar.apps.dashboard.pages.apps.PagesDashboardConfig',
    'oscar.apps.dashboard.ranges.apps.RangesDashboardConfig',
    'oscar.apps.dashboard.reviews.apps.ReviewsDashboardConfig',
    'oscar.apps.dashboard.vouchers.apps.VouchersDashboardConfig',
    'oscar.apps.dashboard.communications.apps.CommunicationsDashboardConfig',
    'oscar.apps.dashboard.shipping',

    # 3rd-party apps that oscar depends on
    'widget_tweaks',
    'haystack',
    'treebeard',
    'sorl.thumbnail',
    'django_tables2',  

    # Additional apps
    'storages', # pip install django-storages
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'vlzb/templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.communication.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
        'URL': 'http://127.0.0.1:8983/solr',
        'INCLUDE_SPELLING': True,
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# Oscar variables
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



OSCAR_DASHBOARD_NAVIGATION += [
    {
        'label': 'Shipping',
        'children': [
            {
                'label': 'Shipping',
                'url_name': 'dashboard:shipping-method-list',
            },
         ]
    },
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


# STATICFILES_DIRS = [    
#     os.path.join(BASE_DIR, 'static'),
# ]


# if not os.getenv('GAE_APPLICATION', None):
#     UPLOAD_ROOT = os.path.join(BASE_DIR, 'media/')    
#     STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

#     STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#     STATIC_URL = '/static/'

#     MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#     MEDIA_URL = '/media/'  
    
    
#     DOWNLOAD_ROOT = os.path.join(BASE_DIR, "media")
#     DOWNLOAD_URL = "/media/"
    
# else: 
    # for prod environment

DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'

GS_PROJECT_ID = 'bezoder'
GS_BUCKET_NAME = 'mag34'
GS_STATIC_BUCKET_NAME = 'mag34'
GS_MEDIA_BUCKET_NAME = 'mag34'

STATIC_URL = 'https://storage.googleapis.com/{}/static/'.format(GS_STATIC_BUCKET_NAME)
STATIC_ROOT = "static/"

MEDIA_URL = 'https://storage.googleapis.com/{}/media/'.format(GS_MEDIA_BUCKET_NAME)
MEDIA_ROOT = "media/"

UPLOAD_ROOT = 'media/uploads/'

PROJECT_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
DOWNLOAD_ROOT = os.path.join(PROJECT_ROOT, "static/media/downloads")
DOWNLOAD_URL = STATIC_URL + "media/downloads"


# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
#     }
# }


# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
#         'LOCATION': '/tmp/memcached.sock',
#     }
# }