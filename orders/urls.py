from django.urls import path
from . import views

urlpatterns = [
    path('order-list', views.order_list, name='order_list'),
    path('create-order', views.create_order, name='create_order'),
    path('order-detail/<str:order_id>', views.order_detail, name='order_detail'),
    path('edit-order/<str:order_id>', views.edit_order, name='edit_order'),
    path('delete-order/<str:order_id>', views.delete_order, name='delete_order'),
]

