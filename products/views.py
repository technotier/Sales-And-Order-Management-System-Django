from django.shortcuts import render, redirect
from .models import *
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .product_filters import ItemFilter

# Create your views here.
@login_required
def product_list(request):
    items = Item.objects.order_by('-id')
    # Product Filter
    product_filter_search = ItemFilter(request.GET, queryset=items)
    items = product_filter_search.qs
    # Pagination
    paginator = Paginator(items, 1)
    page = request.GET.get('page')
    paged_items = paginator.get_page(page)
    context = {
        "items": paged_items,
        "product_filter_search": product_filter_search
    }
    return render(request, "products/product_list.html", context)

@login_required
def create_product(request):
    if request.method == "POST":
        forms = ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("product_list")
    else:
        forms = ProductForm()
    context = {
        "forms": forms
    }
    return render(request, "products/create_product.html", context)

@login_required
def edit_product(request, item_id):
    product_edit = Item.objects.get(id=item_id)
    edit_product_forms = ProductForm(instance=product_edit)

    if request.method == "POST":
        edit_product_forms = ProductForm(request.POST, request.FILES or None, instance=product_edit)

        if edit_product_forms.is_valid():
            edit_product_forms.save()
            return redirect("product_list")

    context = {
        "edit_product_forms": edit_product_forms
    }
    return render(request, "products/edit_product.html", context)

@login_required
def delete_product(request, item_id):
    product_delete = Item.objects.get(id=item_id)
    if request.method == "POST":
        product_delete.delete()
        return redirect("product_list")
    context = {
        "product_delete": product_delete
    }
    return render(request, "products/delete_product.html", context)

@login_required
def single_category(request, category_id):
    cat = Category.objects.get(id=category_id)
    items = Item.objects.filter(category=cat.id)
    context = {
        "items": items,
        "cat": cat
    }
    return render(request, "products/single_category.html", context)

