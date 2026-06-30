# src/notifier.py
import smtplib
from email.message import EmailMessage
import os

def send_email(report_content):
    sender = "kouemabea@gmail.com" # Ton email Gmail
    recipient = "kouemabea@gmail.com"
    password = os.getenv("EMAIL_PASSWORD") # Ton mot de passe d'application

    msg = EmailMessage()
    msg['Subject'] = "📊 Veille Stratégique : Fintech & Banque CI"
    msg['From'] = sender
    msg['To'] = recipient

    # Conversion du Markdown en HTML propre
    # Version corrigée (sans backslash dans la f-string)
    html_content = """
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 650px; margin: auto; padding: 20px;">
        <div style="background-color: #ffffff; border-left: 5px solid #2c3e50; padding: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            <h1 style="color: #2c3e50; margin-top: 0;">Veille Stratégique</h1>
            <p style="color: #7f8c8d; font-size: 0.9em;">Rapport quotidien - Secteur Fintech & Banque CI</p>
        </div>
        <div style="padding: 20px 0;">
            REPLACE_REPORT_CONTENT
        </div>
        <div style="margin-top: 40px; border-top: 1px solid #eee; padding-top: 20px; font-size: 0.8em; color: #95a5a6; text-align: center;">
            <p>Agent IA Autonome - Veille Sectorielle</p>
        </div>
    </body>
    </html>
    """.replace("REPLACE_REPORT_CONTENT", report_content.replace("**", "<b>").replace("\n", "<br>"))
    
    msg.add_alternative(html_content, subtype='html')
    
    msg.add_alternative(html_content, subtype='html')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)
        print("Mail envoyé avec succès !")
    except Exception as e:
        print(f"Erreur lors de l'envoi du mail : {e}")