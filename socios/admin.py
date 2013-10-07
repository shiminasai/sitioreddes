from django.contrib import admin
from .models import Socios, Pais

class SociosAdmin(admin.ModelAdmin):
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

    #exclude = ['autor']
    list_display = ['nombre','pais','contacto']
    list_filter = ('autor',)
    search_fields = ('nombre',)

admin.site.register(Socios, SociosAdmin)
admin.site.register(Pais)