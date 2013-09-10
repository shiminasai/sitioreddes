#encoding: utf-8

from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from multimedia.models import Fotos
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager
from geoposition.fields import GeopositionField
from multimedia.models import Adjuntos

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    slug = models.SlugField()

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Categorias"

class Eventos(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,editable=False)
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    descripcion = RichTextField('Descripción')
    position = GeopositionField(null=True, blank=True)
    fotos = generic.GenericRelation(Fotos)
    categoria= models.ForeignKey(Categoria,null=True, blank=True)
    tags = TaggableManager()
    adjunto = generic.GenericRelation(Adjuntos)

    autor = models.ForeignKey(User)

    def save(self, *args, **kwargs):
        self.slug = (slugify(self.titulo))
        super(Eventos, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('eventos_detalle', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.titulo
