from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    search_fields = ('quantity', 'ingredient', 'recipe')

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name', )

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ('name', )

admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
