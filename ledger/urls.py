from django.urls import path
from .views import listView, recipeView, recipeView2

urlpatterns = [
    path('recipes/list', listView, name="listView"),
    path('recipe/1', recipeView, name="recipeView"),
    path('recipe/2', recipeView2, name="recipeView2"),
]
