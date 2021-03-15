from rest_framework import viewsets, generics
from controle_gastos_app.models import Categoria, Estabelecimento, FormaPagamento, Gasto, Usuario
from controle_gastos_app.serializer import CategoriaSerializer, EstabelecimentoSerializer, GastoSerializer,PagamentoSerializer, UsuarioSerializer, ListaEstabelecimentosCategoriaSerializer

class CategoriaViewset(viewsets.ModelViewSet):
    """Exibindo todas as categorias cadastradas"""
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class EstabelecimentoViewset(viewsets.ModelViewSet):
    """Exibindo todos os estabelecimentos cadastrados"""
    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer

class GastoViewset(viewsets.ModelViewSet):
    """Exibindo todos os gastos cadastrados"""
    # trazendo todos os gastos do banco de dados
    queryset = Gasto.objects.all()
    # classe responsável por serializar os dados
    serializer_class = GastoSerializer

class PagamentoViewset(viewsets.ModelViewSet):
    """Exibindo todas as formas de pagamento disponíveis"""
    queryset = FormaPagamento.objects.all()
    serializer_class = PagamentoSerializer

class UsuarioViewset(viewsets.ModelViewSet):
    """Exibindo todos os usuários cadastrados"""
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ListaEstabelecimentosCategoria(generics.ListAPIView):
    """Listando os estabelecimentos de uma categoria"""
    # filtrando os estabelecimentos pelo id da categoria
    def get_queryset(self):
        queryset = Estabelecimento.objects.filter(categoria_estabelecimento_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaEstabelecimentosCategoriaSerializer
