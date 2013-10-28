from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Noticias, InicioTexto
from multimedia.models import Videos, Audio, Fotos, Adjuntos
from eventos.models import Eventos, Categoria
from publicaciones.models import Publicaciones
from .forms import ContactForm, PaisForm
from django.core.mail import send_mail
from django.http import HttpResponse
import json
from socios.models import Pais, Socios

def index(request, template='index.html'):
    #ultimas 3 noticias
    noticias_energia = Noticias.objects.filter(categoria__id=1).order_by('-fecha')[0:4]
    noticias_produccion = Noticias.objects.filter(categoria__id=2).order_by('-fecha')[0:4]
    noticias_fortalecimiento = Noticias.objects.filter(categoria__id=3).order_by('-fecha')[0:4]
    #ultimas 5 noticias de distintos paises destacadas
    ultimas_destacadas = []
    for obj in Pais.objects.all():
        info = Noticias.objects.filter(destacada=True,pais=obj).order_by('-id')[0:1]
        if info:
            ultimas_destacadas.append(info)
    #2 videos 
    ultimos_videos = Videos.objects.order_by('-id')[0:2]
    #2 eventos
    ultimos_eventos = Eventos.objects.order_by('-id')[0:4]
    #3 ultimas publicaciones
    ultimas_publicaciones = Publicaciones.objects.order_by('-id')[0:2]
    #4 ultimos audios
    ultimos_audios = Audio.objects.order_by('-id')[0:2]
    #texto al inicio de la pagina
    texto = InicioTexto.objects.filter(id=1)
    #fotos de las publicaciones
    shotos = Publicaciones.objects.order_by('-id')[0:24]
    
    return render(request, template, {'noticias_energia':noticias_energia,
                        'noticias_produccion':noticias_produccion,
                        'noticias_fortalecimiento':noticias_fortalecimiento,
                        'ultimas_destacadas':ultimas_destacadas,
                        'ultimos_videos':ultimos_videos,
                        'ultimos_eventos':ultimos_eventos,
                        'ultimas_publicaciones':ultimas_publicaciones,
                        'ultimos_audios':ultimos_audios,
                        'texto':texto,'shotos':shotos})


class NoticiasList(ListView):
    model = Noticias
    paginate_by = 4

class NoticiasDetailView(DetailView):
    model = Noticias

    def get_context_data(self, **kwargs):
        context = super(NoticiasDetailView, self).get_context_data(**kwargs)
        self.object = self.get_object()
        miobjeto = self.object
        variables = []
        for obj in miobjeto.categoria.all():
            variables.append(obj.id)
        context['relacion'] = Noticias.objects.filter(categoria__in=variables).exclude(id=miobjeto.id)[0:6]
        return context

def multimedia(request, template='multimedia/multimedia.html'):
    ultimos_audios = Audio.objects.order_by('-id')[0:4]
    ultimos_videos = Videos.objects.order_by('-id')[0:4]

    return render(request, template, { 'ultimos_videos':ultimos_videos,  
                                     'ultimos_audios':ultimos_audios})

def filtro_categoria(request,id,template='noticias/noticias_list.html'):
    object_list = Noticias.objects.filter(categoria__id=id)
    return render(request, template, {'object_list':object_list})

def contacto(request, template='contacto.html'):
    form = ContactForm()
    texto2 = InicioTexto.objects.filter(id=2)
    return render(request, template, {'form': form,'texto2':texto2})

def contacto_ajax(request):
    if request.is_ajax():
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['asunto']
            message = form.cleaned_data['mensaje']
            sender = form.cleaned_data['correo']

            recipients = ['crocha09.09@gmail.com',]

            send_mail(subject, message, sender, recipients)
            return HttpResponse( json.dumps( 'exito' ), mimetype='application/json' )
        else:
            return HttpResponse( json.dumps( 'falso' ), mimetype='application/json' )

def mapa_completo(request):
    lista = []
    for objeto in Socios.objects.filter(pais=request.GET['varPais']):
        dicc = dict(nombre=objeto.nombre,
                    id=objeto.id,
                    lon=float(objeto.position.longitude), 
                    lat=float(objeto.position.latitude),
                    ruta=objeto.get_absolute_url(),
                )
    lista.append(dicc)
    serializado = json.dumps(lista)
    return HttpResponse(serializado, mimetype='application/json')

def mapa_completo_dos(request):
    if request.is_ajax():
        lista = []
        for objeto in Socios.objects.all():
            dicc = dict(nombre=objeto.nombre,
                        id=objeto.id,
                        lon=float(objeto.position.longitude), 
                        lat=float(objeto.position.latitude),
                        ruta=objeto.get_absolute_url(),
                    )
            lista.append(dicc)
        serializado = json.dumps(lista)
        return HttpResponse(serializado, mimetype='application/json')

def mapa_pais(request):
    lista = [] 
    for objeto in Pais.objects.filter(id=request.POST['varPais']):  
        dicc = dict( 
            lon=float(objeto.longitud) , 
            lat=float(objeto.latitud),
            )

        lista.append(dicc)

    serializado = json.dumps(lista)
    return HttpResponse(serializado, mimetype='application/json') 

def mapa(request, template='mapa.html'):
    variable = 0
    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            request.session["pais"] =form.cleaned_data['pais']
            variable = 1
    else:
        form = PaisForm()
        variable = 0

    return render(request, template, {'form':form,'variable':variable})

def socios(request, template='socios/socios_lista.html'):
    socios = Socios.objects.all()
    return render(request,template,{'socios':socios})

def ficha_socio(request, id, template='socios/socios_detalle.html'):
    socio = Socios.objects.filter(id=id)
    for obj in socio:
        variable = obj.autor.id
    noticias = Noticias.objects.filter(autor__id=variable)[:4]
    publicaciones = Publicaciones.objects.filter(autor__id=variable)[:4]
    return render(request,template,{'socio':socio, 'noticias':noticias,
                                    'publicaciones':publicaciones})

def socios_pais(request, id_pais, template="socios/socios_lista.html"):
    socios = Socios.objects.filter(pais=id_pais)
    return render(request,template,{'socios':socios})

def recursos(request, template="recursos.html"):
    from itertools import chain

    fotos = Fotos.objects.order_by('-id')[0:6]
    videos = Videos.objects.order_by('-id')[0:6]
    audios = Audio.objects.order_by('-id')[0:6]
    adjuntos1 = Adjuntos.objects.order_by('-id')[0:6]
    documetos = Publicaciones.objects.order_by('-id')[0:6]
    adjuntos = list(chain(adjuntos1, documetos,))

    return render(request, template, {'fotos':fotos,'videos':videos,
                                      'audios':audios, 'adjuntos':adjuntos})