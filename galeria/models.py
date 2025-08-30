from django.db import models
from datetime import datetime

class Fotografia(models.Model):
    #Criando uma lista de categorias
    opcoes_Categoria = [
        ("CLÁSSICO", "Clássico"),
        ("ASSISTIDOS", "Assistidos"),
        ("RECOMENDADOS", "Recomendados"),
        ("ACOMPANHANDO", "Acompanhando")
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=255, null=False, blank=False)
    categoria = models.CharField(max_length=100,choices=opcoes_Categoria, default='') #choices, lista apenas os itens na lista
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True) #Me permite importar uma foto e irá armazenar o caminho dela
    publicada = models.BooleanField(default=False) #ao inserir um item, ele não será publicado de automático
    data = models.DateTimeField(default=datetime.now, blank=False)


def __str__(self):
    return self.nome