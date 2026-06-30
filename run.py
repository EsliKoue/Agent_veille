# run.py
from src.agent import app
from src.notifier import send_email

if __name__ == "__main__":
    result = app.invoke({"company": "Secteur Fintech et Banque CI"})
    report = result.get("report")
    
    # Envoi du mail
    send_email(report)
    print("Rapport généré et envoyé par email.")