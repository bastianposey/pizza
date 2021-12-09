from django.urls import path
from django.urls.resolvers import URLPattern

from . import views


app_name = 'MainPizza'

urlpatterns = [
    path('', views.index, name='index'),
    path('pizzas',views.pizzas, name='pizzas'),
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
    path('new_pizza/', views.new_pizza, name='new_pizza'),
    # pizza_id is in views.py file
    path('new_topping/<int:pizza_id>/', views.new_topping, name='new_topping')
]