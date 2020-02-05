from .models import Clients

def total_client_count(request):
    total_clients = Clients.objects.count()
    return {"total_client_count": total_clients}

