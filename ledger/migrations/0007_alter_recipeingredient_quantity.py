# Generated by Django 5.1.6 on 2025-03-26 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0006_alter_recipeingredient_ingredient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='quantity',
            field=models.CharField(max_length=99),
        ),
    ]
