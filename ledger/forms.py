from django import forms
from .models import Recipe


class RecipeForm(forms. ModelForm):
    class Meta:
        model = Recipe
        fields = ['name',]
    name = forms.CharField(label='New Recipe Name:', max_length=100)
