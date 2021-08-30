from django.contrib import admin
from .models import bags,Register_users

# Register your models here.
# @admin.register(bags,order)
admin.site.register(Register_users)

class MyCustomAdmin(admin.ModelAdmin):
    list_display = ('id','User_name','Email','password')
