from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response

from .forms import ClienteForm, UserForm, EmpresaForm, EmpreendimentoForm, ReferenciaForm, TipoIndicadorForm, PesquisadorForm, IndicadorForm, ResultadoForm
from .schemas import get_schema
from .exceptions import *
from .serializers import ClienteSerializer, UserSerializer, EmpresaSerializer, EmpreendimentoSerializer, ReferenciaSerializer, TipoIndicadorSerializer, IndicadorSerializer, ResultadoSerializer, PesquisadorSerializer
from .models import Cliente, User, Empresa, Empreendimento, Referencia, TipoIndicador, Pesquisador, Indicador, Resultado

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

@api_view(['GET','POST'])
def editar_empreendimento(request, id):
    return generic_update_view(request, Empreendimento, EmpreendimentoSerializer, EmpreendimentoForm, id)

#CLIENTE

@api_view(['GET','POST'])
def criar_cliente(request):
    return generic_create_view(request, Cliente, ClienteSerializer, ClienteForm)

@api_view(['GET','POST'])
def editar_cliente(request, id):
    return generic_update_view(request, Cliente, ClienteSerializer, ClienteForm, id)

#USER

@api_view(['GET','POST'])
def criar_user(request):
    return generic_create_view(request, User, UserSerializer, UserForm)

@api_view(['GET','POST'])
def editar_user(request, id):
    return generic_update_view(request, User, UserSerializer, UserForm, id)

#REFERENCIA

@api_view(['GET','POST'])
def criar_referencia(request):
    return generic_create_view(request, Referencia, ReferenciaSerializer, ReferenciaForm)

@api_view(['GET','POST'])
def editar_referencia(request, id):
    return generic_update_view(request, Referencia, ReferenciaSerializer, ReferenciaForm, id)

#INDICADOR

@api_view(['GET','POST'])
def criar_indicador(request):
    return generic_create_view(request, Indicador, IndicadorSerializer, IndicadorForm)

@api_view(['GET','POST'])
def editar_indicador(request, id):
    return generic_update_view(request, Indicador, IndicadorSerializer, IndicadorForm, id)

#TIPOINDICADOR

@api_view(['GET','POST'])
def criar_tipoindicador(request):
    return generic_create_view(request, TipoIndicador, TipoIndicadorSerializer, TipoIndicadorForm)

@api_view(['GET','POST'])
def editar_tipoindicador(request, id):
    return generic_update_view(request, TipoIndicador, TipoIndicadorSerializer, TipoIndicadorForm, id)

#RESULTADO

@api_view(['GET','POST'])
def criar_resultado(request):
    return generic_create_view(request, Resultado, ResultadoSerializer, ResultadoForm)

@api_view(['GET','POST'])
def editar_resultado(request, id):
    return generic_update_view(request, Resultado, ResultadoSerializer, ResultadoForm, id)

#PESQUISADOR

@api_view(['GET','POST'])
def criar_pesquisador(request):
    return generic_create_view(request, Pesquisador, PesquisadorSerializer, PesquisadorForm)

@api_view(['GET','POST'])
def editar_pesquisador(request, id):
    return generic_update_view(request, Pesquisador, PesquisadorSerializer, PesquisadorForm, id)
















# Ewerton Escreve aqui em baixo:


