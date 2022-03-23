from django.shortcuts import render
from apps.settings.models import Setting, Action
from apps.categories.models import Category
from apps.products.models import Product
from django.http import HttpResponseNotFound
from django.template import loader



# Create your views here.
def index(request):
    home = Setting.objects.latest('id')
    categories = Category.objects.all()[:5]
    most_popular_products = Product.objects.all().order_by('rating')[:8]
    products = Product.objects.all()[:8]
    random_products = Product.objects.all().order_by('?')[:8]
    actions = Action.objects.all().order_by('-id')[:4]
    expensive_products = Product.objects.all().order_by('-price')[:3]
    one_random_product = Product.objects.all().order_by('?')[:1]
    two_random_product = Product.objects.all().order_by('?')[:1]
    context = {
        'home' : home,
        'categories' : categories,
        'products' : products,
        'most_popular_products' : most_popular_products,
        'random_products' : random_products,
        'actions' : actions,
        'expensive_products' : expensive_products,
        'one_random_product' : one_random_product,
        'two_random_product' : two_random_product,
    }
    return render(request, 'index-2.html', context)

def Errorhandler404(request, exception):
    content = loader.render_to_string('404.html', {}, request)
    return HttpResponseNotFound(content)