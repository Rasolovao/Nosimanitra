from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from client.models import  ProductCategory, ProductSubcategory

def product_categ(request):

    ProductCategories = ProductCategory.objects.all()
    ProductSubcategories = ProductSubcategory.objects.all()

    return render(request, 'backend/pages/page_control/product_category/categories.html', {'categories': ProductCategories,'subcategories': ProductSubcategories})

def add_product_categ(request):
    """
    Handles both displaying the form and processing the submission.
    """

    if request.method == 'POST':
        category_name = request.POST.get('category_name')
        
        # --- Basic Validation Error ---
        if not category_name or len(category_name.strip()) == 0:
            # Pass the error message in the context
            context = {'error': 'Category name cannot be empty. Please enter a value.'}
            return render(request, 'backend/pages/page_control/product_category/add.html', context)

        # --- Database Save Error ---
        try:
            ProductCategory.objects.create(name=category_name)
            return redirect('product_categ')
            
        except Exception as e:
            # Pass the error message in the context for database issues
            context = {'error': f'An error occurred while saving. Check if the category already exists.'}
            # Optional: You can also pass back the failed input value
            context['category_name_value'] = category_name 
            return render(request, 'backend/pages/page_control/product_category/add.html', context)

    # Handle GET Request
    return render(request, 'backend/pages/page_control/product_category/add.html')

def edit_product_cat(request, category_id):
    category = ProductCategory.objects.get(id=category_id)
    if request.method == 'POST':
        try:
            
            updatedCategory = request.POST.get('category_name')
            category.name = updatedCategory
            category.save()
            return redirect('product_categ')
        except ProductCategory.DoesNotExist:
            return redirect('product_categ')

    return render(request, 'backend/pages/page_control/product_category/edit.html', {'category': category})





def delete_category(request, category_id):
    if request.method == 'POST':
        try:
            category = ProductCategory.objects.get(id=category_id)
            if category.subcategories.exists():
                context = {
                    'error': 'Cannot delete category with existing subcategories. Please delete subcategories first.',
                    'categories': ProductCategory.objects.all()
                }
                return render(request, 'backend/pages/page_control/product_category/categories.html', context)
            category.delete()
            return redirect('product_categ')
        except ProductCategory.DoesNotExist:
            return redirect('product_categ')
    return redirect('product_categ')
    if request.method == 'POST':
        try:
            category = ProductCategory.objects.get(id=category_id)
            if category.subcategories.exists():
                context = {
                    'error': 'Cannot delete category with existing subcategories. Please delete subcategories first.',
                    'categories': ProductCategory.objects.all()
                }
                return render(request, 'backend/pages/ProductCateg.html', context)
            category.delete()
            return redirect('product_categ')
        except ProductCategory.DoesNotExist:
            return redirect('product_categ')
    return redirect('product_categ')
