from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('create-product', views.create_product, name='create_product'),
    path('edit-product/<str:item_id>', views.edit_product, name='edit_product'),
    path('delete-product/<str:item_id>', views.delete_product, name='delete_product'),
    path('all-categories/<str:category_id>/', views.single_category, name='single_category'),
]
