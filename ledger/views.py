from django.shortcuts import render
from .models import RecipeImage, RecipeIngredient, Ingredient, Recipe
from django.utils import timezone
from .forms import RecipeForm, IngredientForm, RecipeIngredientForm
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
    recipe_form = RecipeForm()
    ingredient_form = IngredientForm()
    recipeingredient_form = RecipeIngredientForm()

    forms = [recipe_form, ingredient_form, recipeingredient_form]
    ctx = { "forms" : forms}

    if(request.method == "POST"):
        recipe_form = RecipeForm(request.POST)
        ingredient_form = IngredientForm(request.POST)
        recipeingredient_form = RecipeIngredientForm(request.POST)

        forms = [recipeingredient_form, ingredient_form, recipe_form]
        valid = [form.is_valid() for form in forms]

        if all(valid):
            r = Recipe()
            r.name = recipe_form.cleaned_data.get('recipe_name')
            r.author = request.user
            r.createdOn = timezone.now()
            r.updatedOn = timezone.now()
            r.save()

            i = Ingredient()
            i.name = ingredient_form.cleaned_data.get('ingredient_name')
            i.save()

            ri = RecipeIngredient()
            ri.quantity = recipeingredient_form.cleaned_data.get('quantity')
            ri.recipe = r
            ri.ingredient = i
            ri.save()

    return render(request, 'addRecipeTemplate.html', ctx)