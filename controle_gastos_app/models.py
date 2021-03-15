from django.db import models
from datetime import datetime

# aqui foram criados os modelos do banco de dados
class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=10, default=None, db_column='Usuário')
    
    def __str__(self):
        return self.nome_usuario

class Categoria(models.Model):
    categoria = models.CharField(max_length=100, blank=False, null=False, db_column='Categoria')

    def __str__(self):
        return self.categoria

class Estabelecimento(models.Model):
    nome_estabelecimento = models.CharField(max_length=100, blank=True, default=None, db_column='Estabelecimento')
    categoria_estabelecimento = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, db_column='Categoria')
    
    def __str__(self):
        return self.nome_estabelecimento

class FormaPagamento(models.Model):
    pagamento = models.CharField(max_length=10, blank=False, null=False, default=None, db_column='Forma de Pagamento')

    def __str__(self):
        return self.pagamento

class Gasto(models.Model):
    # quando o usuário for deletado os gastos dele também serão
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='Usuário')

    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.DO_NOTHING, default=None, db_column='Estabelecimento')

    # quando o pagamento for deletado o respectivo gasto também será
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE, default=None, db_column='Forma de Pagamento') 

    data_pagamento = models.DateTimeField(datetime.now, auto_now=True, db_column='Data de Pagamento')

    # valor_gasto = models.FloatField(blank=False, default=None)
    valor_gasto = models.DecimalField(max_digits=10, decimal_places=2 , blank=False, default=None, db_column='Valor (R$)')
