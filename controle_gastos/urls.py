from django.contrib import admin
from django.urls import path, include
from controle_gastos_app.views import CategoriaViewset, EstabelecimentoViewset, GastoViewset, PagamentoViewset, UsuarioViewset, ListaEstabelecimentosCategoria
from rest_framework import routers

# rota principal
router = routers.DefaultRouter()
# rotas registradas para acesso específico
router.register('gastos', GastoViewset, basename='gastos')
router.register('estabelecimentos', EstabelecimentoViewset, basename='estabelecimentos')
router.register('categorias', CategoriaViewset, basename='categorias')
router.register('usuarios', UsuarioViewset, basename='usuarios')
router.register('pagamentos', PagamentoViewset, basename='pagamentos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('categorias/<int:pk>/estabelecimentos/', ListaEstabelecimentosCategoria.as_view())
]
