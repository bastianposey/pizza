from django.shortcuts import render

from .models import Pizza, Topping

# Create your views here.
def index(request):
    '''The hame page for pizzeria'''
    return render(request, 'MainPizza/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('date_add')

    context = {'pizzas': pizzas}

    return render(request, 'MainPizza/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    # foreign key can be accessed using '_set'
    toppings = pizza.topping_set.all()
    context = {'pizza': pizza, 'toppings':toppings}

    return render(request, 'MainPizza/pizza.html', context)