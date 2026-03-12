from STORA.accounts.models import Employee
from django import forms

class AccountsForms(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        labels = {'first_name': 'First Name',  'last_name': 'Last Name', 'phone': 'Phone Number',
                  'email': 'Email Address', 'role': 'Position'}

        widgets = {'phone': forms.TextInput(attrs={'placeholder': '+359'})}