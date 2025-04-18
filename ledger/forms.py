from django import forms
from django.contrib.auth.models import User


class TaskForm(forms.Form):
    name = forms.CharField(label='Recipe Name', max_length=100)
    author = forms.ModelChoiceField(label='Author', queryset=User.objects.values())