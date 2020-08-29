import os

from oscar.defaults import *
from .variables import *
from .fixed import *

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'django.contrib.flatpages',

    # Additional apps
    'storages', # pip install django-storages

    'allauth', # pip install django-allauth
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.vk',
    'allauth.socialaccount.providers.odnoklassniki',
    'allauth.socialaccount.providers.mailru',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',

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
]





if os.getenv('GAE_APPLICATION', None):
    # Running on production App Engine, so connect to Google Cloud SQL using
    # the unix socket at /cloudsql/<your-cloudsql-connection string>   
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/bezoder:us-central1:bezoder-mysql-micro',
            'USER': MYSQL_USER,
            'PASSWORD': MYSQL_USER_PASS,
            'NAME': 'mag34',
        }
    }
elif eval(os.getenv('DEBUG', "False")):
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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }    
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'NAME': 'mag34',
            'USER': MYSQL_USER,
            'PASSWORD': MYSQL_USER_PASS,
        }
    }

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



STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'



STATIC_URL = 'https://storage.googleapis.com/{}/static/'.format(GS_BUCKET_NAME)
#STATIC_ROOT = "static/"

MEDIA_URL = 'https://storage.googleapis.com/{}/media/'.format(GS_BUCKET_NAME)
#MEDIA_ROOT = "media/"

#UPLOAD_ROOT = 'media/uploads/'


#DOWNLOAD_ROOT = os.path.join(BASE_DIR, "static/media/downloads")
DOWNLOAD_URL = STATIC_URL + "media/downloads"


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


OSCAR_DASHBOARD_NAVIGATION += [
    {
        'label': 'Отправка',
        'children': [
            {
                'label': 'Shipping',
                'url_name': 'dashboard:shipping-method-list',
            },
         ]
    },
]