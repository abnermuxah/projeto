from django.http import HttpResponse
from django.shortcuts import render
from agende.forms import RegisterForm
from .forms import RegisterForm
# Create your views here.


def home(request):
    return render(request, 'home.html')


def cadastro(request):
    form = RegisterForm()  # teste
    return render(request, 'cadastro.html', {
        'form': form,
    })


def agendamento(request):
    return render(request, 'agendamento.html')
