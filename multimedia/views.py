from django.views.generic import ListView
from django.shortcuts import render
from .models import *

class FotosListView(ListView):
    template_name = 'multimedia/fotos_list.html'
    model = Fotos
    paginate_by = 4

class VideosListView(ListView):
    template_name = 'multimedia/videos_list.html'
    model = Videos
    paginate_by = 8

class AudioListView(ListView):
    template_name = 'multimedia/audio_list.html'
    model = Audio
    paginate_by = 8

class AdjuntoListView(ListView):
    template_name = 'multimedia/adjuntos_list.html'
    model = Adjuntos
    paginate_by = 8