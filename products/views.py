from django.shortcuts import render
from products.models import ProductCategory, Products

# Create your views here.
def index(request):
    return render(request, 'products/index.html')


def products(request):
    categories = ProductCategory.objects.all()
    products = Products.objects.all()
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'products/products.html', context=context)


def product(request, product_id):
    product = Products.objects.get(id=product_id)
    context = {
        'product': product,

    }

