# Agent de Veille Stratégique - Fintech & Banque (Côte d'Ivoire)

Un agent IA autonome conçu pour surveiller quotidiennement l'écosystème financier ivoirien (Fintech, banques, régulations BCEAO).

## Fonctionnalités

- **Veille autonome :** Recherche ciblée sur le web via Tavily.
- **Synthèse IA :** Analyse des données par Llama-3-70b (via Groq).
- **Automatisation :** Envoi d'un rapport par email chaque matin via GitHub Actions.

## Structure du projet

- `src/agent.py` : Cœur logique (workflow LangGraph).
- `src/notifier.py` : Logique d'envoi d'emails.
- `.github/workflows/daily_veille.yml` : Automatisation quotidienne.

## Configuration

1. Cloner le projet.
2. Installer les dépendances : `pip install -r requirements.txt`.
3. Configurer les secrets GitHub (`GROQ_API_KEY`, `TAVILY_API_KEY`, `EMAIL_PASSWORD`).
