import logging
import uuid

from django.conf import settings
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, FormView


from oscar.apps.checkout import views, exceptions
from oscar.apps.checkout.mixins import OrderPlacementMixin
from oscar.apps.payment import forms, models

from .forms import PaymentMethodForm


from yandex_checkout import Configuration, Payment

Configuration.account_id = 'dsadsadasdsa'
Configuration.secret_key = 'dsadasdsa'

# payment = Payment.create({
#     "amount": {
#         "value": "100.00",
#         "currency": "RUB"
#     },
#     "confirmation": {
#         "type": "redirect",
#         "return_url": "https://www.merchant-website.com/return_url"
#     },
#     "capture": True,
#     "description": "Заказ №1"
# }, uuid.uuid4())



# ==============
# Payment method
# ==============


class PaymentMethodView(views.PaymentMethodView, FormView):
    """
    View for a user to choose which payment method(s) they want to use.

    This would include setting allocations if payment is to be split
    between multiple sources. It's not the place for entering sensitive details
    like bankcard numbers though - that belongs on the payment details view.
    """
    template_name = "checkout/payment_method.html"
    step = 'payment-method'
    form_class = PaymentMethodForm
    success_url = reverse_lazy('checkout:payment-details')
    pre_conditions = [
        'check_basket_is_not_empty',
        'check_basket_is_valid',
        'check_user_email_is_captured',
        'check_shipping_data_is_captured',]

    skip_conditions = ['skip_unless_payment_is_required']

    def get_success_response(self):
        # No errors in get(), apply our form logic.
        # NOTE that the checks are not make in the post() call, but this is not a problem.
        # We can just store the payment method, and let the next view validate the other states again.
        return FormView.get(self, self.request, self.args, self.kwargs)


    def get_initial(self):
        return {
            'payment_method': self.checkout_session.payment_method(),
        }

    def form_valid(self, form):
        # Store payment method in the CheckoutSessionMixin.checkout_session (a CheckoutSessionData object)
        self.checkout_session.pay_by(form.cleaned_data['payment_method'])
        return super(PaymentMethodView, self).form_valid(form)


class PaymentDetailsView(views.PaymentDetailsView, OrderPlacementMixin):


    template_name = 'checkout/payment_details.html'
    template_name_preview = 'checkout/preview.html'

    pre_conditions = [
        'check_basket_is_not_empty',
        'check_basket_is_valid',
        'check_user_email_is_captured',
        'check_shipping_data_is_captured',
        'check_payment_method_is_captured',]

    def check_payment_method_is_captured(self, request):
        if not self.checkout_session.payment_method():
            raise exceptions.FailedPreCondition(
                url=reverse('checkout:payment-method'),
                message="Пожалуйста выберите метод оплаты"
            )


    def handle_payment(self, order_number, total, **kwargs):
        """
        Handle any payment processing and record payment sources and events.

        This method is designed to be overridden within your project.  The
        default is to do nothing as payment is domain-specific.

        This method is responsible for handling payment and recording the
        payment sources (using the add_payment_source method) and payment
        events (using add_payment_event) so they can be
        linked to the order when it is saved later on.
        """
        pass


    def handle_payment_details_submission(self, request):

        return redirect(reverse_lazy('checkout:preview'))


    def get(self, request, **kwargs):
        if not self.preview:
            return redirect(reverse_lazy('checkout:preview'))
        return self.render_preview(request, **kwargs)


    def render_preview(self, request, **kwargs):
        """
        Show a preview of the order.

        If sensitive data was submitted on the payment details page, you will
        need to pass it back to the view here so it can be stored in hidden
        form inputs.  This avoids ever writing the sensitive data to disk.
        """
        self.preview = True
        ctx = self.get_context_data(**kwargs)
        method = self.checkout_session.payment_method()
        if method == 'cod':
            ctx['payment_method'] = 'Оплата наличными при получении - '
        else:
            ctx['payment_method'] = 'Оплата онлайн на яндекс - '
        return self.render_to_response(ctx)



    def handle_place_order_submission(self, request):
      
        if False:#not all([bankcard_form.is_valid(),
                #    billing_address_form.is_valid()]):
            messages.error(request, "Invalid submission")
            return HttpResponseRedirect(reverse('checkout:payment-details'))

        # Attempt to submit the order, passing the bankcard object so that it
        # gets passed back to the 'handle_payment' method below.
        submission = self.build_submission()
        #submission['payment_kwargs']['bankcard'] = bankcard_form.bankcard
        #submission['payment_kwargs']['billing_address'] = billing_address_form.cleaned_data
        return self.submit(**submission)


class ThankYouView(views.ThankYouView, DetailView):

    template_name = 'checkout/thank_you.html'