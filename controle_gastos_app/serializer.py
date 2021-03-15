from rest_framework import serializers
from controle_gastos_app.models import Categoria, Estabelecimento, Gasto, FormaPagamento , Usuario

class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class EstabelecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estabelecimento
        fields = '__all__'

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaPagamento
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

# mostra a lista de todos os estabelecimentos de acordo com a categoria
class ListaEstabelecimentosCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estabelecimento
        fields = ['nome_estabelecimento']
