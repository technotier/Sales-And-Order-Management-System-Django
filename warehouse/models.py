from django.db import models
from products.models import Category

# Create your models here.
class Warehouse(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.CharField(max_length=500)
    qty = models.IntegerField(default=0)
    measurement = models.CharField(max_length=100)
    original_price = models.IntegerField()
    selling_price = models.IntegerField()
    supplier_name = models.CharField(max_length=500)
    supplier_phone = models.CharField(max_length=500)
    in_house = models.CharField(max_length=500)

    def __str__(self):
        return self.product

    def get_profit(self):
        return self.selling_price - self.original_price
