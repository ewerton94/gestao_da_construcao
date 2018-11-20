from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response

from .forms import EmpresaForm
from .schemas import get_schema
from .exceptions import *
from .serializers import EmpresaSerializer
from .models import Empresa 

def generic_create_view(request, Model, Serializer, Form):
    if request.method == 'POST':
        serializer = Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
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

@api_view(['GET','POST'])
def form_empresas(request):
    return generic_create_view(request, Empresa, EmpresaSerializer, EmpresaForm)

@api_view(['GET','POST'])
def form_editar_empresas(request, id):
    return generic_update_view(request, Empresa, EmpresaSerializer, EmpresaForm, id)


        
