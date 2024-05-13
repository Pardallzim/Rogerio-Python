from django.db import models
from datetime import datetime

# Create your models here.
class Pessoas(models.Model):
    nome = models.CharField(max_length=200)
    cpf =  models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    date_create = models.DateTimeField(default=datetime.now, blank =True)
    casado = models.BooleanField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    path = models.ImageField(upload_to = 'imagens/')