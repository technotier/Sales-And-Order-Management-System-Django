from django.db import models

# Create your models here.
Payment_Choices = (
    ('Cash on Delivery', 'Cash on Delivery'),
    ('Bkash', 'Bkash'),
    ('Bank', 'Bank'),
)

class Clients(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(unique=True)
    address = models.TextField()
    avatar = models.ImageField(upload_to='')
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Clients'

class ClientsOrder(models.Model):
    clients = models.ForeignKey(Clients, on_delete=models.CASCADE, blank=True, null=True)
    ref_no = models.CharField(max_length=100, blank=True, null=True)
    order_submit = models.CharField(max_length=200, blank=True, null=True)
    order_delivered = models.CharField(max_length=200, blank=True, null=True)
    invoice_total = models.IntegerField(default=0, blank=True, null=True)
    payment_choices = models.CharField(max_length=100, choices=Payment_Choices, blank=True, null=True)
    deposit = models.IntegerField(default=0, blank=True, null=True)
    remarks = models.CharField(max_length=1000, default='N/A', blank=True, null=True)

    def __str__(self):
        return self.ref_no

    def get_due(self):
        return self.invoice_total - self.deposit

