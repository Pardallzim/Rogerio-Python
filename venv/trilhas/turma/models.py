from datetime import datetime
from django.db import models

# Create your models here.

class Pessoa(models.Model):
    idpessoa = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    data_nasc = models.DateField()
    solteiro = models.BooleanField()
    salario = models.DecimalField(max_digits=10, decimal_places=2) 

