from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

        widgets = {
            'brand_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 15}),
            'packing': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 70'}),
            'measurement': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: KG'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 550'}),
            'origin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Spain'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nylon Paste'}),
        }
