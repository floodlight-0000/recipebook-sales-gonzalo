# Generated by Django 5.1.6 on 2025-03-20 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0002_ingredient_recipe_recipeingredient_delete_choice_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['name']},
        ),
    ]
