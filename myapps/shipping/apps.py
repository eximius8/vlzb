import oscar.apps.shipping.apps as apps


class ShippingConfig(apps.ShippingConfig):
    name = 'myapps.shipping'

    def ready(self):
        super().ready()
        #self.ShippingMethodView = ShippingMethodView

    def get_urls(self):
        urls = super().get_urls()

        return self.post_process_urls(urls)
