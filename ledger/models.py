from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Django User models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=255)

# Main models

class Recipe(models.Model):
    name = models.CharField(max_length=99)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("detailView", args=[self.id])
    
class Ingredient(models.Model):
    name = models.CharField(max_length=99)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
# Recipe Foreign Key models

class RecipeImage(models.Model):
    image = models.ImageField(upload_to='images/', null=False)
    description = models.CharField(max_length=255, default="no description provided.")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("addImage", args=[self.id])

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
