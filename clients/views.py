from django.shortcuts import render, redirect
from .models import Clients, ClientsOrder
from .forms import ClientForm, ClientsOrderForm
from .client_filters import ClientsOrderFilter
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
@login_required
def clients_detail(request, client_id):
    # Show Client Detail
    single_client = Clients.objects.get(id=client_id)
    # Customer Wise Order Entry
    client_track = Clients.objects.get(id=client_id)
    client_order_store = ClientsOrder.objects.filter(clients=client_track.id)
    # Client Order Filter
    client_order_filter_search = ClientsOrderFilter(request.GET, queryset=client_order_store)
    client_order_store = client_order_filter_search.qs
    # Pagination
    paginator = Paginator(client_order_store, 1)
    page = request.GET.get('page')
    paged_client_order_store = paginator.get_page(page)
    # Customer Wise Total Order Count
    clients_order_count = client_order_store.count()
    context = {
        "single_client": single_client,
        "client_order_store": paged_client_order_store,
        "client_track": client_track,
        "clients_order_count": clients_order_count,
        "client_order_filter_search": client_order_filter_search
    }
    return render(request, "clients/clients_detail.html", context)

@login_required
def create_client(request):
    if request.method == "POST":
        forms = ClientForm(request.POST or None, request.FILES or None)
        if forms.is_valid():
            forms.save()
            return redirect("/")
    else:
        forms = ClientForm()
    context = {
        "forms": forms
    }
    return render(request, "clients/create_client.html", context)

@login_required
def edit_client(request, client_id):
    client_edit = Clients.objects.get(id=client_id)
    edit_client_forms = ClientForm(instance=client_edit)

    if request.method == "POST":
        edit_client_forms = ClientForm(request.POST, request.FILES or None, instance=client_edit)

        if edit_client_forms.is_valid():
            edit_client_forms.save()
            return redirect("/")

    context = {
        "edit_client_forms": edit_client_forms
    }
    return render(request, "clients/edit_client.html", context)

@login_required
def delete_client(request, client_id):
    client_delete = Clients.objects.get(id=client_id)
    if request.method == "POST":
        client_delete.delete()
        return redirect("/")
    context = {
        "client_delete": client_delete
    }
    return render(request, "clients/delete_client.html", context)

@login_required
def client_order_entry(request):
    if request.method == "POST":
        forms = ClientsOrderForm(request.POST or None)
        if forms.is_valid():
            forms.save()
            return redirect("/")
    else:
        forms = ClientsOrderForm()
    context = {
        "forms": forms
    }
    return render(request, "clients/entry_client_order.html", context)

@login_required
def edit_client_order(request, client_id):
    client_order_edit = ClientsOrder.objects.get(id=client_id)
    edit_client_order_forms = ClientsOrderForm(instance=client_order_edit)

    if request.method == "POST":
        edit_client_order_forms = ClientsOrderForm(request.POST, request.FILES or None, instance=client_order_edit)

        if edit_client_order_forms.is_valid():
            edit_client_order_forms.save()
            return redirect("/")

    context = {
        "edit_client_order_forms": edit_client_order_forms
    }
    return render(request, "clients/edit_client_order.html", context)

@login_required
def delete_client_order(request, client_id):
    client_order_delete = ClientsOrder.objects.get(id=client_id)
    if request.method == "POST":
        client_order_delete.delete()
        return redirect("/")
    context = {
        "client_order_delete": client_order_delete
    }
    return render(request, "clients/delete_client_order.html", context)

