from email.policy import default
from django.db import models
from django.http import HttpResponse


class usuario(models.Model):
    nome = models.CharField(max_length=65, default=None)
    cpf = models.IntegerField(max_length=65, default=None)
    data_nasc = models.DateField(default=None)
    senha = models.CharField(max_length=12, default=None)


class unidade (models.Model):
    cod_unid = models.CharField(max_length=65, default=None)
    nome_unid = models.CharField(max_length=65, default=None)


class agendamento(models.Model):
    data = models.DateTimeField()
    cpf = models.ForeignKey(usuario, on_delete=models.CASCADE)
    cod_und = models.ForeignKey(unidade, on_delete=models.CASCADE)
