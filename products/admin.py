from django.contrib import admin
from products.models import ProductCategory, Products

# Register your models here.
admin.site.register(ProductCategory)


@admin.register(Products)
class AdminProducts(admin.ModelAdmin):
    list_display = ('name', 'weight')
    fields = ('name', 'description', 'price', 'count', 'main_image', 'image_1', 'image_2', 'image_3',
              'weight', 'category')
    search_fields = ('name',)
    ordering = ('name',)


