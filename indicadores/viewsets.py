from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Cliente, User, Empresa, Empreendimento, Referencia, TipoIndicador, Indicador, Resultado, Pesquisador, ResultadoCalculado
from .serializers import ClienteSerializer, UserSerializer, EmpresaSerializer, EmpreendimentoSerializer, ReferenciaSerializer, TipoIndicadorSerializer, IndicadorSerializer, ResultadoSerializer, PesquisadorSerializer, ResultadoCalculadoSerializer
from rest_framework.permissions import AllowAny
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
from url_filter.filtersets import ModelFilterSet
from url_filter.integrations.drf import DjangoFilterBackend

class ResultadoCalculadoFilter(ModelFilterSet):
    class Meta(object):
        model = ResultadoCalculado
        fields = ('referencia', 'empreendimento')


class ResultadoViewSet(viewsets.ModelViewSet):
    queryset = ResultadoCalculado.objects.select_related().all()
    serializer_class = ResultadoCalculadoSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('referencia', 'empreendimento')
    permission_classes = (AllowAny,)

    def get_queryset(self):
        qs = super(ResultadoViewSet, self).get_queryset()
        return ResultadoCalculadoFilter(data=self.request.GET, queryset=qs).filter()

    @action(detail=True)
    def por_empresa(self, request, pk=None):
        queryset = self.get_queryset().filter(empreendimento__empresa_id=pk) # pk will be the video name
        resultado = []
        for nome, id in queryset.values_list('empreendimento__nome', 'empreendimento_id').distinct():
            lista = queryset.filter(empreendimento_id=id).values_list('referencia__texto', 'valor')
            d = {
                'nome': nome,
                'legendas': [ref for ref, val in lista],
                'valores': [val for ref, val in lista],
            }
            resultado.append(d)
        return Response(resultado)

    

    @action(detail=False)
    def por_referencia(self, request):
        queryset = self.get_queryset() # pk will be the video name
        resultado = []
        for nome, id in queryset.values_list('indicador__titulo', 'indicador_id').distinct():
            lista = queryset.filter(indicador_id=id).values_list('empreendimento__codigo', 'valor')
            d = {
                'nome': nome,
                'legendas': [ref for ref, val in lista],
                'valores': [val for ref, val in lista],
            }
            resultado.append(d)
        return Response(resultado)

    

class PesquisadorViewSet(viewsets.ModelViewSet):
    queryset = Pesquisador.objects.all()
    serializer_class = PesquisadorSerializer
