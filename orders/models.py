from django.db import models
from django.utils import timezone

from customers.models import Customer
from services.models import Service
from datetime import timedelta

def default_pickup_date():
    return timezone.localdate() + timedelta(days=3)

class Order(models.Model):

    RECEIVED = "RECEIVED"
    WASHING = "WASHING"
    DRYING = "DRYING"
    IRONING = "IRONING"
    READY = "READY"
    COLLECTED = "COLLECTED"

    STATUS_CHOICES = [
        (RECEIVED, "Received"),
        (WASHING, "Washing"),
        (DRYING, "Drying"),
        (IRONING, "Ironing"),
        (READY, "Ready"),
        (COLLECTED, "Collected"),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="orders"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=RECEIVED
    )
    
    pickup_date = models.DateField(
        default=default_pickup_date
    )

    receipt_number = models.CharField(
        max_length=30,
        unique=True,
        blank=True
    )

    advance_paid = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.receipt_number

    @property
    def total_amount(self):
        total = 0

        for item in self.items.all():
            total += item.subtotal()

        return total

    @property
    def total_paid(self):
        return sum(
            payment.amount
            for payment in self.payments.all()
        )

    @property
    def balance_due(self):
        balance = self.total_amount - self.total_paid
        return max(balance, 0)

    @property
    def is_fully_paid(self):
        return self.balance_due <= 0

    def save(self, *args, **kwargs):

        if not self.receipt_number:

            today = timezone.now().strftime("%Y%m%d")

            last_order = Order.objects.order_by("-id").first()

            next_id = 1

            if last_order:
                next_id = last_order.id + 1

            self.receipt_number = (
                f"LDY-{today}-{next_id:04d}"
            )

        super().save(*args, **kwargs)
        
    @property
    def payment_status(self):
        if self.total_paid == 0:
            return "UNPAID"
        elif self.total_paid < self.total_amount:
            return "PARTIAL"
        else:
            return "PAID"


class OrderLine(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.PROTECT
    )

    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.service.name}"

    def subtotal(self):
        return self.quantity * self.service.unit_price