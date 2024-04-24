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
        with smtplib.SMTP("gmail-smtp-in.l.google.com", 25) as server:
            server.ehlo("gmail.com")
            server.starttls()
            server.login(email, senha)
            message = MIMEMultipart()
            message["From"] = email
            message["To"] = destinatario
            message["Subject"] = "SMTP Email Test"
            server.send_message(message)
            
            # Corpo do e-mail
            msg = MIMEText("Segue em anexo o backup.")
            message.attach(msg)

            # Anexo
            with open(arquivo_anexo, "rb") as attachment:
                part = MIMEApplication(
                    attachment.read(), Name=os.path.basename(arquivo_anexo)
                )
            part["Content-Disposition"] = (
                f'attachment; filename="{os.path.basename(arquivo_anexo)}"'
            )
            message.attach(part)
            print("Email enviado com sucesso!")
    except Exception as e:
        with open("error.log", "w") as f:
            f.write(f"Falha ao enviar email: {e}")
        messagebox.showerror(
            "Erro",
            "Ocorreu um erro ao enviar o email. Consulte o arquivo error.log para mais informações.",
        )


def autenticar_email(entry_email, entry_senha, root, destinatario):
    email = entry_email.get()
    senha = entry_senha.get()

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

    destinatario = tk.StringVar()  # Definindo a variável destinatario
    assunto = tk.StringVar()

    tk.Label(frame, text="E-mail destinatário:").grid(row=0, column=0, sticky="w")
    entry_destinatario = tk.Entry(frame, textvariable=destinatario)
    entry_destinatario.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame, text="Assunto:").grid(row=1, column=0, sticky="w")
    entry_assunto = tk.Entry(frame, textvariable=assunto)
    entry_assunto.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame, text="Mensagem:").grid(row=2, column=0, sticky="w")
    entry_mensagem = tk.Text(frame, height=5, width=30)
    entry_mensagem.grid(row=2, column=1, padx=10, pady=5)

    btn_enviar = tk.Button(
        janela_envio_email,
        text="Enviar",
        command=lambda: enviar_email(
            email, senha, entry_destinatario.get(), None
        ),  # Removido o argumento 'root'
    )
    btn_enviar.pack(pady=10)

    btn_copiar_erro = tk.Button(
        janela_envio_email,
        text="Copiar Erro",
        command=lambda: copiar_erro(entry_mensagem),
    )
    btn_copiar_erro.pack(pady=5)

    btn_copiar_erro = tk.Button(
        janela_envio_email,
        text="Copiar Erro",
        command=lambda: copiar_erro(entry_mensagem),
    )
    btn_copiar_erro.pack(pady=5)


def copiar_erro(entry_mensagem):
    erro = pyperclip.paste()
    if erro:
        entry_mensagem.delete("1.0", "end")
        entry_mensagem.insert("1.0", erro)
        messagebox.showinfo(
            "Mensagem Copiada", "Mensagem de erro copiada para o campo de mensagem."
        )


def interface_email(arquivo_anexo):
    root = tk.Tk()
    root.title("Autenticação de E-mail")

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    email = tk.StringVar()
    senha = tk.StringVar()
    destinatario = tk.StringVar()  # Adicionei a variável para o destinatário

    tk.Label(frame, text="E-mail:").grid(row=0, column=0, sticky="w")
    entry_email = tk.Entry(frame, textvariable=email)
    entry_email.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame, text="Senha:").grid(row=1, column=0, sticky="w")
    entry_senha = tk.Entry(frame, textvariable=senha, show="*")
    entry_senha.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame, text="Destinatário:").grid(
        row=2, column=0, sticky="w"
    )  # Adicionei um rótulo para o destinatário
    entry_destinatario = tk.Entry(frame, textvariable=destinatario)
    entry_destinatario.grid(row=2, column=1, padx=10, pady=5)

    btn_autenticar = tk.Button(
        root,
        text="Autenticar",
        command=lambda: autenticar_email(
            entry_email, entry_senha, root, entry_destinatario.get()
        ),  # Passei o destinatário como argumento
    )
    btn_autenticar.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    interface_email(arquivo_anexo=None)

