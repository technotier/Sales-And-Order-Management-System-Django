from django import forms
from django.forms import modelformset_factory
from .models import Customer, Product

class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('ref_no', 'name', 'phone', 'email', 'delivery_date', 'payment_type', 'order_status' )
        labels = {
            'ref_no': 'Ref No.',
            'name': 'Customer Name',
            'phone': 'Phone Number',
            'email': 'Email',
            'delivery_date': 'Delivery Date',
            'payment_type': 'Payment Type',
            'order_status': 'Order Status',
        }

ProductFormset = modelformset_factory(
    Product,
    fields=('name', 'price', 'discount_price', 'quantity', 'quantity_measurement', ),
    extra=1,
    widgets={
        'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
        'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
        'discount_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Discount Price'}),
        'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),
        'quantity_measurement': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'KG/Piece'}),
    }
)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

        widgets = {
            'ref_no': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'delivery_date': forms.TextInput(attrs={'class': 'form-control'}),
        }

