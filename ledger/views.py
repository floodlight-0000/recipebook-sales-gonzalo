from django.shortcuts import render
from .models import RecipeImage, Ingredient, Recipe
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def listView(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes" : recipes
    }
    return render(request, 'listTemplate.html', ctx)

@login_required
def detailView(request, num=''):
    recipe = Recipe.objects.get(id=num)
    ctx = {
        "recipe" : recipe,
        "ingredients" : Ingredient.objects.filter(recipe__recipe__name=recipe.name),
        "images" : RecipeImage.objects.filter(recipe=recipe),
    }
    return render(request, 'recipeTemplate.html', ctx)

@login_required
def addRecipe(request):
    authors = User.objects.values()
    ingredients = Ingredient.objects.all()
    ctx = {
        "authors" : authors,
        "ingredients" : ingredients,
    }
    if(request.method == "POST"):
        r = Recipe()
        r.name = request.POST.get('recipe_name')
        r.author = request.POST.get('recipe_author')
        r.createdOn = timezone.now()
        r.updatedOn = timezone.now()
        # new_ingredients = ingredients.objects.get(pk=request.POST.get('recipe_ingredients'))
        r.save()
    return render(request, 'addRecipeTemplate.html', ctx)