from django.urls import path
from products.views import index, products, product

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('products/<int:product_id>', product, name='product'),
]
