from django.shortcuts import render
from .models import RecipeImage, Ingredient, Recipe
from django.contrib.auth.decorators import login_required

@login_required
def listView(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes" : recipes
    }
    return render(request, 'listTemplate.html',ctx)

@login_required
def detailView(request, num=''):
    recipe = Recipe.objects.get(id=num)
    ctx = {
        "recipe" : recipe,
        "ingredients" : Ingredient.objects.filter(recipe__recipe__name=recipe.name),
        "images" : RecipeImage.objects.filter(recipe=recipe),
    }
    return render(request, 'recipeTemplate.html',ctx)
