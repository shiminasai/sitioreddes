from django.contrib import admin
from .models import Socios, Pais

class SociosAdmin(admin.ModelAdmin):
    list_display = ['nombre','pais','contacto']
    list_filter = ('autor',)
    search_fields = ('nombre',)

admin.site.register(Socios, SociosAdmin)
admin.site.register(Pais)