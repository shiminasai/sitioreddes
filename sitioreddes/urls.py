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
)

urlpatterns += staticfiles_urlpatterns()

if DEBUG:
    urlpatterns += patterns('',
                (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
                )
