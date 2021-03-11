from django.db import models
from datetime import datetime

class gastos(models.Model):
    id_gastos = models.IntegerField,
    id_usuario = models.IntegerField,
    id_estabelecimento = models.IntegerField,
    id_categoria = models.IntegerField,
    valor = models.FloatField,
    data_gasto = models.DateField(datetime.now),
    forma_pagamento = models.CharField(max_length=8)

    def __str__(self):
        return self.id_gastos

class usuarios(models.Model):
    id_usuario = models.IntegerField,
    usuario = models.CharField(max_length=10)

class estabelecimentos(models.Model):
    id_estabelecimento = models.IntegerField,
    estabelecimento = models.CharField(max_length=10)

class categorias(models.Model):
    CATEGORIA = (
        ('B', 'Bar'),
        ('D', 'Delivery'),
        ('M', 'Mercado')
    )
    id_categoria = models.IntegerField,
    categoria = models.CharField(max_length=1, choices=CATEGORIA, blank=False, null=False)