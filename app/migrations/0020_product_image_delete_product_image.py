# Generated by Django 5.1 on 2024-10-29 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_rename_category_main_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='media/products'),
        ),
        migrations.DeleteModel(
            name='product_image',
        ),
    ]
