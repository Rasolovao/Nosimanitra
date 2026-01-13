from django.db import models
import os
from django.utils.deconstruct import deconstructible

# Create your models here.

class MonthlyDailyDeal(models.Model):
    # Optional human-readable month/year (kept for backward compatibility/display)
    is_promotion = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    # Flags indicating the type of promotion
    is_monthly = models.BooleanField(default=False)
    is_daily = models.BooleanField(default=False)

    # Optional time window for the promotion (if set, the promotion is active only between these datetimes)
    deal_start = models.DateTimeField(null=True, blank=True)
    deal_end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.month} {self.year}"

class ProductCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class ProductSubcategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        unique_together = ('name', 'category')

    def __str__(self):
        return f"{self.name} ({self.category.name})"

@deconstructible
class ProductImagePath:
    def __call__(self, instance, filename):
        product_id = instance.product.id or 'temp'
        return os.path.join('product_images', str(product_id), filename)

upload_to_product_folder = ProductImagePath()

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=50, unique=True)
    brand = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(ProductSubcategory, on_delete=models.SET_NULL, null=True, blank=True)
    MonthlyDailyDeal = models.ForeignKey(MonthlyDailyDeal, on_delete=models.SET_NULL, null=True, blank=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.brand})"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=upload_to_product_folder)
    alt_text = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Image for {self.product.name}"

class MainCarousel(models.Model):
    image = models.ImageField(upload_to='carousel/')
    alt_text = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return   f"Image for {self.id}"