import datetime
import shutil
import schedule
import time
import os


def job():
    print("Backup realizado em:", datetime.datetime.now())


def entrada_usuario():
    while True:
        dia_backup = input("Informe a data para a realização do backup (DD/MM/YYYY): ")
        hora_backup = input("Informe a hora para a realização do backup (HH:MM): ")
        return dia_backup, hora_backup


def configurar_backup(dia_backup, hora_backup):

    horario_scheduled = f"{dia_backup} {hora_backup}"
    schedule.every().day.at(horario_scheduled).do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


def realizar_backup():
    while True:
        try:
            diretorio_atual = input(
                "Informe o diretório que deseja realizar o backup: "
            )
            diretorio_destino = input(
                "Informe o diretório que deseja salvar o arquivo de backup: "
            )

            # Verifica se o diretório de destino já existe
            if os.path.exists(diretorio_destino):
                print(f"O diretório de destino '{diretorio_destino}' já existe.")
                continue

            # Realizando o backup apenas se o diretório de destino não existir
            backup = shutil.copytree(diretorio_atual, diretorio_destino)
            if backup:
                print(f"Backup realizado com sucesso para: {diretorio_destino}")
                break

        except ValueError:
            print(
                "Formato inválido. Certifique-se de inserir a data e hora no formato correto (DD/MM/YYYY HH:MM)."
            )
        except shutil.Error as e:
            print(f"Falha ao realizar o backup. Erro: {e}. Por favor, tente novamente.")


def main():
    print("Bem-vindo! Por favor, informe a data e a hora para a realização do backup:")
    dia_backup, hora_backup = entrada_usuario()
    configurar_backup(dia_backup, hora_backup)


if __name__ == "__main__":
    main()
