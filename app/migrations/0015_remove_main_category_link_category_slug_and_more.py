# Generated by Django 5.1 on 2024-10-23 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main_category',
            name='link',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=1, unique=True),
        ),
        migrations.AddField(
            model_name='main_category',
            name='slug',
            field=models.SlugField(default=1, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=1, unique=True),
        ),
    ]
