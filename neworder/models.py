from django.db import models
from django.utils import timezone
from datetime import timedelta

def get_default_date():
    return timezone.now().date() + timedelta(days=10)

class NewOrder(models.Model):
    internal_ref_no = models.CharField(max_length=20, unique=True)

    order_date = models.DateTimeField(default=timezone.now)

    ORDER_TYPE_CHOICES = [
        ('exchange', 'Exchange'),
        ('delivery', 'Delivery'),
        ('empty', 'Empty'),
        ('on-site tip', 'On-site Tip'),
    ]
    order_type = models.CharField(max_length=30, choices=ORDER_TYPE_CHOICES)

    name_or_company = models.CharField(max_length=100)

    postcode = models.CharField(max_length=20)

    address = models.TextField()

    expected_collection_date = models.DateField(default=get_default_date)
    
    collection_date = models.DateField(null=True, blank=True)

    contact_number = models.CharField(max_length=20)

    SKIP_SIZE_CHOICES = [
        ('4', '4 Yard'),
        ('6', '6 Yard'),
        ('8', '8 Yard'),
        ('10', '10 Yard'),
        ('12', '12 Yard'),
        ('16', '16 Yard'),
        ('RORO', 'RORO'),
        ('Bin', 'Bin'),
    ]
    skip_size = models.CharField(max_length=5, choices=SKIP_SIZE_CHOICES)

    quantity = models.PositiveIntegerField()

    total_amount_with_vat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    PAYMENT_METHOD_CHOICES = [
        ('account', 'Account'),
        ('bank_transfer', 'Bank Transfer'),
        ('card', 'Card'),
        ('cash', 'Cash'),
        ('cheque', 'Cheque'),
    ]
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES , null=True, blank=True)

    inv_or_card_no = models.CharField(max_length=100, null=True, blank=True)

    payment_date = models.DateField(null=True, blank=True)

    remark = models.TextField(blank=True, null=True)

    fulfillment_date = models.DateField(null=True, blank=True)

    days_hired = models.PositiveIntegerField(null=True, blank=True)

    extra_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    exchange_delivery_ref_no = models.CharField(max_length=100, null=True, blank=True)

    net_weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    driver = models.CharField(max_length=100, null=True, blank=True)

    skip_number = models.CharField(max_length=100, null=True, blank=True)

    email = models.EmailField(null=True, blank=True)

    sorted_date = models.DateField(null=True, blank=True)

    extra_charge_waste = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Order #{self.internal_ref_no} - {self.name_or_company}"
