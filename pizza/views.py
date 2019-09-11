from django.shortcuts import render
from pizza.models import Pizza
from django.db.models import Sum, Count


def index(request):
    pizza = Pizza.objects.values('name', 'price', 'pizza_type__name').annotate(
                    total_price=Sum('pizza_transaction__price'),
                    total_sold=Count('pizza_transaction')
                ).order_by('-total_sold')

    context = {
        'title': 'Pizza App',
        'pizza': pizza
    }
    return render(request, 'index.html', context)
