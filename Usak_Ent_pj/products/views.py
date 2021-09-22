from django.shortcuts import render
from django.contrib import messages

from .form import Register_userForm

from .product_selector import(get_Categories,get_Category)

# Create your views here.

def manage_user(request):
    Registeruser = Register_userForm()
    get_Categorys = get_Categories()
    if request.method == "POST":
        Registeruser = Register_userForm(request.POST,request.FILES)
        if Registeruser.is_valid():
            Registeruser.save()
            messages.success(request,'user registered successfully')
        else:
            messages.warning(request,'invalid user input')    
    context={
        "Register_userForm":Register_userForm,
        "get_Categorys":get_Categorys
    }
    return render (request,"index.html",context)        

