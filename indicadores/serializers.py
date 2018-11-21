from rest_framework import serializers
from .models import Cliente, User, Empresa, Empreendimento, Referencia, TipoIndicador, Pesquisador, Indicador, Resultado

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
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Empresa
        fields = '__all__'

class EmpreendimentoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Empreendimento
        fields = '__all__'
    
    

class ReferenciaSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Referencia
        fields = '__all__'

class TipoIndicadorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = TipoIndicador
        fields = '__all__'

class IndicadorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Indicador
        fields = '__all__'

class ResultadoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Resultado
        fields = '__all__'

class PesquisadorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Pesquisador
        fields = '__all__'






# Ewerton Escreve aqui em baixo:
