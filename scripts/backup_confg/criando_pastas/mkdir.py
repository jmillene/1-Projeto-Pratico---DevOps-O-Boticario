import os

def verificar_diretorio_existente(nome_diretorio):
    return os.path.exists(nome_diretorio)

def criando_diretorio():
    nome_diretorio = input("Por favor! Informe o nome do diretório que deseja criar: ")
    while True:
        try:
            if verificar_diretorio_existente(nome_diretorio):
                print(f"O diretório '{nome_diretorio}' já existe!")
                pergunta = input("Deseja criar outro diretório? (s/n): ")
                if pergunta.lower() == "n":
                    break
                nome_diretorio = input("Por favor! Informe o nome do diretório que deseja criar: ")
            else:
                os.mkdir(nome_diretorio)
                print(f"Diretório '{nome_diretorio}' criado com sucesso!")
                break
        except Exception as e:
            print(f"Ocorreu um erro ao criar o diretório: {e}")

criando_diretorio()
