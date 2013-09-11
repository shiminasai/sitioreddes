from django.contrib import admin
from .models import Eventos, Categoria
from multimedia.models import *

class FotosAdmin(generic.GenericTabularInline):
    model = Fotos
    extra = 1

class AdjuntosAdmin(generic.GenericTabularInline):
    model = Adjuntos
    extra = 1

class EventosAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha_inicio','fecha_finalizacion','autor']
    list_filter = ('autor','categoria')
    search_fields = ('titulo',)
    inlines = [FotosAdmin, AdjuntosAdmin]

admin.site.register(Eventos, EventosAdmin)
admin.site.register(Categoria)