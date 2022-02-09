from ast import Global
from cmath import log
from http.client import LineTooLong
from posixpath import split
from re import template
from unittest import loader
from urllib import response
from urllib.request import Request
from django import http
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
                # salvar o CPF p usar em outra função
                request.session['cpf'] = cpf
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
    cpf = request.session['cpf']  # pegar o CPF da sessão
    login_valid = usuario.objects.values_list(
        'cpf', 'nome', 'data_nasc')
    # pegar os dados do CPF logado
    for i in range(len(login_valid)):
        if cpf == login_valid[i][0]:
            nome = login_valid[i][1]
            data_nasc = str(login_valid[i][2])
            idade = datetime.datetime.today().year - int(data_nasc[:4])
    # unidades cadastradas
    unidades = unidade.objects.values_list(
        'nome_unid')
    context = {
        'cpf': cpf,
        'nome': nome,
        'data_nasc': data_nasc,
        'idade':  idade,
        'unidades': unidades

    }
    return render(request, 'agendamento.html', context)
