import logging

from django.conf import settings
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import FormView


from oscar.apps.checkout import views, exceptions
from oscar.apps.checkout.mixins import OrderPlacementMixin
from oscar.apps.payment import forms, models


#from paypal.payflow import facade



from .forms import PaymentMethodForm



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
    """
    An example view that shows how to integrate BOTH Paypal Express
    (see get_context_data method)and Payppal Flow (the other methods).
    Naturally, you will only want to use one of the two.
    """
    template_name = 'checkout/payment_details.html'
    template_name_preview = 'checkout/preview.html'
    skip_conditions = ['skip_unless_payment_is_required', 'skip_for_cod_payment']
    



    def skip_for_cod_payment(self, request):
        """
        if payment method is cash on delivery skip the view
        """
        method = self.checkout_session.payment_method()
        if not self.preview:
            raise exceptions.PassedSkipCondition(
                url=reverse('checkout:preview')
            )





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
    
    



        
        


    # def handle_place_order_submission(self, request):
    #     # Helper method to check that the hidden forms wasn't tinkered
    #     # with.
    # #    bankcard_form = forms.BankcardForm(request.POST)
    # #    billing_address_form = forms.BillingAddressForm(request.POST)
    #     if False:#not all([bankcard_form.is_valid(),
    #             #    billing_address_form.is_valid()]):
    #         messages.error(request, "Invalid submission")
    #         return HttpResponseRedirect(reverse('checkout:payment-details'))

    #     # Attempt to submit the order, passing the bankcard object so that it
    #     # gets passed back to the 'handle_payment' method below.
    #     submission = self.build_submission()
    #     #submission['payment_kwargs']['bankcard'] = bankcard_form.bankcard
    #     #submission['payment_kwargs']['billing_address'] = billing_address_form.cleaned_data
    #     return self.submit(**submission)

    # def handle_payment(self, order_number, total, **kwargs):
    #     """
    #     Make submission to PayPal
    #     """
    #     # Using authorization here (two-stage model).  You could use sale to
    #     # perform the auth and capture in one step.  The choice is dependent
    #     # on your business model.
    #     #facade.authorize(
    #      #   order_number, total.incl_tax,
    #       #  kwargs['bankcard'], kwargs['billing_address']
    #       #  )

    #     # Record payment source and event
    #   #  source_type, is_created = models.SourceType.objects.get_or_create(
    #    #     name='PayPal')
    #     source = source_type.sources.model(
    #         source_type=source_type,
    #         amount_allocated=total.incl_tax, currency=total.currency)
    #     self.add_payment_source(source)
    #     self.add_payment_event('Authorised', total.incl_tax)
