from django.db import models


class usuario(models.Model):
    nome = models.CharField(max_length=65, default=None)
    cpf = models.CharField(max_length=11, primary_key=True)
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
    cpf = models.IntegerField(max_length=11,
                              default=None)
    cod_und = models.IntegerField(max_length=11,
                                  default=None)
