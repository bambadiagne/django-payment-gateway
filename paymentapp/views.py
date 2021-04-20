from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
import hashlib
from . import forms
from paydunya import InvoiceItem
from .paydunya_conf import invoice,PAYDUNYA_ACCESS_TOKENS
from .models import Product
import json
def payment_page(request):
 pass
 #   invoice = paydunya.Invoice(settings.store)
    
def checked(request):
    try:
        hash_=request.POST['data']['hash']
        if(hash_== hashlib.sha512(settings.PAYDUNYA_ACCESS_TOKENS["PAYDUNYA-MASTER-KEY"]).hexdigest()):
            if(request.POST['data']['status'] == "completed"):
                pass
        else:
            print("Cette requête n'a pas été émise par PayDunya")
    except:
        print("Une erreur est survenue")
def order(request,product_id):
    product_to_buy=Product.objects.filter(pk=product_id).first()
    invoice.add_items([InvoiceItem(
    name=product_to_buy.product_title,
    quantity=1,
    unit_price=str(4000),
    total_price=str(4000),
    description=product_to_buy.product_description
  ),])
    invoice.total_amount=product_to_buy.product_price
    successful, response = invoice.create()
    if successful:
        print(successful)
        return redirect("home")
    print(response)    