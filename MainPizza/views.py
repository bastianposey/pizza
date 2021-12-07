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