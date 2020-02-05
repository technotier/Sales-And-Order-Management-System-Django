from django.db import models
from clients.models import Clients

# Create your models here.
Payment_Options = (
    ('Cash on Delivery', 'Cash on Delivery'),
    ('Bkash', 'Bkash'),
    ('Bank', 'Bank'),
)

class EntryOrder(models.Model):
    ref_no = models.CharField(max_length=200, unique=True)
    customer_name = models.ForeignKey(Clients, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    payment_type = models.CharField(max_length=200, choices=Payment_Options)
    invoice_total = models.IntegerField()
    deposit = models.IntegerField()
    due_collection_date = models.CharField(max_length=200)
    order_delivered = models.CharField(max_length=200)
    remarks = models.CharField(max_length=1000, default='N/A')

    def __str__(self):
        return self.ref_no

    def get_due(self):
        return self.invoice_total - self.deposit
