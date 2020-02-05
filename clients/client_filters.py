import django_filters
from .models import *
from django_filters import CharFilter

class ClientsFilter(django_filters.FilterSet):
    email = CharFilter(field_name='email', lookup_expr='icontains')
    class Meta:
        model = Clients
        fields = {
            'phone'
        }

class ClientsOrderFilter(django_filters.FilterSet):
    ref_no = CharFilter(field_name='ref_no', lookup_expr='icontains')
    class Meta:
        model = ClientsOrder
        fields = {
            'invoice_total'
        }