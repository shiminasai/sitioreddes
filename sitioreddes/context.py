from eventos.models import Categoria
from taggit.models import Tag
from socios.models import Pais

def globales(request):
    categorias = Categoria.objects.all()
    tags = Tag.objects.all()
    paises = Pais.objects.all()
    return {'categorias':categorias, 'tags':tags, 'paises':paises}