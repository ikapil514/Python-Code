# Generated by Django 4.2.1 on 2023-06-08 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caketake', '0016_remove_fps_order_product_image_product_more_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fps',
            old_name='floor',
            new_name='floor_size',
        ),
        migrations.RenameField(
            model_name='fps',
            old_name='size',
            new_name='weight',
        ),
        migrations.RemoveField(
            model_name='product',
            name='ready',
        ),
        migrations.AddField(
            model_name='fps',
            name='making_time',
            field=models.TimeField(default='01:30'),
        ),
    ]
