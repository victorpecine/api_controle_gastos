from django.db import models
from datetime import datetime

# aqui foram criados os modelos do banco de dados

class Gasto(models.Model):
    id_usuario = models.IntegerField,
    id_estabelecimento = models.IntegerField,
    id_categoria = models.IntegerField,
    valor = models.FloatField,
    data_gasto = models.DateField(datetime.now),
    forma_pagamento = models.CharField(max_length=8)

    def __str__(self):
        return self.id_gastos

class Usuario(models.Model):
    usuario = models.CharField(max_length=10)

class Estabelecimento(models.Model):
    estabelecimento = models.CharField(max_length=10)

class Categoria(models.Model):
    CATEGORIA = (
        ('B', 'Bar'),
        ('D', 'Delivery'),
        ('M', 'Mercado')
    )
    categoria = models.CharField(max_length=1, choices=CATEGORIA, blank=False, null=False, unique=True)

class FormaPagamento(models.Model):
    PAGAMENTO = (
        ('Deb', 'Débito'),
        ('Din', 'Dinheiro'),
        ('Cre', 'Crédito')
    )
    forma_de_pagamento = models.CharField(max_length=3, choices=PAGAMENTO, blank=False, null=False, unique=True)
