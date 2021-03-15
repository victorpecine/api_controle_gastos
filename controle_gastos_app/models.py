from django.db import models
from datetime import datetime

# aqui foram criados os modelos do banco de dados
class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=10, default=None)
    
    def __str__(self):
        return self.nome_usuario

class Categoria(models.Model):
    categoria = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.categoria

class Estabelecimento(models.Model):
    nome_estabelecimento = models.CharField(max_length=100, blank=True, default=None)
    categoria_estabelecimento = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, default=1)
    
    def __str__(self):
        return self.nome_estabelecimento

# class FormaPagamento(models.Model):
#     PAGAMENTO = (
#         ('Deb', 'Débito'),
#         ('Din', 'Dinheiro'),
#         ('Cre', 'Crédito')
#     )
#     forma_de_pagamento = models.CharField(max_length=3, choices=PAGAMENTO, blank=False, null=False, default='Deb')

class FormaPagamento(models.Model):
    pagamento = models.CharField(max_length=10, blank=False, null=False, default=None)

    def __str__(self):
        return pagamento

class Gasto(models.Model):
    # quando o usuário for deletado os gastos dele também serão
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.DO_NOTHING, default=None)

    # quando o pagamento for deletado o respectivo gasto também será
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE, default=None) 

    data_pagamento = models.DateTimeField(datetime.now, auto_now=True)

    valor_gasto = models.FloatField(blank=False, default=None)
