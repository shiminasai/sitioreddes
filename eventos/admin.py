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
	inlines = [FotosAdmin, AdjuntosAdmin]

admin.site.register(Eventos, EventosAdmin)
admin.site.register(Categoria)