# Generated by Django 3.2.7 on 2022-03-22 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220322_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_img',
            field=models.ImageField(default=1, upload_to='', verbose_name='product_img/'),
            preserve_default=False,
        ),
    ]