import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os
import zipfile
from entrada_usuario_email_senha import interface_email
from programando_bkp import solicitar_data_hora_backup

# Função para selecionar diretório de origem
def selecionar_diretorio_origem():
    diretorio = filedialog.askdirectory(
        title="Por favor! Selecione o diretório de origem"
    )
    if diretorio:
        diretorio_raiz.set(diretorio)
        selecionar_diretorio_destino()  # Após selecionar a origem, chama a função para selecionar o destino

# Função para selecionar diretório de destino
def selecionar_diretorio_destino():
    diretorio = filedialog.askdirectory(
        title="Por favor! Selecione o diretório de destino"
    )
    if diretorio:
        diretorio_destino.set(diretorio)
        realizar_backup(diretorio)  # Passando o diretório de destino como argumento

# Função para realizar o backup dos arquivos para o diretório de destino
def realizar_backup(diretorio_destino):  # Adicionando o diretório de destino como argumento
    try:
        diretorio_origem = diretorio_raiz.get()

        # Verificar se o diretório de destino já existe
        if os.path.exists(diretorio_destino):
            resposta = messagebox.askquestion(
                "Diretório Já Existe",
                "O diretório de destino já existe. Deseja criar um novo diretório?",
            )
            if resposta == "yes":
                diretorio_destino = filedialog.askdirectory(
                    title="Selecione um novo diretório de destino"
                )
                if not diretorio_destino:
                    return  # Se o usuário cancelar, não faz nada
            else:
                messagebox.showinfo(
                    "Info",
                    f"O backup não será realizado. Diretório de destino existente: '{diretorio_destino}'"
                )
                return

        # Copiar os arquivos para o diretório de destino
        shutil.copytree(diretorio_origem, diretorio_destino)

        # Após a conclusão do backup, zipar o diretório de destino
        nome_arquivo_zip = zipar_pasta(diretorio_destino)

        if nome_arquivo_zip:
            messagebox.showinfo(
                "Sucesso",
                f"Backup realizado com sucesso e zipado: {nome_arquivo_zip}",
            )

            # Verificar se deseja enviar o backup por e-mail
            while True:
                pergunta = (
                    input("Deseja enviar o backup por e-mail? (S/N): ").strip().lower()
                )
                if pergunta == "s":
                    interface_email(arquivo_anexo=None)
                    break
                elif pergunta == "n":
                    break
                else:
                    print("Por favor, responda 'S' para Sim ou 'N' para Não.")
    except Exception as e:
        with open("error.log", "w") as f:
            f.write(f"Falha ao realizar o backup: {e}")
        messagebox.showerror("Erro", f"Falha ao realizar o backup: {e}")

# Função para zipar a pasta de backup
def zipar_pasta(diretorio_destino):
    try:
        nome_arquivo_zip = os.path.join(diretorio_destino, "backup.zip")
        with zipfile.ZipFile(nome_arquivo_zip, "w") as zip_ref:
            for root, _, files in os.walk(diretorio_destino):
                for file in files:
                    zip_ref.write(
                        os.path.join(root, file),
                        os.path.relpath(os.path.join(root, file), diretorio_destino),
                    )
        return nome_arquivo_zip
    except Exception as e:
        with open("error.log", "w") as f:
            f.write(f"Erro ao zipar a pasta de backup: {e}")
        messagebox.showerror("Erro", f"Erro ao zipar a pasta de backup: {e}")
        return None

# Inicialização do Tkinter
root = tk.Tk()
root.withdraw()  # Esconder a janela principal

# Variáveis de controle
diretorio_raiz = tk.StringVar()
diretorio_destino = tk.StringVar()

if __name__ == "__main__":
    solicitar_data_hora_backup()  # Solicita a data e hora antes de selecionar o diretório de origem
    selecionar_diretorio_origem()
