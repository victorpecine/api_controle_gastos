from django.contrib import admin
from controle_gastos_app.models import Categoria, Estabelecimento, FormaPagamento, Gasto, Usuario

class Gastos(admin.ModelAdmin):
    # infos disponibilizadas na tela de admin
    list_display = ('id', 'estabelecimento', 'forma_pagamento', 'data_pagamento')

    # campos que possiblitam a alteração do gasto
    list_display_links = ('estabelecimento', 'forma_pagamento')

    # campos de busca
    search_fields = ('id', 'estabelecimento', 'forma_pagamento', 'data_pagamento')

    # criando paginação
    list_per_page = 20

admin.site.register(Gasto, Gastos)

class Categorias(admin.ModelAdmin):
    list_display = ('id', 'categoria')
    list_display_links = ('id', 'categoria')
    search_fields = ('id', 'categoria',)
    list_per_page = 20

admin.site.register(Categoria, Categorias)

class Estabelecimentos(admin.ModelAdmin):
    list_display =  ('id', 'nome_estabelecimento', 'categoria_estabelecimento')
    list_display_links =  ('nome_estabelecimento', 'categoria_estabelecimento')
    search_fields =  ('id', 'nome_estabelecimento', 'categoria_estabelecimento')
    list_per_page = 20

admin.site.register(Estabelecimento, Estabelecimentos)

class FormasPagamento(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    search_fields = ('id',)
    list_per_page = 20

admin.site.register(FormaPagamento, FormasPagamento)

class Usuarios(admin.ModelAdmin):
    list_display =  ('id', 'nome_usuario')
    list_display_links =  ('id', 'nome_usuario')
    search_fields = ('id', 'nome_usuario')
    list_per_page = 20

admin.site.register(Usuario, Usuarios)
