from django.core.management.base import BaseCommand
from pizza.models import Pizza, Transaction
from pizza.utils import generate_pizza_id
import random
import datetime


class Command(BaseCommand):

    def handle(self, *args, **options):
        pizza = Pizza.objects.all()
        if pizza.count() > 0:
            rand = random.randrange(0, pizza.count()-1)
            pizza_rand = pizza[rand]
            transaction = Transaction.objects.create(pizza=pizza_rand)
            print("Sold: {} for {}.".format(
                    transaction.pizza.name,
                    transaction.price
                ))
