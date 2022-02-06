import re
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def cadastro(request):
    return render(request, 'cadastro.html')


def agendamento(request):
    return HttpResponse('AGENDAMENTO')
