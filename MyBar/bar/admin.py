from django.contrib import admin

from .models import Cocktail, Components, Ingredient

admin.site.register(Cocktail)
admin.site.register(Components)
admin.site.register(Ingredient)