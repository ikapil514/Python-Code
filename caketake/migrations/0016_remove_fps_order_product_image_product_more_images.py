# Generated by Django 4.2.1 on 2023-06-07 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caketake', '0015_fps_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fps',
            name='order',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='cake/image.img'),
        ),
        migrations.AddField(
            model_name='product',
            name='more_images',
            field=models.ImageField(default='', upload_to='morecake/image.img'),
        ),
    ]
