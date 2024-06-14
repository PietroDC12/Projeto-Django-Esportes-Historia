from django.shortcuts import render, get_object_or_404
from estrutura.models import Noticia

def index(request):
    noticias = Noticia.objects.all()
    return render(request, 'index.html', {"cards": noticias})

def noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    return render(request, 'noticia.html', {"noticia": noticia})