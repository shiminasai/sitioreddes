#encoding: utf-8

from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from multimedia.models import Fotos
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager
from multimedia.models import Adjuntos
from eventos.models import Categoria
from socios.models import Pais

# Create your models here.
class Noticias(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,editable=False)
    fecha = models.DateField()
    descripcion = RichTextField('Descripción')
    fotos = generic.GenericRelation(Fotos)
    categoria= models.ManyToManyField(Categoria, 
                                    null=True, blank=True)
    pais = models.ForeignKey(Pais)
    tags = TaggableManager()
    destacada = models.BooleanField()
    adjunto = generic.GenericRelation(Adjuntos)

    autor = models.ForeignKey(User)

    def save(self, *args, **kwargs):
        self.slug = (slugify(self.titulo))
        super(Noticias, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('noticias_detalle', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'
        ordering = ('-fecha',)

    def __unicode__(self):
        return u'%s' % self.titulo

class InicioTexto(models.Model):
    nombre = models.CharField(max_length=150)
    texto = RichTextField()

    def __unicode__(self):
        return u'%s' % str(self.nombre)