from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from client.models import Product, ProductCategory, ProductSubcategory, ProductImage

def delete_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        return redirect('product')
    except Product.DoesNotExist:
        return redirect('product')

def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    categories = ProductCategory.objects.all()
    subcategories = ProductSubcategory.objects.all()
    images = ProductImage.objects.filter(product=product_id)

    context = {
        'product': product,
        'categories': categories,
        'subcategories': subcategories,
        'images': images,
    }


    if request.method == 'POST':
        try:
            product.name = request.POST.get('name')
            product.description = request.POST.get('description')
            product.price = request.POST.get('price')
            product.brand = request.POST.get('brand')
            product.reference = request.POST.get('reference')
            product.category = ProductCategory.objects.get(id=request.POST.get('category'))
            product.subcategory = ProductSubcategory.objects.get(id=request.POST.get('subcategory'))
            
            # Handle image updates
            # The form sends back an image_id for each image field.
            # We use this ID to update the correct ProductImage object.
            for i in range(1, len(images) + 1):
                image_file = request.FILES.get(f'image{i}')
                image_id = request.POST.get(f'image_id_{i}')

                if image_file and image_id:
                    try:
                        product_image = ProductImage.objects.get(id=image_id, product=product)

                        # Delete the old image file before saving the new one
                        if product_image.image:
                            product_image.image.delete(save=False)

                        # Save the new image
                        product_image.image = image_file
                        product_image.save()
                    except ProductImage.DoesNotExist:
                        # If the image object doesn't exist, create a new one
                        ProductImage.objects.create(product=product, image=image_file)
                elif image_file and not image_id:
                    # If a new image file is provided but no image_id, it means a new image is being added.
                    ProductImage.objects.create(product=product, image=image_file)

            product.save()
            return redirect('product')
        except Product.DoesNotExist:
            return redirect('product')
        except Product.DoesNotExist:
            return redirect('product')
    return render(request, 'backend/pages/page_control/product/edit.html', context)

def product(request):
    products = Product.objects.all()
    return render(request, 'backend/pages/page_control/product/Products.html', {'products': products})

def add_product(request):
    categories = ProductCategory.objects.all()
    subcategories = ProductSubcategory.objects.all()
    context = {
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
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')    
        image3 = request.FILES.get('image3')

        if not image1 or not image2 or not image3 or not name or not description or not price or not reference or not brand or not category or not subcategory:
            return render(request, 'backend/pages/page_control/product/add.html', {
                'error': 'All fields are required.',
                'categories': categories,
                'subcategories': subcategories,
            })

        product = Product(
            name=name,
            description=description,
            price=price,
            reference=reference,
            brand=brand,
            category=category,
            subcategory=subcategory
        )
        product.save()

        # Handle image uploads
        for i in range(1, 4):
            image_file = request.FILES.get(f'image{i}')
            if image_file:
                ProductImage.objects.create(product=product, image=image_file)

        return redirect('product') # Redirect to product list
    return render(request, 'backend/pages/page_control/product/add.html', context)
