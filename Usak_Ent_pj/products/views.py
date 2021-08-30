from django.shortcuts import render
from django.contrib import messages

from .form import Register_userForm

# Create your views here.

def manage_user(request):
    Registeruser = Register_userForm()
    if request.method == "POST":
        Registeruser = Register_userForm(request.POST,request.FILES)
        if Register_userForm.is_valid():
            Register_userForm.save()
            messages.success(request,'user registered successfully')
        else:
            messages.warning(request,'invalid user input')    
    context={
        "Register_userForm":Register_userForm
    }
    return render (request,"index.html",context)        

