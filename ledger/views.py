from django.shortcuts import render
from .models import Ingredient, Recipe

def listView(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes" : recipes
    }
    return render(request, 'listTemplate.html',ctx)

def recipe(request, num=''):
    recipe = Recipe.objects.get(id=num)
    ctx = {
        "recipe" : recipe,
        "ingredients" : Ingredient.objects.filter(recipe__recipe__name=recipe.name),
    }
    return render(request, 'recipeTemplate.html',ctx)
