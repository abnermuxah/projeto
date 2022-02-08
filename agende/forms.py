from dataclasses import fields
from django import forms
# from django.contrib.auth.models import User
from .models import usuario, agendamento

# criar um form atrelado a um model


class RegisterForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = '__all__'


class Login(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ['cpf', 'senha']


class Agendamento(forms.ModelForm):
    class Meta:
        model = agendamento
        fields = '__all__'
