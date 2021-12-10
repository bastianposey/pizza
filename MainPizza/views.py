from django.shortcuts import render, redirect
from .forms import CommentForm
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
    comments = pizza.comment_set.all()
    context = {'pizza': pizza, 'toppings':toppings,'comments':comments}

    return render(request, 'MainPizza/pizza.html', context)

'''
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
'''

def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()

            return redirect('MainPizza:pizza', pizza_id=pizza_id)
    # context is a dictionary that allows us to pass data to our template
    context = {'form': form, 'pizza':pizza}

    return render(request, 'MainPizza/new_comment.html', context)