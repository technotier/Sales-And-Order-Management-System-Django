from django.shortcuts import render, redirect
from .forms import CustomerModelForm, ProductFormset, OrderForm
from .models import Customer, Product
from django.contrib.auth.decorators import login_required
from .order_filters import OrderFilter
from django.core.paginator import Paginator

# Create your views here.
@login_required()
def create_order(request):
    if request.method == 'GET':
        customerform = CustomerModelForm(request.GET or None)
        formset = ProductFormset(queryset=Product.objects.none())
    elif request.method == 'POST':
        customerform = CustomerModelForm(request.POST)
        formset = ProductFormset(request.POST)
        if customerform.is_valid() and formset.is_valid():
            # first save this book, as its reference will be used in `Author`
            customer = customerform.save()
            for form in formset:
                # so that `book` instance can be attached.
                product = form.save(commit=False)
                product.customer = customer
                product.save()
            return redirect('order_list')
    context = {
        "customerform": customerform,
        'formset': formset,
    }
    return render(request, "orders/create_order.html", context)

@login_required()
def order_list(request):
    customers = Customer.objects.order_by('-id')

    # Client Order Filter
    order_filter_search = OrderFilter(request.GET, queryset=customers)
    customers = order_filter_search.qs

    # Pagination
    paginator = Paginator(customers, 1)
    page = request.GET.get('page')
    paged_customers = paginator.get_page(page)

    total_orders = customers.count()
    order_confirmed = customers.filter(order_status="Confirmed").count()
    order_delivered = customers.filter(order_status="Delivered").count()
    order_pending = customers.filter(order_status="Pending").count()

    context = {
        "customers": paged_customers,
        "order_filter_search": order_filter_search,
        "total_orders": total_orders,
        "order_confirmed": order_confirmed,
        "order_delivered": order_delivered,
        "order_pending": order_pending,
    }
    return render(request, "orders/order_list.html", context)

@login_required()
def order_detail(request, order_id):
    single_order = Customer.objects.get(id=order_id)
    single_product = Product.objects.filter(customer=single_order.id)
    context = {
        "single_order": single_order,
        "single_product": single_product
    }
    return render(request, "orders/order_detail.html", context)

@login_required()
def edit_order(request, order_id):
    order_edit = Customer.objects.get(id=order_id)
    edit_order_forms = OrderForm(instance=order_edit)

    if request.method == "POST":
        edit_order_forms = OrderForm(request.POST, request.FILES or None, instance=order_edit)

        if edit_order_forms.is_valid():
            edit_order_forms.save()
            return redirect("order_list")

    context = {
        "edit_order_forms": edit_order_forms
    }
    return render(request, "orders/edit_order.html", context)

@login_required()
def delete_order(request, order_id):
    order_delete = Customer.objects.get(id=order_id)
    if request.method == "POST":
        order_delete.delete()
        return redirect("order_list")
    context = {
        "order_delete": order_delete
    }
    return render(request, "orders/delete_order.html", context)

