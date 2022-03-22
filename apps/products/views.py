from django.shortcuts import render
from apps.products.models import Product
from apps.settings.models import Setting

# Create your views here.
def product_detail(request, id):
    product = Product.objects.get(id = id)
    home = Setting.objects.latest('id')
    random_product = Product.objects.all().order_by('?')
    context = {
        'product' : product,
        'home' : home,
        'random_products' : random_product,
    }
    return render(request, 'product-details.html', context)