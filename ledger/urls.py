from django.urls import path
from .views import listView, recipe1, recipe2

urlpatterns = [
    path('', listView, name="listView"),
    path('recipe/1', recipe1, name="recipe1"),
    path('recipe/2', recipe2, name="recipe2"),
]
