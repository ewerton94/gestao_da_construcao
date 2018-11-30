# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.exceptions import APIException

class EmailExistente(APIException):
    status_code = 503
    default_detail = 'Email já cadastrado no sistema.'
    default_code = 'email_cadastrado'

class MethodNotAllowed(APIException):
    status_code = 405
    default_detail = 'Requisição HTTP não permitida'
    default_code = 'disciplina_existente'

class FormularioInvalido(APIException):
    status_code = 400
    default_detail = 'Formulário inválido'
    default_code = 'formulario_invalido'

class HorariosCoincidentes(APIException):
    status_code = 503
    default_detail = 'Verifique os horários da oferta acadêmica! Você está tentando se matricular em disciplinas cujos horários coincidem.'
    default_code = 'horarios_coincidentes'

class UsuarioDeslogado(APIException):
    status_code = 401
    default_detail = 'Você não está conectado, entre no sistema para continuar.'
    default_code = 'usuario_deslogado'

class EmailInexistente(APIException):
    status_code = 401
    default_detail = 'E-mail não cadastrado no sistema.'
    default_code = 'email_invalido'

class SenhaInvalida(APIException):
    status_code = 401
    default_detail = 'Senha inválida!'
    default_code = 'email_invalido'

class ForaDePeriodo(APIException):
    status_code = 401
    default_detail = 'Por favor, siga o calendário acadêmico! Não é possível fazer matrícula ou reajuste neste momento.'
    default_code = 'fora_de_periodo'

class UsuarioNaoEncontrado(APIException):
    status_code = 403
    default_detail = 'Usuário não encontrado no sistema.'
    default_code = 'usuario_nao_encontrado'

class UsuarioEncontrado(APIException):
    status_code = 403
    default_detail = 'Usuário já logado no sistema.'
    default_code = 'usuario_ja_encontrado'
