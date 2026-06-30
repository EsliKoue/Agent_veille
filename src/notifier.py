# src/notifier.py
import smtplib
from email.message import EmailMessage
import os

def send_email(report_content):
    # Remplace par tes informations
    sender = "kouemabea@gmail.com"
    recipient = "kouemabea@gmail.com"
    password = os.getenv("EMAIL_PASSWORD") # La clé sera sécurisée sur GitHub

    msg = EmailMessage()
    msg.set_content(report_content)
    msg['Subject'] = "Veille Stratégique : Fintech & Banque CI"
    msg['From'] = sender
    msg['To'] = recipient

    # Exemple pour Gmail
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)