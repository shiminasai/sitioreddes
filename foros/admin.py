from django.contrib import admin
from models import *
from foros.models import *
from foros.forms import *
from multimedia.models import Adjuntos, Audio, Fotos, Videos

class DocumentosInline(generic.GenericTabularInline):
    model = Adjuntos
    extra = 1

class ImagenInline(generic.GenericTabularInline):
    model = Fotos
    extra = 1

class VideosInline(generic.GenericTabularInline):
    model = Videos
    extra = 1

class AudiosInline(generic.GenericTabularInline):
    model = Audio
    extra = 1

class ForoAdmin(admin.ModelAdmin):
    inlines = [DocumentosInline, ImagenInline, 
              VideosInline, AudiosInline]
    form = ForosForm

class AportesAdmin(admin.ModelAdmin):
    inlines = [DocumentosInline, ImagenInline, 
              VideosInline, AudiosInline]
    form = AporteForm

class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'usuario', 'aporte')
    form = ComentarioForm

admin.site.register(Foros, ForoAdmin)
admin.site.register(Aportes, AportesAdmin)
admin.site.register(Comentarios, ComentariosAdmin)
#admin.site.register(Adjuntos)
