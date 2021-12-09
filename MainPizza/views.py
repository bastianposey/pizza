from django.shortcuts import render, redirect
from .forms import PizzaForm, ToppingForm
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

def new_pizza(request):
    if request.method != 'POST':
        form = PizzaForm()
    else:
        form = PizzaForm(data=request.POST)

        if form.is_valid():
            new_pizza = form.save(commit=False)
            new_pizza.owner = request.user
            new_pizza.save()

            return redirect('MainPizza:pizzas')
    context = {'form': form}
    return render(request, 'MainPizza/new_pizza.html', context)

def new_topping(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = ToppingForm()
    else:
        form = ToppingForm(data=request.POST)

        if form.is_valid():
            new_topping = form.save(commit=False)
            new_topping.pizza = pizza
            new_topping.save()

            return redirect('MainPizza:pizza', pizza_id=pizza_id)
    # context is a dictionary that allows us to pass data to our template
    context = {'form': form, 'pizza':pizza}

    return render(request, 'MainPizza/new_topping.html', context)