from rest_framework import viewsets
from .models import Cliente, User, Empresa, Empreendimento, Referencia, TipoIndicador, Indicador, Resultado, Pesquisador
from .serializers import ClienteSerializer, UserSerializer, EmpresaSerializer, EmpreendimentoSerializer, ReferenciaSerializer, TipoIndicadorSerializer, IndicadorSerializer, ResultadoSerializer, PesquisadorSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EmpreendimentoViewSet(viewsets.ModelViewSet):
    queryset = Empreendimento.objects.all()
    serializer_class = EmpreendimentoSerializer

class ReferenciaViewSet(viewsets.ModelViewSet):
    queryset = Referencia.objects.all()
    serializer_class = ReferenciaSerializer

class TipoIndicadorViewSet(viewsets.ModelViewSet):
    queryset = TipoIndicador.objects.all()
    serializer_class = TipoIndicadorSerializer

class IndicadorViewSet(viewsets.ModelViewSet):
    queryset = Indicador.objects.all()
    serializer_class = IndicadorSerializer

class ResultadoViewSet(viewsets.ModelViewSet):
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer

class PesquisadorViewSet(viewsets.ModelViewSet):
    queryset = Pesquisador.objects.all()
    serializer_class = PesquisadorSerializer
