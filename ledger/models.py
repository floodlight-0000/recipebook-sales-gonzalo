from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=255)

class Ingredient(models.Model):
    name = models.CharField(max_length=99)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("ingredientView", args=[self.id])

class Recipe(models.Model):
    name = models.CharField(max_length=99)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("recipeView", args=[self.id])

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=99)
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE,
        related_name='recipe'
    )
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE,
        related_name='ingredients'
    )
