from django.urls import path
from apps.estrutura.views import index, noticia, buscar, nova_noticia, editar_noticia, excluir_noticia, filtro

urlpatterns = [
    path('', index, name='index'),
    path('noticia/<int:noticia_id>', noticia, name='noticia'),
    path('buscar', buscar, name='buscar'),
    path('nova/noticia', nova_noticia, name='nova_noticia'),
    path('editar/noticia/<int:noticia_id>', editar_noticia, name='editar_noticia'),
    path('excluir/noticia/<int:noticia_id>', excluir_noticia, name='excluir_noticia'),
    path('filtro/<str:materia>', filtro, name='filtro'),
]