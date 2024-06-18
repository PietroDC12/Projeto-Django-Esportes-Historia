from django.db import models
from datetime import datetime

class Escritor(models.Model):
    nome = models.CharField(max_length=30, null=False, blank=False)
    sobrenome = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.nome

class Noticia(models.Model):

    TAG_MATERIA =[
        ("FUTEBOL", "Futebol"),
        ("OUTRO ESPORTE", "Outro esporte"),
    ]

    escritor = models.ForeignKey(Escritor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, null=False, blank=False)
    subtitulo = models.CharField(max_length=100, null=False, blank=False)
    materia = models.CharField(max_length=100, choices=TAG_MATERIA, default='')
    corpo_texto = models.TextField(max_length=10000, null=False, blank=False)
    date_noticia = models.DateTimeField(default=datetime.now, blank=True)
    imagem_noticia = models.ImageField(upload_to='./setup/static/assets/imagens/banco_imagens/', blank=True)
    imagem_fonte = models.CharField(max_length=100, null=False, blank=True)
    publicada = models.BooleanField(default=False)


    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'