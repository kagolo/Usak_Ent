from django.db import models
from django.db.models.fields.files import ImageField
from django_countries.fields import CountryField

# Create your models here.
class bags(models.Model):
    item_number=models.CharField(max_length=200,null=False,unique=True)
    item_name=models.CharField(max_length=200,null=False)
    stock_date=models.DateField(auto_now_add=True)
    country=CountryField(multiple=False)
    item_image=models.ImageField()

# class order(models.Model):
#     pass  

class Register_users(models.Model):
    User_name=models.CharField(max_length=200,null=False)
    Email=models.EmailField()
    password=models.CharField(max_length=100)


    
    

