from django import forms

class LoginForms(forms.Form): #Passando os inputs
    nome_login = forms.CharField(
        label= 'Nome de usuario',
        required= True,
        max_length= 100,
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: Ana"
            }
        )
    )

    senha = forms.CharField(
        label= 'Senha',
        required= True,
        max_length= 70,
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        ) #para esconder a senha
    )

    


class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label= 'Nome de usuario',
        required= True,
        max_length= 100,
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: Ana"
            }
        )
    )

    email = forms.EmailField(
        label= 'E-mail',
        required= True,
        max_length= 100,
        widget= forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex: Ana@email.com"
            }
        )
    )

    senha = forms.CharField(
        label= 'Senha',
        required= True,
        max_length= 70,
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        ) #para esconder a senha
    )
