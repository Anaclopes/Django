from django.shortcuts import render
from usuarios.forms import LoginForms, CadastroForms

def login(request):
    login_form = LoginForms(prefix='login')
    cadastro_form = CadastroForms(prefix='cad')
    return render(request, "usuarios/auth.html", {
            'login_form': login_form,
            'cadastro_form': cadastro_form,
            'show_register': False,   # começa mostrando LOGIN
            'VERSION': '1'            # se quiser forçar cache-bust
        })

def cadastro(request):
    login_form = LoginForms(prefix='login')
    cadastro_form = CadastroForms(prefix='cad')

    if request == "POST":
        cadastro_form(request.POST)
        
    return render(request, "usuarios/auth.html", {
            'login_form': login_form,
            'cadastro_form': cadastro_form,
            'show_register': True,    # começa mostrando CADASTRO
            'VERSION': '1'
        })