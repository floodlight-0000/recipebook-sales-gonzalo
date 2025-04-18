from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from .models import Profile, Recipe, Ingredient, RecipeImage, RecipeIngredient

# Django User admins

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]

# Main admins

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name', 'author', 'createdOn', 'updatedOn')

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ('name',)

# Recipe Foreign Key admins

class RecipeImageAdmin(admin.ModelAdmin):
    model = RecipeImage
    search_fields = ('image', 'description', 'recipe')

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    search_fields = ('quantity', 'ingredient', 'recipe')

# Registry

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)

admin.site.register(RecipeImage, RecipeImageAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

