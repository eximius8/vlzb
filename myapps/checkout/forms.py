from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from oscar.apps.checkout.forms import ShippingAddressForm as OldShippingAddressForm
from oscar.core.loading import get_model

VOLGA_CITIES = [
    ('Волжский', 'Волжский'),
    ('Волгоград', 'Волгоград'),
    ('Средняя Ахтуба', 'Средняя Ахтуба'),    
    ('Краснослободск', 'Краснослободск'),
]

class  ShippingAddressForm(OldShippingAddressForm):

    class Meta:        
        model = get_model('order', 'shippingaddress')
        fields = [
            'first_name', 'last_name', #'title',
            'line1', 'line2', #'line3', #'line4',
            'state', 
            'postcode', 'country',
            'phone_number', 'notes',
        ]
        labels = {
            'first_name': 'Имя и Отчество (при наличии)',
            'state': 'Город',
           # 'title': 'Отчество (при наличии)',
           # 'line1': 'Отчество (при наличии)',
         #   'line2': 'Первая строка адреса', 
          #  'line3': 'Вторая строка адреса',            
        }
        widgets = {
            'state': forms.Select(choices=VOLGA_CITIES),
            'title': forms.TextInput(attrs={'maxlength':50}),
        }


class PaymentMethodForm(forms.Form):
    """
    Extra form for the custom payment method.
    """
    payment_method = forms.ChoiceField(
        label=_("Выберите способ оплаты"),
        choices=settings.OSCAR_PAYMENT_METHODS,
        widget=forms.RadioSelect()
    )


    def get_payment_method_display(payment_method):
        return dict(settings.OSCAR_PAYMENT_METHODS).get(payment_method)