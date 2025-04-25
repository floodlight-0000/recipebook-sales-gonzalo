from django.urls import path
from . import views

urlpatterns = [
    path('', views.listView, name="listView"),
    path('recipe/<int:num>/', views.detailView, name="detailView"),
    path('recipe/add/', views.addRecipe, name="addRecipe"),
    path('recipe/<int:num>/add_image', views.addImage, name="addImage"),
]
