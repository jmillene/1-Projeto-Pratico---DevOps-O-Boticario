import imaplib
from user.entrada_usuario_email_senha import obter_email, obter_senha


def verificar_credenciais_usuario(email, senha, servidor_imap):
    try:
        # Conecta ao servidor IMAP do provedor de e-mail
        mail = imaplib.IMAP4_SSL(servidor_imap)
        # Fazer login com o e-mail e senha fornecidos
        mail.login(email, senha)

        print("Credenciais corretas!")
        mail.logout()
        return True
    except Exception as e:

        print("Credenciais incorretas:", e)
        return False


servidor_imap_gmail = "imap.gmail.com"  # Servidor IMAP do Gmail
servidor_imap_outlook = "outlook.office365.com"  # Servidor IMAP do Outlook (Hotmail)
servidor_imap_yahoo = "imap.mail.yahoo.com"

# Verifica credenciais para o Gmail
verificar_credenciais_usuario(obter_email, obter_senha, servidor_imap_gmail)

# Verifica credenciais para o Outlook (Hotmail)
verificar_credenciais_usuario(obter_email, obter_senha, servidor_imap_outlook)

# Verifica credenciais para o Yahoo
verificar_credenciais_usuario(obter_email, obter_senha, servidor_imap_yahoo)
