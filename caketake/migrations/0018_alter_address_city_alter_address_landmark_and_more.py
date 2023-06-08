# Generated by Django 4.2.1 on 2023-06-08 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caketake', '0017_rename_floor_fps_floor_size_rename_size_fps_weight_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='landmark',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip',
            field=models.PositiveIntegerField(default='223344'),
        ),
    ]
