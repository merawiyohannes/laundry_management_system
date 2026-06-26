from django.db import models


class Service(models.Model):

    ITEM = "ITEM"
    KG = "KG"

    PRICING_TYPE_CHOICES = [
        (ITEM, "Per Item"),
        (KG, "Per Kilogram"),
    ]

    name = models.CharField(max_length=100)

    pricing_type = models.CharField(
        max_length=10,
        choices=PRICING_TYPE_CHOICES,
        default=ITEM
    )

    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name