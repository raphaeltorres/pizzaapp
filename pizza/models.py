from django.db import models


class PizzaType(models.Model):
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return '{}'.format(self.name)


class Pizza(models.Model):
    name = models.CharField(unique=True, max_length=100)
    pizza_type = models.ForeignKey(
        PizzaType,
        on_delete=models.CASCADE,
        related_name="pizza_types"
    )

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0.00
    )

    def __str__(self):
        return '{}-{}'.format(self.name, self.pizza_type.name)


class Transaction(models.Model):
    pizza = models.ForeignKey(
        Pizza,
        on_delete=models.CASCADE,
        related_name="pizza_transaction"
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        default=0.00
    )

    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.pizza.price
        super(Transaction, self).save(*args, **kwargs)
