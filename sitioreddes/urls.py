from django.conf.urls import patterns, include, url
from settings import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'noticias.views.index', name='index'),
    url(r'^noticias/', include('noticias.urls')),
    url(r'^publicaciones/', include('publicaciones.urls')),
    url(r'^multimedias/', include('multimedia.urls')),
    url(r'^eventos/', include('eventos.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^search/', include('googlesearch.urls')),
    url(r'^ver_mapa_completo_dos/$', 'noticias.views.mapa_completo_dos', name='mapa-completo-dos'),
    url(r'^ver_mapa_completo/$', 'noticias.views.mapa_completo', name='mapa-completo'),
    url(r'^mapas/$', 'noticias.views.mapa', name='mapas'),
    url(r'^lista/socios/$', 'noticias.views.socios', name='lista-socios'),
    url(r'^socios/(?P<id>\d+)/$', 'noticias.views.ficha_socio', name='ficha-socio'),
    url(r'^posicion_mapa/$', 'noticias.views.mapa_pais', name="posicion_mapa"),
    url(r'^recursos/$', 'noticias.views.recursos', name='recursos'),
    url('^pages/', include('django.contrib.flatpages.urls')),
)

urlpatterns += staticfiles_urlpatterns()

if DEBUG:
    urlpatterns += patterns('',
                (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
                )
