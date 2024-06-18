from django.shortcuts import render, get_object_or_404
from estrutura.models import Noticia

def index(request):
    noticias = Noticia.objects.order_by("date_noticia").filter(publicada=True)
    return render(request, 'index.html', {"cards": noticias})

def noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    return render(request, 'noticia.html', {"noticia": noticia})

def buscar(request):
    noticias = Noticia.objects.order_by("date_noticia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            noticias = noticias.filter(titulo__icontains=nome_a_buscar)

    return render(request, "buscar.html", {"cards": noticias})