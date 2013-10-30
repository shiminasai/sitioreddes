from django.views.generic import ListView
from django.shortcuts import render
from .models import *
from publicaciones.models import *

class FotosListView(ListView):
    template_name = 'multimedia/fotos_list.html'
    model = Fotos
    paginate_by = 6

class VideosListView(ListView):
    template_name = 'multimedia/videos_list.html'
    queryset= Videos.objects.order_by('-id')
    #model = Videos
    paginate_by = 6

class AudioListView(ListView):
    template_name = 'multimedia/audio_list.html'
    model = Audio
    paginate_by = 6

class AdjuntoListView(ListView):
    template_name = 'multimedia/adjuntos_list.html'
    model = Publicaciones
    paginate_by = 12