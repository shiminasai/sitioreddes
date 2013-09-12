from django.conf.urls import patterns, include, url

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
)
