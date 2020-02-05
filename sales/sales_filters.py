import django_filters
from .models import *
from django_filters import CharFilter

class EntryOrderFilter(django_filters.FilterSet):
    ref_no = CharFilter(field_name='ref_no', lookup_expr='icontains')
    class Meta:
        model = EntryOrder
        fields = {
            'phone_number'
        }
