from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views



from .templates.backend.pages.page_control.product.product_views import (
    delete_product,
    edit_product,
    product,
    add_product,
)
from .templates.backend.pages.page_control.product_category.product_category_views import (
    product_categ,
    add_product_categ,
    edit_product_cat,
    delete_category,
)

from .templates.backend.pages.page_control.product_subcategory.product_subcategory_view import (
    product_sub_categ,                                                                                                      
    add_product_sub_categ,
    edit_product_sub,
    delete_subcategory,
)         

from .templates.backend.pages.page_control.carousel.carousel_view import (
    main_carousel_control,
    add_main_carousel,
    delete_image
)

from .templates.backend.pages.page_control.navbar_control.navbar_control_view import (
    navbar_control
)



urlpatterns = [
    # Add your backend app URLs here
    path('',login_required(views.home), name='home'),
  
    path('product-categories/', login_required(product_categ), name='product_categ'),
    path('add-product-category/',login_required(add_product_categ), name='add_product_categ'),
    path('product-subcategories/',login_required(product_sub_categ), name='product_sub_categ'),
    path('add-product-subcategory/',login_required(add_product_sub_categ), name='add_product_sub_categ'),
    path('delete-category/<int:category_id>/',login_required(delete_category), name='delete_category'),
    path('delete-subcategory/<int:subcategory_id>/',login_required(delete_subcategory), name='delete_subcategory'),
    path('edit-category/<int:category_id>/',login_required(edit_product_cat), name='edit_category_cat'),
    path('edit-subcategory/<int:subcategory_id>/',login_required(edit_product_sub), name='edit_subcategory'),
    path('product/', login_required(product), name='product'),
    path('product/add/', login_required(add_product), name='add_product'),
    path('product/edit/<int:product_id>/',login_required(edit_product), name='edit_product'),
    path('product/delete/<int:product_id>/', login_required(delete_product), name='delete_product'),
    path("main_carousel_control/", login_required(main_carousel_control), name="main_carousel_control"),
    path('add-main-carousel', login_required(add_main_carousel), name='add_main_carousel'),
    path('delete-image/<int:image_id>/', login_required(delete_image), name='delete_image'),
    path('navbar_control/', login_required(navbar_control), name='navbar_control'),
    path('login/', auth_views.LoginView.as_view(template_name='user_account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
]

