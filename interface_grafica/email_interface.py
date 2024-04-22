import tkinter as tk
from user.entrada_usuario_email_senha import iniciar_login


def interface_email():

    # Cria janela principal
    root = tk.Tk()
    root.title("Login")

    # Frame para organizar os widgets
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    # Rótulo e campo de entrada para o e-mail
    tk.Label(frame, text="E-mail:").grid(row=0, column=0, sticky="w")
    entry_email = tk.Entry(frame)
    entry_email.grid(row=0, column=1, padx=10, pady=5)

    # Rótulo e campo de entrada para a senha
    tk.Label(frame, text="Senha:").grid(row=1, column=0, sticky="w")
    entry_senha = tk.Entry(frame, show="*")
    entry_senha.grid(row=1, column=1, padx=10, pady=5)

    # Botão para iniciar o processo de login
    btn_login = tk.Button(root, text="Login", command=iniciar_login)
    btn_login.pack(pady=10)

    # Executa a janela
    root.mainloop()
