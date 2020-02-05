import django_filters
from .models import *
from django_filters import CharFilter

class OrderFilter(django_filters.FilterSet):
    ref_no = CharFilter(field_name='ref_no', lookup_expr='icontains')
    class Meta:
        model = Customer
        fields = {
            'phone'
        }
