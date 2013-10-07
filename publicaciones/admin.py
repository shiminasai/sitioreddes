from django.contrib import admin
from .models import Publicaciones

class PublicacionesAdmin(admin.ModelAdmin):
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
    list_display = ['titulo', 'fecha','autor']
    list_filter = ('autor',)
    search_fields = ('titulo',)

admin.site.register(Publicaciones, PublicacionesAdmin)