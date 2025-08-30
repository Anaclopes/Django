from django.contrib import admin
from galeria.models import Fotografia


#Personalizando a forma como irá aparecer cada objeto na página de admin
class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada", "data")
    list_display_links = ("id", "nome")
    search_fields = ("nome",) #Adicionando um campo de buscas pelo nome (a virgula é obrigatória no final)
    list_filter = ("categoria",) #criando um filtro por categoria
    list_editable = ("publicada",) #alterando se está publicada ou não
    list_per_page =10 #limitando quantos itens serão exibidos por página

admin.site.register(Fotografia, ListandoFotografias) #Registrando o banco de dados no admin
