from django.contrib import admin

# Register your models here.
from .models import Comment, Pizza, Topping

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Comment)