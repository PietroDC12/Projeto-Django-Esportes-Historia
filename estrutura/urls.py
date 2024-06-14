from django.urls import path
from estrutura.views import index, noticia

urlpatterns = [
    path('', index, name='index'),
    path('noticia/<int:noticia_id>', noticia, name='noticia')
]