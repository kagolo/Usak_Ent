from django.contrib import admin
from .models import bags,Register_users,Scarves,Ladies_wear,Men_wear,Category

# Register your models here.
# @admin.register(bags,order)
admin.site.register(Register_users)
admin.site.register(Category)
admin.site.register(bags)
admin.site.register(Scarves)
admin.site.register(Ladies_wear)
admin.site.register(Men_wear)

# class MyCustomAdmin(admin.ModelAdmin):
#     list_display = ('id','User_name','Email','password')
