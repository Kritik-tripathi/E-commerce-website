# Generated by Django 5.1 on 2024-10-02 07:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_main_category_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='category',
            name='Main_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='app.main_category'),
        ),
    ]
