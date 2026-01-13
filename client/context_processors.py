from .models import ProductCategory

def categories_processor(request):
    categories = ProductCategory.objects.all()
    return {'categories': categories}
