import django_filters
from .models import Category
from django_filters import CharFilter

class CategoryFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model = Category
        fields = '__all__'