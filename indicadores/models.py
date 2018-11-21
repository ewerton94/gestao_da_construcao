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
    codigo = models.SlugField(null=True, unique=True, blank=True)

    def __str__(self):
        return self.nome

    def gerar_codigo(self):
        self.condigo = 'EMP'+rand_slug(3)

class Pesquisador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    email = models.EmailField()
    
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cliente")
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="clientes")
    email = models.EmailField()
    funcao = models.CharField(max_length=500, choices=FUNCAO_TUPLE)

    def is_supervisor(self):
        return self.funcao == 'supervisor'
        
    def is_tecnico(self):
        return self.funcao == 'tecnico'

class Empreendimento(models.Model):
    nome = models.CharField(max_length=500)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="empreendimentos")

class Referencia(models.Model):
    texto = models.CharField(max_length=500)

class TipoIndicador(models.Model):
    titulo = models.CharField(max_length=500)
    modelo = models.CharField(max_length=500, choices=TIPOS_INDICADOR)

    def __str__(self):
        return self.titulo

class Indicador(models.Model):
    tipo = models.ForeignKey(TipoIndicador, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=500)
    descricao = models.TextField()
    campo1 = models.CharField(max_length=500)
    campo2 = models.CharField(max_length=500)

    def __str__(self):
        return self.titulo + ' (' + self.unidade_de_medida + ')'

class Resultado(models.Model):
    empreendimento = models.ForeignKey(Empreendimento, on_delete=models.CASCADE)
    referencia = models.ForeignKey(Referencia, on_delete=models.CASCADE)
    indicador = models.ForeignKey(Indicador, on_delete=models.CASCADE)
    conferido_por = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor_campo_1 = models.FloatField()
    valor_campo_2 = models.FloatField()



    







