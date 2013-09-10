from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from .models import Audio, Videos

urlpatterns = patterns('',
        url(r'^audio/$',  ListView.as_view(model=Audio,
                                           queryset=Audio.objects.all(),
                                           paginate_by=5), 
                                           name='audio_lista'),

        url(r'^audio/(?P<slug>[-_\w]+)/$', DetailView.as_view(model=Audio,
                                                        queryset=Audio.objects.all(),
                                                        ), 
                                                        name='audio_detalles'),
        url(r'^videos/$',  ListView.as_view(model=Videos,
                                           queryset=Videos.objects.all(),
                                           paginate_by=5), 
                                           name='videos_lista'),

        url(r'^videos/(?P<slug>[-_\w]+)/$', DetailView.as_view(model=Videos,
                                                        queryset=Videos.objects.all(),
                                                        ), 
                                                        name='videos_detalles'),
    )