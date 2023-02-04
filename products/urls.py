from django.urls import path
from products.views import index, products, product, about_us, contact

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('products/<int:product_id>', product, name='product'),
    path('products/category/<int:category_id>', products, name='category'),
    path('aboutus/', about_us, name='about_us'),
    path('contact/', contact, name='contact'),
]
