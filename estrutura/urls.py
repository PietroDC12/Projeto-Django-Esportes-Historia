from django.urls import path
from estrutura.views import index, historia

urlpatterns = [
    path('', index, name='index'),
    path('historia/', historia, name='historia')
]