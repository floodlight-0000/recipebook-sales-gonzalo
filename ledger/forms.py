from django import forms
from .models import Recipe, RecipeIngredient, Ingredient

recipes = Recipe.objects.all()
ingredients = Ingredient.objects.all()

class RecipeForm(forms.Form):
    recipe_name = forms.CharField(label='New Recipe Name:', max_length=99)

class IngredientForm(forms.Form):
    ingredient_name = forms.CharField(label='(OPTIONAL) Add new ingredient?', max_length=99, required=False)

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity']
    quantity = forms.CharField(label='Quantity:', max_length=99)
    ingredient = forms.ModelChoiceField(ingredients)

