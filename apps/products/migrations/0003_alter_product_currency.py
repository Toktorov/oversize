# Generated by Django 4.0.3 on 2022-03-23 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('KGZ', 'KGZ'), ('RUB', 'RUB'), ('EURO', 'EURO'), ('USD', 'USD'), ('Audio', (('vinyl', 'Vinyl'), ('cd', 'CD')))], default='KGZ', max_length=255, null=True),
        ),
    ]
