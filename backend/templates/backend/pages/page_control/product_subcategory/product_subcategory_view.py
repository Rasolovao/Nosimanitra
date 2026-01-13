from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from client.models import  ProductCategory, ProductSubcategory


def product_sub_categ(request):

    subcategories = ProductSubcategory.objects.all()

    return render(request, 'backend/pages/page_control/product_subcategory/subcategories.html', {'subcategories': subcategories})

def add_product_sub_categ(request):

    if request.method == 'POST':
        subcategory_name = request.POST.get('subcategory-name')
        category_id = request.POST.get('category-name')
        
        # --- Basic Validation Error ---
        if not subcategory_name or len(subcategory_name.strip()) == 0:
            # Pass the error message in the context
            context = {'error': 'Subcategory name cannot be empty. Please enter a value.'}
            context['categories'] = ProductCategory.objects.all()
            return render(request, 'backend/pages/page_control/product_subcategory/add.html', context)
        
        # --- Database Save Error ---
        try:
            category = ProductCategory.objects.get(id=category_id)
            ProductSubcategory.objects.create(name=subcategory_name, category=category)
            return redirect('product_sub_categ') 
            
        except ProductCategory.DoesNotExist:
            context = {'error': 'Selected category does not exist.'}
            context['categories'] = ProductCategory.objects.all()
            return render(request, 'backend/pages/page_control/product_subcategory/add.html', context)
        
        except Exception as e:
            # Pass the error message in the context for database issues
            context = {'error': f'An error occurred while saving. Check if the subcategory already exists for the selected category.'}
            # Optional: You can also pass back the failed input value
            context['subcategory_name_value'] = subcategory_name 
            context['categories'] = ProductCategory.objects.all()
            return render(request, 'backend/pages/page_control/product_subcategory/add.html', context)        
    return render(request, 'backend/pages/page_control/product_subcategory/add.html')

def delete_subcategory(request, subcategory_id):
    if request.method == 'POST':
        try:
            subcategory = ProductSubcategory.objects.get(id=subcategory_id)
            subcategory.delete()
            return redirect('product_sub_categ')
        except ProductSubcategory.DoesNotExist:
            # Handle the case where the subcategory does not exist
            return redirect('product_sub_categ')
        
    

    

def edit_product_sub(request,  subcategory_id):
        categories = ProductCategory.objects.all()
        subcategory = ProductSubcategory.objects.get(id=subcategory_id) 
        if request.method == 'POST':
            try:
                updatedSubcategory = request.POST.get('subcategory_name')
                updatedCategory = request.POST.get('category_name')
                subcategory.name = updatedSubcategory
                subcategory.category = ProductCategory.objects.get(id=updatedCategory)
                subcategory.save()
                return redirect('product_sub_categ')
            except (ProductSubcategory.DoesNotExist, ProductCategory.DoesNotExist):
                return redirect('product_sub_categ')
        return render(request, 'backend/pages/page_control/product_subcategory/edit.html', {'subcategory': subcategory, 'categories': categories})
