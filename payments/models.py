from django.db import models

from orders.models import Order

class Payment(models.Model):

    CASH = "CASH"
    TELEBIRR = "TELEBIRR"

    METHOD_CHOICES = [
        (CASH, "Cash"),
        (TELEBIRR, "Telebirr"),
    ]

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="payments"
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_method = models.CharField(
        max_length=20,
        choices=METHOD_CHOICES,
        default=CASH
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount}"