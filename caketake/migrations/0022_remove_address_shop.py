# Generated by Django 4.2.1 on 2023-06-09 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caketake', '0021_address_shop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='shop',
        ),
    ]