from locale import currency
from django.db import models
from apps.categories.models import Category

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    product_img = models.ImageField(upload_to = 'product_img/')
    price = models.IntegerField()
    old_price = models.IntegerField(default=0)
    CURRENCY_CHOICES = (
        ('KGZ', 'KGZ'),
        ('RUB', 'RUB'),
        ('EURO', 'EURO'),
        ('USD', 'USD'),
    )
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=255, default='KGZ', null = True)
    rating = models.IntegerField(default=0)
    description = models.TextField()
    count = models.IntegerField(default="0")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = "product_category")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image")
    image = models.ImageField(upload_to = 'product_image/')

class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = "product_size")
    shoe_size = models.IntegerField(default=32)
