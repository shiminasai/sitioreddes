from django.shortcuts import render, get_object_or_404
from .models import Publicaciones
from taggit.managers import TaggableManager
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def filtro_publicaciones(request,categoria,template='noticias/noticias_list.html'):
    #tag_object = get_object_or_404(Tag, name=categoria)
    #object_list = TaggedItem.objects.get_by_model(Publicacion(), tag_object)
    object_list = Publicaciones.objects.filter(categoria=categoria)
    return render(request, template, {'object_list':object_list})
