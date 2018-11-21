from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response

from .forms import EmpresaForm, EmpreendimentoForm
from .schemas import get_schema
from .exceptions import *
from .serializers import EmpresaSerializer, EmpreendimentoSerializer
from .models import Empresa, Empreendimento

def generic_create_view(request, Model, Serializer, Form):
    if request.method == 'POST':
        serializer = Serializer(data=request.data)
        print(dir(serializer))
        print(request.data)
        print('foi')

        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        form = Form()  # or TestForm(data={'title':'My Title'})
        schema = get_schema(form)
        return Response(schema)
    else:
        raise MethodNotAllowed

def generic_update_view(request, Model, Serializer, Form, id):
    obj = Model.objects.get(id=id)
    if request.method == 'POST':
        serializer = Serializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        form = Form(instance=obj)  # or TestForm(data={'title':'My Title'})
        schema = get_schema(form)
        return Response(schema)
    else:
        raise MethodNotAllowed

#EMPRESAS

@api_view(['GET','POST'])
def form_empresas(request):
    return generic_create_view(request, Empresa, EmpresaSerializer, EmpresaForm)

@api_view(['GET','POST'])
def form_editar_empresas(request, id):
    return generic_update_view(request, Empresa, EmpresaSerializer, EmpresaForm, id)


#EMPREENDIMENTO

@api_view(['GET','POST'])
def criar_empreendimento(request):
    return generic_create_view(request, Empreendimento, EmpreendimentoSerializer, EmpreendimentoForm)

















# Ewerton Escreve aqui em baixo:
from .forms import ResultadoForm
from .models import Indicador, Cliente, Referencia, Empreendimento, Resultado
from .graphs import get_graph
@api_view(['GET','POST'])
def visualizar_resultados(request):
    a = str(get_graph())
    return Response({'grafico': a})


@api_view(['GET','POST'])
def form_indicadores(request):
    if request.method == 'POST':
        data = request.data
        fixo = ['conferido_por', 'referencia', 'empreendimento']
        cliente = Cliente.objects.get(id=data['conferido_por'])
        referencia = Referencia.objects.get(id=data['referencia'])
        empreendimento = Empreendimento.objects.get(id=data['empreendimento'])
        indicadores = {}
        for key, value in data.items():
            if key[0].isdigit():
                indicadores.setdefault(int(key[0]), {})[key[-1]] = value
        for id, respostas in indicadores.items():
            indicador = Indicador.objects.get(id=id)
            r = {}
            for i in range(1, 3):
                r[i] = respostas.get(str(i), 0)
                
            Resultado.objects.create(
                conferido_por=cliente,
                referencia=referencia,
                empreendimento=empreendimento,
                indicador=indicador,
                valor_campo_1=r[1],
                valor_campo_2=r[2]
            )

        return Response('ok')
            



    if request.method == 'GET':
        form = ResultadoForm()  
        schema = get_schema(form)
        indicadores = Indicador.objects.filter(tipo__modelo='mensal')
        
        schema['schema'] = {
            'groups':[
                {
                    'legend': 'Dados de identificação da resposta',
                    'fields': schema['schema']['fields']
                }
            ]
        }
        for indicador in indicadores:
            op = [
                {'label': indicador.campo1,'model': str(indicador.id)+'-valor_campo_1' },
                {'label': indicador.campo2,'model': str(indicador.id)+'-valor_campo_2' }
            ]
            schema['schema']['groups'].append(
                {
                    'legend': indicador.titulo,
                    'styleClasses':'row',
                    'tag': 'div',
                    'fields': [
                        {
                            
                                'type': "input",
                                'inputType': "number",
                                'id': e['model'],
                                'label': e['label'],
                                'model': e['model'],
                                'styleClasses':'col-md-6',
                                'tag': 'div',
                                
                            

                        } for e in op
                    ]
                }
            )


        return Response(schema)
    else:
        raise MethodNotAllowed



