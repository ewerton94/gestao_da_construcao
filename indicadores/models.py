from django.db import models
from django.contrib.auth.models import User
import random
import string

def rand_slug(n):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(n))

FUNCAO_TUPLE = (
    ('tecnico', 'Técnico'),
    ('supervisor', 'Supervisor')
)

TIPOS_INDICADOR = (
    ('fixo', 'Fixo'),
    ('mensal', 'Mensal')
)

class Empresa(models.Model):
    nome = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    cnpj = models.IntegerField()
    telefone = models.IntegerField()

    def __str__(self):
        return self.nome


class Pesquisador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    email = models.EmailField()
    nome = models.CharField(max_length=500)

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cliente")
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="clientes")
    email = models.EmailField()
    nome = models.CharField(max_length=500)
    funcao = models.CharField(max_length=500, choices=FUNCAO_TUPLE)

    def is_supervisor(self):
        return self.funcao == 'supervisor'

    def is_tecnico(self):
        return self.funcao == 'tecnico'

    def __str__(self):
        return self.email

class Empreendimento(models.Model):
    nome = models.CharField(max_length=500)
    endereco = models.TextField(default='')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="empreendimentos")
    codigo = models.CharField(max_length=10, null=True, unique=True, blank=True)

    def __str__(self):
        return self.nome

    def gerar_codigo(self, n=3):
        c = str(rand_slug(n))
        self.codigo = c
        self.save()

class Referencia(models.Model):
    class Meta:
        ordering = ['ordem', 'id']
    texto = models.CharField(max_length=500)
    situacao = models.BooleanField(default=True)
    ordem = models.IntegerField(default=0)
    def __str__(self):
        return self.texto

TYPES_OF_VALUE = (
    ('number', 'Aberta (Número inteiro)'),
    ('number', 'Aberta (Número decimal)'),
    ('text', 'Aberta (Texto)'),
    ('select', 'Múltipla escolha'),
)


class CampoIndicador(models.Model):
    #indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE, related_name='campos')
    campo = models.CharField(max_length=500)
    type_value = models.CharField(max_length=500, choices=TYPES_OF_VALUE)
    nome_variavel = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.campo + ' ' + self.type_value

class TipoIndicador(models.Model):
    titulo = models.CharField(max_length=500)
    modelo = models.CharField(max_length=500, choices=TIPOS_INDICADOR)
    campos = models.ManyToManyField(CampoIndicador, blank=True)

    def __str__(self):
        return self.titulo

class Indicador(models.Model):
    class Meta:
        ordering = ['ordem', 'id']
    tipo = models.ForeignKey(TipoIndicador, on_delete=models.CASCADE, related_name='indicadores')
    titulo = models.CharField(max_length=500)
    descricao = models.TextField()
    unit = models.CharField(max_length=500, default='')
    ordem = models.IntegerField(default=0)
    def __str__(self):
        return self.titulo

class TCPO(models.Model):
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE, related_name='tcpos')
    referencia = models.ForeignKey(Referencia, on_delete=models.CASCADE)
    valor = models.FloatField()

class Resultado(models.Model):
    empreendimento = models.ForeignKey(Empreendimento, on_delete=models.CASCADE)
    referencia = models.ForeignKey(Referencia, on_delete=models.CASCADE)
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE)
    campo_indicador = models.ForeignKey(CampoIndicador, on_delete=models.CASCADE)
    conferido_por = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor = models.TextField(default='')
    error = models.BooleanField(default=False)
    calculado = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.valor is None:
            self.valor = '0'
        super(Resultado, self).save(*args, **kwargs)

class ResultadoCalculado(models.Model):
    empreendimento = models.ForeignKey(Empreendimento, on_delete=models.CASCADE)
    referencia = models.ForeignKey(Referencia, on_delete=models.CASCADE)
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE)
    valor = models.FloatField()
