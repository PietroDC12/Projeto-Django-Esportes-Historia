from django.urls import path
from estrutura.views import index

urlpatterns = [
    path('', index)
]