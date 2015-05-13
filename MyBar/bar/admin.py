from django.contrib import admin

from .models import Cocktail, Components, Ingredient


class ComponentsInline(admin.TabularInline):
    model = Components
    extra = 0

class CocktailAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,               {'fields': ['Name']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    inlines = [ComponentsInline]


admin.site.register(Cocktail, CocktailAdmin)
admin.site.register(Ingredient)