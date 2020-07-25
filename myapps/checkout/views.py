from oscar.apps.checkout.views import ShippingMethodView as CoreShippingMethodView


# class ShippingMethodView(CoreShippingMethodView):
#     template_name = 'offer/new_list.html'

from oscar.apps.checkout import views
from oscar.apps.payment import models


class PaymentMethodView(views.PaymentMethodView):


    def get(self, request, *args, **kwargs):
        # By default we redirect straight onto the payment details view. Shops
        # that require a choice of payment method may want to override this
        # method to implement their specific logic.
        return self.get_success_response('gfdgfd')

# Subclass the core Oscar view so we can customise
class PaymentDetailsView(views.PaymentMethodView):
    template='offercxzc/new_list.html'

# Subclass the core Oscar view so we can customise
class PaymentDetailsView(views.PaymentDetailsView):
    template='ocxzcxzffer/new_list.html'

    def handle_payment(self, order_number, total, **kwargs):
        # Talk to payment gateway.  If unsuccessful/error, raise a
        # PaymentError exception which we allow to percolate up to be caught
        # and handled by the core PaymentDetailsView.
        reference = gateway.pre_auth(order_number, total.incl_tax, kwargs['bankcard'])

        # Payment successful! Record payment source
        source_type, __ = models.SourceType.objects.get_or_create(
            name="SomeGateway")
        source = models.Source(
            source_type=source_type,
            amount_allocated=total.incl_tax,
            reference=reference)
        self.add_payment_source(source)

        # Record payment event
        self.add_payment_event('pre-auth', total.incl_tax)
