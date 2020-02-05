from django.shortcuts import render, redirect
from .models import Warehouse
from .forms import WarehouseForm
from .warehouse_filters import WarehouseFilter
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from IMS.custom_decorators import role_required, admin_only

# Create your views here.
@login_required
@admin_only
def warehouse_list(request):
    warehouses = Warehouse.objects.order_by('-id')
    # Client Order Filter
    warehouse_filter_search = WarehouseFilter(request.GET, queryset=warehouses)
    warehouses = warehouse_filter_search.qs
    # Pagination
    paginator = Paginator(warehouses, 1)
    page = request.GET.get('page')
    paged_warehouses = paginator.get_page(page)
    context = {
        "warehouses": paged_warehouses,
        "warehouse_filter_search": warehouse_filter_search
    }
    return render(request, "warehouse/warehouse_list.html", context)

@login_required
@admin_only
def create_warehouse(request):
    if request.method == "POST":
        forms = WarehouseForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("warehouse_list")
    else:
        forms = WarehouseForm()
    context = {
        "forms": forms
    }
    return render(request, "warehouse/create_warehouse.html", context)

@login_required()
@admin_only
def edit_warehouse(request, warehouse_id):
    warehouse_edit = Warehouse.objects.get(id=warehouse_id)
    edit_warehouse_forms = WarehouseForm(instance=warehouse_edit)

    if request.method == "POST":
        edit_warehouse_forms = WarehouseForm(request.POST, request.FILES or None, instance=warehouse_edit)

        if edit_warehouse_forms.is_valid():
            edit_warehouse_forms.save()
            return redirect("warehouse_list")

    context = {
        "edit_warehouse_forms": edit_warehouse_forms
    }
    return render(request, "warehouse/edit_warehouse.html", context)

@login_required
@admin_only
def delete_warehouse(request, warehouse_id):
    warehouse_delete = Warehouse.objects.get(id=warehouse_id)
    if request.method == "POST":
        warehouse_delete.delete()
        return redirect("warehouse_list")
    context = {
        "warehouse_delete": warehouse_delete
    }
    return render(request, "warehouse/delete_warehouse.html", context)
