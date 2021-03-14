from rest_framework import viewsets
from controle_gastos_app.models import Categoria, Estabelecimento, Gasto, Usuario
from controle_gastos_app.serializer import CategoriaSerializer, EstabelecimentoSerializer, GastoSerializer, UsuarioSerializer

class GastosViewset(viewsets.ModelViewSet):
    """Exibindo todos os gastos cadastrados"""
    # trazendo todos os alunos do banco de dados
    queryset = Gasto.objects.all
    # classe responsável por serializar os dados
    serializer_class = GastoSerializer

class CategoriaViewset(viewsets.ModelViewSet):
    """Exibindo todas as categorias cadastrados"""
    queryset = Categoria.objects.all
    serializer_class = CategoriaSerializer

class EstabelecimentoViewset(viewsets.ModelViewSet):
    """Exibindo todos os estabelecimentos cadastrados"""
    queryset = Estabelecimento.objects.all
    serializer_class = EstabelecimentoSerializer

class UsuarioViewset(viewsets.ModelViewSet):
    """Exibindo todos os usuários cadastrados"""
    queryset = Usuario.objects.all
    serializer_class = UsuarioSerializer
