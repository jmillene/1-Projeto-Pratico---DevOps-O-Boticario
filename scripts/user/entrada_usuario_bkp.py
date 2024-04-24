from entrada_usuario_email_senha import interface_email


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


entrada_usuario_enviar_email()
