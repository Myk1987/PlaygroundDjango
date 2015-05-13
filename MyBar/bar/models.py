from django.db import models


class Ingredient(models.Model):
    # pk
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    Description = models.CharField(max_length=500)
    alcohol  = models.IntegerField()
    # Avg. Prices
    # Where to buy

class Cocktail (models.Model):
    # Pk
    name = models.CharField(max_length=100)
    glass = models.CharField(max_length=100)
    recipe = models.CharField(max_length=1000)
    description = models.CharField(max_length=400)
    history = models.CharField(max_length=1000)
    #recommendations
    #Rating

class Components(models.Model):
    coctail = models.ForeignKey(Cocktail)
    ingredient = models.ForeignKey(Ingredient)
    amount = models.CharField(max_length=100)


