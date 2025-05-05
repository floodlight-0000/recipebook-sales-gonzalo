from django import forms
from django.forms import Form, ModelForm, CheckboxSelectMultiple
from .models import RecipeIngredient, Ingredient

all_ingredients = Ingredient.objects.all()

# Each form has standardized internal variables for referencing in the addRecipe template.
# They are used to populate heading and subtitle text.
# This acts similarly to a ctx.

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

    # while not required by the specs, this form can handle multiple inputs of ingredients via
    # the ModelMultipleChoiceField. Handling of the resulting set of inputs is done in the
    # associated addRecipe view. A more intuitive widget replaces the default option.

    ingredients = forms.ModelMultipleChoiceField(all_ingredients, widget=CheckboxSelectMultiple) 

class ImageForm(Form):
    image = forms.ImageField()
    description = forms.CharField(label='Add description', max_length=255, required=False)
