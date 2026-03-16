from django import forms
from django.forms import inlineformset_factory
from .models import SaleItems, SaleAttributes

class SaleForms(forms.ModelForm):
    class Meta:
        model = SaleAttributes
        fields = ['cashier']

saleItemFormset = inlineformset_factory(SaleAttributes, SaleItems,
                                        fields=['sale_item', 'sale_quantity'], extra=3, can_delete=True )