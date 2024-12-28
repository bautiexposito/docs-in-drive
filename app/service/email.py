import os
from dotenv import load_dotenv
from email.message import EmailMessage
import ssl
import smtplib
# import certifi

load_dotenv()

email_sender = "bautistaaexpositooo@gmail.com"
password = os.getenv("EMAIL_PASSWORD")

def send_email(email_receiver: str, file_name: str, visibility: str):
    subject = "Visibilidad modificada de su archivo en Drive"
    body = f"""
        Hola,
        La visibilidad de su archivo '{file_name}' ha sido modificada a '{visibility}'.
        Saludos.
    """

    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)

    # context = ssl.create_default_context()
    context = ssl._create_unverified_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
