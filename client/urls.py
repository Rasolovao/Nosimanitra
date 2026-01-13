from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('filter_products/', views.filter_products, name='filter_products'),
    path('api/categories-with-subcategories/', views.category_with_subcategories_api),
    path('api/filter-products/', views.filter_products_api),
    path('api/product-search-suggestions/', views.product_search_suggestions_api),
]
