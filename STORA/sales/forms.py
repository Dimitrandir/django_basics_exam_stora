from django import forms
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from django.forms.models import BaseInlineFormSet
from .models import SaleItems, SaleAttributes

class SaleForms(forms.ModelForm):
    class Meta:
        model = SaleAttributes
        fields = ['cashier']

saleItemFormset = inlineformset_factory(SaleAttributes, SaleItems,
                                        fields=['sale_item', 'sale_quantity'], extra=9, can_delete=True)

