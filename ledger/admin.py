from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from .models import Profile, Recipe, RecipeIngredient, Ingredient


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]


class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    search_fields = ('quantity', 'ingredient', 'recipe')

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    search_fields = ('name', )

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    search_fields = ('name', )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
