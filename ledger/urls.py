from django.urls import path
from . import views

urlpatterns = [
    path('', views.listView, name="listView"),
    path('recipe/<int:num>/', views.detailView, name="detailView"),
]
