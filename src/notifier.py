# src/notifier.py
import smtplib
import os
import re
from email.message import EmailMessage

def send_email(report_content):
    sender = "kouemabea@gmail.com"  # À remplacer par ton adresse
    recipient = "kouemabea@gmail.com"
    password = os.getenv("EMAIL_PASSWORD")

    msg = EmailMessage()
    msg['Subject'] = "📊 Veille Stratégique : Marchés Financiers & Économie"
    msg['From'] = sender
    msg['To'] = recipient

    # 1. Conversion des liens Markdown [Texte](URL) en <a href="URL">Texte</a>
    html_body = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" style="color: #3498db;">\1</a>', report_content)
    
    # 2. Conversion des titres de sections (ex: "1. Titre") en <h3>
    html_body = re.sub(r'(\d\.\s[^\n]+)', r'<h3 style="color: #2c3e50; border-bottom: 1px solid #eee; margin-top: 20px;">\1</h3>', html_body)
    
    # 3. Conversion des tirets en listes HTML et nettoyage des retours à la ligne
    html_body = html_body.replace("- ", "<li>")
    html_body = html_body.replace("\n", "<br>")

    # Construction du template HTML final
    html_content = f"""
    <html>
    <body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; color: #333; line-height: 1.6; padding: 20px;">
        <div style="max-width: 650px; margin: auto; border: 1px solid #e1e1e1; border-radius: 10px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <div style="background-color: #2c3e50; color: #ffffff; padding: 20px; text-align: center;">
                <h1 style="margin: 0; font-size: 22px;">Rapport de Veille Financière</h1>
            </div>
            <div style="padding: 30px;">
                {html_body}
            </div>
            <div style="background-color: #f8f9f9; padding: 15px; text-align: center; font-size: 12px; color: #7f8c8d;">
                <p>Agent IA Autonome - Veille Sectorielle Temps Réel</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    msg.add_alternative(html_content, subtype='html')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)
        print("Mail envoyé avec succès !")
    except Exception as e:
        print(f"Erreur lors de l'envoi du mail : {e}")