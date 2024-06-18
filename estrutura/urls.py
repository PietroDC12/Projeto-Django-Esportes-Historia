from django.urls import path
from estrutura.views import index, noticia, buscar

urlpatterns = [
    path('', index, name='index'),
    path('noticia/<int:noticia_id>', noticia, name='noticia'),
    path('buscar', buscar, name='buscar'),
]