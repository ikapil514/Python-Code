# Generated by Django 4.2.1 on 2023-06-18 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caketake', '0033_alter_shop_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='address',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
