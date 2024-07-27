from django.db import models

# Create your models here.

class Estacionamento(models.Model):
    nomeCliente = models.CharField(max_length=150, null=False, blank=False)
    nomeCarro = models.CharField(max_length=150, null=False, blank=False)
    placa = models.CharField(max_length=150, null=False, blank=False)
    dataEntrada = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    dataSaida = models.DateTimeField(null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True)
