from django.contrib import admin
from controle_gastos_app.models import Categoria, Estabelecimento, Gasto, Usuario

class Gastos(admin.ModelAdmin):
    # infos disponibilizadas na tela de admin
    list_display = ('id', 
                    'id_usuario', 
                    'id_estabelecimento', 
                    'id_categoria', 
                    'valor', 
                    'data_gasto', 
                    'forma_pagamento')
    # campos que possiblitam a alteração do gasto
    list_display_links = ('id', 
                          'id_usuario', 
                          'id_estabelecimento', 
                          'id_categoria', 
                          'valor', 
                          'data_gasto', 
                          'forma_pagamento')
    # campos de busca
    search_fields = ('id', 
                     'id_estabelecimento', 
                     'id_categoria', 
                     'valor',)
    # criando paginação
    list_per_page = 20

admin.site.register(Gasto, Gastos)

class Categorias(admin.ModelAdmin):
    list_display = ('id', 'categoria')
    list_display_links = ('id', 'categoria')
    search_fields = ('id', 'categoria')
    list_per_page = 20

admin.site.register(Categoria, Categorias)

class Estabelecimentos(admin.ModelAdmin):
    list_display = ('id', 'estabelecimento')
    list_display_links = ('id', 'estabelecimento')
    search_fields = ('id', 'estabelecimento')
    list_per_page = 20

admin.site.register(Estabelecimento, Estabelecimentos)

class Usuarios(admin.ModelAdmin):
    list_display = ('id', 'usuario')
    list_display_links = ('id', 'usuario')
    search_fields = ('id', 'usuario')
    list_per_page = 20

admin.site.register(Usuario, Usuarios)
