from django import forms
from django.contrib.auth import forms as auth_forms
from .models import BasicUserMod, Customer
from PIL import Image
from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    
    class Meta:
        model = BasicUserMod
        fields = ('first_name', 'last_name', 'username', 'password', 'email')


