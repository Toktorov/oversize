from django.contrib import admin
from apps.products.models import Product, ProductImage, ProductSize

# Register your models here.
class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductSizeAdmin(admin.TabularInline):
    model = ProductSize
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    inlines = [ProductImageAdmin, ProductSizeAdmin]

admin.site.register(Product, ProductAdmin)
