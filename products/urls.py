from django.urls import path
from . import views

urlpatterns = [
 path("",views.all_products,name="all_products"),
 path("new",views.new_product,name="new_product"),
 path("new_category",views.new_category,name="new_category"),
 path("<int:product_id>",views.get_one_product,name="one_product"),
 path("update/<int:product_id>",views.update_product,name="update_product"),
 path("delete/<int:product_id>",views.delete_product,name="delete_product"),  
]