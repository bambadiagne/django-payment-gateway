from django.shortcuts import render,redirect
from paymentapp.models import Product,Category
from .forms import ProductForm
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
        print(request.POST)
        print(request.FILES)
        if(product_form.is_valid()):
            product_form.save()
            return redirect('all_products')
        
        return render(request,"products/new_product.html",{"errors":product_form.errors})     
def update_product(request,product_id):
    one_product=Product.objects.filter(pk=product_id).first()
    
    if(request.method=="GET"):
        return render(request,"products/update_product.html")    
    elif(request.method=="POST"):    
        pass
    
def delete_product(request,product_id):

    Product.objects.filter(id=product_id).first().delete()    
    return redirect("all_products")    
    