from django.shortcuts import render
from products.models import ProductCategory, Products


# Create your views here.
def index(request):
    return render(request, 'products/index.html')


def products(request, category_id=None):
    categories = ProductCategory.objects.all()
    products = Products.objects.filter(category=category_id) if category_id else Products.objects.all()
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
    return render(request, 'products/product.html', context)


def about_us(request):
    return render(request, 'products/aboutus.html')


def contact(request):
    return render(request, 'products/contact.html')
