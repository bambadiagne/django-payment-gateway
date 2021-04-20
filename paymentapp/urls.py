from django.urls import path
from . import views

urlpatterns = [
 path("checked",views.checked,name="checked"),
 path("order_product/<int:product_id>",views.order,name="order_product")   
]