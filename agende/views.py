from http.client import LineTooLong
from posixpath import split
from re import A, template
from unittest import loader
from urllib import response
from urllib.request import Request
from django import http
from django.template import RequestContext
from django.core.exceptions import ValidationError
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from agende.models import usuario, unidade  # , agendamento
from agende.models import agendamento as agend
import datetime
import calendar

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
    data_rec = request.POST.get('data')
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
        'nome_unid', 'cod_unid')
    context = {
        'cpf': cpf,
        'nome': nome,
        'data_nasc': data_nasc,
        'idade':  idade,
        'unidades': unidades
    }

    # horario = request.POST.get('data')
    # return HttpResponse(horario[:4]) retorna o ano informado
    # if request.method == 'GET':
    # return HttpResponse(horario)
    if request.method == 'POST':
        agendados = agend.objects.values_list(
            'data', 'cpf', 'cod_und')
        cad = agend(cpf=cpf, cod_und=request.POST.get('unidade'),
                    data=data_rec)
        hora, minu = int(data_rec[11:13]), int(data_rec[14:16])
        data_rec = datetime.date(
            int(data_rec[:4]), int(data_rec[5:7]), int(data_rec[8:10]))
        # se o dia for hoje | sabado ou domingo => não cadastrar
        if (data_rec <= datetime.date.today()) or (calendar.day_name[data_rec.weekday()] == 'Saturday') or (calendar.day_name[data_rec.weekday()] == 'Sunday') or (hora < 8) or (hora > 12):
            return HttpResponse("Não é possível cadastrar dias anteriories, dias atuais nem sabados e domingos, e horario diferente de 8 as 12.")
        for i in range(len(agendados)):
            if cpf == str(agendados[i][1]):
                return HttpResponse("Não pode agendar Está Agendado ou Data Inválida")
        cad.save()
        return HttpResponse("Agendado com Sucesso")
    return render(request, 'agendamento.html', context)


"""""
        

"""
