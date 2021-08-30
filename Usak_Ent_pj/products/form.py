from crispy_forms.helper import FormHelper

from django.db.models.base import Model
from django.forms import ModelForm
from django import forms

from .models import(Register_users)

class Register_userForm(forms.ModelForm):


    class Meta:
        Model = Register_users
        fields = ['User_name','Email','password']
    # def __init__(self, *args, **kwargs):
    #     super(Register_userForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()        
    
