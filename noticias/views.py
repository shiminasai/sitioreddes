from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Noticias, InicioTexto
from multimedia.models import Videos, Audio
from eventos.models import Eventos
from publicaciones.models import Publicaciones
from .forms import ContactForm, PaisForm
from django.core.mail import send_mail
from django.http import HttpResponse
import json
from tagging.models import Tag, TaggedItem
from socios.models import Pais, Socios

def index(request, template='index.html'):
    #ultimas 3 noticias
    noticias_energia = Noticias.objects.filter(categoria__id=1).order_by('-fecha')[0:4]
    print noticias_energia
    noticias_produccion = Noticias.objects.filter(categoria__id=2).order_by('-fecha')[0:4]
    noticias_fortalecimiento = Noticias.objects.filter(categoria__id=3).order_by('-fecha')[0:4]
    #ultimas 5 noticias de distintos paises destacadas
    ultimas_destacadas = []
    for obj in Pais.objects.all():
        ultimas_destacadas.append(Noticias.objects.filter(destacada=True,pais=obj).order_by('-id')[0:1])

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
    
    return render(request, template, {'noticias_energia':noticias_energia,
                        'noticias_produccion':noticias_produccion,
                        'noticias_fortalecimiento':noticias_fortalecimiento,
                        'ultimas_destacadas':ultimas_destacadas,
                        'ultimos_videos':ultimos_videos,
                        'ultimos_eventos':ultimos_eventos,
                        'ultimas_publicaciones':ultimas_publicaciones,
                        'ultimos_audios':ultimos_audios,
                        'texto':texto})


class NoticiasList(ListView):
    model = Noticias
    paginate_by = 4

class NoticiasDetailView(DetailView):
    model = Noticias

def multimedia(request, template='multimedia/multimedia.html'):
    ultimos_audios = Audio.objects.order_by('-id')[0:4]
    ultimos_videos = Videos.objects.order_by('-id')[0:4]

    return render(request, template, { 'ultimos_videos':ultimos_videos,  
                                     'ultimos_audios':ultimos_audios})

def filtro_categoria(request,categoria1,template='noticias/noticias_list.html'):
    try:
        tag1 = Tag.objects.get(name=categoria1)
    except:
        tag1 = ''
    object_list = TaggedItem.objects.get_union_by_model(Noticias, [tag1])
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

def ficha_socio(request, id, template='socios.html'):
    socio = Socios.objects.filter(id=id)
    return render(request,template,{'socio':socio})