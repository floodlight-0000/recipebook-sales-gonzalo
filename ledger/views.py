from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import RecipeImage, RecipeIngredient, Ingredient, Recipe
from .forms import RecipeForm, IngredientForm, RecipeIngredientForm, ImageForm

# View function for list view.

@login_required
def listView(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes" : recipes
    }
    return render(request, 'listTemplate.html', ctx)

# View function for detailed view. 
# It makes use of the associative identity, 
# RecipeIngredient, to filter ingredients per recipe. 
# Images are filtered via a simpler foreign key relationship.

@login_required
def detailView(request, num):
    recipe = Recipe.objects.get(id=num)
    ctx = {
        "recipe" : recipe,
        "ingredients" : Ingredient.objects.filter(recipe__recipe__name=recipe.name),
        "images" : RecipeImage.objects.filter(recipe=recipe),
    }
    return render(request, 'recipeTemplate.html', ctx)

# View function for image adding view.
# Uses ImageForm form.

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
            ri.recipe = recipe # automatic assignment; user does not need to select this
            ri.save()
            response = redirect(recipe.get_absolute_url()) 
            return response # redirect to associated recipe's detailed view.
    ctx = {
        "recipe" : recipe,
        "image_form" : image_form,
    }

    return render(request, 'addImage.html',ctx)

# View function for the view to add new items.
# Uses three different forms which can be filled in separately.

@login_required
def addRecipe(request):
    recipe_form = RecipeForm()
    ingredient_form = IngredientForm()
    recipeingredient_form = RecipeIngredientForm()

    forms = [recipe_form, ingredient_form, recipeingredient_form] # ctx to loop over in associated template.
    msg = "Add recipes, assign ingredients to recipes, or make new ingredients." # default msg when no duplicate names.

    if(request.method == "POST"):
        recipe_form = RecipeForm(request.POST)
        ingredient_form = IngredientForm(request.POST)
        recipeingredient_form = RecipeIngredientForm(request.POST)

        # Conditionals for form validation are handled separately. No submission of all 3 at once
        # to avoid conflicts involving recipes or ingredients which do not exist yet.

        if recipe_form.is_valid():
            r = Recipe()
            r.name = recipe_form.cleaned_data.get('recipe_name')
            r.author = request.user
            if duplicateItem(Recipe, r.name, r.author): # 3rd optional arg filled in (author)
                msg = f"Recipe '{r.name}' already exists for user ({r.author})." # msg for duplicate recipe under same user.
            else:
                r.createdOn = timezone.now() # format of timezone.now() matches DateTimeField in Recipe model.
                r.updatedOn = r.createdOn # if it's new, it's the same.
                r.save()
                msg = f"Recipe '{r.name}' added successfully!"

        if ingredient_form.is_valid():
            i = Ingredient()
            i.name = ingredient_form.cleaned_data.get('ingredient_name') 
            if duplicateItem(Ingredient, i.name): # 3rd optional arg left blank (author)
                msg = f"Ingredient '{i.name}' already exists." # msg for duplicate ingredient regardless of user.
            else:
                i.save()
                msg = f"Ingredient '{i.name}' added successfully!" 
            
        if recipeingredient_form.is_valid():
            # these 3 are the same for every ingredient, so no need to loop over them
            ingredients = recipeingredient_form.cleaned_data.get('ingredients')
            recipe = recipeingredient_form.cleaned_data.get('recipe')
            quantity = recipeingredient_form.cleaned_data.get('quantity')
            
            # loop over the set of all chosen ingredients, creating new associative entities 
            # and adding them to the database one by one. It works even if only 1 ingredient is selected.
            # the only caveat is that individual quantity assignment is not supported (that requires JS)
            for ingredient in ingredients:
                ri = RecipeIngredient()
                ri.quantity = quantity
                ri.recipe = recipe
                ri.ingredient = ingredient
                ri.save()
            msg = f"{quantity} of ingredient/s successfully assigned to recipe '{recipe}.'"

    ctx = { 
        "forms" : forms,
        "msg" : msg,
    }

    return render(request, 'addRecipe.html', ctx)

# Helper function for duplicate name handling. Covers both recipe and ingredient duplicates.

def duplicateItem(model, name, author=None): # author is an optional argument
    if model == Recipe:
        items = model.objects.filter(author=author) 
    else:
        items = model.objects.all()    

    for item in items:
        if item.name == name:
            return True
    return False