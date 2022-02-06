from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse('PAGINA DE LOGIN')


def cadastro(request):
    return HttpResponse('CADASTRO')


def agendamento(request):
    return HttpResponse('AGENDAMENTO')
