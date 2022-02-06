from django.db import models
from django.http import HttpResponse


class usuario(models.Model):
    nome_completo = models.CharField(max_length=60)
