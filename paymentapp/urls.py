from django.urls import path
from . import views

urlpatterns = [
 path("checked",views.checked,name="checked")   
]