from django import forms
from .models import Recipe, RecipeIngredient, Ingredient

recipes = Recipe.objects.all()
ingredients = Ingredient.objects.all()

class RecipeForm(forms.Form):
    class_name = "recipe"
    recipe_name = forms.CharField(label='New Recipe Name:', max_length=99)

class IngredientForm(forms.Form):
    class_name = "ingredient"
    ingredient_name = forms.CharField(label='(OPTIONAL) Add new ingredient?', max_length=99)

class RecipeIngredientForm(forms.ModelForm):
    class_name = "recipe_ingredient"
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity']
    quantity = forms.CharField(label='Quantity:', max_length=99)
    ingredient = forms.ModelChoiceField(ingredients) 
    # --find a way to make this a checkbox
    # --use loop to create multiple recipeIngredient objects

class ImageForm(forms.Form):
    class_name = "image"
    image = forms.ImageField()
    description = forms.CharField(label='add description', max_length=255, required=False)
