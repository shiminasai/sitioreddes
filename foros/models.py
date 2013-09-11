# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
import datetime
from south.modelsinspector import add_introspection_rules
from ckeditor.fields import RichTextField
from multimedia.models import Audio, Fotos, Videos, Adjuntos

add_introspection_rules ([], ["^ckeditor\.fields\.RichTextField"])

class Foros(models.Model):
    nombre = models.CharField(max_length=200)
    creacion = models.DateField(default=datetime.datetime.now())
    apertura = models.DateField('Apertura y recepción de aportes')
    cierre = models.DateField('Cierre de aportes')
    fecha_skype = models.DateField('Propuesta de reunión skype')
    memoria = models.DateField('Propuesta entrega de memoria')
    contenido = RichTextField()
    contraparte = models.ForeignKey(User)
    documentos = generic.GenericRelation(Adjuntos)
    fotos = generic.GenericRelation(Fotos)
    video = generic.GenericRelation(Videos)
    audio = generic.GenericRelation(Audio)

    class Meta:
    	verbose_name_plural = "Foros"
        ordering = ['-creacion']

    def __unicode__(self):
    	return self.nombre

    def get_absolute_url(self):
        return "/foros/ver/%d" % (self.id)

class Aportes(models.Model):
    foro = models.ForeignKey(Foros)
    fecha = models.DateField(default=datetime.datetime.now())
    contenido = RichTextField()
    user = models.ForeignKey(User)
    adjuntos = generic.GenericRelation(Adjuntos)
    fotos = generic.GenericRelation(Fotos)
    video = generic.GenericRelation(Videos)
    audio = generic.GenericRelation(Audio)

    class Meta:
        verbose_name_plural = "Aportes"

    def __unicode__(self):
        return self.foro.nombre

class Comentarios(models.Model):
    fecha = models.DateField(default=datetime.datetime.now())
    usuario = models.ForeignKey(User)
    comentario = RichTextField()
    aporte = models.ForeignKey(Aportes)

    class Meta:
        verbose_name_plural = "Comentarios"

    def __unicode__(self):
        return self.usuario.username
