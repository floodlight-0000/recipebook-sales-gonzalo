# Generated by Django 5.1.6 on 2025-03-20 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0003_alter_ingredient_options_alter_recipe_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='quantity',
            field=models.CharField(max_length=9),
        ),
    ]
