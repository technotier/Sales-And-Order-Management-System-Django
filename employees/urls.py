from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('employee/<str:employee_id>', views.employee_detail, name='employee_detail'),
    path('add-employee', views.add_employee, name='add_employee'),
    path('edit-employee/<str:employee_id>', views.edit_employee, name='edit_employee'),
    path('delete-employee/<str:employee_id>', views.delete_employee, name='delete_employee'),
    path('accounts/', views.account_settings, name='account_settings'),
    path('profile/', views.profile_settings, name='profile_settings'),
]

