# Generated by Django 3.2.7 on 2022-03-23 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default="2021-01-05 06:00:00.000000-09:00"),
            preserve_default=False,
        ),
    ]