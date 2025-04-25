from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import RecipeImage, RecipeIngredient, Ingredient, Recipe
from .forms import RecipeForm, IngredientForm, RecipeIngredientForm, ImageForm

@login_required
def listView(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes" : recipes
    }
    return render(request, 'listTemplate.html', ctx)

@login_required
def detailView(request, num):
    recipe = Recipe.objects.get(id=num)
    ctx = {
        "recipe" : recipe,
        "ingredients" : Ingredient.objects.filter(recipe__recipe__name=recipe.name),
        "images" : RecipeImage.objects.filter(recipe=recipe),
    }
    return render(request, 'recipeTemplate.html', ctx)

@login_required
def addImage(request, num):
    recipe = Recipe.objects.get(id=num)
    image_form = ImageForm()
    if(request.method == "POST"):
        image_form = ImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            ri = RecipeImage()
            ri.image = image_form.cleaned_data.get('image')
            ri.description = image_form.cleaned_data.get('description')
            ri.recipe = recipe
            ri.save()
            response = redirect(recipe.get_absolute_url())
            return response
    ctx = {
        "recipe" : recipe,
        "image_form" : image_form,
    }

    return render(request, 'addImage.html',ctx)

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
        is_valid = [form.is_valid() for form in forms]
        

        if recipe_form.is_valid():
            r = Recipe()
            r.name = recipe_form.cleaned_data.get('recipe_name') # --find a way to detect existing names
            r.author = request.user
            r.createdOn = timezone.now()
            r.updatedOn = timezone.now()
            if r.name: r.save()

        if ingredient_form.is_valid():
            i = Ingredient()
            i.name = ingredient_form.cleaned_data.get('ingredient_name') # --prevent duplicate ingredients
            if i.name: i.save()
            
        if all(is_valid):
            ri = RecipeIngredient()
            ri.quantity = recipeingredient_form.cleaned_data.get('quantity')
            ri.recipe = recipeingredient_form.cleaned_data.get('recipe')
            ri.ingredient = recipeingredient_form.cleaned_data.get('ingredient')
            ri.save()

    return render(request, 'addRecipeTemplate.html', ctx)

    # forms = [recipeingredient_form, ingredient_form, recipe_form]
    # valid = [form.is_valid() for form in forms]

    # if all(valid):
    #     r = Recipe()
    #     i = Ingredient()

    #     r.name = recipe_form.cleaned_data.get('recipe_name') # --find a way to detect existing names
    #     i.name = ingredient_form.cleaned_data.get('ingredient_name') # --prevent duplicate ingredients

    #     r.author = request.user
    #     r.createdOn = timezone.now()
    #     r.updatedOn = timezone.now()
    #     r.save()

    #     ri = RecipeIngredient()
    #     ri.quantity = recipeingredient_form.cleaned_data.get('quantity')
    #     ri.ingredient = recipeingredient_form.cleaned_data.get('ingredient')
    #     ri.recipe = r

    #     if i.name:
    #         i.save()
    #         ri.ingredient = i
    #     ri.save()