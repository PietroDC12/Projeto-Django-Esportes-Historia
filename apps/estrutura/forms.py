from django import forms

from apps.estrutura.models import Noticia

class NoticiaForms(forms.ModelForm):
    class Meta:
        model = Noticia
        exclude = ['publicada',]

        labels = {
            'escritor': 'Escritor',
            'titulo': 'Título',
            'subtitulo': 'Subtítulo',
            'materia': 'Categoria',
            'corpo_texto': 'Matéria',
            'imagem_noticia': 'Imagem',
            'date_noticia': 'Data de publicação',
            'imagem_fonte': 'Fonte da imagem',
            'usuario': 'Usuário registrado'
        }

        widgets = {
            'escritor' : forms.Select(attrs={'class':'form-control'}),
            'titulo' : forms.TextInput(attrs={'class':'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class':'form-control'}),
            'materia' : forms.Select(attrs={'class':'form-control'}),
            'corpo_texto' : forms.Textarea(attrs={'class':'form-control'}),
            'imagem_noticia' : forms.FileInput(attrs={'class':'form-control'}),
            'date_noticia' : forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'imagem_fonte' : forms.TextInput(attrs={'class':'form-control'}),
            'usuario': forms.Select(attrs={'class':'form-control'}),
                }