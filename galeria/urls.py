from django.urls import path
from galeria.views import *

urlpatterns = [
    path('', index, name='index'), #Isolando as urls do app galeria
    path('imagem/', imagem, name='imagem') #O name serve para poder referenciar na tag html depois
]