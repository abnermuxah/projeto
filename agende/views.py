from cmath import log
from urllib.request import Request
from django.template import RequestContext
from django.core.exceptions import ValidationError
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from agende.forms import RegisterForm, Login
from agende.models import usuario
from .forms import Agendamento, RegisterForm
from django.contrib.auth import authenticate
import datetime
# Create your views here.


def home(request):
    login = Login(request.POST)
    if request.method == 'POST':
        cpf_rec = login.data['cpf']
        senha_rec = login.data['senha']
        login_valid = usuario.objects.values_list('cpf', 'senha')
        i = 0
        while (i < len(login_valid)):
            if str(cpf_rec) == str(login_valid[i][0]) and str(senha_rec) == str(login_valid[i][1]) and len(cpf_rec) == 11:
                # return render(request, 'agendamento.html')
                return redirect('/agendamento')
            i = i + 1
        return HttpResponse("CPF Inválido ou Senha Incorreta, tente novamente")

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
    agendamento = Agendamento(request.POST)
    if request.method == 'POST':
        HttpResponse("Buc")
    else:
        agendamento = Agendamento()
    return render(request, 'agendamento.html', {'agendamento': agendamento})
