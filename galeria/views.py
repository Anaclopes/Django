from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse #Biblioteca para definir diversas formas de responder a uma requisição
from galeria.models import Fotografia


def index(request): #recebendo a requisição
    #fotografias = Fotografia.objects.all() #passando todos itens que tenho no banco
    #mais antigo primeiro, mais novo depois
    fotografias = Fotografia.objects.order_by("-data").filter(publicada = True) #passando apenas as publicadas
    #render permite retornar e enviar 
    return render(request, 'galeria/index.html', {"cards": fotografias}) #O parâmetro sempre virá primeiro

#recebendo a imagem
def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id) #ou puxa o objeto ou dá um 404
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia}) #acessando o objeto no banco de dados ao qual o id faz referência

def buscar(request):
    fotografias = Fotografia.objects.order_by("-data").filter(publicada = True) 

    if "buscar" in request.GET: #Verificando se tenho buscar na minha url
        #faz referÊncia ao input
        nome_a_buscar = request.GET['buscar'] #Verificando o que está sendo buscado e buscando
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar) #verificando se os nomes que temos existe alguma parte do que estamos buscando

    return render(request, "galeria/buscar.html", {"cards": fotografias})
