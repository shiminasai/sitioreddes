from django.contrib import admin
from .models import *

class AudiosAdmin(generic.GenericTabularInline):
    model = Audio
    extra = 1

class VideosAdmin(generic.GenericTabularInline):
    model = Videos
    extra = 1

class MultimediaAdmin(admin.ModelAdmin):
    def queryset(self, request):
        if request.user.is_superuser:
            return self.model.objects.all()
        elif request.user.is_staff:
            return self.model.objects.filter(autor=request.user)

    def save_model(self, request, obj, form, change):
        instance = form.save(commit=False)
        instance.autor = request.user
        instance.save()
        return instance

    exclude = ['autor']
    inlines = [VideosAdmin, AudiosAdmin]

admin.site.register(Multimedia,MultimediaAdmin)
admin.site.register(Videos)
admin.site.register(Fotos)
admin.site.register(Audio)