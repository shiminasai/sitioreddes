from django.contrib import admin
from .models import *

class AudiosAdmin(generic.GenericTabularInline):
    model = Audio
    extra = 1

class VideosAdmin(generic.GenericTabularInline):
    model = Videos
    extra = 1

class MultimediaAdmin(admin.ModelAdmin):
    inlines = [AudiosAdmin, VideosAdmin]

admin.site.register(Multimedia,MultimediaAdmin)
admin.site.register(Videos)
admin.site.register(Fotos)
admin.site.register(Audio)