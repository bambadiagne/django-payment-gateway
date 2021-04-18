from django.shortcuts import render,redirect
from paymentapp.models import Product,Category
from .forms import ProductForm,CategoryForm
from filestack import Client
import os
client = Client(os.environ.get("FILESTACK_API_KEY"))
from .utils import handle_uploaded_file
def new_category(request):
    if(request.method=="GET"):
        category_form=CategoryForm()
        return render(request,'products/new_category.html',{"category_form":category_form})
    elif(request.method=="POST"):
        category_form=CategoryForm(request.POST)
        if(category_form.is_valid()):
            category_form.save()
            return redirect('all_products')    

def all_products(request):
    
    products=Product.objects.all()
    return render(request,"products/all_products.html",{"products":products})

def get_one_product(request,product_id):
    one_product=Product.objects.filter(pk=product_id).first()
    return render(request,"products/one_product.html",{"one_product":one_product})    

def new_product(request):
    
    if(request.method=="GET"):
        product_form=ProductForm()    
        return render(request,"products/new_product.html",{"product_form":product_form})    
    elif(request.method=="POST"):    
        product_form=ProductForm(request.POST,request.FILES)
        if(product_form.is_valid()):
            new_product=product_form.save(commit=False)
            
            store_params = {
            "mimetype": "image/png"
            }
            new_filelink = client.upload(filepath=handle_uploaded_file(request.FILES["product_image"]), store_params=store_params)
            new_product.product_image=new_filelink.url
            new_product.save()
            
            return redirect('all_products')
        
        return render(request,"products/new_product.html",{"errors":product_form.errors})     
def update_product(request,product_id):
    one_product=Product.objects.filter(id=product_id)
    product_form=ProductForm(instance=one_product)
    if(request.method=="GET"):
        return render(request,"products/update_product.html",{"product_form":product_form,"product_id":product_id})    
    elif(request.method=="POST"):    
        product_form=ProductForm(request.POST,request.FILES)
        if(product_form.is_valid()):
            if(product_form.has_changed()):
                one_product.update(*request.POST)
                return redirect('all_products')
            return redirect('all_products')
        return render(request,"products/new_product.html",{"errors":product_form.errors}) 
    
def delete_product(request,product_id):

    Product.objects.filter(id=product_id).first().delete()    
    return redirect("all_products")    
    