from django.db import models
from apps.categories.models import Category

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    old_price = models.IntegerField()
    rating = models.IntegerField()
    description = models.TextField()
    count = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'product_image/')

    def __str__(self):
        return self.product
        