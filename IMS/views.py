from django.shortcuts import render, redirect
from clients.models import Clients
from products.models import Category
from products.forms import CategoryForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from clients.client_filters import ClientsFilter
from products.category_filters import CategoryFilter
# PDF Generate
from django.http import HttpResponse
import datetime
from orders.models import Customer, Product

from .utils import render_to_pdf

@login_required
def index(request):
    clients = Clients.objects.order_by('-id')
    categories = Category.objects.order_by('-id')
    # Client Filter
    client_filter_search = ClientsFilter(request.GET, queryset=clients)
    clients = client_filter_search.qs
    # Category Filter
    category_filter_search = CategoryFilter(request.GET, queryset=categories)
    categories = category_filter_search.qs
    # Pagination for Customers
    paginator = Paginator(clients, 1)
    page = request.GET.get('page')
    paged_clients = paginator.get_page(page)
    # Pagination for Category
    paginator = Paginator(categories, 1)
    page = request.GET.get('page')
    paged_category = paginator.get_page(page)
    # Total Client Count
    total_clients = clients.count()
    context = {
        "clients": paged_clients,
        "categories": paged_category,
        "total_clients": total_clients,
        "client_filter_search": client_filter_search,
        "category_filter_search": category_filter_search
    }
    return render(request, "home.html", context)

@login_required
def create_category(request):
    if request.method == "POST":
        forms = CategoryForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("/")
    else:
        forms = CategoryForm()
    context = {
        "forms": forms
    }
    return render(request, "create_category.html", context)

@login_required()
def edit_category(request, category_id):
    category_edit = Category.objects.get(id=category_id)
    edit_category_forms = CategoryForm(instance=category_edit)

    if request.method == "POST":
        edit_category_forms = CategoryForm(request.POST, request.FILES or None, instance=category_edit)

        if edit_category_forms.is_valid():
            edit_category_forms.save()
            return redirect("/")

    context = {
        "edit_category_forms": edit_category_forms
    }
    return render(request, "edit_category.html", context)

@login_required()
def delete_category(request, category_id):
    category_delete = Category.objects.get(id=category_id)
    if request.method == "POST":
        category_delete.delete()
        return redirect("/")
    context = {
        "category_delete": category_delete
    }
    return render(request, "delete_category.html", context)

def invoice_pdf(request, order_id):
    single_order = Customer.objects.get(id=order_id)
    single_product = Product.objects.filter(customer=single_order.id)
    context = {
        "single_order": single_order,
        "single_product": single_product
    }
    pdf = render_to_pdf('pdf/invoice.html', context)
    return HttpResponse(pdf, content_type='application/pdf')

