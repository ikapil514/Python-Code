# Generated by Django 4.2.1 on 2023-06-06 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caketake', '0014_remove_product_product_collection_alter_fps_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fps',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='caketake.order'),
            preserve_default=False,
        ),
    ]
