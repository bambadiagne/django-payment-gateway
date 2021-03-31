from django.urls import path
from . import views

urlpatterns = [
 path("signup",views.signup,name="signup"),
 path("signin",views.signin,name="signin"),
 path("all_products",views.all_products,name="all_products")   
]