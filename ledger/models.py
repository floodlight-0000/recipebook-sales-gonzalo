from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=99)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ingredient_detail', args=[str(self.name)])

class Recipe(models.Model):
    name = models.CharField(max_length=99)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("recipeView", args=[self.id])

class RecipeIngredient(models.Model):
    quantity = models.IntegerField(default=0)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('recipeIngredient_detail', args=[str(self.name)])


# Create 3 models:
# --Ingredient 
# --Has 'name' as its field
# DONE
# Recipe
# --Has 'name' as its field
# DONE
# RecipeIngredient
# --Needs a 'Quantity' field
# --Needs an 'Ingredient' field which is a foreign key to the 'Ingredient' model above
# --Needs a 'Recipe' field which is a foreign key to the 'Recipe' model above
# DONE
# Set the string representation and absolute urls of the Ingredient and Recipe models

# Modify the list view created from the previous lab.
# This view should now use the Recipe model

# The list view just has to list the recipe names, with the appropriate links

# Modify the detailed view to use the Recipe model. (hints below)

# Bonus points: Create an admin panel for each of the models, with proper 
# admin customization (ie. list displays, search fields, filters, and inline editing)