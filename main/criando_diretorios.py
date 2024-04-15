import os


def criando_diretorio():
    while True:
        diretorio_atual = os.getcwd()
        print(f"Diretório atual: {diretorio_atual}")
        pergunta = input("Deseja criar um diretório? Sim[s] ou Não[n]? ").lower()
        if pergunta not in ["s", "n"]:
            print("Por favor, escolha 's' ou 'n'!")
        elif pergunta == "s":
            resposta = input("Digite um nome para seu diretório: ")
            try:
                os.mkdir(resposta)
                print(f"Diretório '{resposta}' criado com sucesso!")
            except OSError as error:
                print(f"Erro ao criar o diretório: {error}")
        elif pergunta == "n":
            resposta = input("Por favor informe o caminho do novo diretório: ")
            os.chdir(resposta)
            resposta = input("Digite um nome para seu diretório: ")
            try:
                os.mkdir(resposta)
                print(f"Diretório '{resposta}' criado com sucesso!")
            except OSError as error:
                print(f"Erro ao criar o diretório: {error}")
        else:
            print("Saindo do programa.")


criando_diretorio()
