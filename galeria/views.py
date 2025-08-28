from django.shortcuts import render
from django.http import HttpResponse #Biblioteca para definir diversas formas de responder a uma requisição

def index(request): #recebendo a requisição
    return render(request, 'galeria/index.html') #O parâmetro sempre virá primeiro

def imagem(request):
    return render(request, 'galeria/imagem.html')