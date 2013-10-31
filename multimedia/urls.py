from django.conf.urls import patterns, url
from .views import FotosListView, AudioListView, VideosListView, AdjuntoListView
from .models import *

urlpatterns = patterns('',
        url(r'^audios/$',  AudioListView.as_view(), 
                                           name='audio_lista'),
        url(r'^videos/$',  VideosListView.as_view(), 
                                           name='videos_lista'),
        url(r'^fotos/$',  FotosListView.as_view(), 
                                           name='fotos_lista'),
        url(r'^adjuntos/$',  AdjuntoListView.as_view(), 
                                           name='adjuntos_lista'),
    )