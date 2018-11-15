from rest_framework import serializers
from .models import Cliente, User, Empresa

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


