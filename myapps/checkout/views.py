from oscar.apps.checkout.views import ShippingMethodView as CoreShippingMethodView
from django.conf import settings
from django.views.generic import FormView


# class ShippingMethodView(CoreShippingMethodView):
#     template_name = 'offer/new_list.html'

from oscar.apps.checkout import views
from oscar.apps.payment import models



from . import forms

from django.urls import reverse, reverse_lazy
from oscar.core.loading import get_model, get_class
from oscar.apps.checkout import exceptions

OscarPaymentMethodView = get_class("checkout.views", "PaymentMethodView")

# Sample pre-condition
class CheckCountryPreCondition(object):
    """DRY class for check country in session pre_condition"""

    def get_pre_conditions(self, request):
        if 'check_country_in_session' not in self.pre_conditions:
            return self.pre_conditions + ['check_country_in_session']
        return super().get_pre_conditions(request)

    def check_country_in_session(self, request):
        if request.session.get('country', None) is None:
            raise exceptions.FailedPreCondition(
                    url=reverse('checkout:shipping-address'),
                )


class PaymentMethodView(OscarPaymentMethodView, FormView):
    """
    View for a user to choose which payment method(s) they want to use.

    This would include setting allocations if payment is to be split
    between multiple sources. It's not the place for entering sensitive details
    like bankcard numbers though - that belongs on the payment details view.
    """
    template_name = "customcheckout/payment_method.html"
    step = 'payment-method'
    form_class = forms.PaymentMethodForm
    success_url = reverse_lazy('checkout:payment-details')

    pre_conditions = [
        'check_basket_is_not_empty',
        'check_basket_is_valid',
        'check_user_email_is_captured',
        'check_shipping_data_is_captured',
        'check_payment_data_is_captured',
    ]
    skip_conditions = ['skip_unless_payment_is_required']

    def get(self, request, *args, **kwargs):
        # if only single payment method, store that
        # and then follow default (redirect to preview)
        # else show payment method choice form
        if len(settings.OSCAR_PAYMENT_METHODS) == 1:
            self.checkout_session.pay_by(settings.OSCAR_PAYMENT_METHODS[0][0])
            return redirect(self.get_success_url())
        else:
            return FormView.get(self, request, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        # Redirect to the correct payments page as per the method (different methods may have different views &/or additional views)
        return reverse_lazy('checkout:preview')

    def get_initial(self):
        return {
            'payment_method': self.checkout_session.payment_method(),
        }

    def form_valid(self, form):
        # Store payment method in the CheckoutSessionMixin.checkout_session (a CheckoutSessionData object)
        self.checkout_session.pay_by(form.cleaned_data['payment_method'])
        return super().form_valid(form)

class PaymentDetailsView(views.PaymentDetailsView):

    def handle_payment(self, order_number, total, **kwargs):
        # Talk to payment gateway.  If unsuccessful/error, raise a
        # PaymentError exception which we allow to percolate up to be caught
        # and handled by the core PaymentDetailsView.
        reference = gateway.pre_auth(order_number, total.incl_tax, kwargs['bankcard'])

        # Payment successful! Record payment source
        source_type, __ = models.SourceType.objects.get_or_create(name="SomeGateway")
        source = models.Source(
            source_type=source_type,
            amount_allocated=total.incl_tax,
            reference=reference)
        self.add_payment_source(source)

        # Record payment event
        self.add_payment_event('pre-auth', total.incl_tax)
