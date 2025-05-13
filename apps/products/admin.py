from django.contrib import admin
from .models import Product, Category, ProductImage, Review
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(Review)

