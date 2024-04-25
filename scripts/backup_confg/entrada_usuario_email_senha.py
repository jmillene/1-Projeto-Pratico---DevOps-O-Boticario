from email.mime.application import MIMEApplication
import smtplib
import tkinter as tk
from tkinter import messagebox
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import google_auth_oauthlib
import pyperclip
import os


def enviar_email(email, senha, destinatario, arquivo_anexo):
    try:
        with smtplib.SMTP(
            "smtp.gmail.com", 587
        ) as server:  # Alterado para o servidor do Gmail
            server.starttls()
            server.login(email, senha)
            message = MIMEMultipart()
            message["From"] = email
            message["To"] = destinatario
            message["Subject"] = "Assunto do E-mail"

            # Corpo do e-mail
            msg = MIMEText("Segue em anexo o backup.")
            message.attach(msg)

            # Anexo (arquivo zipado)
            with open(arquivo_anexo, "rb") as attachment:
                part = MIMEApplication(
                    attachment.read(), Name=os.path.basename(arquivo_anexo)
                )
            part["Content-Disposition"] = (
                f'attachment; filename="{os.path.basename(arquivo_anexo)}"'
            )
            message.attach(part)

            server.send_message(message)
            print("Email enviado com sucesso!")
    except Exception as e:
        with open("error.log", "w") as f:
            f.write(f"Falha ao enviar email: {e}")
        messagebox.showerror(
            "Erro",
            "Ocorreu um erro ao enviar o email. Consulte o arquivo error.log para mais informações.",
        )


def autenticar_email(entry_email, entry_senha, root, entry_destinatario):
    email = entry_email.get()
    senha = entry_senha.get()
    destinatario = entry_destinatario.get()

    try:
        # Configurar o fluxo de autenticação do Google
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            "cliente_secret.json",
            scopes=["https://www.googleapis.com/auth/gmail.send"],
        )

        # Iniciar a autenticação
        credentials = flow.run_local_server()

        # Obter a resposta de autenticação
        google_auth_response = credentials.to_json()

        # Exibir mensagem de autenticação bem-sucedida
        messagebox.showinfo("Autenticação", "Autenticação bem-sucedida!")

        # Chamar a função para enviar e-mails
        enviar_email(email, senha, destinatario, arquivo_anexo=None)
    except Exception as e:
        with open("error.log", "w") as f:
            f.write(f"Falha na autenticação: {e}")
        messagebox.showerror(
            "Autenticação",
            "Ocorreu um erro. Consulte o arquivo error.log para mais informações.",
        )


def abrir_janela_envio_email(email, senha, root):
    root.withdraw()  # Esconde a janela de autenticação
    janela_envio_email = tk.Toplevel()
    janela_envio_email.title("Envio de E-mail")

    frame = tk.Frame(janela_envio_email)
    frame.pack(padx=20, pady=20)

    tk.Label(frame, text="E-mail destinatário:").grid(row=0, column=0, sticky="w")
    entry_destinatario = tk.Entry(frame)
    entry_destinatario.grid(row=0, column=1, padx=10, pady=5)

    btn_enviar = tk.Button(
        janela_envio_email,
        text="Enviar",
        command=lambda: enviar_email(email, senha, entry_destinatario.get(), None),
    )
    btn_enviar.pack(pady=10)


def copiar_erro(entry_mensagem):
    erro = pyperclip.paste()
    if erro:
        entry_mensagem.delete("1.0", "end")
        entry_mensagem.insert("1.0", erro)
        messagebox.showinfo(
            "Mensagem Copiada", "Mensagem de erro copiada para o campo de mensagem."
        )


def interface_email():
    root = tk.Tk()
    root.title("Autenticação de E-mail")

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    tk.Label(frame, text="E-mail:").grid(row=0, column=0, sticky="w")
    entry_email = tk.Entry(frame)
    entry_email.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame, text="Senha:").grid(row=1, column=0, sticky="w")
    entry_senha = tk.Entry(frame, show="*")
    entry_senha.grid(row=1, column=1, padx=10, pady=5)

    btn_autenticar = tk.Button(
        root,
        text="Autenticar",
        command=lambda: autenticar_email(entry_email, entry_senha, root),
    )
    btn_autenticar.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    interface_email()
