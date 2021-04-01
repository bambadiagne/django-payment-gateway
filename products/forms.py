from django import forms
from django.forms.fields import CharField
from  django.core.validators import RegexValidator
from paymentapp.models import Product

# Create your models here.


class ProductForm(forms.ModelForm):
   
    class Meta:
        model=Product
        fields=["product_title","product_price","product_description","product_description","product_image","category_name"]
