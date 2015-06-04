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

    def __str__(self):
        return self.name


class Cocktail (models.Model):
    # Pk
    name = models.CharField(max_length=100)
    link_name = models.CharField(max_length=100)
    glass = models.CharField(max_length=100)
    recipe = models.CharField(max_length=1000)
    description = models.CharField(max_length=400)
    history = models.CharField(max_length=1000)
    #recommendations
    #Rating


    def save(self, *args, **kwargs):
        if not self.id:
            self.link_name = self.name.replace(" ", "_")
        super(Cocktail, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Components(models.Model):
    cocktail = models.ForeignKey(Cocktail)
    ingredient = models.ForeignKey(Ingredient)
    amount = models.CharField(max_length=100)


