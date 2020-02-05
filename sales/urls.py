from django.urls import path
from . import views

urlpatterns = [
    path('sales_list', views.sales_list, name='sales_list'),
    path('create-sales', views.create_sales, name='create_sales'),
    path('edit-sales/<str:sales_id>', views.edit_sales, name='edit_sales'),
    path('delete-sales/<str:sales_id>', views.delete_sales, name='delete_sales'),
]

