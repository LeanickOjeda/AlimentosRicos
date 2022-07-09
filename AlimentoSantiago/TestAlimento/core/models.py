from django.db import models


# Create your models here.
class MenuSemana(models.Model):
    nrocatalogo = models.CharField(max_length=6, primary_key=True, verbose_name='Nro catalogo')
    dia = models.CharField(max_length=25, verbose_name='dia')
    platofondo = models.CharField(max_length=25, null=True, blank=True, verbose_name='Plato Fondo')
    Ensalada = models.CharField(max_length=25, null=True, blank=True, verbose_name='Ensalada')
    Postre = models.CharField(max_length=25, null=True, blank=True, verbose_name='Postre')