# Generated by Django 4.2.13 on 2024-08-02 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estrutura', '0002_noticia_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='materia',
            field=models.CharField(choices=[('Futebol', 'Futebol'), ('Basquete', 'Basquete'), ('MMA', 'MMA'), ('Outro Esporte', 'Outro esporte')], default='', max_length=100),
        ),
    ]
