# Generated by Django 4.2.1 on 2023-06-05 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caketake', '0008_product_product_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='food_type',
            field=models.CharField(choices=[('Veg', 'Veg'), ('Non-Veg', 'Non-Veg')], max_length=8),
        ),
    ]
