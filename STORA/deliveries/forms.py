from django import forms
from django.forms import inlineformset_factory
from STORA.deliveries.models import DeliveryAttributes, DeliveryItems


class DeliveryForms(forms.ModelForm):
    class Meta:
        model = DeliveryAttributes
        fields = ['receiver', 'supplier' , 'time_of_delivery', 'document_type', 'document_number', 'document_date']
        labels = {'receiver': 'Receiver', 'time_of_delivery': 'Delivery Date', 'document_type': 'Document Type',
                  'document_number': 'Document Number', 'document_date': 'Document Date', 'supplier': 'Supplier'}
        widgets = {'document_date': forms.DateInput(attrs={'type': 'date'})}

    def __init__(self, *args, current_user=None, **kwargs):
        super().__init__(*args, **kwargs)
        if current_user is not None:
            self.fields['receiver'].disabled = True
            self.fields['receiver'].initial = current_user


class DeliveryItemForm(forms.ModelForm):

    product_code = forms.CharField(
        label='Product Code / Barcode',
        required=False,
        widget=forms.TextInput(attrs={'class': 'product-code-input', 'placeholder': 'Scan or type code'})
    )

    product_name = forms.CharField(
        label='Product Name',
        required=False,
        disabled=True,
        widget=forms.TextInput(attrs={'class': 'product-name-input'})
    )

    delivery_quantity = forms.IntegerField(
        label='Quantity',
        required=False,
        widget=forms.NumberInput(attrs={'min': 1, 'class': 'quantity-input'})
    )

    delivery_price = forms.DecimalField(
        label='Unit Price',
        required=False,
        decimal_places=2,
        max_digits=9,
        widget=forms.NumberInput(attrs={'class': 'unit-price-input'})
    )

    line_total = forms.DecimalField(
        label='Line Total',
        required=False,
        disabled=True,
        decimal_places=2,
        max_digits=9,
        widget=forms.NumberInput(attrs={'class': 'line-total-input'})
    )

    class Meta:
        model = DeliveryItems
        fields = ['delivery_item', 'delivery_quantity', 'price_at_delivery', 'total_price_row']
        widgets = {
            'delivery_item': forms.HiddenInput(),
            'price_at_delivery': forms.HiddenInput(),
            'total_price_row': forms.HiddenInput(),
        }


DeliveryItemFormSet = inlineformset_factory(
    DeliveryAttributes,
    DeliveryItems,
    form=DeliveryItemForm,
    extra=1,
    can_delete=True,
)


