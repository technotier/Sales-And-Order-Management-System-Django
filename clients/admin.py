from django.contrib import admin
from .models import Clients, ClientsOrder

# Register your models here.
admin.site.register(Clients)
admin.site.register(ClientsOrder)

