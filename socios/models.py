# -*- coding: utf-8 -*-

from django.db import models
from geoposition.fields import GeopositionField
from django.contrib.contenttypes import generic
from multimedia.models import Fotos
from django.template.defaultfilters import slugify

# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length=200)
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = u'Paises'

class Socios(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.ForeignKey(Pais)
    position = GeopositionField(null=True, blank=True)
    contacto = models.CharField(max_length=250)
    telefono = models.CharField(max_length=50)
    logo = generic.GenericRelation(Fotos)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Socios'