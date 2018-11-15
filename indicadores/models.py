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
    email = models.EmailField()
    cnpj = models.IntegerField()
    telefone = models.IntegerField()
    codigo = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.nome

    def gerar_codigo(self):
        self.condigo = 'EMP'+rand_slug(3)
        
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    email = models.EmailField()
    funcao = models.CharField(max_length=500, choices=FUNCAO_TUPLE)

class Empreendimento(models.Model):
    nome = models.CharField(max_length=500)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

class Referencia(models.Model):
    texto = models.CharField(max_length=500)

class TipoIndicador(models.Model):
    titulo = models.CharField(max_length=500)
    modelo = models.CharField(max_length=500, choices=TIPOS_INDICADOR)

class Indicador(models.Model):
    tipo = models.ForeignKey(TipoIndicador, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=500)
    descricao = models.TextField()
    unidade_de_medida = models.CharField(max_length=500)

class Resultado(models.Model):
    empreendimento = models.ForeignKey(Empreendimento, on_delete=models.CASCADE)
    referencia = models.ForeignKey(Referencia, on_delete=models.CASCADE)
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE)
    conferido_por = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor = models.FloatField()



    







