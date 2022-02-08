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
    if request.method == 'POST':
        # login = Login(request.POST)
        login = Login(request.POST)
        # validação de usuario
        # se CPF tiver cadastrado entrar e
        # se Senha for igual a do CPF cadastrado entrar
        # para pagina de agendamento

        # validar CPF
        cpf_rec = login.data['cpf']
        senha_rec = login.data['senha']
        login_valid = usuario.objects.values_list('cpf', 'senha')
        i = 0
        for i in range(len(login_valid)):
            if (str(cpf_rec) == str(login_valid[i][0]) and str(senha_rec) == str(login_valid[i][1]) and len(cpf_rec) == 11):
                return render(request, 'agendamento.html')
        return HttpResponse("CPF ou Senha Incorretos")
        # if (str(cpf_rec) in str(login_valid[0][0])):

    else:
        login = Login()


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

    return render(request, 'agendamento.html', {'form': form})


def agendamento(request):
    return render(request, 'agendamento.html')
