from django.db import models

# Create your models here.
Payment_Choices = (
    ('Cash on Delivery', 'Cash on Delivery'),
    ('Bkash', 'Bkash'),
    ('Bank', 'Bank'),
)

Order_Choices = (
    ('Confirmed', 'Confirmed'),
    ('Delivered', 'Delivered'),
    ('Pending', 'Pending'),
    ('Cancelled', 'Cancelled'),
)

class Customer(models.Model):
    ref_no = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    delivery_date = models.CharField(max_length=200)
    payment_type = models.CharField(max_length=100, choices=Payment_Choices)
    order_status = models.CharField(max_length=100, choices=Order_Choices)
    order_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_product(self):
        return ', '.join(self.products.all().values_list('name', flat=True))
        #return self.products.values('name', 'price', 'discount_price', 'quantity')

    def get_total_amount(self):
        return sum(self.products.all().values_list('total_amount', flat=True))

    def get_total_price(self):
        total = 0
        for order_product in self.products.all():
            total += order_product.get_final_price()
        return total

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(blank=True, null=True)
    discount_price = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    quantity_measurement = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, related_name='products', on_delete=models.SET_NULL, null=True)
    total_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.name


    def get_total_price(self):
        return self.quantity * self.price

    def get_total_discount_price(self):
        return self.quantity * self.discount_price

    def get_amount_saved(self):
        return self.get_total_price() - self.get_total_discount_price()

    def get_total_amount(self):
        return Product.objects.all().aggregate(Sum('total_amount'))

    def get_final_price(self):
        if self.discount_price:
            return self.get_total_discount_price()
        return self.get_total_price()