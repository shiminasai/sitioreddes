from django.views.generic import ListView, DetailView
from .models import Eventos

class EventosList(ListView):
	model = Eventos

class EventosDetailView(DetailView):
    model = Eventos

    # def get_context_data(self, **kwargs):
    #     context = super(EventosDetailView, self).get_context_data(**kwargs)
    #     context['eventos_list'] = Eventos.objects.all()
    #     return context