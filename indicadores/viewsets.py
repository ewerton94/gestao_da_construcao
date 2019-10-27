from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Cliente, User, Empresa, Empreendimento, Referencia, TipoIndicador, Indicador, Resultado, Pesquisador, ResultadoCalculado, TCPO
from .serializers import ClienteSerializer, UserSerializer, EmpresaSerializer, EmpreendimentoSerializer, ReferenciaSerializer, TipoIndicadorSerializer, IndicadorSerializer, ResultadoSerializer, PesquisadorSerializer, ResultadoCalculadoSerializer
from rest_framework.permissions import AllowAny
import pandas as pd
import numpy as np

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
        print(queryset.values_list('empreendimento__nome', 'empreendimento_id', 'indicador__ordem').distinct())
        for nome, id, ordem in queryset.values_list('empreendimento__nome', 'empreendimento_id').distinct():
            lista = queryset.filter(empreendimento_id=id).values_list('referencia__texto', 'valor')
            d = {
                'nome': nome,
                'ordem': ordem,
                'legendas': [ref for ref, val in lista],
                'valores': [val for ref, val in lista],
            }
            resultado.append(d)
        print(sorted(resultado, key=lambda x: x['ordem']))
        return Response(sorted(resultado, key=lambda x: x.ordem))

    

    @action(detail=False)
    def por_referencia(self, request):
        queryset = self.get_queryset() # pk will be the video name
        resultado = []
        for nome, id, ordem in queryset.values_list('indicador__titulo', 'indicador_id', 'indicador__ordem').distinct():
            cols = ['empreendimento__codigo', 'referencia_id', 'valor']
            lista = queryset.filter(indicador_id=id).values_list(*cols)
            calculados = pd.DataFrame(list(lista), columns=cols)
            DIC_TCPO = {(t.referencia_id, t.indicador_id): t.valor for t in TCPO.objects.filter()}
            print()
            calculados['TCPO'] = calculados['referencia_id'].apply(lambda x: DIC_TCPO.get((int(x), int(id)), np.nan))
            calculados = calculados.groupby('empreendimento__codigo').mean()
            calculados = calculados.fillna('')
            #print(calculados)
            #print(calculados.mean())
            legendas = calculados.index
            d = {
                'nome': nome,
                'ordem': ordem,
                'legendas': legendas,
                'valores': calculados.valor.values,
                'tcpo': calculados.TCPO.values
            }
            resultado.append(d)
        #print('\n\n\n\n\n\n---------')
        #print(sorted(resultado, key=lambda x: x['ordem']))
        return Response(sorted(resultado, key=lambda x: x['ordem']))

    

class PesquisadorViewSet(viewsets.ModelViewSet):
    queryset = Pesquisador.objects.all()
    serializer_class = PesquisadorSerializer
