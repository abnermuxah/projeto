from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
# criar um form atrelado a um model


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
