import shutil
import os
from interface_grafica.dir_interface import selecionar_diretorio_raiz
from interface_grafica.dir_interface import selecionar_diretorio_destino


def diretorio_backup():
    while True:
        try:
            selecionar_diretorio_raiz()
            selecionar_diretorio_destino()

            if os.path.exists(selecionar_diretorio_destino):
                print(
                    f"O diretório de destino '{selecionar_diretorio_destino}' já existe."
                )
                continue

            shutil.copytree(selecionar_diretorio_raiz, selecionar_diretorio_destino)
            print(f"Backup realizado com sucesso para: {selecionar_diretorio_destino}")
            return selecionar_diretorio_destino
        except ValueError:
            print(
                "Formato inválido. Certifique-se de inserir a data e hora no formato correto (DD/MM/YYYY HH:MM)."
            )
        except shutil.Error as e:
            print(f"Falha ao realizar o backup. Erro: {e}. Por favor, tente novamente.")
        return None
    
