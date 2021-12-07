from django.shortcuts import render

# Create your views here.
def index(request):
    '''The hame page for pizzeria'''
    return render(request, 'MainPizza/index.html')