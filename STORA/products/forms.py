from django import forms

from STORA.products.models import Product, Category, Suppliers


class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        labels = {'name': 'Product Name', 'delivery_price': 'Last Delivery Price', 'sell_price': 'Selling Price',
                  'quantity': 'Current Stock'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs['readonly'] = True
        self.fields['quantity'].help_text = '"Quantity cannot be changed manually.Use Deliveries, Sales, or Inventory Audit modules to update stock levels."'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        labels = {'name': 'Category Name', 'description': 'Description',}


class SuppliersForm(forms.ModelForm):
    class Meta:
        model = Suppliers
        fields = '__all__'

        labels = {'name': 'Supplier Name', 'bulstat': 'BULSTAT', 'vat_n': 'VAT Number',
                  'phone': 'Phone Number','email': 'Email Address',}