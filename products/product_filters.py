import django_filters
from .models import *
from django_filters import CharFilter

class ItemFilter(django_filters.FilterSet):
    Brand = CharFilter(field_name='brand_name', lookup_expr='icontains')
    class Meta:
        model = Item
        fields = {
            'price'
        }
