from eventos.models import Categoria

def globales(request):
    categorias = Categoria.objects.all()

    return {'categorias':categorias, }