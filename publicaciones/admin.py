from django.contrib import admin
from .models import Publicaciones

class PublicacionesAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha','autor']
    list_filter = ('autor',)
    search_fields = ('titulo',)

admin.site.register(Publicaciones, PublicacionesAdmin)