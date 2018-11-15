from rest_framework import serializers
from .models import Cliente, User, Empresa, Empreendimento, Referencia, TipoIndicador, Indicador, Resultado

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class EmpreendimentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empreendimento
        fields = '__all__'

class ReferenciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Referencia
        fields = '__all__'

class TipoIndicadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoIndicador
        fields = '__all__'

class IndicadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Indicador
        fields = '__all__'

class ResultadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resultado
        fields = '__all__'
