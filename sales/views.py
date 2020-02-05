from django.shortcuts import render, redirect
from .models import EntryOrder
from .forms import SalesForm
from .sales_filters import EntryOrderFilter
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def sales_list(request):
    sales = EntryOrder.objects.order_by('-id')
    # Entry Order Filter
    entry_order_filter_search = EntryOrderFilter(request.GET, queryset=sales)
    sales = entry_order_filter_search.qs
    # Pagination
    paginator = Paginator(sales, 1)
    page = request.GET.get('page')
    paged_sales = paginator.get_page(page)
    context = {
        "sales": paged_sales,
        "entry_order_filter_search": entry_order_filter_search
    }
    return render(request, "sales/sales_list.html", context)

@login_required
def create_sales(request):
    if request.method == "POST":
        forms = SalesForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("sales_list")
    else:
        forms = SalesForm()
    context = {
        "forms": forms
    }
    return render(request, "sales/create_sales.html", context)

@login_required()
def edit_sales(request, sales_id):
    sales_edit = EntryOrder.objects.get(id=sales_id)
    edit_sales_forms = SalesForm(instance=sales_edit)

    if request.method == "POST":
        edit_sales_forms = SalesForm(request.POST, request.FILES or None, instance=sales_edit)

        if edit_sales_forms.is_valid():
            edit_sales_forms.save()
            return redirect("sales_list")

    context = {
        "edit_sales_forms": edit_sales_forms
    }
    return render(request, "sales/edit_sales.html", context)

@login_required()
def delete_sales(request, sales_id):
    sales_delete = EntryOrder.objects.get(id=sales_id)
    if request.method == "POST":
        sales_delete.delete()
        return redirect("sales_list")
    context = {
        "sales_delete": sales_delete
    }
    return render(request, "sales/delete_sales.html", context)

