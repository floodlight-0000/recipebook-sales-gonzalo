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
    msg = "Add recipes, assign ingredients to recipes, or make new ingredients."

    if(request.method == "POST"):
        recipe_form = RecipeForm(request.POST)
        ingredient_form = IngredientForm(request.POST)
        recipeingredient_form = RecipeIngredientForm(request.POST)
        
        if recipe_form.is_valid():
            r = Recipe()
            r.name = recipe_form.cleaned_data.get('recipe_name')
            r.author = request.user
            if duplicateItem(Recipe, r.name, r.author):
                msg = r.name + " already exists for current user."
            else:
                r.createdOn = timezone.now()
                r.updatedOn = timezone.now()
                r.save()
                msg = r.name + " added successfully!"

        if ingredient_form.is_valid():
            i = Ingredient()
            i.name = ingredient_form.cleaned_data.get('ingredient_name') 
            if duplicateItem(Ingredient, i.name):
                msg = i.name + " already exists."
            else:
                i.save()
                msg = i.name + " added successfully!"
            
        if recipeingredient_form.is_valid():
            ingredients = recipeingredient_form.cleaned_data.get('ingredients')
            for ingredient in ingredients:
                ri = RecipeIngredient()
                ri.quantity = recipeingredient_form.cleaned_data.get('quantity')
                ri.recipe = recipeingredient_form.cleaned_data.get('recipe')
                ri.ingredient = ingredient
                ri.save()
            msg = "ingredients successfully assigned!"

    ctx = { 
        "forms" : forms,
        "msg" : msg,
    }

    return render(request, 'addRecipe.html', ctx)

# Helper function for duplicate name handling

def duplicateItem(model, name, author=None):
    if model == Recipe:
        items = model.objects.filter(author=author)
    else:
        items = model.objects.all()    

    for item in items:
        if item.name == name:
            return True
    return False