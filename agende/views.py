from atexit import register
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from agende.forms import RegisterForm
from .forms import RegisterForm
import datetime
# Create your views here.


def home(request):
    return render(request, 'home.html')


def cadastro(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        # validação dos dados permitir > 18
        ano_atual = datetime.datetime.today().year
        ano_nasc = form.data['data_nasc']
        idade = ano_atual - int(ano_nasc[6:])

        if len(form.data['cpf']) == 11 and idade >= 18:
            # form.save()

            return HttpResponse('Deu certo parça')

        # if form.is_valid():
            # return HttpResponse('Cadastro efetuado com sucesso!')
            # return HttpResponse(form.data['cpf'])
    else:
        form = RegisterForm()
    return render(request, 'cadastro.html', {'form': form})


def agendamento(request):
    return render(request, 'agendamento.html')
