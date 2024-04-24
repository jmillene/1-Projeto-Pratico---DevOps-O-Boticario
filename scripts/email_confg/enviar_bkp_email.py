import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def enviar_backup_por_email():
    smtp_server = "smtp.example.com"
    smtp_port = 587
    email_usuario = input("Informe o seu email: ")
    senha_usuario = input("Informe sua senha: ")

    msg = MIMEMultipart()
    msg["Subject"] = "E-mail com anexo"
    msg["From"] = email_usuario
    msg["To"] = input("Informe o e-mail do destinatário: ")

    body = MIMEText("Olá, seu backup está em anexo!")
    msg.attach(body)

    file_path = input("Informe o caminho do arquivo de backup: ")
    attachment = open(file_path, "rb")
    part = MIMEBase("application", "octet-stream")
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment; filename= %s" % file_path)
    msg.attach(part)

    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(email_usuario, senha_usuario)
        smtp.send_message(msg)
