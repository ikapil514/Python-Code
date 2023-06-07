# Generated by Django 4.2.1 on 2023-06-05 08:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caketake', '0003_remove_order_shop_remove_shop_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fps',
            name='floor',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fps',
            name='size',
            field=models.PositiveSmallIntegerField(help_text='* in pounds', validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
