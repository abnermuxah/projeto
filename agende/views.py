from cmath import log
from http.client import LineTooLong
from posixpath import split
from urllib.request import Request
from django.template import RequestContext
from django.core.exceptions import ValidationError
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from agende.forms import RegisterForm, Login, Agendamento
from agende.models import usuario, unidade, agendamento
from .forms import Agendamento, RegisterForm
import datetime
# Create your views here.


def home(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')
        login_valid = usuario.objects.values_list('cpf', 'senha')
        i = 0
        while (i < len(login_valid)):
            if cpf == str(login_valid[i][0]) and senha == str(login_valid[i][1]) and len(cpf) == 11:
                # return render(request, 'agendamento.html')
                return redirect('/agendamento')
            i = i + 1
        return HttpResponse("CPF Inválido ou Senha Incorreta, tente novamente")
    return render(request, 'home.html')


def cadastro(request):
    if request.method == 'POST':
        # validação dos dados permitir > 18
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        ano_atual = datetime.datetime.today().year
        ano_nasc = int(request.POST.get('data_nasc')[:4])
        data_nasc = request.POST.get('data_nasc')
        ano_atual = int(datetime.datetime.today().year)
        senha = request.POST.get('senha')
        senha2 = request.POST.get('senha2')
        idade = ano_atual - ano_nasc
        login_valid = usuario.objects.values_list('cpf', 'senha')
        if len(cpf) != 11 or idade <= 18 or senha != senha2:
            return HttpResponse("Dados Inválidos : CPF ou Idade < 18 ou Senha Diferente")
        else:
            # verificar se o CPF informado pertence a base de dados
            for i in range(len(login_valid)):
                if cpf == login_valid[i][0]:
                    return HttpResponse("Ja existe esse CPF cadastrado")
            cad = usuario(nome=nome, cpf=cpf, data_nasc=data_nasc,
                          senha=senha, senha2=senha2)
            cad.save()
            return HttpResponse("Usuario cadastrado com sucesso!")

    else:
        return render(request, 'cadastro.html')


def agendamento(request):
    if request.method == 'GET':
        x = request.GET.get('name')
        return HttpResponse(x)
        # return render(request, 'agendamento.html')
