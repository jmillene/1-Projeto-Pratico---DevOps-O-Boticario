import tkinter as tk
from tkinter import simpledialog, messagebox

def validar_data(dia, mes, ano):
    try:
        dia = int(dia)
        mes = int(mes)
        ano = int(ano)
        if dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 1:
            return False
        if mes in [4, 6, 9, 11] and dia > 30:
            return False
        if mes == 2:
            if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
                if dia > 29:
                    return False
            elif dia > 28:
                return False
        return True
    except ValueError:
        return False

def validar_hora(hora, minuto):
    try:
        hora = int(hora)
        minuto = int(minuto)
        if hora < 0 or hora > 23 or minuto < 0 or minuto > 59:
            return False
        return True
    except ValueError:
        return False

def validar_data_hora(data, hora, minuto):
    partes_data = data.split('/')
    if len(partes_data) != 3:
        return False
    dia, mes, ano = partes_data
    return validar_data(dia, mes, ano) and validar_hora(hora, minuto)

def solicitar_data_hora_backup():
    while True:
        data = simpledialog.askstring("Data do Backup", "Por favor, informe a data do backup no formato dia/mês/ano (1-31/1-12/ano): ")
        hora_minuto = simpledialog.askstring("Hora do Backup", "Por favor, informe a hora e os minutos do backup no formato hora:minuto (0-23:0-59):")
        if None in [data, hora_minuto]:  # Se o usuário clicar em Cancelar
            return None

        partes_hora_minuto = hora_minuto.split(':')
        if len(partes_hora_minuto) != 2:
            messagebox.showerror("Erro", "Hora inserida incorreta. Por favor, insira no formato correto.")
            continue

        hora, minuto = partes_hora_minuto
        if validar_data_hora(data, hora, minuto):
            return f"{data} {hora}:{minuto}"
        else:
            messagebox.showerror("Erro", "Data ou hora inseridas incorretas. Por favor, insira no formato correto.")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal

    data_hora_backup = solicitar_data_hora_backup()
    if data_hora_backup:
        print("Data e hora do backup:", data_hora_backup)
