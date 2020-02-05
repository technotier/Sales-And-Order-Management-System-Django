from django import forms
from .models import Clients, ClientsOrder

class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: John Doe'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ex: john@gmail.com'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 01785625623'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 15}),
        }


class ClientsOrderForm(forms.ModelForm):
    class Meta:
        model = ClientsOrder
        fields = '__all__'

        widgets = {
            'ref_no': forms.TextInput(attrs={'class': 'form-control'}),
            'order_submit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jan 20, 2020'}),
            'order_delivered': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jan 20, 2020'}),
            'invoice_total': forms.NumberInput(attrs={'class': 'form-control'}),
            'deposit': forms.NumberInput(attrs={'class': 'form-control'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 15}),
        }

