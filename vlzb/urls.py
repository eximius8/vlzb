from django.apps import apps
from django.urls import include, path
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
#from oscar.apps import shop
#from paypal.express.dashboard.app import application

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.

    path(settings.SECRET_ADMIN_URL, admin.site.urls),   

    # paypal
   # path('checkout/paypal/', include('paypal.express.urls')),
    # Optional paypal
    #path(r'^dashboard/paypal/express/', application.urls),

    path('', include(apps.get_app_config('oscar').urls[0])),  
] 

#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


