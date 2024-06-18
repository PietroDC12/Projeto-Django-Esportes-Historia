from django.contrib import admin
from .models import Escritor, Noticia

class Escritores(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    search_fields = ('id',)
    list_filter = ('id',)
    list_per_page = 10

admin.site.register(Escritor, Escritores)


class Noticias(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'publicada')
    list_display_links = ('id',)
    search_fields = ('id',)
    list_editable = ('publicada',)
    list_per_page = 10

admin.site.register(Noticia, Noticias)