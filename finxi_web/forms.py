from django import forms
from .models import BasicUserMod, Customer, House


class UserForm(forms.ModelForm):
    class Meta:
        model = BasicUserMod
        fields = ("first_name", "last_name", "username", "password", "email")


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ("title", "about", "street", "district", "city", "rent")
