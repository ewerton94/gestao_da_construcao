from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate, login as auth_login

from .forms import ClienteForm, UserForm, EmpresaForm, EmpreendimentoForm, ReferenciaForm, TipoIndicadorForm, PesquisadorForm, IndicadorForm, ResultadoForm
from .schemas import get_schema
from .exceptions import *
from .serializers import ClienteSerializer, UserSerializer, EmpresaSerializer, EmpreendimentoSerializer, ReferenciaSerializer, TipoIndicadorSerializer, IndicadorSerializer, ResultadoSerializer, PesquisadorSerializer
from .models import Cliente, User, Empresa, Empreendimento, Referencia, TipoIndicador, Pesquisador, Indicador, Resultado, ResultadoCalculado
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


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
        raise MethodNotAllowed()


@csrf_exempt
@api_view(['GET'])
def obtem_usuario_logado(request):
    if request.method == 'GET':
        user = request.user
        permissions = user.get_all_permissions()
        view_permissions = [e.split('_')[1] for e in permissions if 'view' in e]
        add_permissions = [e.split('_')[1] for e in permissions if 'add' in e]
        if user.is_authenticated:
            cliente = Cliente.objects.filter(user=user).first()
            pesquisador = Pesquisador.objects.filter(user=user).first()
            nome = ''
            if cliente:
                nome = cliente.nome
                cliente = cliente.id
            else:
                cliente = None
            if pesquisador:
                nome = pesquisador.nome
                pesquisador = pesquisador.id
            else:
                pesquisador = None
            
            return Response({'user': {'id': user.id, 'nome': nome, 'username': user.username, 'view_permissions':view_permissions, 'add_permissions':add_permissions}, 'cliente': cliente, 'pesquisador': pesquisador})
        raise UsuarioNaoEncontrado()
    raise MethodNotAllowed()


@api_view(['GET'])
@permission_classes((AllowAny,))
def atualizar_calculos(request):
    if request.method == 'GET':
        resultados_a_calcular = Resultado.objects.select_related().filter(calculado=False)
        empreendimentos = resultados_a_calcular.values_list('empreendimento_id', 'empreendimento_id').distinct()
        referencias = resultados_a_calcular.values_list('referencia_id', 'empreendimento_id').distinct()
        indicadores = resultados_a_calcular.values_list('indicador_id', 'empreendimento_id').distinct()
        resultados_calculados = []
        for empreendimento, _ in empreendimentos:
            r_e = resultados_a_calcular.filter(empreendimento_id=empreendimento)
            for referencia, _ in referencias:
                r_r = r_e.filter(referencia_id=referencia)
                for indicador, _ in indicadores:
                    r_i = r_r.filter(indicador_id=indicador)
                    if r_i:
                        formula = r_i[0].indicador.unit
                        #print('Formula inicial: ', formula)
                        for k, v in r_i.values_list('campo_indicador__nome_variavel', 'valor'):
                            if k:
                                #print(k, v)
                                formula = formula.replace(k, str(v))
                                #print(k, '=', str(v))
                        #print(formula)
                        valor = eval(formula)
                        #print(valor)
                        resultados_calculados.append(ResultadoCalculado(
                            empreendimento_id=empreendimento,
                            referencia_id=referencia,
                            indicador_id=indicador,
                            valor=valor
                        ))
        if resultados_calculados:
            ResultadoCalculado.objects.bulk_create(resultados_calculados)
            resultados_a_calcular.update(calculado=True)
            return Response('Cálculos Atualizados!')
        return Response('nenhum indicador a calcular!')
                        


    raise MethodNotAllowed()

@api_view(['GET'])
def obtem_usuario_deslogado(request):
    if request.method == 'GET':
        user = request.user
        if user.is_authenticated:
            raise UsuarioEncontrado()
        else:
            return Response('ok')
'''
@api_view(['POST'])
def login(request):
    username = request.data['username']
    password = request.data['password']
    print(username)
    try:
        usuario=User.objects.get(username=username)
    except:
        raise EmailInexistente()
    new_user = authenticate(username=username, password=password)
    if new_user is not None:
        auth_login(request, new_user)
        print(new_user)
        return Response("OK")
    else:
        raise SenhaInvalida()
'''
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=status.HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    print(token)
    return Response({'token': token.key},
status=status.HTTP_200_OK)
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
from .forms import ResultadoForm
from .models import Indicador, Cliente, Referencia, Empreendimento, Resultado

@api_view(['POST'])
def criar_codigos(request):
    data = request.data
    if data['gerar'] == 'ok':
        print('entrou certo')
        for emp in Empreendimento.objects.all():
            try:
                emp.gerar_codigo()
                print(emp)
            except:
                emp.gerar_codigo(2)
        return Response({'message': "Códigos gerados com sucesso"})
    return Response({'message': "Variável gerar não definida!"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def form_indicadores(request):
    if request.method == 'POST':
        data = request.data
        fixo = ['conferido_por', 'referencia', 'empreendimento']
        #cliente = Cliente.objects.get(id=data['conferido_por'])
        #referencia = Referencia.objects.get(id=data['referencia'])
        #empreendimento = Empreendimento.objects.get(id=data['empreendimento'])
        indicadores = {}
        for key, value in data.items():
            key = key.split('-')
            if key[0].isdigit():
                indicadores.setdefault(int(key[0]), {})[key[-1]] = value
        for indicador_id, respostas in indicadores.items():
            r = {}
            for campo_indicador_id, resposta in respostas.items():
                Resultado.objects.create(
                    conferido_por_id=request.user.cliente.id,
                    referencia_id=data['referencia'],
                    empreendimento_id=data['empreendimento'],
                    indicador_id=indicador_id,
                    campo_indicador_id=campo_indicador_id,
                    valor=resposta
                )

        return Response('ok')




    if request.method == 'GET':
        forms_tipos = []
        form = ResultadoForm()
        schema = get_schema(form)
        fields = []
        for f in schema['schema']['fields']:
            f['styleClasses'] = 'px-1'

        schema['schema'] = {
                'groups':[
                    {
                        'legend': 'Dados de identificação da resposta',
                        'fields': schema['schema']['fields']
                    }
                ]
            }
        forms_tipos.append(schema)
        for tipo in TipoIndicador.objects.filter(modelo='mensal').prefetch_related('campos'):
            schema = {'titulo': tipo.titulo, 'schema': {'groups': []}}
            indicadores = tipo.indicadores.all()

          
            for indicador in indicadores:
                op = [
                    {'label': campo_indicador.campo, 'inputType': campo_indicador.type_value , 'model': str(indicador.id)+'-valor_campo-'+ str(campo_indicador.id) } for campo_indicador in indicador.tipo.campos.all() 
                ]
                schema['schema']['groups'].append(
                    {
                        'legend': indicador.titulo,
                        'styleClasses':'row',
                        'tag': 'div',
                        'fields': [
                            {

                                    'type': "input",
                                    'inputType': e['inputType'],
                                    'id': e['model'],
                                    'label': e['label'],
                                    'model': e['model'],
                                    'styleClasses':'col-md-4 col-12 mx-1',
                                    'tag': 'div',



                            } for e in op
                        ]
                    }
                )
            forms_tipos.append(schema)


        return Response(forms_tipos)
    else:
        raise MethodNotAllowed
