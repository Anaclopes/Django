from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth #para verificar credenciais


def login(request):
    login_form = LoginForms(prefix='login')
    cadastro_form = CadastroForms(prefix='cad')

    if request.method == "POST":
        login_form = LoginForms(request.POST, prefix='login') #puxando o formulário

        if login_form.is_valid():
            nome=login_form["nome_login"].value()
            senha=login_form["senha"].value()

        #Verificando as credenciais
        usuario = auth.authenticate(
            request,
            username=nome, #comparando os campos do banco com os inputs
            password=senha
        )

        if usuario is not None: #Verificando se não tem nada em branco
            auth.login(request, usuario) #Fazendo login
            messages.success(request, f'{usuario} logado com Sucesso')
            return redirect('index') #enviando para a home
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')

    return render(request, "usuarios/auth.html", {
            'login_form': login_form,
            'cadastro_form': cadastro_form,
            'show_register': False,   # começa mostrando LOGIN
            'VERSION': '1'            # se quiser forçar cache-bust
        })

def cadastro(request):

    login_form = LoginForms(prefix='login')
    cadastro_form = CadastroForms(prefix='cad')

    if request.method == "POST":
        cadastro_form = CadastroForms(request.POST, prefix='cad')
        
        if cadastro_form.is_valid(): #Verificando se as informações são válidas
            nome =  cadastro_form["nome_cadastro"].value() #Pegando as informações dos valores
            email = cadastro_form["email"].value()
            senha = cadastro_form["senha"].value()

            #Verificando se já tem um usuário com esse nome
            if User.objects.filter(username=nome).exists():
                messages.error(request, "Este nome de usuário já está em uso. Tente outro.")
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            ) #Se não tiver no banco, irá criar.

            usuario.save() #gravando o usuário no banco de dados
            messages.success(request, "Cadastro realizado com sucesso! Agora você pode fazer login.")
            return redirect('login')

    return render(request, "usuarios/auth.html", {
            'login_form': login_form,
            'cadastro_form': cadastro_form,
            'show_register': True,    # começa mostrando CADASTRO
            'VERSION': '1'
        })

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect('login')