from django.db import models
from django.http import HttpResponse


class cadastro(models.Model):
    nome_completo = models.CharField(max_length=60)
    nome_completo = models.CharField(max_length=60)
    data_nasc = models.CharField(max_length=10)
    senha = models.CharField(max_length=10)
