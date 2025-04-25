from django import forms
from .models import Recipe, RecipeIngredient, Ingredient

recipes = Recipe.objects.all()
ingredients = Ingredient.objects.all()

class RecipeForm(forms.Form):
    class_name = "recipe"
    recipe_name = forms.CharField(label='New Recipe name:', max_length=99)

class IngredientForm(forms.Form):
    class_name = "ingredient"
    ingredient_name = forms.CharField(label='New Ingredient name:', max_length=99)

class RecipeIngredientForm(forms.ModelForm):
    class_name = "recipe_ingredient"
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity', 'recipe']
    # --find a way to make this a checkbox
    # --use loop to create multiple recipeIngredient objects

class ImageForm(forms.Form):
    class_name = "image"
    image = forms.ImageField()
    description = forms.CharField(label='Add description', max_length=255, required=False)
