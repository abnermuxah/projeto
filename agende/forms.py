from dataclasses import fields
from django import forms
#from django.contrib.auth.models import User
from .models import usuario
# criar um form atrelado a um model


class RegisterForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = '__all__'
