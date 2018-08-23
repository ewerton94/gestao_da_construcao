from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    cnpj = models.IntegerField()
    telefone = models.IntegerField()

    def __str__(self):
        return self.nome

