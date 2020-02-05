"""IMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('accounts/', include('accounts.urls')),
    path('clients/', include('clients.urls')),
    path('employees/', include('employees.urls')),
    path('orders/', include('orders.urls')),
    path('products/', include('products.urls')),
    path('create-category', views.create_category, name='create_category'),
    path('edit-category/<str:category_id>', views.edit_category, name='edit_category'),
    path('delete-categoryt/<str:category_id>', views.delete_category, name='delete_category'),
    path('sales/', include('sales.urls')),
    path('warehouse/', include('warehouse.urls')),
    path('generate-invoice/<str:order_id>', views.invoice_pdf, name='invoice_pdf'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
