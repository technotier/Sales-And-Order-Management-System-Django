import django_filters
from .models import *
from django_filters import CharFilter

class WarehouseFilter(django_filters.FilterSet):
    product = CharFilter(field_name='product', lookup_expr='icontains')
    supplier_name = CharFilter(field_name='supplier_name', lookup_expr='icontains')
    class Meta:
        model = Warehouse
        fields = {
            'supplier_phone'
        }
