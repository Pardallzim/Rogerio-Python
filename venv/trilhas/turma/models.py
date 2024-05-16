from datetime import datetime
from django.db import models

# Create your models here.

class Pessoa(models.Model):
    idpessoa = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    data_nasc = models.DateField()
    solteiro = models.BooleanField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    path = models.ImageField(upload_to = 'imagens/')

class Usuarios(models.Model):
    nome = models.CharField(max_length=180)
    email = models.EmailField()

class Pedido(models.Model):
    numero = models.IntegerField()

class Itens(models.Model):
    nome = models.CharField(max_length=240)
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    path = models.ImageField(upload_to = 'imagens/')


