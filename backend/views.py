from unicodedata import category
from django.shortcuts import render
from django.template import context
from client.models import ProductCategory, ProductSubcategory, Product
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):

    return render(request, 'backend/pages/index.html')

def product(request):

    products = Product.objects.all()

    return render(request, 'backend/pages/Products.html', {'products': products})

def add_product(request):
    product_db = Product.objects.all()
    categories = ProductCategory.objects.all()
    subcategories = ProductSubcategory.objects.all()
    context={
        'categories': categories,
        'subcategories': subcategories,
    }
   
   
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        reference = request.POST.get('reference')
        brand = request.POST.get('brand')
        category = ProductCategory.objects.get(id=request.POST.get('category'))
        subcategory = ProductSubcategory.objects.get(id=request.POST.get('subcategory'))

        # Create a new Product instance
        product = Product(
            name=name,
            description=description,
            price=price,
            reference=reference,
            brand=brand,
            category=category,
            subcategory=subcategory
        )
    
        product.save()  # Save the product to the database

        return HttpResponseRedirect('/product/')  # Redirect to a success page or product list
    return render(request, 'backend/pages/addProduct.html', context)

# myapp/views.py

from django.shortcuts import render, redirect

