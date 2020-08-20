from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from oscar.apps.checkout.forms import ShippingAddressForm as OldShippingAddressForm
from oscar.core.loading import get_model

VOLGA_CITIES = [
    ('VLZ', 'Волжский'),
    ('VLG', 'Волгоград'),
    ('SRA', 'Средняя Ахтуба'),
    ('LEN', 'Ленинск'),
    ('KRA', 'Краснослободск'),
]

class  ShippingAddressForm(OldShippingAddressForm):

    class Meta:        
        model = get_model('order', 'shippingaddress')
        fields = [
            'first_name', 'last_name',
            'line2', 'line1', 'line3', #'line4',
            'state', 
            'postcode', 'country',
            'phone_number', 'notes',
        ]
        labels = {
            'state': 'Город',
            'line2': 'Отчество (при наличии)',
            'line1': 'Первая строка адреса', 
            'line3': 'Вторая строка адреса',            
        }
        widgets = {
            'state': forms.Select(choices=VOLGA_CITIES),
        }


class PaymentMethodForm(forms.Form):
    """
    Extra form for the custom payment method.
    """
    payment_method = forms.ChoiceField(
        label=_("Select a payment method"),
        choices=settings.OSCAR_PAYMENT_METHODS,
        widget=forms.RadioSelect()
    )


    def get_payment_method_display(payment_method):
        return dict(settings.OSCAR_PAYMENT_METHODS).get(payment_method)