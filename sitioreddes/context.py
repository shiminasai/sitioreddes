from eventos.models import Categoria
from taggit.models import Tag
from socios.models import Pais
from publicaciones.models import Publicaciones

def globales(request):
    categorias = Categoria.objects.all()
    tags = Tag.objects.all()
    paises = Pais.objects.all()
    publi = Publicaciones.objects.order_by('-id')[:3]
    return {'categorias':categorias, 'tags':tags, 'paises':paises,'publi':publi}