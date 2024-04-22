import re
from user.verificar_credenciais_usuario import verificar_credenciais_usuario
from interface_grafica.email_interface import entry_email, entry_senha


def obter_email():
    while True:
        email = entry_email.get()
        regex = r"^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$"

        if email == "" or email == 0:
            print("Campo e-mail vazio!")
        elif email != regex:
            print("Formato inválido de e-mail!")
        else:
            verificar_credenciais_usuario
        return email


def obter_senha():
    while True:
        senha = entry_senha.get()
        if senha == " " or senha == 0:
            print("Campo senha vazio!")
        else:
            verificar_credenciais_usuario
        return senha


def iniciar_login():
    obter_email()
    obter_senha()
