
from .models import Publicaciones
from django.views.generic import ListView
from taggit.models import Tag

class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

class TagIndexView(TagMixin, ListView):
    template_name = 'publicaciones/publicaciones_list.html'
    model = Publicaciones
    paginate_by = '7'
    context_object_name = 'publicacion'

    def get_queryset(self):
        return Publicaciones.objects.filter(categoria__slug=self.kwargs.get('slug'))