from django.urls import path
from estrutura.views import index, historia

urlpatterns = [
    path('', index),
    path('historia/', historia)
]