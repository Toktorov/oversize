from django.shortcuts import render
from apps.settings.models import Setting
from apps.categories.models import Category
from apps.products.models import Product

# Create your views here.
def index(request):
    home = Setting.objects.latest('id')
    categories = Category.objects.all()[:5]
    most_popular_products = Product.objects.all().order_by('rating')[:8]
    products = Product.objects.all()[:8]
    context = {
        'home' : home,
        'categories' : categories,
        'products' : products,
        'most_popular_products' : most_popular_products
    }
    return render(request, 'index-2.html', context)

