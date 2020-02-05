from django.urls import path
from . import views

urlpatterns = [
    path('<str:client_id>', views.clients_detail, name='clients_detail'),
    path('create-client/', views.create_client, name='create_client'),
    path('edit-client/<str:client_id>', views.edit_client, name='edit_client'),
    path('delete-client/<str:client_id>', views.delete_client, name='delete_client'),
    path('client-order-entry/', views.client_order_entry, name='client_order_entry'),
    path('edit-client-order/<str:client_id>', views.edit_client_order, name='edit_client_order'),
    path('delete-client-order/<str:client_id>', views.delete_client_order, name='delete_client_order'),
]

