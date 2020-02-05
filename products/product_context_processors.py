from .models import Item

def total_product_count(request):
    total_product = Item.objects.count()
    return {"total_product_count": total_product}

