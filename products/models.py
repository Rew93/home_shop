from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(default='Ця інформація знаходиться в розробці.')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'Category'


class Products(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(default='Ця інформація знаходиться в розробці.')
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    count = models.PositiveIntegerField(default=0)
    main_image = models.ImageField(upload_to='product_image')
    image_1 = models.ImageField(blank=True, null=True, upload_to='product_image')
    image_2 = models.ImageField(blank=True, null=True, upload_to='product_image')
    image_3 = models.ImageField(blank=True, null=True, upload_to='product_image')
    date_creations = models.DateTimeField(auto_now_add=True)
    weight = models.DecimalField(default=0, max_digits=6, decimal_places=1)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Products'
