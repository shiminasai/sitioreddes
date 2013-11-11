# -*- coding: utf-8 -*-

from django.utils.feedgenerator import Atom1Feed
from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from .models import Noticias
from eventos.models import Categoria
from datetime import datetime, time

current_site = Site.objects.get_current()

class NoticiasFeed(Feed):
    title = "%s: Ultimas noticias" % current_site.name
    link = "http://red-des.org/"
    author_name = "RED-DES CentroAmerica"
    description = "Ultimas noticias %s" % current_site.name
    feed_type = Atom1Feed
    
    #description_template = 'feeds/entry_description.html'
    #title_template = 'feeds/entry_title.html'
    #
    def items(self):
        return Noticias.objects.order_by('-fecha')[:8]

    def item_link(self, item): 
        return reverse("noticias_detalle", args=[item.slug])

    def item_title(self, item):
        return item.titulo

    def item_description(self, item):
        return item.descripcion
    
    def item_pubdate(self, item):
        return datetime.combine(item.fecha, time())
    
class CategoriaFeed(NoticiasFeed):
    def description(self, obj):
        return "%s: Latest entries in category '%s'" % (current_site.name, obj.nombre)
    
    def get_object(self, request, slug):
        return Categoria.objects.get(slug=slug)
    
    #def items(self, obj):
    #    return obj.objects.all()[:6]
    
    #def link(self, obj):
    #    return obj.get_absolute_url()
    
    def title(self, obj):
        return "%s: Ultimas entradas por categoria '%s'" % (current_site.name, obj.nombre)