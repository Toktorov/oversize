from django.contrib import admin
from apps.products.models import Product, ProductImage

# Register your models here.
class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    inlines = [ProductImageAdmin]

admin.site.register(Product, ProductAdmin)
