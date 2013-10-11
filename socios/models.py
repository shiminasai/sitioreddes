# -*- coding: utf-8 -*-

from django.db import models
from geoposition.fields import GeopositionField
from django.contrib.contenttypes import generic
from multimedia.models import Fotos
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from sitioreddes.utils import get_file_path

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
    nombre = models.CharField('Nombre organización',max_length=50)
    pais = models.ForeignKey(Pais)
    position = GeopositionField(null=True, blank=True)
    descripcion = models.TextField()
    contacto = models.CharField(max_length=250)
    telefono = models.CharField(max_length=50)
    logo = ImageField(upload_to=get_file_path, blank=True, null=True)
    autor = models.ForeignKey(User)
    pagina_web = models.URLField(blank=True, null=True)

    fileDir = 'logosocios/'

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return '/socios/%d/' % (self.id,)

    class Meta:
        verbose_name_plural = 'Socios'