from django import forms
from django.forms import Form, ModelForm, CheckboxSelectMultiple
from .models import RecipeIngredient, Ingredient

all_ingredients = Ingredient.objects.all()

class RecipeForm(Form):
    class_name = "recipe"
    heading_text = "Add New Recipe"
    recipe_name = forms.CharField(label='New Recipe name:', max_length=99)

class IngredientForm(Form):
    class_name = "ingredient"
    heading_text = "Add New Ingredient"
    ingredient_name = forms.CharField(label='New Ingredient name:', max_length=99)

class RecipeIngredientForm(ModelForm):
    class_name = "recipe_ingredient"
    heading_text = "Assign Ingredient/s to a Recipe"

    class Meta:
        model = RecipeIngredient
        fields = ['recipe', 'quantity']

    ingredients = forms.ModelMultipleChoiceField(all_ingredients, widget=CheckboxSelectMultiple) 

class ImageForm(Form):
    image = forms.ImageField()
    description = forms.CharField(label='Add description', max_length=255, required=False)
