from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
