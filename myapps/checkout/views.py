from oscar.apps.checkout.views import ShippingMethodView as CoreShippingMethodView


class ShippingMethodView(CoreShippingMethodView):
    template_name = 'offer/new_list.html'
