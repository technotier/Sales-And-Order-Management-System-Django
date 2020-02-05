from django import forms
from .models import EntryOrder

class SalesForm(forms.ModelForm):
    class Meta:
        model = EntryOrder
        fields = '__all__'

        widgets = {
            'ref_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 01785256897'}),
            'invoice_total': forms.NumberInput(attrs={'class': 'form-control'}),
            'deposit': forms.NumberInput(attrs={'class': 'form-control'}),
            'due_collection_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Jan 01, 2020'}),
            'order_delivered': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Jan 01, 2020'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 15}),
        }
