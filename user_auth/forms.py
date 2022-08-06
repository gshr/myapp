
# import the standard Django Forms
# from built-in library
from dataclasses import field
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import  CustomerModel
# creating a form
class RegistrationForm(ModelForm):
    class Meta:
        model=CustomerModel
        fields = "__all__"