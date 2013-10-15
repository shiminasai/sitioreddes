from eventos.models import Categoria
from taggit.models import Tag

def globales(request):
    categorias = Categoria.objects.all()
    tags = Tag.objects.all()
    return {'categorias':categorias, 'tags':tags}