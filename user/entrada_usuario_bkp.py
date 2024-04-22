import datetime
import shutil
import schedule
import time
import os
from interface_grafica.email_interface import interface_email


def entrada_usuario_enviar_email():
    while True:
        pergunta = str(
            input("Deseja enviar backup por e-mail? Sim[s] ou Não[n]? ")
        ).lower()
        if pergunta == "s":
            interface_email()
            break
        elif pergunta == "n":
            break
        else:
            print("Por favor, responda 's' ou 'n'.")


def entrada_usuario_backup():
    while True:
        dia_backup = input("Informe a data para a realização do backup (DD/MM/YYYY): ")
        hora_backup = input("Informe a hora para a realização do backup (HH:MM): ")

        try:
            data_hora_backup = datetime.datetime.strptime(
                f"{dia_backup} {hora_backup}", "%d/%m/%Y %H:%M"
            )
            return data_hora_backup
        except ValueError:
            print(
                "Formato de data ou hora inválido. Certifique-se de inserir a data no formato DD/MM/YYYY e a hora no formato HH:MM."
            )
