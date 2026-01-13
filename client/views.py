from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import ProductCategory, ProductImage, ProductSubcategory, Product,MainCarousel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer, ProductCategorySerializer, ProductSubcategorySerializer
from django.db.models import Q
from django.core.paginator import Paginator



# Create your views here.
def index(request):

   main_carousel_images = MainCarousel.objects.all()
   products = Product.objects.all()
   
   context = {'products': products, 'images': main_carousel_images, 'current_nav': 'nav'}
   return render(request, 'client/pages/index.html', context)

def product_detail(request, product_id):

   product = get_object_or_404(Product, id=product_id)
   productCategory = product.category
   productImages = ProductImage.objects.filter(product=product)
   
   products = Product.objects.filter(category=productCategory).exclude(id=product.id)[:4]  # Get 4 related products from the same category excluding the current product
   return render(request, 'client/pages/productDetail.html', {'product': product, 'products': products, 'productImages': productImages})


def filter_products(request):

   return render(request, 'client/pages/filterProduct.html')

@api_view(['GET'])
def category_with_subcategories_api(request):
   product_categories = ProductCategory.objects.all()
   serializer = ProductCategorySerializer(product_categories, many=True)
   return Response(serializer.data)


@api_view(['GET'])
def filter_products_api(request):
    filters = request.query_params.get('filters', None)
    search_term = request.query_params.get('search', None)

    products = Product.objects.all().prefetch_related('images')

    if filters:
        filters_list = filters.split(',')
        products = products.filter(
            Q(category__name__in=filters_list) |
            Q(subcategory__name__in=filters_list)
        )

    if search_term:
        products = products.filter(
            Q(name__icontains=search_term) |
            Q(description__icontains=search_term)
        )

    serializer = ProductSerializer(products.distinct(), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_search_suggestions_api(request):
    search_term = request.query_params.get('search', '')
    if len(search_term) < 2:
        return JsonResponse([], safe=False)
        
    products = Product.objects.filter(name__icontains=search_term).values_list('name', flat=True)[:5]
    return JsonResponse(list(products), safe=False)


