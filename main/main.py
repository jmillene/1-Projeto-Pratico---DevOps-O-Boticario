from backup_confg.backup_confg import diretorio_backup
from dir_confg.criando_diretorios import job
from email_confg.enviar_bkp_email import enviar_backup_por_email
from interface_grafica.dir_interface import selecionar_diretorio_raiz, selecionar_diretorio_destino
from interface_grafica.email_interface import interface_email
from user.entrada_usuario_bkp import entrada_usuario_enviar_email
from user.entrada_usuario_bkp import entrada_usuario_backup
from user.verificar_credenciais_usuario import verificar_credenciais_usuario
from user.entrada_usuario_email_senha import obter_email, obter_senha 

def main():
    diretorio_backup()
    data_hora_inicio_backup = job()
    print("Data e hora de início do backup:", data_hora_inicio_backup)
    enviar_backup_por_email()
    selecionar_diretorio_raiz()
    selecionar_diretorio_destino()
    interface_email()
    entrada_usuario_enviar_email()
    entrada_usuario_backup()
    email = obter_email()
    senha = obter_senha()
    verificar_credenciais_usuario(email, senha)

main()
