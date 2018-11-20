from rest_framework import serializers
from .models import Cliente, User, Empresa, Empreendimento, Referencia, TipoIndicador, Indicador, Resultado

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Cliente
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = User
        fields = '__all__'

class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Empresa
        fields = '__all__'

class EmpreendimentoSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Empreendimento
        fields = '__all__'

class ReferenciaSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Referencia
        fields = '__all__'

class TipoIndicadorSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = TipoIndicador
        fields = '__all__'

class IndicadorSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Indicador
        fields = '__all__'

class ResultadoSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Resultado
        fields = '__all__'
