from django.contrib import admin

# Register your models here.
from .models import ProductCategory, ProductSubcategory, Product,ProductImage,MainCarousel

admin.site.register(ProductCategory)
admin.site.register(ProductSubcategory)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(MainCarousel)
