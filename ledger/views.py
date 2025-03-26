from django.shortcuts import render
from .models import Ingredient, Recipe, RecipeIngredient

# ctx_old = {
#     "recipes": [
#         {
#             "name": "Recipe 1",
#             "ingredients": [
#                 {
#                     "name": "tomato",
#                     "quantity": "3pcs"
#                 },
#                 {
#                     "name": "onion",
#                     "quantity": "1pc"
#                 },
#                 {
#                     "name": "pork",
#                     "quantity": "1kg"
#                 },
#                 {
#                     "name": "water",
#                     "quantity": "1L"
#                 },
#                 {
#                     "name": "sinigang mix",
#                     "quantity": "1 packet"
#                 }
#             ],
#             "link": "/recipe/1"
#         },
#         {
#             "name": "Recipe 2",
#             "ingredients": [
#                 {
#                     "name": "garlic",
#                     "quantity": "1 head"
#                 },
#                 {
#                     "name": "onion",
#                     "quantity": "1pc"
#                 },
#                 {
#                     "name": "vinegar",
#                     "quantity": "1/2cup"
#                 },
#                 {
#                     "name": "water",
#                     "quantity": "1 cup"
#                 },
#                 {
#                     "name": "salt",
#                     "quantity": "1 tablespoon"
#                 },
#                 {
#                     "name": "whole black peppers",
#                     "quantity": "1 tablespoon"
#                 },
#                 {
#                     "name": "pork",
#                     "quantity": "1 kilo"
#                 }
#             ],
#             "link": "/recipe/2"
#         }
#     ]
# }

def listView(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes" : recipes
    }
    return render(request, 'listTemplate.html',ctx)

def recipe(request, num=''):
    recipe = Recipe.objects.get(id=num)
    ctx = {
        "recipe" : recipe,
        "ingredients" : Ingredient.objects.filter(recipe__recipe__name=recipe.name),
    }
    return render(request, 'recipeTemplate.html',ctx)
