from django.shortcuts import render, get_object_or_404, redirect
from apps.estrutura.models import Noticia
from apps.estrutura.forms import NoticiaForms

from django.contrib import messages

def index(request):
    noticias = Noticia.objects.order_by("-date_noticia").filter(publicada=True)
    return render(request, 'index.html', {"cards": noticias})

def noticia(request, noticia_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado.')
        return redirect('login')
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    return render(request, 'noticias/noticia.html', {"noticia": noticia})

def nova_noticia(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado.')
        return redirect('login')
    
    form = NoticiaForms(request.POST)
    if request.method == 'POST':
        form = NoticiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova notícia cadastrada!')
            return redirect('index')
        
    return render(request, 'noticias/nova_noticia.html', {'form': form})

def editar_noticia(request, noticia_id):
    noticia = Noticia.objects.get(id=noticia_id)
    form = NoticiaForms(instance=noticia)

    if request.method == 'POST':
        form = NoticiaForms(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Notícia editada com sucesso!')
            return redirect('index')

    return render(request, 'noticias/editar_noticia.html', {'form': form, 'noticia_id': noticia_id})

def excluir_noticia(request, noticia_id):
    noticia = Noticia.objects.get(id=noticia_id)
    noticia.delete()

    messages.success(request, 'Notícia excluída com sucesso')
    return redirect('index')

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado.')
        return redirect('login')

    noticias = Noticia.objects.order_by("date_noticia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            noticias = noticias.filter(titulo__icontains=nome_a_buscar)

    return render(request, "buscar.html", {"cards": noticias})

def filtro(request, materia):
    noticias = Noticia.objects.order_by("-date_noticia").filter(publicada=True, materia=materia)

    return render(request, 'index.html', {"cards": noticias})