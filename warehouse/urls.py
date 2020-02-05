from django.urls import path
from . import views

urlpatterns = [
    path('warehouse-list', views.warehouse_list, name='warehouse_list'),
    path('create-warehouse', views.create_warehouse, name='create_warehouse'),
    path('edit-warehouse/<str:warehouse_id>', views.edit_warehouse, name='edit_warehouse'),
    path('delete-warehouse/<str:warehouse_id>', views.delete_warehouse, name='delete_warehouse'),
]
