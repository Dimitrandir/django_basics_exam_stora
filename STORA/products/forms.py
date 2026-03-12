from django import forms

from STORA.products.models import Product


class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        labels = {'name': 'Product Name', 'delivery_price': 'Last Delivery Price', 'sell_price': 'Selling Price',
                  'quantity': 'Current Stock'}