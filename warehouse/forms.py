from django import forms
from .models import Warehouse

class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = '__all__'

        widgets = {
            'product': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'qty': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '150'}),
            'measurement': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'KG/Packet'}),
            'original_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '150'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '200'}),
            'supplier_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Supplier Name'}),
            'supplier_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Supplier Phone'}),
            'in_house': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Jan 01, 2020'}),
        }
