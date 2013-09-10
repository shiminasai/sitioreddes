from django.conf.urls import patterns, url
from eventos.views import EventosList, EventosDetailView

urlpatterns = patterns('',
    url(r'^lista/$', view=EventosList.as_view(), 
                       name='evento_lista'),
    
    url(r'^(?P<slug>[-_\w]+)/$', view=EventosDetailView.as_view(), 
                                 name='eventos_detalle'),
    )