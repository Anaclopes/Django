from django.urls import path
from galeria.views import *

urlpatterns = [
    path('', index, name='index'), #Isolando as urls do app galeria
    #pegando a imagem pelo id
    path('imagem/<int:foto_id>', imagem, name='imagem'), #O name serve para poder referenciar na tag html depois
    path("buscar", buscar, name='buscar') #criando o método de buscar
]