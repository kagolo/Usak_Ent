from django.contrib import admin
from .models import bags

# Register your models here.
# @admin.register(bags,order)
admin.site.register(bags)

class MyCustomAdmin(admin.ModelAdmin):
    list_display = ('id','item_number','item_name', 'stock_date','country','item_image')
