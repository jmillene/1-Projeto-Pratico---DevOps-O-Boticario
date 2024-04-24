import tkinter as tk
from tkinter import filedialog

# Função para selecionar o diretório raiz
def selecionar_diretorio_raiz():
    diretorio = filedialog.askdirectory(title="Por favor! Selecione o diretório raiz")
    if diretorio:
        diretorio_raiz.set(diretorio)

# Função para selecionar o diretório de destino
def selecionar_diretorio_destino():
    diretorio = filedialog.askdirectory(title="Por favor! Selecione o diretório de destino")
    if diretorio:
        diretorio_destino.set(diretorio)

root = tk.Tk()
root.withdraw()  # Esconder a janela principal

# Variáveis de controle
diretorio_raiz = tk.StringVar()
diretorio_destino = tk.StringVar()



