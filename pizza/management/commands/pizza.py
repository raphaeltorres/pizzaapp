from django.core.management.base import BaseCommand
from pizza.models import Pizza, PizzaType
from pizza.utils import generate_pizza_id
import random
import datetime


class Command(BaseCommand):

    def handle(self, *args, **options):
        pizza_type = PizzaType.objects.all()
        rand = random.randrange(0, pizza_type.count())
        price_random = random.randrange(100, 1000)
        dt = datetime.datetime.now()
        pizza_type_rand = pizza_type[rand]
        pizza = Pizza.objects.create(
            name=generate_pizza_id(pizza_type_rand.name, dt),
            pizza_type=pizza_type_rand,
            price=price_random
        )
        print("Pizza: {} was created.".format(pizza.name))
