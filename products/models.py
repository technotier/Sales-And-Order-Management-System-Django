from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=100)
    description = models.TextField()
    packing = models.IntegerField()
    measurement = models.CharField(max_length=250, default='KG')
    price = models.IntegerField()
    origin = models.CharField(max_length=250)
    in_stock = models.BooleanField(default='Available')

    def __str__(self):
        return self.brand_name

