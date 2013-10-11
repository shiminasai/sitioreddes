#encoding: utf-8

from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from sitioreddes.utils import get_file_path
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager
from sorl.thumbnail import ImageField

# Create your models here.
class Publicaciones(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,editable=False)
    fecha = models.DateField('Fecha de publicación')
    descripcion = RichTextField('Descripción')
    adjunto = models.FileField(upload_to=get_file_path, null=True, blank=True)
    portada = ImageField(upload_to=get_file_path, blank=True, null=True)
    categoria= TaggableManager(blank=True)

    fileDir = 'publicaciones/'

    autor = models.ForeignKey(User)

    def save(self, *args, **kwargs):
        self.slug = (slugify(self.titulo))
        super(Publicaciones, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('publicaciones_detalles', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = u'Publicación'
        verbose_name_plural = u'Publicaciones'
        ordering = ('-id',)

    def __unicode__(self):
        return u'%s' % self.titulo