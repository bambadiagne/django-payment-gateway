from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login,logout
from paymentapp import forms

def home(request):
    return render(request,"index.html")
def signup(request):
    if(request.method=="GET"):
       user_form=forms.UserForm()
       return render(request,"auth/signup.html",{"errors":""}) 
    elif(request.method=="POST"):
       user_form=forms.UserForm(request.POST)
       if(user_form.is_valid()):
            user_created=user_form.save(commit=False)
            user_created.password=make_password(user_created.password)
            user_created.save()
            return render(request,"auth/signin.html")
       else:
           return render(request,"auth/signup.html",{"errors":user_form.errors})
def signin(request):
    if(request.method=="GET"):
       return render(request,"auth/signin.html",{"errors":""}) 
    elif(request.method=="POST"):
        email=request.POST['email'] 
        password=request.POST['password']
        
        if(email and password):
            user_ = authenticate(request, email=request.POST['email'], password=request.POST['password'])
            if(user_):
                login(request,user_)
                return redirect('all_products')
            else:    
                return render(request,"auth/signin.html",{"errors":"Mot de passe ou identifiant incorrect"})
        else:
           return render(request,"auth/signin.html",{"errors":"Un de vos champs est nul"})
def logout_view(request):
    logout(request)
    return redirect('home')               