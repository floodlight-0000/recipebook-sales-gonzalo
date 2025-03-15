from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def listView(request):
    template = loader.get_template('listTemplate.html')
    return HttpResponse(template.render())

def recipeView(request):
    template = loader.get_template('recipeTemplate.html')
    return HttpResponse(template.render())

def recipeView2(request):
    template = loader.get_template('recipeTemplate2.html')
    return HttpResponse(template.render())