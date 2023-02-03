from django.contrib import admin
from products.models import ProductCategory, Products

# Register your models here.
admin.site.register(ProductCategory)


@admin.register(Products)
class AdminProducts(admin.ModelAdmin):
    list_display = ('name', 'weight')
    fields = ('name', 'description', 'price', 'count', 'image', 'date_creations', 'weight', 'category')
    search_fields = ('name',)
    ordering = ('name',)


