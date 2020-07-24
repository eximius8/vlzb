import oscar.apps.checkout.apps as apps

from django.urls import path
#from .views import ShippingMethodView


class CheckoutConfig(apps.CheckoutConfig):
    name = 'myapps.checkout'

    def ready(self):
        super().ready()
        #self.ShippingMethodView = ShippingMethodView

    def get_urls(self):
        urls = super().get_urls()

        return self.post_process_urls(urls)
