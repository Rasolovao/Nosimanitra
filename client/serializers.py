# serializers.py
from rest_framework import serializers
from .models import ProductCategory, ProductSubcategory, Product, ProductImage, MonthlyDailyDeal

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image', 'alt_text']

class ProductSubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSubcategory
        fields = ['id', 'name']

class ProductCategorySerializer(serializers.ModelSerializer):
    subcategories = ProductSubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'subcategories']

class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(read_only=True)
    subcategory = ProductSubcategorySerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    
    # include monthly/daily deal info if present
    monthly_daily_deal = serializers.SerializerMethodField()

    def get_monthly_daily_deal(self, obj):
        if getattr(obj, 'MonthlyDailyDeal', None):
            deal = obj.MonthlyDailyDeal
            return {
                'id': deal.id,
                'description': deal.description,
                'is_monthly': deal.is_monthly,
                'is_daily': deal.is_daily,
                'deal_start': deal.deal_start,
                'deal_end': deal.deal_end,
            }
        return None

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'reference', 'brand', 'category', 'subcategory', 'monthly_daily_deal', 'created_at', 'updated_at', 'images']