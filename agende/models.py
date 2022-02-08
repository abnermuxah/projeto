from datetime import datetime
from email.policy import default
from django.db import models
from django.http import HttpResponse


class usuario(models.Model):
    nome = models.CharField(max_length=65, default=None)
    cpf = models.IntegerField(primary_key=True, default=None)
    data_nasc = models.DateField()
    senha = models.CharField(max_length=12, default=None)
    senha2 = models.CharField(max_length=12, default=None)

    def __str__(self):
        return self.nome


class unidade (models.Model):
    cod_unid = models.IntegerField(
        default=None, primary_key=True)
    nome_unid = models.CharField(max_length=65, default=None)

    def __str__(self):
        return self.nome_unid


class agendamento(models.Model):
    data = models.DateTimeField()
    cod_agend = models.IntegerField(primary_key=True, default=None)
    cpf = models.ForeignKey(usuario, on_delete=models.CASCADE)
    cod_und = models.ForeignKey(unidade, on_delete=models.CASCADE)


# valodações
