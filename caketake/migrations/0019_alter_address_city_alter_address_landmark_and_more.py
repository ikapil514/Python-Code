# Generated by Django 4.2.1 on 2023-06-08 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caketake', '0018_alter_address_city_alter_address_landmark_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(default='HMH', max_length=250),
        ),
        migrations.AlterField(
            model_name='address',
            name='landmark',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(default='Sector', max_length=250),
        ),
    ]
