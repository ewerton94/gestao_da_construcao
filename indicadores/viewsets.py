from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Cliente, User, Empresa, Empreendimento, Referencia, TipoIndicador, Indicador, Resultado, Pesquisador, ResultadoCalculado, TCPO
from .serializers import ClienteSerializer, UserSerializer, EmpresaSerializer, EmpreendimentoSerializer, ReferenciaSerializer, TipoIndicadorSerializer, IndicadorSerializer, ResultadoSerializer, PesquisadorSerializer, ResultadoCalculadoSerializer
from rest_framework.permissions import AllowAny
import pandas as pd
import numpy as np
from rest_framework import status
from construction_manager.permissions import CustomPermission
from url_filter.filtersets import ModelFilterSet
from url_filter.integrations.drf import DjangoFilterBackend


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = (CustomPermission,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EmpreendimentoViewSet(viewsets.ModelViewSet):
    queryset = Empreendimento.objects.all()
    serializer_class = EmpreendimentoSerializer
    permission_classes = (CustomPermission,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('empresa', )

    def get_queryset(self):
        r = super(EmpreendimentoViewSet, self).get_queryset()
        if not self.request.user.is_staff:
            r = r.filter(empresa=self.request.user.cliente.empresa)
        return r

    

class ReferenciaViewSet(viewsets.ModelViewSet):
    queryset = Referencia.objects.filter(situacao=True)
    serializer_class = ReferenciaSerializer
    permission_classes = (CustomPermission,)

class TipoIndicadorViewSet(viewsets.ModelViewSet):
    queryset = TipoIndicador.objects.all()
    serializer_class = TipoIndicadorSerializer
    permission_classes = (CustomPermission,)

class IndicadorViewSet(viewsets.ModelViewSet):
    queryset = Indicador.objects.all()
    serializer_class = IndicadorSerializer
    permission_classes = (CustomPermission,)


class ResultadoCalculadoFilter(ModelFilterSet):
    class Meta(object):
        model = ResultadoCalculado
        fields = ('referencia', 'empreendimento')
        


class ResultadoViewSet(viewsets.ModelViewSet):
    queryset = ResultadoCalculado.objects.select_related().all()
    serializer_class = ResultadoCalculadoSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('referencia', 'empreendimento')
    permission_classes = (CustomPermission,)

    def get_queryset(self):
        qs = super(ResultadoViewSet, self).get_queryset()
        return ResultadoCalculadoFilter(data=self.request.GET, queryset=qs).filter()

    @action(detail=False)
    def por_empresa(self, request):
        if request.user.is_staff:
            queryset = self.get_queryset()
        else:
            cliente = Cliente.objects.filter(user=request.user)
            if cliente:
                empresa = cliente.first().empresa
                queryset = self.get_queryset().filter(empreendimento__empresa=empresa)
            else:
                return Response('Não permitido', status=status.HTTP_400_BAD_REQUEST)
        resultado = []
        DIC_REFERENCIA = {r.texto: r.id for r in Referencia.objects.all()}
        DIC_TCPO = {(t.referencia_id, t.indicador_id): t.valor for t in TCPO.objects.filter()}
        
        for nome, id, ordem in queryset.values_list('indicador__titulo', 'indicador_id', 'indicador__ordem').distinct():
            cols = ['empreendimento__nome', 'referencia_id', 'referencia__ordem', 'referencia__texto', 'valor']
            lista = queryset.filter(indicador_id=id).values_list(*cols)
            calculados = pd.DataFrame(lista, columns=cols)
            calculados = calculados.sort_values(by=['referencia__ordem', 'referencia_id'])
            print(str(calculados))
            calculados['TCPO'] = calculados['referencia_id'].apply(lambda x: DIC_TCPO.get((int(x), int(id)), ''))
            calculados = calculados.sort_values(by=['referencia__ordem', 'referencia_id'])
            print(calculados)
            del calculados['referencia__ordem']
            calculados = calculados.groupby('empreendimento__nome')
            dados = list(zip(calculados['TCPO'].apply(list).values, calculados['valor'].apply(list).values, calculados['referencia__texto'].apply(list).values))
            #for i, e in enumerate(dados):

                
            emps = calculados.max().index
            dados = zip(emps, dados)
            

            
            #print(calculados)
            #print(calculados.mean())
            d = {
                'nome': nome,
                'ordem': ordem,
                'dados': [{
                    'empreendimento': empreendimento,
                    'legendas': d[2],
                    'valores': d[1],
                    'tcpo': d[0]
                    } for empreendimento, d in dados
                ],
                
            }
            resultado.append(d)
        return Response(sorted(resultado, key=lambda x: x['ordem']))

    

    @action(detail=False)
    def por_referencia(self, request):
        queryset = self.get_queryset() # pk will be the video name
        resultado = []
        DIC_TCPO = {(t.referencia_id, t.indicador_id): t.valor for t in TCPO.objects.filter()}
        for nome, id, ordem in queryset.values_list('indicador__titulo', 'indicador_id', 'indicador__ordem').distinct():
            cols = ['empreendimento__codigo', 'referencia_id', 'valor']
            lista = queryset.filter(indicador_id=id).values_list(*cols)
            calculados = pd.DataFrame(list(lista), columns=cols)
            calculados = calculados.sort_values(by='referencia_id')
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
