from django.shortcuts import render
from django.http import HttpResponse #Biblioteca para definir diversas formas de responder a uma requisição

dados = {
    1: {
        "nome": "Nebulosa de Carina",
        "legenda": "webbtelecope.org / NASA / James Webb"
    },

    2:{
        "nome": "Galaxia NGC 1079",
        "legenda": "nasa.org / NASA / Hubble"
    }
}

def index(request): #recebendo a requisição
    #render permite retornar e enviar 
    return render(request, 'galeria/index.html', {"cards": dados}) #O parâmetro sempre virá primeiro

def imagem(request):
    return render(request, 'galeria/imagem.html')