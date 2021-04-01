from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
import hashlib
from . import forms
import paydunya
from payment_test import settings

def payment_page(request):
    invoice = paydunya.Invoice(settings.store)
    
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