"""Usak_Ent_pj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from Usak_Ent_pj.products.views import manage_user
# from Usak_Ent_pj.products.form import Register_userForm
from django.contrib import admin
from django.urls import path

from products import views

admin.site.site_header="Usak Ent project"
admin.site.index_title="Usak Enterprises"
admin.site.site_title="Usak Enterprises Ltd"

urlpatterns = [
    path('', views.manage_user,name="login"),
    path('admin/', admin.site.urls),
]
