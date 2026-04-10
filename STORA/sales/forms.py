from django import forms
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from django.forms.models import BaseInlineFormSet
from .models import SaleItems, SaleAttributes

class SaleForms(forms.ModelForm):
    class Meta:
        model = SaleAttributes
        fields = ['cashier']
        labels = {'cashier': 'Cashier'}

saleItemFormset = inlineformset_factory(
    SaleAttributes,
    SaleItems,
    fields=['sale_item', 'sale_quantity'],
    extra=3,
    can_delete=True,
    widgets = {
    'sale_item': forms.Select(attrs={'style': 'width: 100%;'}),
    'sale_quantity': forms.NumberInput(attrs={'min': 1}),} )


