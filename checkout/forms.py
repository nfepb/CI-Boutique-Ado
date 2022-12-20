from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Telling Django which fields it will be associated
    with.
    """
    class Meta:
        model.Order
        fields = (
            'full_name',
            'email',
            'phone_number',
            'country',
            'postcode',
            'town_or_city',
            'street_address_1',
            'street_address_2',
            'county',
        )

    def __init__(self, *args, **kwargs):
        """
        Adds placeholders and classes, remove auto-
        generated placeholders and set autofocus on
        1st field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postcode',
            'town_or_city': 'Town or City',
            'street_address_1': 'Street Address 1',
            'street_address_2': 'Street Address 2',
            'county': 'County',
        }

    self.fields['full_name'].widget.attrs['autofocus'] = True
    for field in self.fields:
        if self.fields[field].required:
            placeholder = f"{placeholders[field]} *"
        else:
            placeholder = placeholders[field]
        self.placeholders[field].widget.attrs['placeholder'] = placeholder
        self.placeholders[field].widget.attrs['class'] = 'stripe-style-input'
        self.placeholders[field].label = False
