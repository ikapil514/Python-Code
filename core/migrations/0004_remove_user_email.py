# Generated by Django 4.2.1 on 2023-06-12 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]
