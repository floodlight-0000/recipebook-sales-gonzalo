from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# Create 3 models:
# --Ingredient 
# --Has 'name' as its field

# Recipe
# --Has 'name' as its field

# RecipeIngredient
# --Needs a 'Quantity' field
# --Needs an 'Ingredient' field which is a foreign key to the 'Ingredient' model above
# --Needs a 'Recipe' field which is a foreign key to the 'Recipe' model above

# Set the string representation and absolute urls of the Ingredient and Recipe models

# Modify the list view created from the previous lab.
# This view should now use the Recipe model

# The list view just has to list the recipe names, with the appropriate links

# Modify the detailed view to use the Recipe model. (hints below)

# Bonus points: Create an admin panel for each of the models, with proper 
# admin customization (ie. list displays, search fields, filters, and inline editing)