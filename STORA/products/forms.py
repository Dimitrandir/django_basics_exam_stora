from django import forms
from django.forms import inlineformset_factory

from STORA.products.models import Product, Category, Suppliers, Barcode


class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        labels = {
            'name': 'Product Name',
            'delivery_price': 'Last Delivery Price',
            'sell_price': 'Selling Price',
            'quantity': 'Current Stock',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs['readonly'] = True
        self.fields['quantity'].help_text = (
            'Quantity cannot be changed manually. Use Deliveries, Sales, modules to update stock levels.'
        )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        labels = {'name': 'Category Name', 'description': 'Description'}


class SuppliersForm(forms.ModelForm):
    class Meta:
        model = Suppliers
        fields = '__all__'

        labels = {
            'name': 'Supplier Name',
            'bulstat': 'BULSTAT',
            'vat_n': 'VAT Number',
            'phone': 'Phone Number',
            'email': 'Email Address',
        }


class BarcodeForm(forms.ModelForm):
    class Meta:
        model = Barcode
        fields = ['code']
        labels = {
            'code': 'Barcode Number',
        }
        widgets = {
            'code': forms.TextInput(attrs={'placeholder': 'Scan or enter barcode'}),
        }


BarcodeFormSet = inlineformset_factory(
    Product,
    Barcode,
    form=BarcodeForm,
    extra=3,
    can_delete=True,
)