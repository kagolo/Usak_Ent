from django.db import models
from django.db.models.fields.files import ImageField
from django_countries.fields import CountryField

# Create your models here.
class Category(models.Model):
    CAT_TYPE_CHOICES=[
        ('BAGS','BAGS'),
        ('SCARVES','SCARVES'),
        ('MEN_WEAR','MEN_WEAR'),
        ('LADIES_WEAR','LADIES_WEAR')
    ]
    item_name=models.CharField(max_length=300,choices=CAT_TYPE_CHOICES)
class bags(models.Model):
    item_number=models.CharField(max_length=200,null=False,unique=True)
    item_name=models.CharField(max_length=200,null=False)
    stock_date=models.DateField(auto_now_add=True)
    country=CountryField(multiple=False)
    item_image=models.ImageField()
    item_price=models.CharField(max_length=200,null=False)
    STATUS_TYPE_CHOICES=[
        ('USED','USED'),
        ('NEW','NEW')
    ]
    item_status=models.CharField(max_length=100,choices=STATUS_TYPE_CHOICES)
    SPECIAL_DEAL_TYPE_CHOICES=[
        ('YES', 'YES'),
        ('NO', 'NO')
    ]
    item_special_deal=models.CharField(max_length=200,choices=SPECIAL_DEAL_TYPE_CHOICES)
    SPECIAL_OFFER_TYPE_CHOICES=[
        ('YES', 'YES'),
        ('NO', 'NO')
    ]
    item_special_offer=models.CharField(max_length=200,choices=SPECIAL_OFFER_TYPE_CHOICES)
    item_sub_image1=models.ImageField()
    item_sub_image2=models.ImageField()
    item_sub_image3=models.ImageField()


class Scarves(models.Model):
    item_number=models.CharField(max_length=200,null=False,unique=True)
    item_name=models.CharField(max_length=200,null=False)
    stock_date=models.DateField(auto_now_add=True)
    country=CountryField(multiple=False)
    item_image=models.ImageField()
    item_price=models.CharField(max_length=200,null=False)
    STATUS_TYPE_CHOICES=[
        ('USED','USED'),
        ('NEW','NEW')
    ]
    item_status=models.CharField(max_length=100,choices=STATUS_TYPE_CHOICES)
    SPECIAL_DEAL_TYPE_CHOICES=[
        ('YES', 'YES'),
        ('NO', 'NO')
    ]
    item_special_deal=models.CharField(max_length=200,choices=SPECIAL_DEAL_TYPE_CHOICES)
    SPECIAL_OFFER_TYPE_CHOICES=[
        ('YES', 'YES'),
        ('NO', 'NO')
    ]
    item_special_offer=models.CharField(max_length=200,choices=SPECIAL_OFFER_TYPE_CHOICES)
    item_sub_image1=models.ImageField()
    item_sub_image2=models.ImageField()
    item_sub_image3=models.ImageField()

class Men_wear(models.Model):
    item_number=models.CharField(max_length=200,null=False,unique=True)
    item_name=models.CharField(max_length=200,null=False)
    stock_date=models.DateField(auto_now_add=True)
    country=CountryField(multiple=False)
    item_image=models.ImageField()
    item_price=models.CharField(max_length=200,null=False)
    STATUS_TYPE_CHOICES=[
        ('USED','USED'),
        ('NEW','NEW')
    ]
    item_status=models.CharField(max_length=100,choices=STATUS_TYPE_CHOICES)
    SPECIAL_DEAL_TYPE_CHOICES=[
        ('YES', 'YES'),
        ('NO', 'NO')
    ]
    item_special_deal=models.CharField(max_length=200,choices=SPECIAL_DEAL_TYPE_CHOICES)
    SPECIAL_OFFER_TYPE_CHOICES=[
        ('YES', 'YES'),
        ('NO', 'NO')
    ]
    item_special_offer=models.CharField(max_length=200,choices=SPECIAL_OFFER_TYPE_CHOICES)
    item_sub_image1=models.ImageField()
    item_sub_image2=models.ImageField()
    item_sub_image3=models.ImageField()

class Ladies_wear(models.Model):
    item_number=models.CharField(max_length=200,null=False,unique=True)
    item_name=models.CharField(max_length=200,null=False)
    stock_date=models.DateField(auto_now_add=True)
    country=CountryField(multiple=False)
    item_image=models.ImageField()
    item_price=models.CharField(max_length=200,null=False)
    STATUS_TYPE_CHOICES=[
        ('USED','USED'),
        ('NEW','NEW')
    ]
    item_status=models.CharField(max_length=100,choices=STATUS_TYPE_CHOICES)
    SPECIAL_DEAL_TYPE_CHOICES=[
        ('YES', 'YES'),
        ('NO', 'NO')
    ]
    item_special_deal=models.CharField(max_length=200,choices=SPECIAL_DEAL_TYPE_CHOICES)
    SPECIAL_OFFER_TYPE_CHOICES=[
        ('YES', 'YES'),
        ('NO', 'NO')
    ]
    item_special_offer=models.CharField(max_length=200,choices=SPECIAL_OFFER_TYPE_CHOICES)
    item_sub_image1=models.ImageField()
    item_sub_image2=models.ImageField()
    item_sub_image3=models.ImageField()

class Register_users(models.Model):
    User_name=models.CharField(max_length=200,null=False)
    Email=models.EmailField()
    password=models.CharField(max_length=100)

 # class order(models.Model):
#     pass 



    
    

