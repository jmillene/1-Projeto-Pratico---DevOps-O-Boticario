import datetime
import shutil
import schedule
import time
import os
import aspose.zip as az


from enviar_bkp_email import enviar_backup_por_email


def job():
    print("Backup realizado em:", datetime.datetime.now())
    print("Backup realizado com sucesso.")

    while True:
        pergunta = str(
            input("Deseja enviar backup por e-mail? Sim[s] ou Não[n]? ")
        ).lower()
        if pergunta == "s":
            enviar_backup_por_email()
            break
        elif pergunta == "n":
            break
        else:
            print("Por favor, responda 's' ou 'n'.")


def entrada_usuario():
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


def diretorio_backup():
    while True:
        try:
            diretorio_atual = input(
                "Informe o diretório que deseja realizar o backup: "
            )
            diretorio_destino = input(
                "Informe o diretório que deseja salvar o arquivo de backup: "
            )

            if os.path.exists(diretorio_destino):
                print(f"O diretório de destino '{diretorio_destino}' já existe.")
                continue

            backup = shutil.copytree(diretorio_atual, diretorio_destino)
            if backup:
                print(f"Backup realizado com sucesso para: {diretorio_destino}")
                return diretorio_atual, diretorio_destino
        except ValueError:
            print(
                "Formato inválido. Certifique-se de inserir a data e hora no formato correto (DD/MM/YYYY HH:MM)."
            )
        except shutil.Error as e:
            print(f"Falha ao realizar o backup. Erro: {e}. Por favor, tente novamente.")
        return None, None


def configurar_backup(data_hora_backup, diretorio_origem, diretorio_destino):
    schedule.every().day.at(data_hora_backup.strftime("%H:%M")).do(job)
    if diretorio_destino:
    # Criar arquivo a partir de uma pasta
        with az.Archive() as archive:
            # Adicionar pasta ao zip
            archive.create_entries("files")
    # Crie e salve o arquivo zip
    archive.save('my_archive_from_folder.zip')

    print(
        f"Backup agendado para o diretório de origem '{diretorio_origem}' e destino '{diretorio_destino}'."
    )
    print("Aguardando a hora do backup...")

    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            print("\nBackup agendado interrompido.")
            break


def main():
    print("Bem-vindo! Por favor, informe a data e a hora para a realização do backup:")
    diretorio_atual, diretorio_destino = diretorio_backup()
    data_hora_backup = entrada_usuario()
    configurar_backup(data_hora_backup, diretorio_atual, diretorio_destino)


if __name__ == "__main__":
    main()
