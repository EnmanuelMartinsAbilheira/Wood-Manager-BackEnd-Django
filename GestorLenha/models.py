from django.db import models
from django.conf import settings
# Create your models here.

class Encomenda(models.Model):
               data_entrega = models.DateTimeField('Data de Entrega')
               quantidade = models.IntegerField()
               cliente = models.ForeignKey(
                              settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE
               )
               preco = models.FloatField()
               morada_entrega = models.CharField(max_length=200)
               estado = models.CharField(max_length=200)

class Config(models.Model):
               preco_tonelada = models.FloatField()

