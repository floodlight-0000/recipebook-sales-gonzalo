from django.shortcuts import render
from .models import RecipeImage, RecipeIngredient, Ingredient, Recipe
from django.utils import timezone
from django.contrib.auth.models import User
from .forms import RecipeForm
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
    ingredients = Ingredient.objects.all()
    form = RecipeForm()

    if(request.method == "POST"):
        form = RecipeForm(request.POST)

        if form.is_valid():
            r = Recipe()
            r.name = form.cleaned_data.get('name')
            r.author = request.user
            r.createdOn = timezone.now()
            r.updatedOn = timezone.now()
            r.save()
            
    ctx = {
        "ingredients" : ingredients,
        "form" : form,
    }
    return render(request, 'addRecipeTemplate.html', ctx)