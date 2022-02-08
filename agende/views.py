from cmath import log
from django.template import RequestContext
from django.core.exceptions import ValidationError
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from agende.forms import RegisterForm, Login
from agende.models import usuario
from .forms import RegisterForm
from django.contrib.auth import authenticate
import datetime
# Create your views here.


def home(request):
    login = Login(request.POST)
    if request.method == 'POST':

        return HttpResponse(login.data['cpf'])
    else:
        login = Login()

    return render(request, 'home.html', {'login': login})


def cadastro(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        # validação dos dados permitir > 18
        ano_atual = datetime.datetime.today().year
        ano_nasc = form.data['data_nasc']
        idade = ano_atual - int(ano_nasc[6:])

        if len(form.data['cpf']) == 11 and idade >= 18 and form.data['senha'] == form.data['senha2']:
            form.save()
            return HttpResponse('Cadastro efetuado com sucesso!')

        else:
            # return HttpResponse('Cadastro efetuado com sucesso!')
            # return HttpResponse(form.data['cpf'])
            return HttpResponse('ERRO: CPF Inválido ou Menor de 18 anos ou Senha Inválida')
    else:
        form = RegisterForm()

    return render(request, 'cadastro.html', {'form': form})


def agendamento(request):
    return render(request, 'agendamento.html')
